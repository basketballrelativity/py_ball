#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:01:08 2018

@author: patrickmcfarlane

leaderboard.py contains the LeaderBoard class that
enables API calls for leader board endpoints
"""

from __init__ import api_call, parse_api_call

class LeaderBoard:
    """ The LeaderBoard class contains all resources needed to use the
    leader board API calls. stats.nba.com has the following leader board
    API endpoints:
        - homepageleaders: Top 5 leaders in a number of statistical
        categories.
        - homepagev2: Groups of top 5 leaders in statistical categories
        related to a given concept.
        - leaderstiles: Top 5 leaders in a number of statistical
        categories, some included in 'homepageleaders' and some
        not.
        - leagueleaders: Longer list of league leaders in a number
        of statistical categories.

    The LeaderBoard class has the following required parameters:

        @param league_id (LeagueID in the API): String of a two-digit
        number corresponding to the league. '00' is the NBA, '10' is
        the WNBA, and '01' is the ABA.

        @param stat_category (StatCategory in the API): String corresponding
        to the StatCategory desired in the API response. Valid values
        include:
            - 'Points', 'Rebounds', 'Assists', 'Defense', 'Clutch',
            'Playmaking', 'Efficiency', 'Fast Break','Scoring Breakdown'
        The stat_category parameter is only required by the 'homepageleaders'
        endpoint
        
        @param stat_category_ll (StatCategory in the API): String corresponding
        to the StatCategory desired in the API response. Valid values
        include:
            - 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT'
            'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST'
            'STL', 'BLK', 'TOV', 'PTS', 'EFF'
        The stat_category_ll parameter is only required by the 'leagueleaders'
        endpoint

        @param stat_type (StatType in the API): String corresponding
        to the StatType desired in the API response. Valid values
        include:
            - 'Traditional', 'Advanced', 'Tracking'
        The stat_type parameter is only required by the 'homepagev2'
        endpoint.

        @param stat (Stat in the API): String corresponding
        to the Stat desired in the API response. Valid values
        include:
            - 'PTS', 'REB', 'AST', 'FG_PCT', 'FT_PCT', 'FG3_PCT'
            'STL', 'BLK'
        The stat parameter is only required by the 'leaderstiles'
        endpoint.

        @param season (Season in the API): String of a two-year
        season in a YYYY-ZZ format, where the ZZ are the last two
        digits of the following year. For example, '2017-18' is a valid
        value of Season and represents the 2017-18 NBA season. Season is
        required by the 'commonallplayers' and 'commonplayoffseries'
        endpoints.

        @param season_type (SeasonType in the API): String indicating
        the type of season for which data is desired. Valid values include:
            - 'Regular Season', 'Pre Season', 'Playoffs'

        @param player_or_team (PlayerOrTeam in the API): String indicating
        whether data returned is for 'Player' or 'Team' leaders.

        @param game_scope (GameScope in the API): String indicating the
        period of time for which data is desired. Valid values include:
            - 'Season', 'Last 10', 'Yesterday', 'Finals'

        @param player_scope (PlayerScope in the API): String indicating
        the type of players for which data is desired. Valid values include:
            - 'All Players', 'Rookies'

        @param per_mode (PerMode in the API): String indicating the rate
        of the statistics to be returned. Valid values include:
            - 'Totals', 'PerGame', 'Per48'
        The per_mode parameter is only required by the 'leagueleaders'
        endpoint.

        @param scope (Scope in the API): String indicating the type of
        players for which data is desired. This is nearly identical to
        player_scope above, but for the 'leagueleaders' endpoint. Valid
        values include:
            - 'S' (All players), 'Rookies'

    Attributes:

        api_resp: JSON object of the API response. The API response
        has three keys. The 'resource' key describes the type of
        response returned (the endpoint in this instance). The 'parameters'
        key describes the parameters provided in the API call. The
        'resultSets' key contains the data returned in the API call.

        data: A dictionary of response names. Each response name is a
        key to a list of dictionaries containing the corresponding data.
    """

    def __init__(self, endpoint='homepageleaders',
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
                                 params=params)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)
