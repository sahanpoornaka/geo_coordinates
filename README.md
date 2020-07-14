[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Retrieving Longitudes and Latitudes from Map Service Providers  
This contains example codes to retrieve geo coordinates from APIs provided by Google, Here and ArcGIS for your data analysis.

## Contributors
1. [Kevin Patel](https://github.com/PatelKeviin) \(GitHub Username: PatelKeviin\)  
    Functions:  
    - get_geo_coordinates_from_google
    - get_geo_coordinates_from_here
    - get_geo_coordinates_from_arcgis          
        
1. [Khushbu Patel](https://github.com/khushbuupatel) \(GitHub Username: khushbuupatel\)
    - get_geo_coordinates_from_arcgis_with_login
    - get_batch_geo_coordinates_from_arcgis_with_login

## How to use

The code contains examples for APIs from Google, Here and ArcGIS. In practice you might only need one service.
Copy only the function for your preferred.   

### Code

The code is in [geo_coordinates.py](./geo_coordinates.py).  
Check the examples given at the end of the file.

Credentials are in the format given in [api_keys.json](./api_keys.json). Put your own in the `private_data` folder.


### Credentials

No credentials are required for the following function.
- get_geo_coordinates_from_arcgis          

For the remaining functions, the access was free for developers.   

To use the following functions, you have to get API keys from the respective map service providers.
- get_geo_coordinates_from_google
- get_geo_coordinates_from_here  
The API keys were free for testing when this code was developed. Hope they are still free for developers.

To use the following, you have to create an account on ArcGIS.
- get_geo_coordinates_from_arcgis_with_login
- get_batch_geo_coordinates_from_arcgis_with_login  
The account was free for testing when this code was developed. Hope it is still free for developers.
   
## Sponsor
DataDisca Pty Ltd, Melbourne, Australia

[https://www.datadisca.com](https://www.datadisca.com)

