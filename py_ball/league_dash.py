#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:44:34 2018

@author: patrickmcfarlane

league_dash.py contains the LeagueDashboard class that
enables API calls for general league performance statitics
related endpoints
"""

from __init__ import api_call, parse_api_call

class LeagueDash:
    """ The LeagueDash class contains all resources needed
    to use the league performance stats related API calls. stats.nba.com
    has the following league performance stats related API endpoints:
        - leaguedashlineups
        - leaguedashplayerbiostats
        - leaguedashplayerclutch
        - leaguedashplayershotlocations
        - leaguedashplayerptshot
        - leaguedashplayerstats
        - leaguedashptdefend
        - leaguedashptteamdefend
        - leaguedashteamptshot

    The LeagueDash class has the following required parameters:

        @param league_id (LeagueID in the API): String of a two-digit
        number corresponding to the league. '00' is the NBA, '10' is
        the WNBA, and '01' is the ABA.

        @param season (Season in the API): String of a two-year
        season in a YYYY-ZZ format, where the ZZ are the last two
        digits of the following year. For example, '2017-18' is a valid
        value of Season and represents the 2017-18 NBA season. Season is
        required by the 'commonallplayers' and 'commonplayoffseries'
        endpoints.

        @param season_id (SeasonID in the API): String of a year
        season in a YYYY format. For example, '2017' is a valid
        value of SeasonID and represents the 2017-18 NBA season.
        SeasonID is required by the 'playoffpicture' endpoint.

        @param current_season (IsOnlyCurrentSeason in the API): Boolean
        value ('1' or '0') indicating whether only the current season
        should be returned ('1'). A value of '0' returns all players
        in league history. IsOnlyCurrentSeason is required by the
        'commonallplayers' endpoint.

    Attributes:

        api_resp: JSON object of the API response. The API response
        has three keys. The 'resource' key describes the type of
        response returned (the endpoint in this instance). The 'parameters'
        key describes the parameters provided in the API call. The
        'resultSets' key contains the data returned in the API call.

        data: A dictionary of response names. Each response name is a
        key to a list of dictionaries containing the corresponding data.
    """

    def __init__(self, endpoint='leaguedashlineups',
                 league_id='00', group_quantity='5',
                 per_mode='PerGame', plus_minus='N',
                 rank='Y', pace_adjust='N',
                 measure_type='Base', period='0',
                 vs_conference='', last_n_games='0',
                 team_id='0', location='', outcome='',
                 date_from='', date_to='', opp_team_id='0',
                 season='2017-18', vs_division='',
                 game_segment='', month='0',
                 season_type='Regular Season', season_segment='',
                 clutch_time='Last 5 Minutes',
                 ahead_behind='',
                 point_diff='0', game_scope='',
                 player_experience='',
                 player_position='', starters_bench=''):

        # Controlling the parameters depending on the endpoint
        if endpoint in ['leaguedashlineups']:
            params = {'LeagueID': league_id,
                      'GroupQuantity': group_quantity,
                      'PerMode': per_mode,
                      'PlusMinus': plus_minus,
                      'Rank': rank,
                      'PaceAdjust': pace_adjust,
                      'MeasureType': measure_type,
                      'Period': period,
                      'VsConference': vs_conference,
                      'Location': location,
                      'Outcome': outcome,
                      'DateFrom': date_from,
                      'DateTo': date_to,
                      'TeamID': team_id,
                      'OpponentTeamID': opp_team_id,
                      'Season': season,
                      'VsDivision': vs_division,
                      'GameSegment': game_segment,
                      'Month': month,
                      'SeasonType': season_type,
                      'SeasonSegment': season_segment,
                      'LastNGames': last_n_games}
        elif endpoint in ['leaguedashplayerbiostats']:
            params = {'LeagueID': league_id,
                      'PerMode': per_mode,
                      'Season': season,
                      'SeasonType': season_type}
        elif endpoint in ['leaguedashplayerclutch']:
            params = {'LeagueID': league_id,
                      'ClutchTime': clutch_time,
                      'AheadOrBehind': ahead_behind,
                      'PointDiff': point_diff,
                      'GameScope': game_scope,
                      'PlayerExperience': player_experience,
                      'PlayerPosition': player_position,
                      'StartersOrBench': starters_bench,
                      'PerMode': per_mode,
                      'PlusMinus': plus_minus,
                      'Rank': rank,
                      'PaceAdjust': pace_adjust,
                      'MeasureType': measure_type,
                      'Period': period,
                      'VsConference': vs_conference,
                      'Location': location,
                      'Outcome': outcome,
                      'DateFrom': date_from,
                      'DateTo': date_to,
                      'TeamID': team_id,
                      'OpponentTeamID': opp_team_id,
                      'Season': season,
                      'VsDivision': vs_division,
                      'GameSegment': game_segment,
                      'Month': month,
                      'SeasonType': season_type,
                      'SeasonSegment': season_segment,
                      'LastNGames': last_n_games}


        self.api_resp = api_call(endpoint=endpoint,
                                 params=params)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)




