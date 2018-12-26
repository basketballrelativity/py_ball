#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:43:34 2018

@author: patrickmcfarlane

test_boxscore.py

This function contains the tests for
functions in the boxscore.py file
"""

from .__init__ import HEADERS
from ..boxscore import BoxScore

def test_boxscore_advanced():
    """ tests the boxscoreadvancedv2 endpoint of the Boxscore class
    """

    example_boxscore = BoxScore(headers=HEADERS, game_id='0021500002')

    table_names = example_boxscore.data.keys()

    assert 'PlayerStats' in table_names
    assert 'TeamStats' in table_names

    example_player_stats = example_boxscore.data['PlayerStats'][0]
    example_team_stats = example_boxscore.data['TeamStats'][0]

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

def test_boxscore_four_factors():
    """ tests the boxscorefourfactorsv2 endpoint of the Boxscore class
    """

    example_boxscore = BoxScore(headers=HEADERS,
                                endpoint='boxscorefourfactorsv2',
                                game_id='0021500002')

    table_names = example_boxscore.data.keys()

    assert 'sqlPlayersFourFactors' in table_names
    assert 'sqlTeamsFourFactors' in table_names

    example_player_stats = example_boxscore.data['sqlPlayersFourFactors'][0]
    example_team_stats = example_boxscore.data['sqlTeamsFourFactors'][0]

    assert list(example_player_stats.keys()) == ['GAME_ID',
                                                 'TEAM_ID',
                                                 'TEAM_ABBREVIATION',
                                                 'TEAM_CITY',
                                                 'PLAYER_ID',
                                                 'PLAYER_NAME',
                                                 'START_POSITION',
                                                 'COMMENT',
                                                 'MIN',
                                                 'EFG_PCT',
                                                 'FTA_RATE',
                                                 'TM_TOV_PCT',
                                                 'OREB_PCT',
                                                 'OPP_EFG_PCT',
                                                 'OPP_FTA_RATE',
                                                 'OPP_TOV_PCT',
                                                 'OPP_OREB_PCT']

    assert list(example_team_stats.keys()) == ['GAME_ID',
                                               'TEAM_ID',
                                               'TEAM_NAME',
                                               'TEAM_ABBREVIATION',
                                               'TEAM_CITY',
                                               'MIN',
                                               'EFG_PCT',
                                               'FTA_RATE',
                                               'TM_TOV_PCT',
                                               'OREB_PCT',
                                               'OPP_EFG_PCT',
                                               'OPP_FTA_RATE',
                                               'OPP_TOV_PCT',
                                               'OPP_OREB_PCT']

def test_boxscore_misc():
    """ tests the boxscoremiscv2 endpoint of the Boxscore class
    """

    example_boxscore = BoxScore(headers=HEADERS,
                                endpoint='boxscoremiscv2',
                                game_id='0021500002')

    table_names = example_boxscore.data.keys()

    assert 'sqlPlayersMisc' in table_names
    assert 'sqlTeamsMisc' in table_names

    example_player_stats = example_boxscore.data['sqlPlayersMisc'][0]
    example_team_stats = example_boxscore.data['sqlTeamsMisc'][0]

    assert list(example_player_stats.keys()) == ['GAME_ID',
                                                 'TEAM_ID',
                                                 'TEAM_ABBREVIATION',
                                                 'TEAM_CITY',
                                                 'PLAYER_ID',
                                                 'PLAYER_NAME',
                                                 'START_POSITION',
                                                 'COMMENT',
                                                 'MIN',
                                                 'PTS_OFF_TOV',
                                                 'PTS_2ND_CHANCE',
                                                 'PTS_FB',
                                                 'PTS_PAINT',
                                                 'OPP_PTS_OFF_TOV',
                                                 'OPP_PTS_2ND_CHANCE',
                                                 'OPP_PTS_FB',
                                                 'OPP_PTS_PAINT',
                                                 'BLK',
                                                 'BLKA',
                                                 'PF',
                                                 'PFD']

    assert list(example_team_stats.keys()) == ['GAME_ID',
                                               'TEAM_ID',
                                               'TEAM_NAME',
                                               'TEAM_ABBREVIATION',
                                               'TEAM_CITY',
                                               'MIN',
                                               'PTS_OFF_TOV',
                                               'PTS_2ND_CHANCE',
                                               'PTS_FB',
                                               'PTS_PAINT',
                                               'OPP_PTS_OFF_TOV',
                                               'OPP_PTS_2ND_CHANCE',
                                               'OPP_PTS_FB',
                                               'OPP_PTS_PAINT',
                                               'BLK',
                                               'BLKA',
                                               'PF',
                                               'PFD']

def test_boxscore_player_track():
    """ tests the boxscoremiscv2 endpoint of the Boxscore class
    """

    example_boxscore = BoxScore(headers=HEADERS,
                                endpoint='boxscoreplayertrackv2',
                                game_id='0021500002')

    table_names = example_boxscore.data.keys()

    assert 'PlayerStats' in table_names
    assert 'TeamStats' in table_names

    example_player_stats = example_boxscore.data['PlayerStats'][0]
    example_team_stats = example_boxscore.data['TeamStats'][0]

    assert list(example_player_stats.keys()) == ['GAME_ID',
                                                 'TEAM_ID',
                                                 'TEAM_ABBREVIATION',
                                                 'TEAM_CITY',
                                                 'PLAYER_ID',
                                                 'PLAYER_NAME',
                                                 'START_POSITION',
                                                 'COMMENT',
                                                 'MIN',
                                                 'SPD',
                                                 'DIST',
                                                 'ORBC',
                                                 'DRBC',
                                                 'RBC',
                                                 'TCHS',
                                                 'SAST',
                                                 'FTAST',
                                                 'PASS',
                                                 'AST',
                                                 'CFGM',
                                                 'CFGA',
                                                 'CFG_PCT',
                                                 'UFGM',
                                                 'UFGA',
                                                 'UFG_PCT',
                                                 'FG_PCT',
                                                 'DFGM',
                                                 'DFGA',
                                                 'DFG_PCT']

    assert list(example_team_stats.keys()) == ['GAME_ID',
                                               'TEAM_ID',
                                               'TEAM_NAME',
                                               'TEAM_ABBREVIATION',
                                               'TEAM_CITY',
                                               'MIN',
                                               'DIST',
                                               'ORBC',
                                               'DRBC',
                                               'RBC',
                                               'TCHS',
                                               'SAST',
                                               'FTAST',
                                               'PASS',
                                               'AST',
                                               'CFGM',
                                               'CFGA',
                                               'CFG_PCT',
                                               'UFGM',
                                               'UFGA',
                                               'UFG_PCT',
                                               'FG_PCT',
                                               'DFGM',
                                               'DFGA',
                                               'DFG_PCT']
    
def test_boxscore_scoring():
    """ tests the boxscorescoringv2 endpoint of the Boxscore class
    """

    example_boxscore = BoxScore(headers=HEADERS,
                                endpoint='boxscorescoringv2',
                                game_id='0021500002')

    table_names = example_boxscore.data.keys()

    assert 'sqlPlayersScoring' in table_names
    assert 'sqlTeamsScoring' in table_names

    example_player_stats = example_boxscore.data['sqlPlayersScoring'][0]
    example_team_stats = example_boxscore.data['sqlTeamsScoring'][0]

    assert list(example_player_stats.keys()) == ['GAME_ID',
                                                 'TEAM_ID',
                                                 'TEAM_ABBREVIATION',
                                                 'TEAM_CITY',
                                                 'PLAYER_ID',
                                                 'PLAYER_NAME',
                                                 'START_POSITION',
                                                 'COMMENT',
                                                 'MIN',
                                                 'PCT_FGA_2PT',
                                                 'PCT_FGA_3PT',
                                                 'PCT_PTS_2PT',
                                                 'PCT_PTS_2PT_MR',
                                                 'PCT_PTS_3PT',
                                                 'PCT_PTS_FB',
                                                 'PCT_PTS_FT',
                                                 'PCT_PTS_OFF_TOV',
                                                 'PCT_PTS_PAINT',
                                                 'PCT_AST_2PM',
                                                 'PCT_UAST_2PM',
                                                 'PCT_AST_3PM',
                                                 'PCT_UAST_3PM',
                                                 'PCT_AST_FGM',
                                                 'PCT_UAST_FGM']

    assert list(example_team_stats.keys()) == ['GAME_ID',
                                               'TEAM_ID',
                                               'TEAM_NAME',
                                               'TEAM_ABBREVIATION',
                                               'TEAM_CITY',
                                               'MIN',
                                               'PCT_FGA_2PT',
                                               'PCT_FGA_3PT',
                                               'PCT_PTS_2PT',
                                               'PCT_PTS_2PT_MR',
                                               'PCT_PTS_3PT',
                                               'PCT_PTS_FB',
                                               'PCT_PTS_FT',
                                               'PCT_PTS_OFF_TOV',
                                               'PCT_PTS_PAINT',
                                               'PCT_AST_2PM',
                                               'PCT_UAST_2PM',
                                               'PCT_AST_3PM',
                                               'PCT_UAST_3PM',
                                               'PCT_AST_FGM',
                                               'PCT_UAST_FGM']

def test_boxscore_summary():
    """ tests the boxscoresummaryv2 endpoint of the Boxscore class
    """

    example_boxscore = BoxScore(headers=HEADERS,
                                endpoint='boxscoresummaryv2',
                                game_id='0021500002')

    table_names = example_boxscore.data.keys()

    assert 'GameSummary' in table_names
    assert 'OtherStats' in table_names
    assert 'Officials' in table_names
    assert 'InactivePlayers' in table_names
    assert 'GameInfo' in table_names
    assert 'LineScore' in table_names
    assert 'LastMeeting' in table_names
    assert 'SeasonSeries' in table_names
    assert 'AvailableVideo' in table_names

    example_game_summary = example_boxscore.data['GameSummary'][0]
    example_other_stats = example_boxscore.data['OtherStats'][0]
    example_officials = example_boxscore.data['Officials'][0]
    example_inactive_players = example_boxscore.data['InactivePlayers'][0]
    example_game_info = example_boxscore.data['GameInfo'][0]
    example_line_score = example_boxscore.data['LineScore'][0]
    example_last_meeting = example_boxscore.data['LastMeeting'][0]
    example_season_series = example_boxscore.data['SeasonSeries'][0]
    example_available_video = example_boxscore.data['AvailableVideo'][0]

    assert list(example_game_summary.keys()) == ['GAME_DATE_EST',
                                                 'GAME_SEQUENCE',
                                                 'GAME_ID',
                                                 'GAME_STATUS_ID',
                                                 'GAME_STATUS_TEXT',
                                                 'GAMECODE',
                                                 'HOME_TEAM_ID',
                                                 'VISITOR_TEAM_ID',
                                                 'SEASON',
                                                 'LIVE_PERIOD',
                                                 'LIVE_PC_TIME',
                                                 'NATL_TV_BROADCASTER_ABBREVIATION',
                                                 'LIVE_PERIOD_TIME_BCAST',
                                                 'WH_STATUS']

    assert list(example_other_stats.keys()) == ['LEAGUE_ID',
                                                'TEAM_ID',
                                                'TEAM_ABBREVIATION',
                                                'TEAM_CITY',
                                                'PTS_PAINT',
                                                'PTS_2ND_CHANCE',
                                                'PTS_FB',
                                                'LARGEST_LEAD',
                                                'LEAD_CHANGES',
                                                'TIMES_TIED',
                                                'TEAM_TURNOVERS',
                                                'TOTAL_TURNOVERS',
                                                'TEAM_REBOUNDS',
                                                'PTS_OFF_TO']

    assert list(example_officials.keys()) == ['OFFICIAL_ID',
                                              'FIRST_NAME',
                                              'LAST_NAME',
                                              'JERSEY_NUM']

    assert list(example_inactive_players.keys()) == ['PLAYER_ID',
                                                     'FIRST_NAME',
                                                     'LAST_NAME',
                                                     'JERSEY_NUM',
                                                     'TEAM_ID',
                                                     'TEAM_CITY',
                                                     'TEAM_NAME',
                                                     'TEAM_ABBREVIATION']

    assert list(example_game_info.keys()) == ['GAME_DATE',
                                              'ATTENDANCE',
                                              'GAME_TIME']

    assert list(example_line_score.keys()) == ['GAME_DATE_EST',
                                               'GAME_SEQUENCE',
                                               'GAME_ID',
                                               'TEAM_ID',
                                               'TEAM_ABBREVIATION',
                                               'TEAM_CITY_NAME',
                                               'TEAM_NICKNAME',
                                               'TEAM_WINS_LOSSES',
                                               'PTS_QTR1',
                                               'PTS_QTR2',
                                               'PTS_QTR3',
                                               'PTS_QTR4',
                                               'PTS_OT1',
                                               'PTS_OT2',
                                               'PTS_OT3',
                                               'PTS_OT4',
                                               'PTS_OT5',
                                               'PTS_OT6',
                                               'PTS_OT7',
                                               'PTS_OT8',
                                               'PTS_OT9',
                                               'PTS_OT10',
                                               'PTS']

    assert list(example_last_meeting.keys()) == ['GAME_ID',
                                                 'LAST_GAME_ID',
                                                 'LAST_GAME_DATE_EST',
                                                 'LAST_GAME_HOME_TEAM_ID',
                                                 'LAST_GAME_HOME_TEAM_CITY',
                                                 'LAST_GAME_HOME_TEAM_NAME',
                                                 'LAST_GAME_HOME_TEAM_ABBREVIATION',
                                                 'LAST_GAME_HOME_TEAM_POINTS',
                                                 'LAST_GAME_VISITOR_TEAM_ID',
                                                 'LAST_GAME_VISITOR_TEAM_CITY',
                                                 'LAST_GAME_VISITOR_TEAM_NAME',
                                                 'LAST_GAME_VISITOR_TEAM_CITY1',
                                                 'LAST_GAME_VISITOR_TEAM_POINTS']

    assert list(example_season_series.keys()) == ['GAME_ID',
                                                  'HOME_TEAM_ID',
                                                  'VISITOR_TEAM_ID',
                                                  'GAME_DATE_EST',
                                                  'HOME_TEAM_WINS',
                                                  'HOME_TEAM_LOSSES',
                                                  'SERIES_LEADER']

    assert list(example_available_video.keys()) == ['GAME_ID',
                                                    'VIDEO_AVAILABLE_FLAG',
                                                    'PT_AVAILABLE',
                                                    'PT_XYZ_AVAILABLE',
                                                    'WH_STATUS',
                                                    'HUSTLE_STATUS',
                                                    'HISTORICAL_STATUS']

def test_boxscore_traditional():
    """ tests the boxscoretraditionalv2 endpoint of the Boxscore class
    """

    example_boxscore = BoxScore(headers=HEADERS,
                                endpoint='boxscoretraditionalv2',
                                game_id='0021500002')

    table_names = example_boxscore.data.keys()

    assert 'PlayerStats' in table_names
    assert 'TeamStats' in table_names
    assert 'TeamStarterBenchStats' in table_names

    example_player_stats = example_boxscore.data['PlayerStats'][0]
    example_team_stats = example_boxscore.data['TeamStats'][0]
    example_team_bench_stats = example_boxscore.data['TeamStarterBenchStats'][0]

    assert list(example_player_stats.keys()) == ['GAME_ID',
                                                 'TEAM_ID',
                                                 'TEAM_ABBREVIATION',
                                                 'TEAM_CITY',
                                                 'PLAYER_ID',
                                                 'PLAYER_NAME',
                                                 'START_POSITION',
                                                 'COMMENT',
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
                                                 'STL',
                                                 'BLK',
                                                 'TO',
                                                 'PF',
                                                 'PTS',
                                                 'PLUS_MINUS']

    assert list(example_team_stats.keys()) == ['GAME_ID',
                                              'TEAM_ID',
                                              'TEAM_NAME',
                                              'TEAM_ABBREVIATION',
                                              'TEAM_CITY',
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
                                              'STL',
                                              'BLK',
                                              'TO',
                                              'PF',
                                              'PTS',
                                              'PLUS_MINUS']

    assert list(example_team_bench_stats.keys()) == ['GAME_ID',
                                                     'TEAM_ID',
                                                     'TEAM_NAME',
                                                     'TEAM_ABBREVIATION',
                                                     'TEAM_CITY',
                                                     'STARTERS_BENCH',
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
                                                     'STL',
                                                     'BLK',
                                                     'TO',
                                                     'PF',
                                                     'PTS']

def test_boxscore_usage():
    """ tests the boxscoretraditionalv2 endpoint of the Boxscore class
    """

    example_boxscore = BoxScore(headers=HEADERS,
                                endpoint='boxscoreusagev2',
                                game_id='0021500002')

    table_names = example_boxscore.data.keys()

    assert 'sqlPlayersUsage' in table_names
    assert 'sqlTeamsUsage' in table_names

    example_player_stats = example_boxscore.data['sqlPlayersUsage'][0]
    example_team_stats = example_boxscore.data['sqlTeamsUsage'][0]

    assert list(example_player_stats.keys()) == ['GAME_ID',
                                                 'TEAM_ID',
                                                 'TEAM_ABBREVIATION',
                                                 'TEAM_CITY',
                                                 'PLAYER_ID',
                                                 'PLAYER_NAME',
                                                 'START_POSITION',
                                                 'COMMENT',
                                                 'MIN',
                                                 'USG_PCT',
                                                 'PCT_FGM',
                                                 'PCT_FGA',
                                                 'PCT_FG3M',
                                                 'PCT_FG3A',
                                                 'PCT_FTM',
                                                 'PCT_FTA',
                                                 'PCT_OREB',
                                                 'PCT_DREB',
                                                 'PCT_REB',
                                                 'PCT_AST',
                                                 'PCT_TOV',
                                                 'PCT_STL',
                                                 'PCT_BLK',
                                                 'PCT_BLKA',
                                                 'PCT_PF',
                                                 'PCT_PFD',
                                                 'PCT_PTS']

    assert list(example_team_stats.keys()) == ['GAME_ID',
                                              'TEAM_ID',
                                              'TEAM_NAME',
                                              'TEAM_ABBREVIATION',
                                              'TEAM_CITY',
                                              'MIN',
                                              'USG_PCT',
                                              'PCT_FGM',
                                              'PCT_FGA',
                                              'PCT_FG3M',
                                              'PCT_FG3A',
                                              'PCT_FTM',
                                              'PCT_FTA',
                                              'PCT_OREB',
                                              'PCT_DREB',
                                              'PCT_REB',
                                              'PCT_AST',
                                              'PCT_TOV',
                                              'PCT_STL',
                                              'PCT_BLK',
                                              'PCT_BLKA',
                                              'PCT_PF',
                                              'PCT_PFD',
                                              'PCT_PTS']
