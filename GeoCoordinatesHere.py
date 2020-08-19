"""
Purpose:
This Class Contains Methods To Retrieve Geo Location Information From Here API.

get_geo_coordinates_from_here: Retrieve Latitude and Longitude to a Given Address/Location

Developers:
Kevin Patel (GitHub Username: PatelKeviin)
    get_geo_coordinates_from_here

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""
import logging
import requests


class GeoCoordinatesHere:
    # Set Log Level
    logging.basicConfig(filename='./log/google_log.txt', level=logging.INFO)

    # Class Variables
    connection_params: dict = {}

    def __init__(self, api_key: str) -> None:
        """
        Class Initializer
        @param api_key: Here API Key
        """
        self.connection_params = {'api_key': api_key}

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

    def get_geo_coordinates_from_here(self, location_address: str) -> dict:
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
        base_url = 'https://geocode.search.hereapi.com/v1/geocode'
        endpoint = '{}?q={}&apiKey={}'.format(base_url,
                                              location_address,
                                              self.connection_params['api_key']
                                              )

        try:
            # make the GET request
            results = requests.get(endpoint)

            # check if codes were successfully obtained or not
            if results.status_code == 200:
                items = results.json().get('items')
                if len(items) > 0:
                    location = items[0]['position']

                    return {
                        'status': True,
                        'message': None,
                        'result': {
                            'longitude': location['lng'],
                            'latitude': location['lat']
                        }
                    }
                else:
                    return self.__get_error_msg('Unknown Location. No Results Found')
            elif results.status_code == 400:
                return self.__get_error_msg('Request Failed Validation. Please Check your API key')
            elif results.status_code == 503:
                return self.__get_error_msg('Temporary Server Error. Please Check back again in a short while')
            else:
                return self.__get_error_msg('Some Unknown Error Occurred While Sending Request To Server')

        except ConnectionError:
            return self.__get_error_msg('Connection Error')
        except TypeError:
            return self.__get_error_msg('Type Error')
        except Exception as e:
            return self.__get_error_msg('Unknown Error Occurred, Error: {}'.format(e))
