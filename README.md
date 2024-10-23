# Scripts to Control SolisCloud Inverters

A set of python scripts to set various settings on Solis inverters via SolisCloud for Home Assistant.

# Table of Contents
1. [Installation](#installation)
1. [Services](#services)  
    1.1 [solis_control_battery_charge](#solis_control_battery_charge)  
    1.2 [solis_control_grid_feed](#solis_control_grid_feed)  
    1.3 [solis_control_power_limit](#solis_control_power_limit)  
    1.4 [solis_sync_clock](#solis_sync_clock)  

# Installation
You need the [pyscript plugin](https://hacs-pyscript.readthedocs.io/en/latest/) installed.  
These scripts then just go into the pyscript folder on your install.

The pyscript requires the `all_all_gobal_imports: true` to be set in the configuration either from the UI or in your glabl configuration yaml.

```
pyscript:
  allow_all_imports: true
  hass_is_global: true
```

# Services
There are three services which can be called via HA automations.  They are:
- [solis_control_battery_charge](#solis_control_battery_charge)
- [solis_control_grid_feed](#solis_control_grid_feed)
- [solis_control_power_limit](#solis_control_power_limit)
- [solis_sync_clock](#solis_sync_clock)

N.B.: There are a mixture of quotes and unquoted strings used in the `config` sections of script.  These are needed, so please maintain them where they are and omit them where they are not.

## solis_control_battery_charge
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

## solis_control_grid_feed
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

## solis_control_power_limit
This script sets the power limit on your Solis inverter.  The power limit is a percentage which is used to set the active power generation output of the inverter.  From the [Solis documentation](https://solis-service.solisinverters.com/en/support/solutions/articles/44002032572-control-maximum-active-power-generation):

> It is the desired active power limit divided by the nominal power of the inverter, as shown in the equation below.  
> _For example, this means if a user wants the inverter to only generate a maximum of 3.6kVa (for EEG2012, 70% of the kWp of the PV array) and the inverter has a nominal rating of 5kVA. The user must calculate the percent as shown below._  
> _Therefore, the user must enter 72% into the interface on the inverter._

call the service like this:
```yaml
action: pyscript.solis_control_power_limit
data:
  config:
    secret: API_SECRET
    key_id: "API_KEY"
    username: USERNAME
    password: PASSWORD
    plantId: "PLANT_ID"
  settings:
    powerLimitPercentage: 100
```

| Setting | Description | Values |
| ------- | ----------- | ------ |
| `powerLimitPercentage` | The percentage to limit the active power generation output of the inverter.  See full definition above. | An integer [0-110] |

## solis_sync_clock
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
