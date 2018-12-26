#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:29:03 2018

@author: patrickmcfarlane

playbyplay.py contains the PlayByPlay class that
enables API calls for two play-by-play (pbp) endpoints
"""

from .utils import api_call, parse_api_call

class PlayByPlay:
    """ The PlayByPlay class contains all resources needed to use the 
    pbp-related API calls. `stats.nba.com <https://stats.nba.com>`_
    has the following pbp-related API endpoints:

        - **playbyplay**: Game play-by-play with basic fields, such as \
        play desscription, score, margin, period, and game time.
        - **playbyplayv2**: Game play-by-play with the basic fields above, \
        as well as player information of those involved in the play.

    The PlayByPlay class has the following required parameters:

        @param **headers** (*dict*): Dictionary of request header information
            required by the API. Specifically, the API requires you to declare
            the 'User-Agent' key of the request header dictionary. More information
            can be found `here <https://stackoverflow.com/questions/46781563/
            how-to-obtain-a-json-response-from-the-stats-nba-com-api>`_ and
            an example request header dictionary can be found in the __init__.py
            file in the tests folder of this module.

        @param **game_id** (*str*): GameID in the API. 10-digit string \
            that represents a unique game. The format is two leading zeroes, \
            followed by a season indicator number ('1' for preseason, \
            '2' for regular season, '4' for the post-season), \
            then the trailing digits of the season in which the game \
            took place (e.g. '17' for the 2017-18 season). The following \
            5 digits increment from '00001' in order as the season progresses. \
            For example, '0021600001' is the **game_id** of the first game \
            of the 2016-17 NBA regular season.

        @param **start_period** (*str*): StartPeriod in the API. String of \
            an integer that corresponds to the period for which the \
            boxscore begins.

        @param **end_period** (*str*): EndPeriod in the API. String of an \
            integer that corresponds to the period for which the \
            boxscore ends (Overtime increments logically, e.g. '5' is \
            the first overtime period).

    Attributes:

        **api_resp** (*dict*): JSON object of the API response. The API \
            response has three keys. The 'resource' key describes the \
            type of response returned ('playbyplay' in this instance). \
            The 'parameters' key describes the parameters provided in \
            the API call. The 'resultSets' key contains the data returned \
            in the API call.

        **data** (*dict*): A dictionary of response names. Each response \
            name is a key to a list of dictionaries containing the \
            corresponding data.
    """

    def __init__(self, headers, game_id, endpoint='playbyplay',
                 start_period='1', end_period='10'):

        # Controlling the parameters depending on the endpoint
        params = {'GameID': game_id,
                  'StartPeriod': start_period,
                  'EndPeriod': end_period}

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params,
                                 headers=headers)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)
