# ISS Overhead Notifier

# About
This project uses the [ISS API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)  to receive the latitude and longitude of the International Space Station and it also uses the [Sunrise-sunset API](https://sunrise-sunset.org/api) to see what time the sun rises or sets.

Then we calculate to see when the ISS is above your location and if it is dark outside, if so it sends out an email to you stating to look-up the sky! :) 
Use [latlong.net](https://www.latlong.net/) to find your city's latitude and longitude.
I am running my code in the cloud, so it is always running in the background.

# Usage Example
![This is an image](https://i.imgur.com/WaPBYUy.png)

# Built with
- [Python](https://www.python.org/)

# Dependencies
1. Python v3.x
2. requests
3. datetime
4. smtplib
5. time

# License
- [MIT License](https://github.com/Solyyy/iss_overhead_notifier/blob/main/LICENSE.txt)
