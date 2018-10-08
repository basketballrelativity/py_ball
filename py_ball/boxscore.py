#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:36:55 2018

@author: patrickmcfarlane
"""

from . import api_call

class BoxScore:
    """ The BoxScore class contains all resources needed to use the boxscore-
    related API calls. stats.nba.com has the following boxscore-related
    API endpoints:
        - boxscoreadvancedv2: Game boxscore containing several advanced
        statistcs
        - boxscorefourfactorsv2: Game boxscore containing statistics related
        to the Four Factors, for team and opponent
        - boxscoremiscv2: Game boxscore containing points scored by type
        of change (paint, fastbreak, etc.) for team and opponent
        - boxscoreplayertrackv2: Game boxscore containing aggregated player
        tracking statistics
        - boxscorescoringv2: Game boxscore containing percentage scoring
        statistics broken down by shot type.
        - boxscoresummaryv2: Game boxscore containing a summary of a
        particular matchup (including game metadata and results)
        - boxscoretraditionalv2: Game boxscore containing basic statistics
        - boxscoreusagev2: Game boxscore containing usage statistics
        and percentage

    
    """

    def __init__(self, game_id, endpoint='boxscoreadvancedv2',
                 start_period='0', end_period='10',
                 start_range='0', end_range='0',
                 range_type='1'):

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
                                 params=params)
    