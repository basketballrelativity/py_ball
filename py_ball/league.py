#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:59:39 2018

@author: patrickmcfarlane

league.py contains the League class that
enables API calls for general league related endpoints
"""

from __init__ import api_call, parse_api_call

class League:
    """ The League class contains all resources needed to use the league-
    related API calls. `stats.nba.com <https://stats.nba.com>`_
    has the following league-related API endpoints:

        - **commonallplayers**: Current roster information if the \
        **current_season** flag is '1', historical player information \
        if the **current_season** flag is '0'.
        - **commonteamyears**: Start and end dates for teams in league \
        history.
        - **commonplayoffseries**: Playoff series matchup breakdown by game.
        - **franchisehistory**: Current and defunct franchise histories, \
        including performance and franchise metadata.
        - **playoffpicture**: Current state of the playoff picture by \
        conference.

    The League class has the following required parameters:

        @param **league_id** (*str*): LeagueID in the API. String of a \
            two-digit number corresponding to the league. '00' is the NBA, \
            '10' is the WNBA, and '01' is the ABA.

        @param **season** (*str*): Season in the API. String of a two-year
            season in a YYYY-ZZ format, where the ZZ are the last two \
            digits of the following year. For example, '2017-18' is a valid \
            value of **season** and represents the 2017-18 NBA season. \
            **season** is required by the 'commonallplayers' and \
            'commonplayoffseries' endpoints.

        @param **season_id** (*str*): SeasonID in the API. String of a year \
            season in a YYYY format. For example, '2017' is a valid \
            value of **season_id** and represents the 2017-18 NBA season. \
            **season_id** is required by the 'playoffpicture' endpoint.

        @param **current_season** (*str*): IsOnlyCurrentSeason in the API. \
            Boolean value ('1' or '0') indicating whether only the current \
            season should be returned ('1'). A value of '0' returns all \
            players in league history. **current_season** is required by the \
            'commonallplayers' endpoint.

    Attributes:

        **api_resp** (*dict*): JSON object of the API response. The API \
            response has three keys. The 'resource' key describes the type of \
            response returned (the endpoint in this instance). The 'parameters' \
            key describes the parameters provided in the API call. The \
            'resultSets' key contains the data returned in the API call.

        **data** (*dict*): A dictionary of response names. Each response \
            name is a key to a list of dictionaries containing the \
            corresponding data.
    """

    def __init__(self, endpoint='commonallplayers',
                 league_id='00', season='2017-18',
                 season_id='2017', current_season='1'):

        # Controlling the parameters depending on the endpoint
        if endpoint in ['commonteamyears', 'franchisehistory']:
            params = {'LeagueID': league_id}
        elif endpoint in ['commonplayoffseries']:
            params = {'LeagueID': league_id,
                      'Season': season}
        elif endpoint in ['playoffpicture']:
            params = {'LeagueID': league_id,
                      'SeasonID': season_id}
        else:
            params = {'LeagueID': league_id,
                      'Season': season,
                      'IsOnlyCurrentSeason': current_season}

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)


