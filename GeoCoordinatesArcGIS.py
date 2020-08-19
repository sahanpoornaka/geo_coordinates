"""
Purpose:
This Class Contains Methods To Retrieve Geo Location Information From ArcGIS Using ArcGIS Library For Python.

get_geo_coordinates_from_arcgis:
    Retrieve Latitude and Longitude to a Given Address/Location (No Credentials are
needed) get_geo_coordinates_from_arcgis_with_login:
    Retrieve Latitude and Longitude to a Given Address/Location (With Credentials)
get_batch_geo_coordinates_from_arcgis_with_login:
    Retrieve Latitude and Longitude to a Given Addresses/Locations (With Credentials)

Developers:
Kevin Patel (GitHub Username: PatelKeviin)
    get_geo_coordinates_from_arcgis

Khushbu Patel (GitHub Username: khushbuupatel)
    get_geo_coordinates_from_arcgis_with_login
    get_batch_geo_coordinates_from_arcgis_with_login

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""
import logging
import requests
from arcgis.gis import GIS
from arcgis.geocoding import geocode, batch_geocode


class GeoCoordinatesArcGIS:

    # Set Log Level
    logging.basicConfig(filename='./log/arcgis_log.txt', level=logging.INFO)

    # Class Variables
    connection_params: dict = {}
    username_password_flag = False

    def __init__(self, username: str = None, password: str = None, output_format: str = 'json') -> None:
        """
        Class Initializer
        @param username: Username For The ArcGIS Developer Account
        @param password: Password For The Above User Account
        @param output_format: Required Output Format
        """
        if username and password:
            self.username_password_flag = True
        self.connection_params = {'username': username, 'password': password, 'output_format': output_format}

    @staticmethod
    def __get_error_msg(error_msg: str):
        """
        purpose: Return an Error Object with a given Error Message
        @param error_msg: Error Message
        @return: Dict
            {
                'status': False,
                'message': error_msg,
                'result': None
            }
        """
        return {
            'status': False,
            'message': error_msg,
            'result': None
        }

    def get_geo_coordinates_from_arcgis(self, location_address: str):
        """
        purpose: Retrieve Latitude and Longitude to a Given Address/Location
        @param location_address: Latitude and Longitude needed Address/Location
        @return: Dict
            status: True or False based on success,
            message: Error message if an error occurred
            result:
              {
                'latitude': Latitude of the Address Provided
                'longitude': Longitude of the Address Provided
              }
        """
        base_url = 'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates'
        endpoint = '{}?f={}&singleLine={}'.format(base_url, self.connection_params['output_format'], location_address)

        try:
            # make the GET request
            response = requests.get(endpoint)

            # check if codes were successfully obtained or not
            if response.status_code == 200:
                location = response.json()['candidates'][0]['location']
                return {
                    'status': True,
                    'message': None,
                    'result': {
                        'longitude': location['x'],
                        'latitude': location['y']
                    }
                }
            elif response.status_code == 400:
                return self.__get_error_msg('Request Failed Validation. Please Check your API key')
            elif response.status_code == 503:
                return self.__get_error_msg('Temporary Server Error. Please Check back again in a short while')
            else:
                return self.__get_error_msg('Some Unknown Error Occurred While Sending Request To Server')

        except ConnectionError:
            return self.__get_error_msg('Connection Error')
        except TypeError:
            return self.__get_error_msg('Type Error')
        except Exception as e:
            return self.__get_error_msg('Unknown Error Occurred, Error: {}'.format(e))

    def get_geo_coordinates_from_arcgis_with_login(self, location_address: str):
        """
        purpose: Retrieve Latitude and Longitude to a Given Address/Location With Credentials
        @param location_address: Latitude and Longitude needed Address/Location
        @return: Dict
            status: True or False based on success,
            message: Error message if an error occurred
            result:
              {
                'latitude': Latitude of the Address Provided
                'longitude': Longitude of the Address Provided
                'all_results': Whole Response Object Received From Arc GIS
              }
        """

        # If Username and Password Not Set, Return an error Object
        # if self.username_password_flag:
        #     return self.__get_error_msg('Username or Password is not Set')

        try:
            # Establish Connection To ArcGIS Server Via GIS Library
            GIS("http://www.arcgis.com", self.connection_params['username'], self.connection_params['password'])
            arc_gis_loc = geocode(location_address)
            if len(arc_gis_loc) > 0:
                return {
                    'status': True,
                    'message': None,
                    'result': {
                        'longitude': arc_gis_loc[0]['location']['x'],
                        'latitude': arc_gis_loc[0]['location']['y'],
                        'all_results': arc_gis_loc
                    }
                }
            else:
                return self.__get_error_msg('Unknown Location. No Results Found')
        except ConnectionError:
            return self.__get_error_msg('Connection Error')
        except TypeError:
            return self.__get_error_msg('Type Error')
        except Exception as e:
            return self.__get_error_msg('Unknown Error Occurred, Error: {}'.format(e))

    def get_batch_geo_coordinates_from_arcgis_with_login(self, location_addresses: list):
        """
        purpose: Retrieve Latitude and Longitude to a Given Addresses/Locations With Credentials
        @param location_addresses: Latitude and Longitude needed Addresses/Locations
        @return: Dict
            status: True or False based on success,
            message: Error message if an error occurred
            result:
              {
                'lat_lng_list': List of Longitudes and Latitudes of the Addresses Provided
                    'latitude':
                    'longitude':
                'all_results': Whole Response Object Received From Arc GIS
              }
        """

        # If Username and Password Not Set, Return an error Object
        # if self.username_password_flag:
        #     return self.__get_error_msg('Username or Password is not Set')

        try:
            GIS("http://www.arcgis.com", self.connection_params['username'], self.connection_params['password'])
            arc_gis_locations = batch_geocode(location_addresses)

            if len(arc_gis_locations) > 0:

                # Filter only Latitude and Longitude Values
                lat_lng_list = list(
                    map(lambda loc: {'longitude': loc['location']['x'], 'latitude': loc['location']['y']},
                        arc_gis_locations))

                return {
                    'status': True,
                    'message': None,
                    'result': {
                        'lat_lng_list': lat_lng_list,
                        'all_results': arc_gis_locations
                    }
                }
            else:
                return self.__get_error_msg('Unknown Location. No Results Found')

        except ConnectionError:
            return self.__get_error_msg('Connection Error')
        except TypeError:
            return self.__get_error_msg('Type Error')
        except Exception as e:
            return self.__get_error_msg('Unknown Error Occurred, Error: {}'.format(e))
