#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:01:08 2018

@author: patrickmcfarlane

leaderboard.py contains the LeaderBoard class that
enables API calls for leader board endpoints
"""

from .utils import api_call, parse_api_call

class LeaderBoard:
    """ The LeaderBoard class contains all resources needed to use the
    leader board API calls. `stats.nba.com <https://stats.nba.com>`_
    has the following leader board API endpoints:

        - **homepageleaders**: Top 5 leaders in a number of statistical \
        categories.
        - **homepagev2**: Groups of top 5 leaders in statistical categories \
        related to a given concept.
        - **leaderstiles**: Top 5 leaders in a number of statistical \
        categories, some included in 'homepageleaders' and some \
        not.
        - **leagueleaders**: Longer list of league leaders in a number \
        of statistical categories.

    The LeaderBoard class has the following required parameters:

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

        @param **stat_category** (*str*): StatCategory in the API. String \
            corresponding to the **stat_category** desired in the API \
            response. Valid values include:

                - 'Points', 'Rebounds', 'Assists', 'Defense', \
                'Playmaking', 'Efficiency', 'Fast Break','Scoring Breakdown'

            The stat_category parameter is only required by the \
            'homepageleaders' endpoint.
        
        @param **stat_category_ll** (*str*): StatCategory in the API. String \
            corresponding to the **stat_category** desired in the API response. \
            Valid values include:

                - 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT' \
                'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST' \
                'STL', 'BLK', 'TOV', 'PTS', 'EFF'

            The **stat_category_ll** parameter is only required by the \
            'leagueleaders' endpoint.

        @param **stat_type** (*str*): StatType in the API. String corresponding \
            to the **stat_type** desired in the API response. Valid values \
            include:

                - 'Traditional', 'Advanced', 'Tracking'

            The **stat_type** parameter is only required by the 'homepagev2' \
            endpoint.

        @param **stat** (*str*): Stat in the API. String corresponding \
            to the **stat** desired in the API response. Valid values \
            include:

                - 'PTS', 'REB', 'AST', 'FG_PCT', 'FT_PCT', 'FG3_PCT' \
                'STL', 'BLK'

            The **stat** parameter is only required by the 'leaderstiles' \
            endpoint.

        @param **season** (*str*): Season in the API. String of a two-year \
            season in a YYYY-ZZ format, where the ZZ are the last two \
            digits of the following year. For example, '2017-18' is a valid \
            value of **season** and represents the 2017-18 NBA season.

        @param **season_type** (*str*): SeasonType in the API. String \
            indicating the type of season for which data is desired. \
            Valid values include:

                - 'Regular Season', 'Pre Season', 'Playoffs'

        @param **player_or_team** (*str*): PlayerOrTeam in the API. String \
            indicating whether data returned is for 'Player' or 'Team' \
            leaders.

        @param **game_scope** (*str*): GameScope in the API. String \
            indicating the period of time for which data is desired. \
            Valid values include:

                - 'Season', 'Last 10', 'Yesterday', 'Finals'

        @param **player_scope** (*str*): PlayerScope in the API. String \
            indicating the type of players for which data is desired. \
            Valid values include:

                - 'All Players', 'Rookies'

        @param **per_mode** (*str*): PerMode in the API. String \
            indicating the rate of the statistics to be returned. \
            Valid values include:

                - 'Totals', 'PerGame', 'Per48'

            The **per_mode** parameter is only required by the 'leagueleaders' \
            endpoint.

        @param **scope** (*str*): Scope in the API. String indicating \
            the type of players for which data is desired. This is \
            nearly identical to **player_scope** above, but for the \
            'leagueleaders' endpoint. Valid values include:

                - 'S' (All players), 'Rookies'

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

    def __init__(self, headers, endpoint='homepageleaders',
                 league_id='00', stat_category='Points',
                 stat_category_ll='PTS',
                 stat_type='Tracking', stat='PTS',
                 season='2017-18', season_type='Regular Season',
                 player_or_team='Player', game_scope='Season',
                 player_scope='All Players', per_mode='PerGame',
                 scope='S'):

        # Controlling the parameters depending on the endpoint
        params = {'LeagueID': league_id,
                  'Season': season,
                  'SeasonType': season_type,
                  'PlayerOrTeam': player_or_team,
                  'GameScope': game_scope,
                  'PlayerScope': player_scope}

        if endpoint == 'homepageleaders':
            params ['StatCategory'] = stat_category
        elif endpoint == 'homepagev2':
            params['StatType'] = stat_type
        elif endpoint == 'leaderstiles':
            params['Stat'] = stat
        elif endpoint == 'leagueleaders':
            params['StatCategory'] = stat_category_ll
            params['PerMode'] = per_mode
            params['Scope'] = scope

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params,
                                 headers=headers)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)
