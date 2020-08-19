"""
Purpose: Test Cases to Test "GeoCoordinates.py"

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""

import json
import logging
import pytest

from GeoCoordinatesGoogle import GeoCoordinatesGoogle
from GeoCoordinatesHere import GeoCoordinatesHere
from GeoCoordinatesArcGIS import GeoCoordinatesArcGIS


class TestGeoCoordinates:

    # Set Log Level
    logging.basicConfig(filename='./log/test_log.txt', level=logging.INFO)

    # Open Credentials
    with open("./credentials/google_cred.json", 'r') as file:
        google_cred = json.load(file)

    with open("./credentials/here_cred.json", 'r') as file:
        here_cred = json.load(file)

    with open("./credentials/arcgis_cred.json", 'r') as file:
        arc_cred = json.load(file)

    # Create Objects
    obj_google = GeoCoordinatesGoogle(google_cred['API_KEY'])
    obj_here = GeoCoordinatesHere(here_cred['API_KEY'])
    obj_arc = GeoCoordinatesArcGIS(arc_cred['USERNAME'], arc_cred['PASSWORD'])

    # Google
    @pytest.mark.parametrize("address_, expect", [
        ("Boise,+US", {'longitude': -116.2023137, 'latitude': 43.6150186}),
        ("Colombo,+Sri+Lanka", {'longitude': 79.861243, 'latitude': 6.9270786})
    ])
    def test_get_geo_coordinates_from_google(self, address_, expect):

        exp_lat = expect['latitude']
        exp_lng = expect['longitude']

        lat_lng_google = self.obj_google.get_geo_coordinates_from_google(address_)
        if lat_lng_google['status']:
            resp_lat = lat_lng_google['result']['latitude']
            resp_lng = lat_lng_google['result']['longitude']
            assert resp_lat == pytest.approx(exp_lat, 0.001) and resp_lng == pytest.approx(exp_lng, 0.001)
        else:
            assert False

    @pytest.mark.parametrize("latitude, longitude, expect", [
        (43.6150186, -116.2023137, 822.3980712890625),
        (6.9270786, 79.861243, 11.43205261230469)
    ])
    def test_get_altitude_from_google(self, latitude, longitude, expect):
        response = self.obj_google.get_altitude_from_google(latitude, longitude)

        if response['status']:
            res_latitude = response['result']['latitude']
            res_longitude = response['result']['longitude']
            res_altitude = response['result']['altitude']

            assert res_latitude == pytest.approx(latitude, 0.001) \
                   and res_longitude == pytest.approx(longitude, 0.001) \
                   and res_altitude == pytest.approx(expect, 0.001)
        else:
            assert False

    @pytest.mark.parametrize("address_, expect", [
        ("Boise,+US", {'longitude': -116.2023137, 'latitude': 43.6150186,
                       'altitude': 822.3980712890625}),
        ("Colombo,+Sri+Lanka", {'longitude': 79.861243, 'latitude': 6.9270786,
                                'altitude': 11.43205261230469})
    ])
    def test_get_address_altitude_from_google(self, address_, expect):

        exp_lat = expect['latitude']
        exp_lng = expect['longitude']
        exp_alt = expect['altitude']

        response = self.obj_google.get_address_altitude_from_google(address_)
        if response['status']:
            resp_lat = response['result']['latitude']
            resp_lng = response['result']['longitude']
            resp_alt = response['result']['altitude']

            assert resp_lat == pytest.approx(exp_lat, 0.001) \
                   and resp_lng == pytest.approx(exp_lng, 0.001) \
                   and resp_alt == pytest.approx(exp_alt, 0.001)
        else:
            assert False

    # Here
    @pytest.mark.parametrize("address_, expect", [
        ("Boise,+US", {'longitude': -116.19341, 'latitude': 43.60765}),
        ("Colombo,+Sri+Lanka", {'latitude': 6.93243, 'longitude': 79.84588})
    ])
    def test_get_geo_coordinates_from_here(self, address_, expect):
        exp_lat = expect['latitude']
        exp_lng = expect['longitude']

        response = self.obj_here.get_geo_coordinates_from_here(address_)
        if response['status']:
            resp_lat = response['result']['latitude']
            resp_lng = response['result']['longitude']
            assert resp_lat == pytest.approx(exp_lat, 0.001) and resp_lng == pytest.approx(exp_lng, 0.001)
        else:
            assert False

    # Arc GIS
    @pytest.mark.parametrize("address_, expect", [
        ("Boise,+US", {'latitude': 43.60764000000006, 'longitude': -116.19339999999994}),
        ("Colombo,+Sri+Lanka", {'latitude': 6.932430000000068, 'longitude': 79.84588000000008})
    ])
    def test_get_geo_coordinates_from_arcgis(self, address_, expect):
        exp_lat = expect['latitude']
        exp_lng = expect['longitude']

        response = self.obj_arc.get_geo_coordinates_from_arcgis(address_)
        if response['status']:
            resp_lat = response['result']['latitude']
            resp_lng = response['result']['longitude']
            assert resp_lat == pytest.approx(exp_lat, 0.001) and resp_lng == pytest.approx(exp_lng, 0.001)
        else:
            assert False

    @pytest.mark.parametrize("address_, expect", [
        ("Boise,+US", {'latitude': 43.60764000000006, 'longitude': -116.19339999999994}),
        ("Colombo,+Sri+Lanka", {'latitude': 6.932430000000068, 'longitude': 79.84588000000008})
    ])
    def test_get_geo_coordinates_from_arcgis_with_login(self, address_, expect):
        exp_lat = expect['latitude']
        exp_lng = expect['longitude']

        response = self.obj_arc.get_geo_coordinates_from_arcgis_with_login(address_)
        if response['status']:
            resp_lat = response['result']['latitude']
            resp_lng = response['result']['longitude']
            assert resp_lat == pytest.approx(exp_lat, 0.001) and resp_lng == pytest.approx(exp_lng, 0.001)
        else:
            assert False

    @pytest.mark.parametrize("addresses_, expect", [
        (["Albany", "Boston", "Denver"], [[42.65155000000004, -73.75520999999998],
                                          [42.35866000000004, -71.05673999999993],
                                          [39.74001000000004, -104.99201999999997]])
    ])
    def test_get_batch_geo_coordinates_from_arcgis_with_login(self, addresses_, expect):

        response = self.obj_arc.get_batch_geo_coordinates_from_arcgis_with_login(addresses_)
        if response['status']:
            for res, exp in zip(response['result']['lat_lng_list'], expect):
                exp_lat = exp[0]
                exp_lng = exp[1]
                resp_lat = res['latitude']
                resp_lng = res['longitude']
                assert resp_lat == pytest.approx(exp_lat, 0.001) and resp_lng == pytest.approx(exp_lng, 0.001)
        else:
            assert False
