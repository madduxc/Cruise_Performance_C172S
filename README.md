# Cruise_Performance_C172S

This is an effort to create the framework for an app to calculate cruise performance from the tables given in the Pilot's Operating Handbook and using interpolation.

Currently app does not exist - v0.0.0

Planned steps:
- Create framework for user interface for inputting Temperature, Altitude, and Engine RPM
- Import tables of data
- Validate user inputs and create error messages to return to user 
- Develop modules to look up TAS, Fuel Flow, and Pecent Power for a value that exists on the table
- Develop framework for interpolation at each level: ex. find TAS_at_Temp1_Alt1_RPM1, TAS_at_Temp1_Alt1_RPM2, then interpolation to find TAS_at_Temp1_Alt1_RPM ...
- Create guardrails for interpolations: RPM setting too high/low for altitude, temperature out of range (extrapolation warning)

Future Work
- add a GUI
- add to Time, Fuel, and Distance to climb (or create separate app)
- add to total flight planning app (mulitiple climbs/descents)
