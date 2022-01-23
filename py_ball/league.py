#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:59:39 2018

@author: patrickmcfarlane

league.py contains the League class that
enables API calls for general league related endpoints
"""

from .utils import api_call, parse_api_call

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
        - **leaguegamelog**: Game logs at the player-level across multiple
        games
        - **playoffpicture**: Current state of the playoff picture by \
        conference.

    The League class has the following required parameters:

        @param **headers** (*dict*): Dictionary of request header information
            required by the API. Specifically, the API requires you to declare
            the 'User-Agent' key of the request header dictionary. More information
            can be found `here <https://stackoverflow.com/questions/46781563/
            how-to-obtain-a-json-response-from-the-stats-nba-com-api>`_ and
            an example request header dictionary can be found in the __init__.py
            file in the tests folder of this module.

        @param **league_id** (*str*): LeagueID in the API. String of a \
            two-digit number corresponding to the league. '00' is the NBA, \
            '10' is the WNBA, '01' is the ABA, and '20' is the G-League.

        @param **season** (*str*): Season in the API. String of a two-year
            season in a YYYY-ZZ format, where the ZZ are the last two \
            digits of the following year. For example, '2017-18' is a valid \
            value of **season** and represents the 2017-18 NBA season. \
            **season** is required by the 'commonallplayers' and \
            'commonplayoffseries' endpoints.

        @param **season_id** (*str*): SeasonID in the API. String of a year \
            season in a XYYYY format. X indicates the season type \
            ('1' for preseason, '2' for regular season, '4' for the playoffs). \
            For example, '22017' is a valid \
            value of **season_id** and represents the 2017-18 NBA regular
            season. **season_id** is required by the 'playoffpicture' \
            endpoint.

        @param **current_season** (*str*): IsOnlyCurrentSeason in the API. \
            Boolean value ('1' or '0') indicating whether only the current \
            season should be returned ('1'). A value of '0' returns all \
            players in league history. **current_season** is required by the \
            'commonallplayers' endpoint.

        @param **date_from** (*str*): DateFrom in the API. String of a date \
            in a MM/DD/YYYY format indicating the start date for which \
            data is to be returned.

        @param **date_to** (*str*): DateTo in the API. String of a date \
            in a MM/DD/YYYY format indicating the end date for which \
            data is to be returned.

        @param **season_type** (*str*): SeasonType in the API. String \
            indicating the type of season for data to be returned. \
            Valid values include:

                - 'Regular Season', 'Pre Season', 'Playoffs', 'All Star'

        @param **counter** (*str*): Counter in the API. Unknown definition

        @param **direction** (*str*): Direction in the API. Either
            ascending ("ASC") or descending ("DESC") to indicate the order
            in which to sort the data by the feature provided in **sorter**

        @param **sorter** (*str*): Sorter in the API. Variable name on which
            to sort the results. Valid values include variables returned
            in the response. Note, use "DATE" instead of "GAME_DATE"

        @param **player_or_team** (*str*): PlayerOrTeam in the API. String
            indicating whether to return data for a "Player" ("P") or "Team"
            ("T")

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

    def __init__(self, headers, endpoint='commonallplayers',
                 league_id='00', season='2017-18',
                 season_id='22017', current_season='1',
                 date_from='', date_to='', season_type="Regular Season",
                 counter="1000", direction="DESC", sorter="DATE",
                 player_or_team="P"):

        # Controlling the parameters depending on the endpoint
        if endpoint in ['commonteamyears', 'franchisehistory']:
            params = {'LeagueID': league_id}
        elif endpoint in ['commonplayoffseries']:
            params = {'LeagueID': league_id,
                      'Season': season}
        elif endpoint in ['playoffpicture']:
            params = {'LeagueID': league_id,
                      'SeasonID': season_id}
        elif endpoint in ["leaguegamelog"]:
            params = {'LeagueID': league_id,
                      'Season': season,
                      "DateFrom": date_from,
                      "DateTo": date_to,
                      "SeasonType": season_type,
                      "Counter": counter,
                      "Direction": direction,
                      "Sorter": sorter,
                      "PlayerOrTeam": player_or_team}
        else:
            params = {'LeagueID': league_id,
                      'Season': season,
                      'IsOnlyCurrentSeason': current_season}

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params,
                                 headers=headers)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)


