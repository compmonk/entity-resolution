# coding: utf-8

class FoursquareMayorship:
    """
     Contains venues that this user is mayor of
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getVenue(self):
        return FoursquareVenue(self.base.get("venue", []))

    def getBase(self):
        """
        Internal utility method; retrieve the base JSON object for this element of the response data.
        """
        return self.base

    def getJSONObject(self, json, key):
        """
        Internal utility method; retrieve a sub-object from a JSON object/array; returns an empty object if key is not present
        """
        toReturn = {}

        if json is not None:
            toReturn = json.get(key, {})

        return toReturn

from temboo.outputs.Foursquare.FoursquareVenue import FoursquareVenue