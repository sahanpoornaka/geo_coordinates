"""
Purpose:
This Class Contains Methods To Retrieve Geo Location Information From Google API.

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""
import json


class ExampleRunner:

    if __name__ == "__main__":

        """
        GOOGLE API CALL
        
        get_geo_coordinates_from_google: Retrieve Latitude and Longitude to a Given Address/Location
        get_lat_lng_altitude_from_google: Retrieve Altitude Information for a given Latitude and Longitude
        get_address_altitude_from_google: Retrieve Altitude Information for a given Address/Location
        """

        # Import The Module
        from GeoCoordinatesGoogle import GeoCoordinatesGoogle
        # Load Credentials
        with open('./credentials/google_cred.json', 'r') as file:
            google_cred = json.load(file)
        # Create an Object With Credentials to call the methods
        obj_google = GeoCoordinatesGoogle(google_cred['API_KEY'])

        print("get_geo_coordinates_from_google Result:")
        result = obj_google.get_geo_coordinates_from_google("Colombo")
        print(result)

        print("get_address_altitude_from_google Result:")
        result = obj_google.get_address_altitude_from_google("Kandy")
        print(result)

        print("get_altitude_from_google Result:")
        result = obj_google.get_altitude_from_google(7.487046, 80.364972)
        print(result)

        """
        HERE API CALL

        get_geo_coordinates_from_here: Retrieve Latitude and Longitude to a Given Address/Location
        """

        # Import The Module
        from GeoCoordinatesHere import GeoCoordinatesHere
        # Load Credentials
        with open('./credentials/here_cred.json', 'r') as file:
            here_cred = json.load(file)
        # Create an Object With Credentials to call the methods
        obj_here = GeoCoordinatesHere(here_cred['API_KEY'])

        print("get_geo_coordinates_from_here Result:")
        result = obj_here.get_geo_coordinates_from_here("Colombo")
        print(result)

        """
        ARC GIS API CALL

        get_geo_coordinates_from_arcgis:
            Retrieve Latitude and Longitude to a Given Address/Location (No Credentials are
        needed) get_geo_coordinates_from_arcgis_with_login:
            Retrieve Latitude and Longitude to a Given Address/Location (With Credentials)
        get_batch_geo_coordinates_from_arcgis_with_login:
            Retrieve Latitude and Longitude to a Given Addresses/Locations (With Credentials)
        """

        # Import The Module
        from GeoCoordinatesArcGIS import GeoCoordinatesArcGIS
        # Load Credentials
        with open('./credentials/arcgis_cred.json', 'r') as file:
            arc_cred = json.load(file)
        # Create an Object With Credentials to call the methods
        obj_arc = GeoCoordinatesArcGIS()
        obj_arc_login = GeoCoordinatesArcGIS(arc_cred['USERNAME'], arc_cred['PASSWORD'])

        print("get_geo_coordinates_from_arcgis Result:")
        result = obj_arc.get_geo_coordinates_from_arcgis("Colombo")
        print(result)

        print("get_geo_coordinates_from_arcgis_with_login Result:")
        result = obj_arc_login.get_geo_coordinates_from_arcgis_with_login("Kandy")
        print(result)

        print("get_batch_geo_coordinates_from_arcgis_with_login Result:")
        result = obj_arc_login.get_batch_geo_coordinates_from_arcgis_with_login(["New+York", "Los+Angeles", "Miami"])
        print(result)
