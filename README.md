# solis_control
solis control pyscript for home assistant.
NOTE: you need the (pyscript plugin][https://hacs-pyscript.readthedocs.io/en/latest/] installed.
This script then just goes into the pyscript folder on your install. Once it's there, just call it as below.

## Config
call the service like:
```
service: pyscript.solis_control
data:
  days:
    - chargeCurrent: "50"
      dischargeCurrent: "50"
      chargeStartTime: "03:00"
      chargeEndTime: "04:30"
      dischargeStartTime: "00:00"
      dischargeEndTime: "00:00"
    - chargeCurrent: "50"
      dischargeCurrent: "50"
      chargeStartTime: "00:00"
      chargeEndTime: "00:00"
      dischargeStartTime: "00:00"
      dischargeEndTime: "00:00"
    - chargeCurrent: "50"
      dischargeCurrent: "50"
      chargeStartTime: "00:00"
      chargeEndTime: "00:00"
      dischargeStartTime: "00:00"
      dischargeEndTime: "00:00"
  config:
    secret: API_SECRET
    key_id: API_KEY
    username: USERNAME
    password: PASSWORD
    plantId: PLANT_ID
```
