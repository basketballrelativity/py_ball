#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:36:55 2018

@author: patrickmcfarlane

boxscore.py contains the BoxScore class that
enables API calls for boxscore related endpoints
"""

from .utils import api_call, parse_api_call

class BoxScore:
    """
    The BoxScore class contains all resources needed to use the boxscore-
    related API calls. `stats.nba.com <https://stats.nba.com>`_
    has the following boxscore-related API endpoints:

        - **boxscoreadvancedv2**: Game boxscore containing several advanced \
        statistics
        - **boxscorefourfactorsv2**: Game boxscore containing statistics related \
        to the Four Factors, for team and opponent
        - **boxscoremiscv2**: Game boxscore containing points scored by type \
        of change (paint, fastbreak, etc.) for team and opponent
        - **boxscoreplayertrackv2**: Game boxscore containing aggregated player \
        tracking statistics
        - **boxscorescoringv2**: Game boxscore containing percentage scoring \
        statistics broken down by shot type.
        - **boxscoresummaryv2**: Game boxscore containing a summary of a \
        particular matchup (including game metadata and results)
        - **boxscoretraditionalv2**: Game boxscore containing basic statistics
        - **boxscoreusagev2**: Game boxscore containing usage statistics \
        and percentage

    The BoxScore class has the following required parameters:

        @param **headers** (*dict*): Dictionary of request header information
            required by the API. Specifically, the API requires you to declare
            the 'User-Agent' key of the request header dictionary. More information
            can be found `here <https://stackoverflow.com/questions/46781563/
            how-to-obtain-a-json-response-from-the-stats-nba-com-api>`_ and
            an example request header dictionary can be found in the __init__.py
            file in the tests folder of this module.

        @param **game_id** (*str*): GameID in the API. 10-digit string that represents \
            a unique game. The format is two leading zeroes, followed by a \
            season indicator number ('1' for preseason, \
            '2' for regular season, '4' for the post-season), \
            then the trailing digits of the season in which the game \
            took place (e.g. '17' for the 2017-18 season). The following \
            5 digits increment from '00001' in order as the season progresses. \
            For example, '0021600001' is the **game_id** of the first game of the \
            2016-17 NBA regular season.

        @param **range_type** (*str*): RangeType in the API. **range_type** controls the \
            type of boxscore that is returned. If using the **start_period** and \
            **end_period** parameters (defined below), **range_type** should have a value \
            of '0' (DNP players included) or '1' (DNP players excluded). With \
            a **range_type** value of '2', the **start_range** and **end_range** values can be \
            used to return a boxscore from a customized subset of the given game.

        @param **start_period** (*str*): StartPeriod in the API. String of an integer \
            that corresponds to the period for which the boxscore begins.

        @param **end_period** (str): EndPeriod in the API. String of an integer that \
            corresponds to the period for which the boxscore ends (Overtime \
            increments logically, e.g. '5' is the first overtime period).

        @param **start_range** (*str*): StartRange in the API. String of an integer \
            that corresponds to the tenths of seconds that have elapsed in the \
            game for which the boxscore begins. Valid when **range_type** ='2'.

        @param **end_range** (*str*) : EndRange in the API. String of an integer \
            that corresponds to the tenths of seconds that have elapsed in the \
            game for which the boxscore ends. Valid when **range_type** ='2'.
        
    Attributes:

        - **api_resp** (*dict*): JSON object of the API response. The API response \
            has three keys. The 'resource' key describes the type of \
            response returned ('boxscore' in this instance). The 'parameters' \
            key describes the parameters provided in the API call. The \
            'resultSets' key contains the data returned in the API call.

        - **data** (*dict*): A dictionary of response names. Each response name is a \
            key to a list of dictionaries containing the corresponding data.
    """

    def __init__(self, headers, game_id, endpoint='boxscoreadvancedv2',
                 range_type='1', start_period='0', end_period='10',
                 start_range='0', end_range='0'):

        # Controlling the parameters depending on the endpoint
        if endpoint in ['boxscoreplayertrackv2', 'boxscoresummaryv2']:
            params = {'GameID': game_id}
        else:
            params = {'GameID': game_id,
                      'RangeType': range_type,
                      'StartPeriod': start_period,
                      'EndPeriod': end_period,
                      'StartRange': start_range,
                      'EndRange': end_range}

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params,
                                 headers=headers)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)
                
