#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:43:34 2018

@author: patrickmcfarlane

test_boxscore.py

This function contains the tests for
functions in the boxscore.py
"""

from .__init__ import HEADERS
from ..boxscore import BoxScore

def test_boxscore_advanced():
    """ tests the boxscoreadvancedv2 endpoint of the Boxscore class
    """

    example_boxscore = BoxScore(headers=HEADERS, game_id='0021500002')

    table_names = example_boxscore.data.keys()
    example_player_stats = example_boxscore.data['PlayerStats'][0]
    example_team_stats = example_boxscore.data['TeamStats'][0]

    assert 'PlayerStats' in table_names
    assert 'TeamStats' in table_names

    assert list(example_player_stats.keys()) == ['GAME_ID',
                                                 'TEAM_ID',
                                                 'TEAM_ABBREVIATION',
                                                 'TEAM_CITY',
                                                 'PLAYER_ID',
                                                 'PLAYER_NAME',
                                                 'START_POSITION',
                                                 'COMMENT',
                                                 'MIN',
                                                 'E_OFF_RATING',
                                                 'OFF_RATING',
                                                 'E_DEF_RATING',
                                                 'DEF_RATING',
                                                 'E_NET_RATING',
                                                 'NET_RATING',
                                                 'AST_PCT',
                                                 'AST_TOV',
                                                 'AST_RATIO',
                                                 'OREB_PCT',
                                                 'DREB_PCT',
                                                 'REB_PCT',
                                                 'TM_TOV_PCT',
                                                 'EFG_PCT',
                                                 'TS_PCT',
                                                 'USG_PCT',
                                                 'E_USG_PCT',
                                                 'E_PACE',
                                                 'PACE',
                                                 'PIE']

    assert list(example_team_stats.keys()) == ['GAME_ID',
                                                 'TEAM_ID',
                                                 'TEAM_NAME',
                                                 'TEAM_ABBREVIATION',
                                                 'TEAM_CITY',
                                                 'MIN',
                                                 'E_OFF_RATING',
                                                 'OFF_RATING',
                                                 'E_DEF_RATING',
                                                 'DEF_RATING',
                                                 'E_NET_RATING',
                                                 'NET_RATING',
                                                 'AST_PCT',
                                                 'AST_TOV',
                                                 'AST_RATIO',
                                                 'OREB_PCT',
                                                 'DREB_PCT',
                                                 'REB_PCT',
                                                 'E_TM_TOV_PCT',
                                                 'TM_TOV_PCT',
                                                 'EFG_PCT',
                                                 'TS_PCT',
                                                 'USG_PCT',
                                                 'E_USG_PCT',
                                                 'E_PACE',
                                                 'PACE',
                                                 'PIE']