# Automation: Solis: Slow Charge During Cheap Periods
This automation will run every 5 minutes and set the charge rate and times for cheap periods as configured.  This example is configured for the Octopus Cozy tariff which has three cheap periods of:
- 04:00 - 07:00
- 13:00 - 16:00
- 22:00 - 00:00

## Using the script
To use this script you'll need to validate/modify the following:
1. Trigger - The default trigger will work fine for you if your rate changes at the top/middle of every hour.
2. Conditions - You need to modify these such that the script _won't_ run during your cheap slots.  So modify the times and number of cheap slots.
3. Action - You need to modify the first four lines under `action/data/settings/chargeCurrent`.  These values describe your battery system.  See below for comments.
4. Fill in your SolisCloud API information under `action/data/config`.  See the root [README.md](/README.md) for more info.

Comments aren't supported inside YAML multi-line blocks, so here are some comments of what's going on in the `action/data/settings/chargeCurrent` section:
```yaml
# Set this to your batteries' voltage
{% set voltage = 50.0 %}

# Set this to your batteries' maximum capacity in watts
{% set battery_capacity_in_watts = 3650 %}

# Set this to your batteries' maximum charge rate (in amps)
# You can convert watts to amps via: amps = watts * voltage
{% set max_charge_amps = 37.5 %}

# If your charging windows are all the same length, just set this to the
# number of hours.  If you have windows of different length, you need to add
# the logic here such that charge_hours always is set to the length of the
# current window.  This example sets the charge_hours to 2 if the hour is
# between 16 and 23.  Any other time it assumes the cheap slot is three hours
# long.
{% set charge_hours = 2 if now().hour > 16 and now().hour < 23 else 3 %}

# Perform calculations to get the charge rate (in amps) for your system.
{% set battery_soc = float(states('sensor.solis_remaining_battery_capacity'), 0.0) %}
{% set battery_percent_needed = (100.0 - battery_soc) | round(method="ceil") %}
{% set watts_hours_needed = battery_capacity_in_watts * (battery_percent_needed/100.0) %}
{% set amp_hours_needed = (watts_hours_needed/charge_hours) / voltage %}
{{ min(max(amp_hours_needed | round(method="ceil"), 1), max_charge_amps) }}
```
