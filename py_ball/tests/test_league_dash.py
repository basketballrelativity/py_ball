#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:08:46 2018

@author: patrickmcfarlane

test_league_dash.py

This function contains the tests for
functions in the league_dash.py file
"""

from .__init__ import HEADERS
from ..league_dash import LeagueDash

def test_lineups_dash():
    """ tests the leaguedashlineups endpoint of the LeagueDash class
    """

    example_league = LeagueDash(headers=HEADERS)

    table_names = example_league.data.keys()

    assert 'Lineups' in table_names

    example_lineups = example_league.data['Lineups'][0]

    assert list(example_lineups.keys()) == ['GROUP_SET',
                                            'GROUP_ID',
                                            'GROUP_NAME',
                                            'TEAM_ID',
                                            'TEAM_ABBREVIATION',
                                            'GP',
                                            'W',
                                            'L',
                                            'W_PCT',
                                            'MIN',
                                            'FGM',
                                            'FGA',
                                            'FG_PCT',
                                            'FG3M',
                                            'FG3A',
                                            'FG3_PCT',
                                            'FTM',
                                            'FTA',
                                            'FT_PCT',
                                            'OREB',
                                            'DREB',
                                            'REB',
                                            'AST',
                                            'TOV',
                                            'STL',
                                            'BLK',
                                            'BLKA',
                                            'PF',
                                            'PFD',
                                            'PTS',
                                            'PLUS_MINUS',
                                            'GP_RANK',
                                            'W_RANK',
                                            'L_RANK',
                                            'W_PCT_RANK',
                                            'MIN_RANK',
                                            'FGM_RANK',
                                            'FGA_RANK',
                                            'FG_PCT_RANK',
                                            'FG3M_RANK',
                                            'FG3A_RANK',
                                            'FG3_PCT_RANK',
                                            'FTM_RANK',
                                            'FTA_RANK',
                                            'FT_PCT_RANK',
                                            'OREB_RANK',
                                            'DREB_RANK',
                                            'REB_RANK',
                                            'AST_RANK',
                                            'TOV_RANK',
                                            'STL_RANK',
                                            'BLK_RANK',
                                            'BLKA_RANK',
                                            'PF_RANK',
                                            'PFD_RANK',
                                            'PTS_RANK',
                                            'PLUS_MINUS_RANK']

def test_bio_dash():
    """ tests the leaguedashplayerbiostats endpoint of the LeagueDash class
    """

    example_league = LeagueDash(headers=HEADERS,
                                endpoint='leaguedashplayerbiostats')

    table_names = example_league.data.keys()

    assert 'LeagueDashPlayerBioStats' in table_names

    example_bio = example_league.data['LeagueDashPlayerBioStats'][0]

    assert list(example_bio.keys()) == ['PLAYER_ID',
                                        'PLAYER_NAME',
                                        'TEAM_ID',
                                        'TEAM_ABBREVIATION',
                                        'AGE',
                                        'PLAYER_HEIGHT',
                                        'PLAYER_HEIGHT_INCHES',
                                        'PLAYER_WEIGHT',
                                        'COLLEGE',
                                        'COUNTRY',
                                        'DRAFT_YEAR',
                                        'DRAFT_ROUND',
                                        'DRAFT_NUMBER',
                                        'GP',
                                        'PTS',
                                        'REB',
                                        'AST',
                                        'NET_RATING',
                                        'OREB_PCT',
                                        'DREB_PCT',
                                        'USG_PCT',
                                        'TS_PCT',
                                        'AST_PCT']

def test_clutch_dash():
    """ tests the leaguedashplayerclutch endpoint of the LeagueDash class
    """

    example_league = LeagueDash(headers=HEADERS,
                                endpoint='leaguedashplayerclutch')

    table_names = example_league.data.keys()

    assert 'LeagueDashPlayerClutch' in table_names

    example_clutch = example_league.data['LeagueDashPlayerClutch'][0]

    assert list(example_clutch.keys()) == ['GROUP_SET',
                                           'PLAYER_ID',
                                           'PLAYER_NAME',
                                           'TEAM_ID',
                                           'TEAM_ABBREVIATION',
                                           'AGE',
                                           'GP',
                                           'W',
                                           'L',
                                           'W_PCT',
                                           'MIN',
                                           'FGM',
                                           'FGA',
                                           'FG_PCT',
                                           'FG3M',
                                           'FG3A',
                                           'FG3_PCT',
                                           'FTM',
                                           'FTA',
                                           'FT_PCT',
                                           'OREB',
                                           'DREB',
                                           'REB',
                                           'AST',
                                           'TOV',
                                           'STL',
                                           'BLK',
                                           'BLKA',
                                           'PF',
                                           'PFD',
                                           'PTS',
                                           'PLUS_MINUS',
                                           'NBA_FANTASY_PTS',
                                           'DD2',
                                           'TD3',
                                           'GP_RANK',
                                           'W_RANK',
                                           'L_RANK',
                                           'W_PCT_RANK',
                                           'MIN_RANK',
                                           'FGM_RANK',
                                           'FGA_RANK',
                                           'FG_PCT_RANK',
                                           'FG3M_RANK',
                                           'FG3A_RANK',
                                           'FG3_PCT_RANK',
                                           'FTM_RANK',
                                           'FTA_RANK',
                                           'FT_PCT_RANK',
                                           'OREB_RANK',
                                           'DREB_RANK',
                                           'REB_RANK',
                                           'AST_RANK',
                                           'TOV_RANK',
                                           'STL_RANK',
                                           'BLK_RANK',
                                           'BLKA_RANK',
                                           'PF_RANK',
                                           'PFD_RANK',
                                           'PTS_RANK',
                                           'PLUS_MINUS_RANK',
                                           'NBA_FANTASY_PTS_RANK',
                                           'DD2_RANK',
                                           'TD3_RANK',
                                           'CFID',
                                           'CFPARAMS']

def test_shot_dash():
    """ tests the leaguedashplayershotlocations endpoint of the LeagueDash class
    """

    example_league = LeagueDash(headers=HEADERS,
                                endpoint='leaguedashplayershotlocations')

    table_names = example_league.data.keys()

    assert 'ShotLocations' in table_names

    example_shots = example_league.data['ShotLocations'][0]

    assert list(example_shots.keys()) == ['PLAYER_ID',
                                          'PLAYER_NAME',
                                          'TEAM_ID',
                                          'TEAM_ABBREVIATION',
                                          'AGE',
                                          'FGM_Restricted_Area',
                                          'FGA_Restricted_Area',
                                          'FG_PCT_Restricted_Area',
                                          'FGM_In_The_Paint_(Non-RA)',
                                          'FGA_In_The_Paint_(Non-RA)',
                                          'FG_PCT_In_The_Paint_(Non-RA)',
                                          'FGM_Mid-Range',
                                          'FGA_Mid-Range',
                                          'FG_PCT_Mid-Range',
                                          'FGM_Left_Corner_3',
                                          'FGA_Left_Corner_3',
                                          'FG_PCT_Left_Corner_3',
                                          'FGM_Right_Corner_3',
                                          'FGA_Right_Corner_3',
                                          'FG_PCT_Right_Corner_3',
                                          'FGM_Above_the_Break_3',
                                          'FGA_Above_the_Break_3',
                                          'FG_PCT_Above_the_Break_3',
                                          'FGM_Backcourt',
                                          'FGA_Backcourt',
                                          'FG_PCT_Backcourt']

def test_shooting_dash():
    """ tests the leaguedashplayerptshot endpoint of the LeagueDash class
    """

    example_league = LeagueDash(headers=HEADERS,
                                endpoint='leaguedashplayerptshot')

    table_names = example_league.data.keys()

    assert 'LeagueDashPTShots' in table_names

    example_shots = example_league.data['LeagueDashPTShots'][0]

    assert list(example_shots.keys()) == ['PLAYER_ID',
                                          'PLAYER_NAME',
                                          'PLAYER_LAST_TEAM_ID',
                                          'PLAYER_LAST_TEAM_ABBREVIATION',
                                          'AGE',
                                          'GP',
                                          'G',
                                          'FGA_FREQUENCY',
                                          'FGM',
                                          'FGA',
                                          'FG_PCT',
                                          'EFG_PCT',
                                          'FG2A_FREQUENCY',
                                          'FG2M',
                                          'FG2A',
                                          'FG2_PCT',
                                          'FG3A_FREQUENCY',
                                          'FG3M',
                                          'FG3A',
                                          'FG3_PCT']

def test_stats_dash():
    """ tests the leaguedashplayerstats endpoint of the LeagueDash class
    """

    example_league = LeagueDash(headers=HEADERS,
                                endpoint='leaguedashplayerstats')

    table_names = example_league.data.keys()

    assert 'LeagueDashPlayerStats' in table_names

    example_stats = example_league.data['LeagueDashPlayerStats'][0]

    assert list(example_stats.keys()) == ['PLAYER_ID',
                                          'PLAYER_NAME',
                                          'TEAM_ID',
                                          'TEAM_ABBREVIATION',
                                          'AGE',
                                          'GP',
                                          'W',
                                          'L',
                                          'W_PCT',
                                          'MIN',
                                          'FGM',
                                          'FGA',
                                          'FG_PCT',
                                          'FG3M',
                                          'FG3A',
                                          'FG3_PCT',
                                          'FTM',
                                          'FTA',
                                          'FT_PCT',
                                          'OREB',
                                          'DREB',
                                          'REB',
                                          'AST',
                                          'TOV',
                                          'STL',
                                          'BLK',
                                          'BLKA',
                                          'PF',
                                          'PFD',
                                          'PTS',
                                          'PLUS_MINUS',
                                          'NBA_FANTASY_PTS',
                                          'DD2',
                                          'TD3',
                                          'GP_RANK',
                                          'W_RANK',
                                          'L_RANK',
                                          'W_PCT_RANK',
                                          'MIN_RANK',
                                          'FGM_RANK',
                                          'FGA_RANK',
                                          'FG_PCT_RANK',
                                          'FG3M_RANK',
                                          'FG3A_RANK',
                                          'FG3_PCT_RANK',
                                          'FTM_RANK',
                                          'FTA_RANK',
                                          'FT_PCT_RANK',
                                          'OREB_RANK',
                                          'DREB_RANK',
                                          'REB_RANK',
                                          'AST_RANK',
                                          'TOV_RANK',
                                          'STL_RANK',
                                          'BLK_RANK',
                                          'BLKA_RANK',
                                          'PF_RANK',
                                          'PFD_RANK',
                                          'PTS_RANK',
                                          'PLUS_MINUS_RANK',
                                          'NBA_FANTASY_PTS_RANK',
                                          'DD2_RANK',
                                          'TD3_RANK',
                                          'CFID',
                                          'CFPARAMS']

def test_defend_dash():
    """ tests the leaguedashptdefend endpoint of the LeagueDash class
    """

    example_league = LeagueDash(headers=HEADERS,
                                endpoint='leaguedashptdefend')

    table_names = example_league.data.keys()

    assert 'LeagueDashPTDefend' in table_names

    example_defend = example_league.data['LeagueDashPTDefend'][0]

    assert list(example_defend.keys()) == ['CLOSE_DEF_PERSON_ID',
                                           'PLAYER_NAME',
                                           'PLAYER_LAST_TEAM_ID',
                                           'PLAYER_LAST_TEAM_ABBREVIATION',
                                           'PLAYER_POSITION',
                                           'AGE',
                                           'GP',
                                           'G',
                                           'FREQ',
                                           'D_FGM',
                                           'D_FGA',
                                           'D_FG_PCT',
                                           'NORMAL_FG_PCT',
                                           'PCT_PLUSMINUS']

def test_team_defend_dash():
    """ tests the leaguedashptteamdefend endpoint of the LeagueDash class
    """

    example_league = LeagueDash(headers=HEADERS,
                                endpoint='leaguedashptteamdefend')

    table_names = example_league.data.keys()

    assert 'LeagueDashPtTeamDefend' in table_names

    example_defend = example_league.data['LeagueDashPtTeamDefend'][0]

    assert list(example_defend.keys()) == ['TEAM_ID',
                                           'TEAM_NAME',
                                           'TEAM_ABBREVIATION',
                                           'GP',
                                           'G',
                                           'FREQ',
                                           'D_FGM',
                                           'D_FGA',
                                           'D_FG_PCT',
                                           'NORMAL_FG_PCT',
                                           'PCT_PLUSMINUS']
    
def test_team_shooting_dash():
    """ tests the leaguedashteamptshot endpoint of the LeagueDash class
    """

    example_league = LeagueDash(headers=HEADERS,
                                endpoint='leaguedashteamptshot')

    table_names = example_league.data.keys()

    assert 'LeagueDashPTShots' in table_names

    example_shot = example_league.data['LeagueDashPTShots'][0]

    assert list(example_shot.keys()) == ['TEAM_ID',
                                         'TEAM_NAME',
                                         'TEAM_ABBREVIATION',
                                         'GP',
                                         'G',
                                         'FGA_FREQUENCY',
                                         'FGM',
                                         'FGA',
                                         'FG_PCT',
                                         'EFG_PCT',
                                         'FG2A_FREQUENCY',
                                         'FG2M',
                                         'FG2A',
                                         'FG2_PCT',
                                         'FG3A_FREQUENCY',
                                         'FG3M',
                                         'FG3A',
                                         'FG3_PCT']
