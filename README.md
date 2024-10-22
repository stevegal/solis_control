# Scripts to Control SolisCloud Inverters

solis_control pyscripts for home assistant.
NOTE: you need the [pyscript plugin](https://hacs-pyscript.readthedocs.io/en/latest/) installed.
These scripts then just go into the pyscript folder on your install. Once it's there, just call it as below.

The pyscript requires the `all_all_gobal_imports: true` to be set in the configuration either from the UI or in your glabl configuration yaml.

```
pyscript:
  allow_all_imports: true
  hass_is_global: true
```

## Services
There are three services which can be called via HA automations.  They are:
- solis_control_battery_charge
- solis_control_grid_feed_in
- solis_sync_clock

N.B.: There are a mixture of quotes and unquoted strings used in the `config` sections of script.  These are needed, so please maintain them where they are and omit them where they are not.

### solis_control_battery_charge
This script sets the charge and force discharge times for your Solis inverter.

call the service like this:
```yaml
service: pyscript.solis_control_battery_charge
data:
  config:
    secret: API_SECRET
    key_id: "API_KEY"
    username: USERNAME
    password: PASSWORD
    plantId: "PLANT_ID"
  settings:
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
```

### solis_control_grid_feed_in
This script sets the `Feed in Power Limit Switch`, `Feed in Power Limit Value`, and `Feed in Current Limit Value` settings on your Solis inverter.

call the service like this:
```yaml
action: pyscript.solis_control_grid_feed
data:
  config:
    secret: API_SECRET
    key_id: "API_KEY"
    username: USERNAME
    password: PASSWORD
    plantId: "PLANT_ID"
  settings:
    enabled: true
    powerLimitInWatts: 3000
    currentLimitInAmps: 50
```
| Setting | Description | Values |
| ------- | ----------- | ------ |
| `enabled` | Turns this setting on or off | `true` or `false` |
| `powerLimitInWatts` | Sets the max allowed feed in power limit at the grid connection point | 0 ~ 9900 (must be a multiple of 100) |
| `currentLimitInAmps` | Sets the max allowed feed in current limit at the grid connection point | 0 ~ 52 |

### solis_sync_clock
This script syncs the clock on your Solis inverter to that on your HA.  It doesn't do any timezone modifications, so please ensure your HA and your inverter are set up for the same timezone.

call the service like this:
```yaml
action: pyscript.solis_sync_clock
data:
  config:
    secret: API_SECRET
    key_id: "API_KEY"
    username: USERNAME
    password: PASSWORD
    plantId: "PLANT_ID"
```

Note to find the plantId please follow the excellent instructions in [solis-sensor](https://github.com/hultenvp/solis-sensor)
