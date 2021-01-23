#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:44:34 2018

@author: patrickmcfarlane

league_dash.py contains the LeagueDashboard class that
enables API calls for general league performance statitics
related endpoints
"""

from .utils import api_call, parse_api_call

class LeagueDash:
    """ The LeagueDash class contains all resources needed
    to use the league performance stats related API calls.
    `stats.nba.com <https://stats.nba.com>`_ has the following
    league performance stats related API endpoints:

        *- **leaguedashlineups**: Traditional and plus/minus statistics \
        for sets of lineups between sizes 2 to 5 players, inclusive.
        - **leaguedashplayerbiostats**: Player metadata and performance \
        statistics for a given season.
        *- **leaguedashplayerclutch**: Traditional, plus/minus, and rank \
        statistics for players in a defined clutch period.
        *- **leaguedashplayershotlocations**: Player shooting-related \
        statistics by shot distance/type.
        - **leaguedashplayerptshot**: Shooting-related statistics for \
        a given season by player.
        *- **leaguedashplayerstats**: Traditional, plus/minus, and rank \
        statistics for players.
        - **leaguedashptdefend**: Defensive statistics for a given season \
        by player.
        - **leaguedashptteamdefend**: Defensive statistics for a given \
        season by team.
        - **leaguedashteamptshot**: Shooting-related statistics for a \
        given season by team.

    The LeagueDash class has the following required parameters:

        @param **headers** (*dict*): Dictionary of request header information
            required by the API. Specifically, the API requires you to declare
            the 'User-Agent' key of the request header dictionary. More information
            can be found `here <https://stackoverflow.com/questions/46781563/
            how-to-obtain-a-json-response-from-the-stats-nba-com-api>`_ and
            an example request header dictionary can be found in the __init__.py
            file in the tests folder of this module.

        @param **league_id** (*str*): LeagueID in the API). String of a \
            two-digit number corresponding to the league. '00' is the NBA, \
            '10' is the WNBA, '01' is the ABA, and '20' is the G-League.

        @param **group_quantity** (*str*): GroupQuantity in the API. String \
            of an integer indicating the number of players to include a \
            lineup for the **leaguedashlineups** endpoint. The minimum value \
            is '2' and the maximum value is '5'.

        @param **per_mode** (*str*): PerMode in the API. String indicating \
            the type of rate stats to be returned. Valid values include:

                - 'Totals', 'PerGame', 'MinutesPer', 'Per48', 'Per40', \
                'Per36', 'PerMinute', 'PerPossession', 'PerPlay', \
                'Per100Possessions', 'Per100Plays'

        @param **plus_minus** (*str*): PlusMinus in the API. String \
            representing a Boolean value that indicates whether the values \
            being returned should be in plus-minus form. Valid values \
            include:

                - 'Y', 'N'

        @param **rank** (*str*): Rank in the API. String representing \
            a Boolean value that indicates whether the values being \
            returned should be in rank form. Valid values include:

                - 'Y', 'N'

        @param **pace_adjust** (*str*): PaceAdjust in the API. String \
            representing a Boolean value that indicates whether the \
            values being returned should be pace-adjusted. Valid \
            values include:

                - 'Y', 'N'

        @param **measure_type** (*str*): MeasureType in the API. String \
            indicating the set of statistics to be returned. Valid \
            values include:

                - 'Base', 'Advanced', 'Misc', 'Four Factors', 'Scoring', \
                'Opponent', 'Usage', 'Defense'

        @param **period** (*str*): Period in the API. String of an \
            integer value that corresponds to a desired quarter for data \
            to be returned. A value of '0' returns data across all quarters.

        @param **vs_conference** (*str*): VsConference in the API. String \
            indicating the conference of the opposing team for data to be \
            returned. An empty string returns data across all conferences. \
            Valid values include:

                - 'East', 'West', ''

        @param **last_n_games** (*str*): LastNGames in the API. String of \
            an integer indicating the desired number of most recent games \
            for data to be returned. A value of '0' returns data across \
            all previous games, subject to other constraints in the API call.

        @param **team_id** (*str*): TeamID in the API. String of a 10-digit \
            integer that uniquely identifies a team for which data is to \
            be returned.

        @param **location** (*str*): Location in the API. String indicating \
            the game location for the data to be returned. An empty string \
            returns data across both home and road games. Valid values \
            include:

                - 'Home', 'Road', ''

        @param **outcome** (*str*): Outcome in the API. String indicating \
            the game outcome for the data to be returned. An empty string \
            returns data across both wins and losses. Valid values include:

                - 'W', 'L', ''

        @param **date_from** (*str*): DateFrom in the API. String of a date \
            in a MM/DD/YYYY format indicating the start date for which \
            data is to be returned.

        @param **date_to** (*str*): DateTo in the API. String of a date \
            in a MM/DD/YYYY format indicating the end date for which \
            data is to be returned.

        @param **opp_team_id** (*str*): OpponentTeamID in the API. String \
            of a 10-digit integer that uniquely identifies an opposing \
            team for which data is to be returned.

        @param **season** (*str*): Season in the API. String of a two-year \
            season in a YYYY-ZZ format, where the ZZ are the last two \
            digits of the following year. For example, '2017-18' is a valid \
            value of **season** and represents the 2017-18 NBA season.

        @param **vs_division** (*str*): VsDivision in the API. String \
            indicating the division of the opposing team for data to be \
            returned. An empty string returns data across all divisions. \
            Valid values include:

                - 'Atlantic', 'Central', 'Northwest', 'Pacific', \
                'Southeast', 'Southwest', 'East', 'West',  ''

            The 'East' and 'West' values correspond to conferences.

        @param **game_segment** (*str*): GameSegment in the API. String \
            indicating the section of a game for data to be returned. \
            An empty string returns data across all game segments. \
            Valid values include:

                - 'First Half', 'Overtime', 'Second Half', ''

        @param **month** (*str*): Month in the API. String of an integer \
            corresponding to a month for data to be returned. \
            A value of '0' returns data across all months.

        @param **season_type** (*str*): SeasonType in the API. String \
            indicating the type of season for data to be returned. \
            Valid values include:

                - 'Regular Season', 'Pre Season', 'Playoffs', 'All Star'

        @param **season_segment** (*str*): SeasonSegment in the API. String \
            indicating the section of the season for data to be returned. \
            An empty string returns data across all season segments. \
            Valid values include:

                - 'Pre All-Star', 'Post All-Star', ''

        @param **clutch_time** (*str*): ClutchTime in the API. String that \
            defines the type of clutch time for the data to be returned. \
            Valid values include:

                - 'Last 5 Minutes', 'Last 4 Minutes', 'Last 3 Minutes', \
                'Last 2 Minutes', 'Last 1 Minute', 'Last 30 Seconds', \
                'Last 10 Seconds'

        @param **ahead_behind** (*str*): AheadBehind in the API. String \
            indicating the type of score differential for the data to \
            be returned. Valid values include:

                - 'Ahead or Behind', 'Behind or Tied', 'Ahead or Tied'

        @param **point_diff** (*str*): PointDiff in the API. String of zero \
            or a positive integer indicating the maximum point \
            differential for data to be returned. 

        @param **game_scope** (*str*): GameScope in the API. String \
            indicating the recency of the data to be returned. An \
            empty string returns data across all past games, subject \
            to other constraints in the API call. Valid values include:

                - 'Yesterday', 'Last 10', ''

        @param **player_experience** (*str*): PlayerExperience in the API. \
            String indicating the level of player experience for data to be \
            returned. An empty string returns data across all levels \
            of player experience. Valid values include:

                - 'Rookie', 'Sophomore', 'Veteran', ''

        @param **player_position** (*str*): PlayerPosition in the API. \
            String indicating the player position for data to be returned. \
            An empty string returns data across all player positions. Valid \
            values include:

                - 'F', 'C', 'G', 'C-F', 'F-C', 'F-G', 'G-F', ''

        @param **starters_bench** (*str*): StarterBench in the API. String \
            indicating whether data should be returned for either or both \
            starters or bench players. An empty string returns data across \
            both starters and bench players. Valid values include:

                - 'Starters', 'Bench', ''

        @param **distance_range** (*str*): DistanceRange in the API. String \
            indicating the size/type of the distance range bins for data \
            to be returned. Valid values include:

                - '5ft Range', '8ft Range', 'By Zone'

        @param **defense_category** (*str*): DefenseCategory in the API. \
            String indicating the shot type of defensive data to be returned. \
            Valid values include:

                - 'Overall', '3 Pointers', '2 Pointers', 'Less Than 6Ft', \
                'Less Than 10Ft', 'Greater Than 15Ft'

    Attributes:

        **api_resp** (*dict*): JSON object of the API response. The API \
            response has three keys. The 'resource' key describes the \
            type of response returned (the endpoint in this instance). \
            The 'parameters' key describes the parameters provided in the \
            API call. The 'resultSets' key contains the data returned in \
            the API call.

        **data** (*dict*): A dictionary of response names. Each response \
            name is a key to a list of dictionaries containing the \
            corresponding data.
    """

    def __init__(self, headers, endpoint='leaguedashlineups',
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
                 ahead_behind='Ahead or Behind',
                 point_diff='0', game_scope='',
                 player_experience='',
                 player_position='', starters_bench='',
                 distance_range='By Zone',
                 defense_category='Overall',
                 player_or_team="Player",
                 pt_measure_type='SpeedDistance'):

        # Controlling the parameters depending on the endpoint
        if endpoint not in ['leaguedashplayerbiostats',
                            'leaguedashplayerptshot',
                            'leaguedashteamptshot',
                            'leaguedashptdefend',
                            'leaguedashptteamdefend']:
            params = {'LeagueID': league_id,
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
                      'LastNGames': last_n_games,
                      'GameScope': game_scope,
                      'PlayerExperience': player_experience,
                      'PlayerPosition': player_position,
                      'StarterBench': starters_bench}
        else:
            params = {'LeagueID': league_id,
                      'PerMode': per_mode,
                      'Season': season,
                      'SeasonType': season_type}

        if endpoint in ['leaguedashlineups']:
            params['GroupQuantity'] = group_quantity
        elif endpoint in ['leaguedashplayerclutch',
                          'leaguedashteamclutch']:
            params['ClutchTime'] = clutch_time
            params['AheadBehind'] = ahead_behind
            params['PointDiff'] = point_diff
        elif endpoint in ['leaguedashplayershotlocations',
                          'leaguedashteamshotlocations']:
            params['DistanceRange'] = distance_range
        elif endpoint in ['leaguedashptdefend',
                          'leaguedashptteamdefend']:
            params['DefenseCategory'] = defense_category
        elif endpoint in ["leaguedashptstats"]:
            params["PlayerOrTeam"] = player_or_team
            params["PtMeasureType"] = pt_measure_type


        self.api_resp = api_call(endpoint=endpoint,
                                 params=params,
                                 headers=headers)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)
