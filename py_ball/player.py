#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:47:46 2018

@author: patrickmcfarlane

player.py contains the Player class that
enables API calls for player-related
endpoints
"""

from .utils import api_call, parse_api_call

class Player:
    """ The Player class contains all resources needed
    to use the player-related API calls. `stats.nba.com <https://stats.nba.com>`_
    has the following player performance stats related API endpoints:

        - **playercareerstats**: Season and career stats for a given player, \
        broken down by season type (including college).
        - **playercompare**: Individual and combined (overall) statistics \
        for a given list of players and opposing players.
        - **playerdashboardbyclutch**: Traditional and rank statistics broken \
        down by different definitions of clutch for a player.
        - **playerdashboardbygamesplits**: Traditional and rank statistics \
        broken down by different splits (half, quarter, and score \
        differential).
        - **playerdashboardbygeneralsplits**: Traditional and rank statistics \
        broken down by different splits (win/loss, location, month, \
        pre/post All-Star, days rest). 
        - **playerdashboardbylastngames**: Traditional and rank statistics \
        broken down by the number of n recent games and game number \
        bins.
        - **playerdashboardbyopponent**: Traditional and rank statistics \
        broken down by opponent splits (conference, division, and \
        individual team).
        - **playerdashboardbyshootingsplits**: Traditional and rank statistics \
        broken down by shooting splits (shot distance, shot area, \
        assisted/unassisted, shot type, and indivdual assistant).
        - **playerdashboardbyteamperformance**: Traditional and rank statistics \
        broken down by team performance splits (win/loss, score differential, \
        points for, and points against).
        - **playerdashboardbyyearoveryear**: Traditional and rank statistics \
        broken down by year.
        - **playerdashptpass**: Shooting statistics for passes to and from \
        a player broken down by teammates.
        - **playerdashptreb**: Rebound statistics broken down by shot type, \
        contesting players, and shot/rebound distance.
        - **playerdashptshotdefend**: Defensive statistics broken down \
        by shot type/distance.
        - **playerdashptshots**: Shooting statistics broken down by shot \
        type, shot clock time, number of tribbles, defender proximity, and \
        length of touch.
        - **playergamelog**: Game log statistics for a given year.
        - **playerprofilev2**: Career and season summary statistics broken down \
        by season type.
        - **playervsplayer**: Player statistics versus a given opponent player \
        broken down by several shooting related splits (shot distance and \
        area)
        - **playersvsplayers**: Currently not available
        - **shotchartdetail**: Player and league shot chart data giving results \
        and location-related information for several player actions, \
        such as shots and fouls.

    The Player class has the following required parameters:

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

        @param **player_id** (*str*): PlayerID in the API. String of an \
            integer corresponding to a player ID for a given player.

        @param **player_id_list** (*str*): PlayerIDList in the API. String \
            of a comma-separated list of player IDs for player comparisons \
            to the players given in **vs_player_id_list**. Valid only for \
            the 'playercompare' endpoint.

        @param **vs_player_id_list** (*str*): VsPlayerIDList in the API. 
            String of a comma-separated list of player IDs for player \
            comparisons to the players given in **player_id_list**. \
            Valid only for the 'playercompare' endpoint.

        @param **per_mode** (*str*): PerMode in the API String indicating \
            the type of rate stats to be returned. Valid values include:

                - 'Totals', 'PerGame', 'MinutesPer', 'Per48', 'Per40', \
                'Per36', 'PerMinute', 'PerPossession', 'PerPlay', \
                'Per100Possessions', 'Per100Plays'

        @param **plus_minus** (*str*): PlusMinus in the API. String \
            representing a Boolean value that indicates whether the values \
            being returned should be in plus-minus form. Valid values \
            include:

                - 'Y', 'N'

        @param **rank** (*str*): Rank in the API. String representing a \
            Boolean value that indicates whether the values being returned \
            should be in rank form. Valid values include:

                - 'Y', 'N'

        @param **pace_adjust** (*str*): PaceAdjust in the API. String \
            representing a Boolean value that indicates whether the values \
            being returned should be pace-adjusted. Valid values include:

                - 'Y', 'N'

        @param **measure_type** (*str*): MeasureType in the API. String \
            indicating the set of statistics to be returned. Valid values \
            include:

                - 'Base', 'Advanced', 'Misc', 'Four Factors', 'Scoring', \
                'Opponent', 'Usage', 'Defense'

        @param **period** (*str*): Period in the API. String of an integer \
            value that corresponds to a desired quarter for data to be \
            returned. A value of '0' returns data across all quarters.

        @param **vs_conference** (*str*): VsConference in the API. String \
            indicating the conference of the opposing team for data to be \
            returned. An empty string returns data across all conferences. \
            Valid values include:

                - 'East', 'West', ''

        @param **last_n_games** (*str*): LastNGames in the API. String of an \
            integer indicating the desired number of most recent games \
            for data to be returned. A value of '0' returns data across \
            all previous games, subject to other constraints in the API call.

        @param **team_id** (*str*): TeamID in the API. String of a 10-digit \
            integer that uniquely identifies a team for which data is to \
            be returned.

        @param **location** (*str*): Location in the API. String indicating \
            the game location for the data to be returned. An empty \
            string returns data across both home and road games. \
            Valid values include:

                - 'Home', 'Road', ''

        @param **outcome** (*str*): Outcome in the API. String indicating \
            the game outcome for the data to be returned. An empty \
            string returns data across both wins and losses. Valid \
            values include:

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
            corresponding to a month for data to be returned. A value \
            of '0' returns data across all months.

        @param **season_type** (*str*): SeasonType in the API. String \
            indicating the type of season for data to be returned. \
            Valid values include:

                - 'Regular Season', 'Pre Season', 'Playoffs', 'All Star'

        @param **season_segment** (*str*): SeasonSegment in the API. String \
            indicating the section of the season for data to be returned. \
            An empty string returns data across all season segments. \
            Valid values include:

                - 'Pre All-Star', 'Post All-Star', ''

        @param **vs_player_id** (*str*): VsPlayerID in the API. String of \
            an integer corresponding to a player ID for a given player.

        @param **player_team_id** (*str*): PlayerTeamID in the API. String \
            of an integer corresponding to a team ID for a given team.

        @param **vs_player_team_id** (*str*): VsPlayerTeamID in the API. \
            String of an integer corresponding to a team ID for a given team.

        @param **player_id_x** (*str*): PlayerIDX in the API. String of an \
            integer corresponding to a player ID for a given player. \
            The x (X in the API) is an integer 1 through 5. Valid only \
            for the 'playersvsplayers' endpoint.

        @param **vs_player_id_x** (*str*): VsPlayerIDX in the API. String \
            of an integer corresponding to a player ID for a given player. \
            The x (X in the API) is an integer 1 through 5. Valid only for \
            the 'playersvsplayers' endpoint.

        @param **rookie_year** (*str*): RookieYear in the API. String of \
            a two-year  season in a YYYY-ZZ format, where the ZZ are the \
            last two digits of the following year. For example, '2017-18' \
            is a valid value of **rookie_year** and represents the 2017-18 \
            NBA season. This field should correspond to the rookie year of \
            the player given.

        @param **context_measure** (*str*): ContextMeasure in the API. String \
            of an abbreviated statistic corresponding to the type of action \
            to be included in the data returned. Valid values include:

                - 'PTS', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', \
                'PF', 'EFG_PCT', 'TS_PCT', 'PTS_FB', 'PTS_OFF_TOV', \
                'PTS_2ND_CHANCE', 'PF'

        @param **player_position** (*str*): PlayerPosition in the API. \
            String of a basketball position corresponding to the position \
            of the player given. An empty string returns data across all \
            positions played. Valid values include:

                - 'Guard', 'Center', 'Forward'

        @param **game_id** (*str*): GameID in the API. 10-digit string \
            that represents a unique game. The format is two leading \
            zeroes, followed by a season indicator number ('1' for \
            preseason, '2' for regular season, '4' for the post-season), \
            then the trailing digits of the season in which the game \
            took place (e.g. '17' for the 2017-18 season). The following \
            5 digits increment from '00001' in order as the season progresses. \
            For example, '0021600001' is the **game_id** of the first game of \
            the 2016-17 NBA regular season.

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

    def __init__(self, headers, endpoint='playercareerstats',
                 player_id='2544',
                 player_id_list='2544', vs_player_id_list='201939',
                 league_id='00',
                 per_mode='PerGame', plus_minus='N',
                 rank='Y', pace_adjust='N',
                 measure_type='Base', period='0',
                 vs_conference='', last_n_games='0',
                 team_id='0', location='', outcome='',
                 date_from='', date_to='', opp_team_id='0',
                 season='2017-18', vs_division='',
                 game_segment='', month='0',
                 season_type='Regular Season', season_segment='',
                 vs_player_id='201939',
                 player_team_id='1610612747',
                 vs_player_team_id='1610612744',
                 player_id_1='2544', player_id_2='0',
                 player_id_3='0', player_id_4='0',
                 player_id_5='0',
                 vs_player_id_1 = '201939', vs_player_id_2='0',
                 vs_player_id_3='0', vs_player_id_4='0',
                 vs_player_id_5='0', rookie_year='',
                 context_measure = 'FGA', player_position='',
                 game_id='0011800079'):

        # Controlling the parameters depending on the endpoint
        if endpoint not in ['playercareerstats', 'playergamelog',
                            'playerprofilev2']:
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
                      'PlayerID': player_id,
                      'OpponentTeamID': opp_team_id,
                      'Season': season,
                      'VsDivision': vs_division,
                      'GameSegment': game_segment,
                      'Month': month,
                      'SeasonType': season_type,
                      'SeasonSegment': season_segment,
                      'LastNGames': last_n_games}
        elif endpoint in  ['playercareerstats',
                          'playerprofilev2']:
            params = {'PlayerID': player_id,
                      'PerMode': per_mode}
        elif endpoint == 'playergamelog':
            params = {'PlayerID': player_id,
                      'Season': season,
                      'SeasonType': season_type}
        

        if endpoint in ['playercompare']:
            params['PlayerIDList'] = player_id_list
            params['VsPlayerIDList'] = vs_player_id_list
        elif endpoint in ['playerdashptpass']:
            del params['PlusMinus'], params['PaceAdjust']
            del params['Rank'], params['MeasureType']
            del params['Period'], params['GameSegment']
            params['TeamID'] = team_id
        elif endpoint in ['playerdashptreb',
                          'playerdashptshotdefend',
                          'playerdashptshots']:
            del params['PlusMinus'], params['PaceAdjust']
            del params['Rank'], params['MeasureType']
            params['TeamID'] = team_id
        elif endpoint in ['playervsplayer']:
            params['PlayerID'] = player_id
            params['VsPlayerID'] = vs_player_id
        elif endpoint in ['playersvsplayers']:
            params['PlayerTeamID'] = player_team_id
            params['VsTeamID'] = vs_player_team_id
            params['PlayerID1'] = player_id_1
            params['PlayerID2'] = player_id_2
            params['PlayerID3'] = player_id_3
            params['PlayerID4'] = player_id_4
            params['PlayerID5'] = player_id_5
            params['VsPlayerID1'] = vs_player_id_1
            params['VsPlayerID2'] = vs_player_id_2
            params['VsPlayerID3'] = vs_player_id_3
            params['VsPlayerID4'] = vs_player_id_4
            params['VsPlayerID5'] = vs_player_id_5
        elif endpoint in ['shotchartdetail']:
            params['TeamID'] = team_id
            params['RookieYear'] = rookie_year
            params['ContextMeasure'] = context_measure
            params['PlayerPosition'] = player_position
            params['GameID'] = game_id

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params,
                                 headers=headers)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)
