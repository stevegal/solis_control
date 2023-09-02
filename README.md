# solis_control

# IMPORTANT - LOOKS LIKE SOLIS IS UPDATING TO A V3 VERSION - UNSTABLE FOR THE MOMENT
I'm waiting on documentation for v3 api, and it looks like the v2 control api cid value has been modified for the v3 release and that has changed has
also changed the v2 value! I've looked at the web control version and has some success with changing the to 4644 instead of 103 (from looking at the web site value)
but issue #6 reporter has reported different values, so please make sure you are comfortable before changing anything as I have no appropriate documentation
and misuse could damage your inverter.

solis control pyscript for home assistant.
NOTE: you need the (pyscript plugin][https://hacs-pyscript.readthedocs.io/en/latest/] installed.
This script then just goes into the pyscript folder on your install. Once it's there, just call it as below.

The pyscript requires the `all_all_gobal_imports: true` to be set in the configuration either from the UI or in your glabl configuration yaml.

```
pyscript:
  allow_all_imports: true
  hass_is_global: true
```

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
Note the configuration items like `key_id`, `secret`, `plantId` and `password` must be defined as a string so wrap them in `"` to be sure.
