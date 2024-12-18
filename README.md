# ISS-Finder
This Python script tracks the International Space Station (ISS) in real-time and notifies the user via email when the ISS is overhead and it is dark at their location. The script uses APIs to fetch the ISS location and sunrise/sunset times.

## Features
- Tracks the current position of the ISS.
- Checks if the ISS is within a 5-degree radius of your location.
- Verifies if it is dark at your location based on sunset and sunrise times.
- Sends an email notification to alert you to "look up" when the ISS is overhead at night.

## APIs Used
- Sunrise-Sunset API for sunrise and sunset times.
  ~~  https://api.sunrise-sunset.org/json
  
- Open Notify API for ISS location.
  ~~ http://api.open-notify.org/iss-now.json

## How It Works
 ### Fetches Sunrise/Sunset Data:

 - The script uses your latitude and longitude to get the local sunset and sunrise times.
 
### Fetches ISS Position:
 - Queries the Open Notify API for the current latitude and longitude of the ISS.

### Checks Conditions:

- Verifies if the ISS is overhead (within a 5-degree range of your location).
- Checks if it is currently dark at your location.

### Sends Email Notification:
- If the ISS is overhead and it is dark, the script sends an email notification to the specified email.

### Runs Continuously:
- The script checks the ISS position every 60 seconds.

  
