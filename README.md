# python_weather_practice
Fetching weather data for Oslo/Norway in Python as practice.

Initially using locationforecast API from https://api.met.no/,
however in order to support searching up locations like cities we 
probably need to use the Frost API.

Usage: `python fetchweather.py`

Will start out simple and CLI only, showing only temperatures for tomorrow,
but will eventually be adding CLI-flags for coords and dates
and files for storing coordinates for cities/points. 
Also displaying other info than temps.

Eventually I'll be adding a simple GUI using TKinter.
