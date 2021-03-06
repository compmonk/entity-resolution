# -*- coding: utf-8 -*-

###############################################################################
#
# Trash
# Moves a file to the trash.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Google.Drive.GoogleFile import GoogleFile

import json

class Trash(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Trash Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Drive/Files/Trash')


    def new_input_set(self):
        return TrashInputSet()

    def _make_result_set(self, result, path):
        return TrashResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrashChoreographyExecution(session, exec_id, path)

class TrashInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Trash
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Selector specifying a subset of fields to include in the response.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_FileID(self, value):
        """
        Set the value of the FileID input for this Choreo. ((required, string) The ID of the file to trash.)
        """
        InputSet._set_input(self, 'FileID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)

class TrashResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Trash Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def getFile(self):
        """
        A Google Drive file resource
        """
        return GoogleFile(self.getJSONFromString(self._output.get('Response', [])))

class TrashChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TrashResultSet(response, path)
