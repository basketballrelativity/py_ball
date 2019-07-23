#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:08:30 2018

@author: patrickmcfarlane

draft.py contains the Draft class that
enables API calls for draft related endpoints
"""

from .utils import api_call, parse_api_call

class Draft:
    """ The Draft class contains all resources needed to use the draft-
    related API calls. `stats.nba.com <https://stats.nba.com>`_
    has the following draft-related API endpoints:

        - **draftcombinestats**: Draft combine drill results and measurement \
        data for players.
        - **drafthistory**: Draft results detailing metadata of draftees \
        by season.

    The Draft class has the following required parameters:

        @param **headers** (*dict*): Dictionary of request header information
            required by the API. Specifically, the API requires you to declare
            the 'User-Agent' key of the request header dictionary. More information
            can be found `here <https://stackoverflow.com/questions/46781563/
            how-to-obtain-a-json-response-from-the-stats-nba-com-api>`_ and
            an example request header dictionary can be found in the __init__.py
            file in the tests folder of this module.

        @param **league_id** (*str*): LeagueID in the API. String of a \
            two-digit number corresponding to the league. '00' is the NBA, \
            '10' is the WNBA, '01' is the ABA, and '20' is the G-League. \
            Draft data is only available for the NBA.

        @param **season_year** (*str*): SeasonYear in the API. String of \
            a two-year season year in a YYYY-ZZ format, where the ZZ are the \
            last two digits of the following year. For example, '2017-18' is \
            a valid value of **season_year** and represents the 2017-18 NBA season. \
            'All Time' is a valid value for the 'draftcombinestats' endpoint.

    Attributes:

        **api_resp** (*dict*): JSON object of the API response. The API \
            response has three keys. The 'resource' key describes the type of \
            response returned (the endpoint in this instance). The 'parameters' \
            key describes the parameters provided in the API call. The \
            'resultSets' key contains the data returned in the API call.

        **data** (*dict*): A dictionary of response names. Each response \
            name is a key to a list of dictionaries containing the corresponding \
            data.
    """

    def __init__(self, headers, endpoint='draftcombinestats',
                 league_id='00', season_year='2017-18'):

        # Controlling the parameters depending on the endpoint
        if endpoint in ['drafthistory']:
            params = {'LeagueID': league_id}
        else:
            params = {'LeagueID': league_id,
                      'SeasonYear': season_year}

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params,
                                 headers=headers)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)
