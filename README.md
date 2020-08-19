[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Retrieving Longitudes and Latitudes from Map Service Providers  
This contains example codes to retrieve geo coordinates from the APIs provided 
by [Google](https://cloud.google.com/maps-platform/), 
[Here](https://developer.here.com/) and 
[ArcGIS](https://geocode.arcgis.com/arcgis/) for your data analysis.  

## Contributors
1. [Kevin Patel](https://github.com/PatelKeviin) \(GitHub Username: PatelKeviin\)  
    Functions:  
    - get_geo_coordinates_from_google (GeoCoordinatesGoogle)
    - get_geo_coordinates_from_here (GeoCoordinatesHere)
    - get_geo_coordinates_from_arcgis (GeoCoordinatesArcGIS)         
        
1. [Khushbu Patel](https://github.com/khushbuupatel) \(GitHub Username: khushbuupatel\)
    - get_geo_coordinates_from_arcgis_with_login (GeoCoordinatesArcGIS)  
    - get_batch_geo_coordinates_from_arcgis_with_login (GeoCoordinatesArcGIS)  

### Files

- ExampleRunner: 
    Sample Code to Run the Required API
- GeoCoordinatesGoogle:
    File Containing Functionalities Related to Google API
    - get_geo_coordinates_from_google
    - get_altitude_from_google
    - get_address_altitude_from_google
- GeoCoordinatesHere:
    File Containing Functionalities Related to Here API
    - get_geo_coordinates_from_here
- GeoCoordinatesArcGIS:
    File Containing Functionalities Related to ArcGIS API
    - get_geo_coordinates_from_arcgis
- TestGeoCoordinates:
    Test Class to Test all above Functions

#### Directories

- credentials:
    Directory Containing the required Credentials for each service
    - google_cred.json
    - here_cred.json
    - arcgis_cred.json
- log:
    Directory to keep all the logs

## How to use

1. Setup the Required Libraries Stated in the [requirements.txt](requirements.txt) file
2. Add the Credentials to the relevant file inside [credentials](credentials) directory
2. [ExampleRunner.py](ExampleRunner.py) file contains examples for using the APIs from Google, Here and ArcGIS. In practice you might only need one service.
Copy only the function for your preferred.   
3. [TestGeoCoordinates.py](TestGeoCoordinates.py) Run the all test functions inside the test class using, 
```pytest TestGeoCoordinates.py```
For more Information on Pytest refer [Pytest Documentation](https://docs.pytest.org/en/stable/contents.html)

### Credentials

No credentials are required for the following function.
- get_geo_coordinates_from_arcgis (GeoCoordinatesArcGIS)          

For the remaining functions, the access was free for developers.   

To use the following functions, you have to get API keys from the respective map service providers.
- get_geo_coordinates_from_google (GeoCoordinatesGoogle)
- get_altitude_from_google (GeoCoordinatesGoogle)
- get_address_altitude_from_google (GeoCoordinatesGoogle)
- get_geo_coordinates_from_here (GeoCoordinatesHere)
The API keys were free for testing when this code was developed. Hope they are still free for developers.

To use the following, you have to create an account on ArcGIS.
- get_geo_coordinates_from_arcgis_with_login (GeoCoordinatesArcGIS)
- get_batch_geo_coordinates_from_arcgis_with_login (GeoCoordinatesArcGIS)
The account was free for testing when this code was developed. Hope it is still free for developers.
   
## Sponsor
DataDisca Pty Ltd, Melbourne, Australia

[https://www.datadisca.com](https://www.datadisca.com)

