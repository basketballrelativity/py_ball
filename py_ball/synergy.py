#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:59:39 2019

@author: patrickmcfarlane

synergy.py contains the Synergy class that
enables API calls for synergy-related endpoints
"""

from .utils import api_call, parse_api_call

class Synergy:
    """ The Synergy class contains all resources needed to use the synergy-
    related API calls. `stats.nba.com <https://stats.nba.com>`_
    has the following league-related API endpoints:

        - **synergyplaytypes**: Season Synergy play type stats by
        player or team

    The Synergy class has the following required parameters:

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
            Note that Synergy statistics are only available for the NBA

        @param **season_year** (*str*): SeasonYear in the API. String of a two-year \
            season in a YYYY-ZZ format, where the ZZ are the last two \
            digits of the following year. For example, '2017-18' is a valid \
            value of **season_year** and represents the 2017-18 NBA season.

        @param **season_type** (*str*): SeasonType in the API. String \
            indicating the type of season for data to be returned. \
            Valid values include:

                - 'Regular Season', 'Pre Season', 'Playoffs', 'All Star'

        @param **per_mode** (*str*): PerMode in the API. String indicating \
            the type of rate stats to be returned. Valid values include:

                - 'Totals', 'PerGame', 'MinutesPer', 'Per48', 'Per40', \
                'Per36', 'PerMinute', 'PerPossession', 'PerPlay', \
                'Per100Possessions', 'Per100Plays'

        @param **player_or_team** (*str*): PlayerOrTeam in the API. String \
            indicating whether to return data for players ('P') or teams \
            ('T')

        @param **play_type** (*str*): PlayType in the API. String \
            indicating the type of play as defined by Synergy. Valid \
            values include:

                - 'Cut', 'Handoff', 'Isolation', 'Misc', 'OffScreen', \
                'Postup', 'PRBallHandler', 'PRRollman', 'OffRebound', \
                'Spotup', 'Transition'

        @param **type_grouping** (*str*): TypeGrouping in the API. String \
            indicating the side of the ball for the statistics to be returned. \
            One of 'offensive' or 'defensive'

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

    def __init__(self, headers, endpoint='synergyplaytypes',
                 league_id='00', season_year='2018-19',
                 season_type='Regular Season', per_mode='PerGame',
                 player_or_team='P', play_type='Cut',
                 type_grouping='offensive'):

        # Controlling the parameters depending on the endpoint
        params = {'LeagueID': league_id,
                  'SeasonYear': season_year,
                  'SeasonType': season_type,
                  'PerMode': per_mode,
                  'PlayerOrTeam': player_or_team,
                  'PlayType': play_type,
                  'TypeGrouping': type_grouping}

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params,
                                 headers=headers)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)

