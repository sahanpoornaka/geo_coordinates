"""
Developers:
<Your Name(s)>

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""

from arcgis.gis import GIS
from arcgis.geocoding import geocode, batch_geocode
import requests


def get_geo_coordinates_from_google(location_address: str, connection_params: dict):
    base_url = 'https://maps.googleapis.com/maps/api/geocode'
    endpoint = '{}/{}?address={}&key={}'.format(base_url,
                                                connection_params['output_format'],
                                                location_address,
                                                connection_params['api_key']
                                                )

    # make the GET request
    results = requests.get(endpoint).json()
    # print(address, results)

    # check if codes were successfully obtained or not
    if results['status'] == 'ZERO_RESULTS':
        return None

    location = results['results'][0]['geometry']['location']
    return {
        'longitude': location['lng'],
        'latitude': location['lat']
    }


def get_geo_coordinates_from_here(location_address: str, connection_params: dict):
    base_url = 'https://geocoder.ls.hereapi.com/6.2/geocode.'
    endpoint = '{}{}?searchtext={}&gen=9&apiKey={}'.format(base_url,
                                                           connection_params['output_format'],
                                                           location_address, connection_params['api_key']
                                                           )
    # make the GET request
    results = requests.get(endpoint).json()

    # check if codes were successfully obtained or not
    if len(results['Response']['View']) == 0:
        return None

    location = results['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']
    return {
        'longitude': location['Longitude'],
        'latitude': location['Latitude']
    }


def get_geo_coordinates_from_arcgis(location_address:str, connection_params:dict):
    base_url = 'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates'
    endpoint = f'{base_url}?f={connection_params["output_format"]}&singleLine={location_address}'
    results = requests.get(endpoint).json()

    location = results['candidates'][0]['location']
    return {
        'longitude': location['x'],
        'latitude': location['y']
    }


def get_geo_coordinates_from_arcgis_with_login(location_address:str, connection_params:dict):
    GIS("http://www.arcgis.com", connection_params['ARCGIS_USER'], connection_params['ARCGIS_PASSWORD'])
    arc_gis_loc = geocode(location_address)
    return {
        'longitude': arc_gis_loc[0]['location']['x'],
        'latitude': arc_gis_loc[0]['location']['y'],
        'all_results': arc_gis_loc
    }


def get_batch_geo_coordinates_from_arcgis_with_login(location_addresses:list, connection_params:dict):
    GIS("http://www.arcgis.com", connection_params['ARCGIS_USER'], connection_params['ARCGIS_PASSWORD'])
    arc_gis_locs = batch_geocode(location_addresses)
    return arc_gis_locs


if __name__ == "__main__":
    import json
    with open('./private_data/api_keys.json', 'r') as outfile:
        credentials = json.load(outfile)

    # Google API Call
    connection_params = {
        'output_format': 'json',
        'api_key': credentials['GOOGLE_API_KEY']
    }
    address_ = 'Boise,+US'

    lng_lat_google = get_geo_coordinates_from_google(address_, connection_params)
    print(lng_lat_google)

    # Here API Call
    connection_params = {
        'output_format': 'json',
        'api_key': credentials['HERE_API_KEY']
    }
    address_ = 'Boise,+US'
    lng_lat_here = get_geo_coordinates_from_here(address_, connection_params)
    print(lng_lat_here)

    # ArcGis API Call Method 1
    connection_params_ = {
        'output_format': 'json',
    }
    address_ = 'Boise, US'
    lng_lat_arcgis = get_geo_coordinates_from_arcgis(address_, connection_params_)
    print(lng_lat_arcgis)

    # ArcGis API Call Method 2
    connection_params_ = {
        'ARCGIS_USER': credentials['ARCGIS_USER'],
        'ARCGIS_PASSWORD': credentials['ARCGIS_PASSWORD'],
    }
    address_ = 'Boise, US'
    lng_lat_arcgis2 = get_geo_coordinates_from_arcgis_with_login(address_, connection_params_)
    print(lng_lat_arcgis2)

    # ArcGis API Call Method 2 - Batch
    connection_params_ = {
        'ARCGIS_USER': credentials['ARCGIS_USER'],
        'ARCGIS_PASSWORD': credentials['ARCGIS_PASSWORD'],
    }
    addresses = [
        'Albany',
        'Boston',
        'Denver'
    ]
    lng_lat_arcgis3 = get_batch_geo_coordinates_from_arcgis_with_login(addresses, connection_params_)
    for i, result in enumerate(lng_lat_arcgis3):
        if result['address'] != '':
            print(result['address'])
            print("long = {}, lat = {}".format(result['location']['x'], result['location']['y']))
            print("____________________________")





