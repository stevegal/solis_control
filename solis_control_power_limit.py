from homeassistant.helpers.aiohttp_client import async_get_clientsession
import asyncio
import hashlib
import hmac
import base64
import json
import re
from http import HTTPStatus
from datetime import datetime, timezone

VERB = "POST"
LOGIN_URL = '/v2/api/login'
CONTROL_URL= '/v2/api/control'
INVERTER_URL= '/v1/api/inverterList'

session = async_get_clientsession(hass)

def digest(body: str) -> str:
    return base64.b64encode(hashlib.md5(body.encode('utf-8')).digest()).decode('utf-8')

def passwordEncode(password: str) -> str:
    md5Result = hashlib.md5(password.encode('utf-8')).hexdigest()
    return md5Result

def prepare_header(config: dict[str,str], body: str, canonicalized_resource: str) -> dict[str, str]:
    content_md5 = digest(body)
    content_type = "application/json"
    
    now = datetime.now(timezone.utc)
    date = now.strftime("%a, %d %b %Y %H:%M:%S GMT")
    
    encrypt_str = (VERB + "\n"
        + content_md5 + "\n"
        + content_type + "\n"
        + date + "\n"
        + canonicalized_resource
    )
    hmac_obj = hmac.new(
        config["secret"].encode('utf-8'),
        msg=encrypt_str.encode('utf-8'),
        digestmod=hashlib.sha1
    )
    sign = base64.b64encode(hmac_obj.digest())
    authorization = "API " + config["key_id"] + ":" + sign.decode('utf-8')
    
    header = {
        "Content-MD5":content_md5,
        "Content-Type":content_type,
        "Date":date,
        "Authorization":authorization
    }
    return header

async def login(config):
    body = '{"userInfo":"'+config['username']+'","password":"'+ passwordEncode(config['password'])+'"}'
    header = prepare_header(config, body, LOGIN_URL)
    response = await session.post("https://www.soliscloud.com:13333"+LOGIN_URL, data = body, headers = header)
    status = response.status
    result = ""
    r = json.loads(re.sub(r'("(?:\\?.)*?")|,\s*([]}])', r'\1\2', response.text()))
    if status == HTTPStatus.OK:
        result = r
    else:
        log.warning(status)
        result = response.text()
    
    return result["csrfToken"]

async def getInverterList(config):
    body = '{"stationId":"'+config['plantId']+'"}'
    header = prepare_header(config, body, INVERTER_URL)
    response = await session.post("https://www.soliscloud.com:13333"+INVERTER_URL, data = body, headers = header)
    inverterList = response.json()
    inverterId = ""
    for record in inverterList['data']['page']['records']:
      inverterId = record.get('id')
    return inverterId


def control_power_limit_body(inverterId, power_limit_settings) -> str:
    body = '{"inverterId":"' +inverterId +'", "cid":"15","value":"' \
      + str(int(power_limit_settings['power_limit_percentage'])) + '", "yuanzhi":"0"}'
    
    return body

async def set_power_limit(token, inverterId: str, config, power_limit_settings):
    body = set_power_limit(inverterId, power_limit_settings)
    headers = prepare_header(config, body, CONTROL_URL)
    headers['token']= token
    response = await session.post("https://www.soliscloud.com:13333"+CONTROL_URL, data = body, headers = headers)
    log.warning("solis_control_grid_feed.py - enabled response:" + response.text())
    
@service   
async def solis_control_power_limit(config=None, settings=None): 
    inverterId= getInverterList(config)
    token = login(config)

    set_power_limit(token, inverterId, config, settings)
