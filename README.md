# python_weather_practice
Fetching weather data for Oslo/Norway in Python as practice.  

 usage: python fetchweather.py [options]  
>   options:
> -c      lat,lon  - Provide weather data for the given coordinates.  
> -n      cityname - Provide weather data for the given city, if the coords exist in cities.txt  
> -h               - Presents this text  
    If both coord and city are given, the program will only show the data for the coord.  
    If no options are given the program will default to showing data for Oslo 
    for the following day.  

Initially using locationforecast API from https://api.met.no/,
however in order to support searching up locations like cities we 
probably need to use the Frost API.

Will start out simple and CLI only, showing only temperatures for tomorrow,
but will eventually be adding CLI-flags for coords and dates
and files for storing coordinates for cities/points. 
Also displaying other info than temps.

Eventually I'll be adding a simple GUI using TKinter.
