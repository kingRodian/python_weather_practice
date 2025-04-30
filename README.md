# python_weather_practice
Fetching weather data for Oslo/Norway in Python as practice.  


usage: python fetchweather.py [options]  
>    options     arguments
>        -c      lat,lon  - Provide weather data for the given coordinates.  
>        -n      cityname - Provide weather data for the given city, if the coords exist in cities.txt  
>        -d      days     - Specify the amount of days to show data for. Default is 1, max is 9.  
>        -a               - Show averages for 00-08, 08-12, 12-18 and 18-00 rather than per hour.  
>        -p               - Shows precipitation for that hour. Does nothing with -a flag.  
>        -w               - Shows windspeed and origin of wind. Does nothing with -a flag.  
>        -h               - Presents this text  
>    If both coord and city are given, the program will only show the data for the coord.  
>    If no options are given the program will default to showing data for Oslo   
>    for the current day.  
>    If both coord and city are given, the program will only show the data for the coord.  
>    If no options are given the program will default to showing data for Oslo   
>    for the following day.  

Example: python fetchweather.py -p -d 3 -n sandefjord -w          will show the weather for Sandefjord for 3 days including today, including wind and precipitation.  


Initially using locationforecast API from https://api.met.no/,
however in order to support searching up locations like cities we 
probably need to use the Frost API.

Will start out simple and CLI only.  
Eventually I'll be adding a simple GUI using TKinter. maybe
