#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 20:44:34 2022

@author: patrickmcfarlane

league_hustle.py contains the LeagueHustle class that
enables API calls for player and team hustle stats
"""

from .utils import api_call, parse_api_call

class LeagueHustle:
    """ The LeagueHustle class contains all resources needed
    to use the league hustle stats related API calls.
    `stats.nba.com <https://stats.nba.com>`_ has the following
    league performance stats related API endpoints:

        *- **leaguehustlestatsplayer**: Player hustle stats.

    The LeagueHustle class has the following required parameters:

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

    def __init__(self, headers, endpoint='leaguehustlestatsplayer',
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
                 game_scope='',
                 player_experience='',
                 player_position='', starters_bench='',):

        # Controlling the parameters depending on the endpoint
        if endpoint == "leaguehustlestatsplayer":
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


        self.api_resp = api_call(endpoint=endpoint,
                                 params=params,
                                 headers=headers)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)
