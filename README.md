# solis_control

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

Note to find the plantId please follow the excellent instructions in (solis-sensor)[https://github.com/hultenvp/solis-sensor]
