"""
Purpose:
This Class Contains Methods To Retrieve Geo Location Information From Google API.

get_geo_coordinates_from_google: Retrieve Latitude and Longitude to a Given Address/Location
get_lat_lng_altitude_from_google: Retrieve Altitude Information for a given Latitude and Longitude
get_address_altitude_from_google: Retrieve Altitude Information for a given Address/Location

Developers:
Kevin Patel (GitHub Username: PatelKeviin)
    get_geo_coordinates_from_google

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""
import logging
import logging.config
import requests


class GeoCoordinatesGoogle:

    # Set Log Level
    logging.basicConfig(filename='./log/google_log.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Class Variables
    connection_params: dict = {}

    def __init__(self, api_key: str, output_format: str = 'json') -> None:
        """
        Class Initializer
        @param output_format: Required Output Format
        @param api_key: Google API Key
        """
        self.connection_params = {'output_format': output_format, 'api_key': api_key}

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

    def get_geo_coordinates_from_google(self, location_address: str) -> dict:
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
        base_url = 'https://maps.googleapis.com/maps/api/geocode'
        endpoint = '{}/{}?address={}&key={}'.format(base_url,
                                                    self.connection_params['output_format'],
                                                    location_address,
                                                    self.connection_params['api_key']
                                                    )

        try:
            # make the GET request
            results = requests.get(endpoint).json()

            # check if codes were successfully obtained or not
            if results['status'] == 'OK':
                location = results['results'][0]['geometry']['location']

                return {
                    'status': True,
                    'message': None,
                    'result': {
                        'longitude': location['lng'],
                        'latitude': location['lat']
                    }
                }

            elif results['status'] == 'ZERO_RESULTS':
                return self.__get_error_msg('Zero Results')
        except ConnectionError:
            return self.__get_error_msg('Connection Error')
        except TypeError:
            return self.__get_error_msg('Type Error')
        except Exception as e:
            return self.__get_error_msg('Unknown Error Occurred, Error: {}'.format(e))

    def get_altitude_from_google(self, latitude: float, longitude: float):
        """
        purpose: Retrieve Latitude and Longitude to a Given Address/Location
        @param latitude: Latitude of the Location where Altitude is needed
        @param longitude: Longitude of the Location
        @return: Dict
            status: True or False based on success,
            message: Error message if an error occurred
            result:
              {
                'latitude': Latitude of the given location
                'longitude': Longitude of the given location
                'altitude': Altitude of the given location
              }
        """
        base_url = 'https://maps.googleapis.com/maps/api/elevation'
        endpoint = '{}/{}?locations={},{}&key={}'.format(base_url,
                                                         self.connection_params['output_format'],
                                                         latitude,
                                                         longitude,
                                                         self.connection_params['api_key']
                                                         )

        try:
            # make the GET request
            results = requests.get(endpoint).json()

            # check if codes were successfully obtained or not
            if results['status'] == 'OK':
                altitude = results['results'][0]['elevation']
                location = results['results'][0]['location']
                return {
                    'status': True,
                    'message': None,
                    'result': {
                        'latitude': location['lat'],
                        'longitude': location['lng'],
                        'altitude': altitude
                    }
                }

            elif results['status'] == 'ZERO_RESULTS':
                return self.__get_error_msg('Zero Results')
        except ConnectionError:
            return self.__get_error_msg('Connection Error')
        except TypeError:
            return self.__get_error_msg('Type Error')
        except Exception as e:
            return self.__get_error_msg('Unknown Error Occurred, Error: {}'.format(e))

    def get_address_altitude_from_google(self, location_address: str):
        """
        purpose: Retrieve Latitude and Longitude to a Given Address/Location
        @param location_address: Latitude and Longitude needed Address/Location
        @return: Dict
            status: True or False based on success,
            message: Error message if an error occurred
            result:
              {
                'latitude': Latitude of the given location
                'longitude': Longitude of the given location
                'altitude': Altitude of the given location
              }
        """
        try:
            lat_long = self.get_geo_coordinates_from_google(location_address)
            if lat_long['status']:
                latitude = lat_long['result']['latitude']
                longitude = lat_long['result']['longitude']
                resp = self.get_altitude_from_google(latitude, longitude)
                return {
                    'status': True,
                    'message': None,
                    'result': {
                        'latitude': resp['result']['latitude'],
                        'longitude': resp['result']['longitude'],
                        'altitude': resp['result']['altitude']
                    }
                }
            else:
                return lat_long

        except ConnectionError:
            return self.__get_error_msg('Connection Error')
        except TypeError:
            return self.__get_error_msg('Type Error')
        except Exception as e:
            return self.__get_error_msg('Unknown Error Occurred, Error: {}'.format(e))
