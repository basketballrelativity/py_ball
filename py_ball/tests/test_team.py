#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 09:06:50 2018

@author: patrickmcfarlane

test_team.py

This function contains the tests for
functions in the team.py file
"""

import time

from .__init__ import HEADERS
from ..team import Team

def test_team_clutch():
    """ tests the teamdashboardbyclutch endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                          endpoint='teamdashboardbyclutch')

    table_names = example_team.data.keys()

    assert 'OverallTeamDashboard' in table_names
    assert 'Last5Min5PointTeamDashboard' in table_names
    assert 'Last3Min5PointTeamDashboard' in table_names
    assert 'Last1Min5PointTeamDashboard' in table_names
    assert 'Last30Sec3PointTeamDashboard' in table_names
    assert 'Last10Sec3PointTeamDashboard' in table_names
    assert 'Last5MinPlusMinus5PointTeamDashboard' in table_names
    assert 'Last3MinPlusMinus5PointTeamDashboard' in table_names
    assert 'Last1MinPlusMinus5PointTeamDashboard' in table_names
    assert 'Last30Sec3Point2TeamDashboard' in table_names
    assert 'Last10Sec3Point2TeamDashboard' in table_names

    example_overall = example_team.data['OverallTeamDashboard'][0]
    example_last5_5 = example_team.data['Last5Min5PointTeamDashboard'][0]
    example_last3_5 = example_team.data['Last3Min5PointTeamDashboard'][0]
    example_last1_5 = example_team.data['Last1Min5PointTeamDashboard'][0]
    example_last30_3 = example_team.data['Last30Sec3PointTeamDashboard'][0]
    example_last10_3 = example_team.data['Last10Sec3PointTeamDashboard'][0]
    example_last5 = example_team.data['Last5MinPlusMinus5PointTeamDashboard'][0]
    example_last3 = example_team.data['Last3MinPlusMinus5PointTeamDashboard'][0]
    example_last1 = example_team.data['Last1MinPlusMinus5PointTeamDashboard'][0]
    example_last30_3_2 = example_team.data['Last30Sec3Point2TeamDashboard'][0]
    example_last10_3_2 = example_team.data['Last10Sec3Point2TeamDashboard'][0]

    columns = ['GROUP_SET',
               'GROUP_VALUE',
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
               'PLUS_MINUS_RANK',
               'CFID',
               'CFPARAMS']

    assert list(example_overall.keys()) == columns

    assert list(example_last5_5.keys()) == columns

    assert list(example_last3_5.keys()) == columns

    assert list(example_last1_5.keys()) == columns

    assert list(example_last30_3.keys()) == columns

    assert list(example_last10_3.keys()) == columns

    assert list(example_last5.keys()) == columns

    assert list(example_last3.keys()) == columns

    assert list(example_last1.keys()) == columns

    assert list(example_last30_3_2.keys()) == columns

    assert list(example_last10_3_2.keys()) == columns


def test_team_gamesplits():
    """ tests the teamdashboardbygamesplits endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamdashboardbygamesplits')

    table_names = example_team.data.keys()

    assert 'OverallTeamDashboard' in table_names
    assert 'ByHalfTeamDashboard' in table_names
    assert 'ByPeriodTeamDashboard' in table_names
    assert 'ByScoreMarginTeamDashboard' in table_names
    assert 'ByActualMarginTeamDashboard' in table_names

    example_overall = example_team.data['OverallTeamDashboard'][0]
    example_half = example_team.data['ByHalfTeamDashboard'][0]
    example_period = example_team.data['ByPeriodTeamDashboard'][0]
    example_score = example_team.data['ByScoreMarginTeamDashboard'][0]
    example_margin = example_team.data['ByActualMarginTeamDashboard'][0]

    columns = ['GROUP_SET',
               'GROUP_VALUE',
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
               'PLUS_MINUS_RANK',
               'CFID',
               'CFPARAMS']

    assert list(example_overall.keys()) == columns

    assert list(example_half.keys()) == columns

    assert list(example_period.keys()) == columns

    assert list(example_score.keys()) == columns

    assert list(example_margin.keys()) == columns

def test_team_generalsplits():
    """ tests the teamdashboardbygeneralsplits endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamdashboardbygeneralsplits')

    table_names = example_team.data.keys()

    assert 'OverallTeamDashboard' in table_names
    assert 'LocationTeamDashboard' in table_names
    assert 'WinsLossesTeamDashboard' in table_names
    assert 'MonthTeamDashboard' in table_names
    assert 'PrePostAllStarTeamDashboard' in table_names
    assert 'DaysRestTeamDashboard' in table_names

    example_overall = example_team.data['OverallTeamDashboard'][0]
    example_location = example_team.data['LocationTeamDashboard'][0]
    example_wl = example_team.data['WinsLossesTeamDashboard'][0]
    example_month = example_team.data['MonthTeamDashboard'][0]
    example_star = example_team.data['PrePostAllStarTeamDashboard'][0]
    example_rest = example_team.data['DaysRestTeamDashboard'][0]

    columns = ['GROUP_SET',
               'GROUP_VALUE',
               'SEASON_YEAR',
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
               'PLUS_MINUS_RANK',
               'CFID',
               'CFPARAMS']

    assert list(example_overall.keys()) == columns

    assert list(example_location.keys()) == ['GROUP_SET',
                                             'GROUP_VALUE',
                                             'TEAM_GAME_LOCATION',
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
                                             'PLUS_MINUS_RANK',
                                             'CFID',
                                             'CFPARAMS']

    assert list(example_wl.keys()) == ['GROUP_SET',
                                       'GROUP_VALUE',
                                       'GAME_RESULT',
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
                                       'PLUS_MINUS_RANK',
                                       'CFID',
                                       'CFPARAMS']

    assert list(example_month.keys()) == ['GROUP_SET',
                                          'GROUP_VALUE',
                                          'SEASON_MONTH_NAME',
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
                                          'PLUS_MINUS_RANK',
                                          'CFID',
                                          'CFPARAMS']

    assert list(example_star.keys()) == ['GROUP_SET',
                                         'GROUP_VALUE',
                                         'SEASON_SEGMENT',
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
                                         'PLUS_MINUS_RANK',
                                         'CFID',
                                         'CFPARAMS']

    assert list(example_rest.keys()) == ['GROUP_SET',
                                         'GROUP_VALUE',
                                         'TEAM_DAYS_REST_RANGE',
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
                                         'PLUS_MINUS_RANK',
                                         'CFID',
                                         'CFPARAMS']

def test_team_lastngames():
    """ tests the teamdashboardbylastngames endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamdashboardbylastngames')

    table_names = example_team.data.keys()

    assert 'OverallTeamDashboard' in table_names
    assert 'Last5TeamDashboard' in table_names
    assert 'Last10TeamDashboard' in table_names
    assert 'Last15TeamDashboard' in table_names
    assert 'Last20TeamDashboard' in table_names
    assert 'GameNumberTeamDashboard' in table_names

    example_overall = example_team.data['OverallTeamDashboard'][0]
    example_last5 = example_team.data['Last5TeamDashboard'][0]
    example_last10 = example_team.data['Last10TeamDashboard'][0]
    example_last15 = example_team.data['Last15TeamDashboard'][0]
    example_last20 = example_team.data['Last20TeamDashboard'][0]
    example_game = example_team.data['GameNumberTeamDashboard'][0]

    columns = ['GROUP_SET',
               'GROUP_VALUE',
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
               'PLUS_MINUS_RANK',
               'CFID',
               'CFPARAMS']

    assert list(example_overall.keys()) == columns

    assert list(example_last5.keys()) == columns

    assert list(example_last10.keys()) == columns

    assert list(example_last15.keys()) == columns

    assert list(example_last20.keys()) == columns

    assert list(example_game.keys()) == columns
    
def test_team_opponent():
    """ tests the teamdashboardbyopponent endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                          endpoint='teamdashboardbyopponent')

    table_names = example_team.data.keys()

    assert 'OverallTeamDashboard' in table_names
    assert 'ConferenceTeamDashboard' in table_names
    assert 'DivisionTeamDashboard' in table_names
    assert 'OpponentTeamDashboard' in table_names

    example_overall = example_team.data['OverallTeamDashboard'][0]
    example_conference = example_team.data['ConferenceTeamDashboard'][0]
    example_division = example_team.data['DivisionTeamDashboard'][0]
    example_opponent = example_team.data['OpponentTeamDashboard'][0]

    columns = ['GROUP_SET',
               'GROUP_VALUE',
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
               'PLUS_MINUS_RANK',
               'CFID',
               'CFPARAMS']
    
    assert list(example_overall.keys()) == columns

    assert list(example_conference.keys()) == columns

    assert list(example_division.keys()) == columns

    assert list(example_opponent.keys()) == columns

def test_team_shootingsplits():
    """ tests the teamdashboardbyshootingsplits endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                          endpoint='teamdashboardbyshootingsplits')

    table_names = example_team.data.keys()

    assert 'OverallTeamDashboard' in table_names
    assert 'Shot5FTTeamDashboard' in table_names
    assert 'Shot8FTTeamDashboard' in table_names
    assert 'ShotAreaTeamDashboard' in table_names
    assert 'AssitedShotTeamDashboard' in table_names
    assert 'ShotTypeTeamDashboard' in table_names
    assert 'AssistedBy' in table_names

    example_overall = example_team.data['OverallTeamDashboard'][0]
    example_5ft = example_team.data['Shot5FTTeamDashboard'][0]
    example_8ft = example_team.data['Shot8FTTeamDashboard'][0]
    example_area = example_team.data['ShotAreaTeamDashboard'][0]
    example_assisted = example_team.data['AssitedShotTeamDashboard'][0]
    example_type = example_team.data['ShotTypeTeamDashboard'][0]
    example_assistedby = example_team.data['AssistedBy'][0]

    columns = ['GROUP_SET',
               'GROUP_VALUE',
               'FGM',
               'FGA',
               'FG_PCT',
               'FG3M',
               'FG3A',
               'FG3_PCT',
               'EFG_PCT',
               'BLKA',
               'PCT_AST_2PM',
               'PCT_UAST_2PM',
               'PCT_AST_3PM',
               'PCT_UAST_3PM',
               'PCT_AST_FGM',
               'PCT_UAST_FGM',
               'FGM_RANK',
               'FGA_RANK',
               'FG_PCT_RANK',
               'FG3M_RANK',
               'FG3A_RANK',
               'FG3_PCT_RANK',
               'EFG_PCT_RANK',
               'BLKA_RANK',
               'PCT_AST_2PM_RANK',
               'PCT_UAST_2PM_RANK',
               'PCT_AST_3PM_RANK',
               'PCT_UAST_3PM_RANK',
               'PCT_AST_FGM_RANK',
               'PCT_UAST_FGM_RANK',
               'CFID',
               'CFPARAMS']

    assert list(example_overall.keys()) == columns

    assert list(example_5ft.keys()) == columns

    assert list(example_8ft.keys()) == columns

    assert list(example_area.keys()) == columns

    assert list(example_assisted.keys()) == columns

    assert list(example_type.keys()) == columns

    assert list(example_assistedby.keys()) == ['GROUP_SET',
                                               'PLAYER_ID',
                                               'PLAYER_NAME',
                                               'FGM',
                                               'FGA',
                                               'FG_PCT',
                                               'FG3M',
                                               'FG3A',
                                               'FG3_PCT',
                                               'EFG_PCT',
                                               'BLKA',
                                               'PCT_AST_2PM',
                                               'PCT_UAST_2PM',
                                               'PCT_AST_3PM',
                                               'PCT_UAST_3PM',
                                               'PCT_AST_FGM',
                                               'PCT_UAST_FGM',
                                               'FGM_RANK',
                                               'FGA_RANK',
                                               'FG_PCT_RANK',
                                               'FG3M_RANK',
                                               'FG3A_RANK',
                                               'FG3_PCT_RANK',
                                               'EFG_PCT_RANK',
                                               'BLKA_RANK',
                                               'PCT_AST_2PM_RANK',
                                               'PCT_UAST_2PM_RANK',
                                               'PCT_AST_3PM_RANK',
                                               'PCT_UAST_3PM_RANK',
                                               'PCT_AST_FGM_RANK',
                                               'PCT_UAST_FGM_RANK',
                                               'CFID',
                                               'CFPARAMS']

def test_team_teamperformance():
    """ tests the teamdashboardbyteamperformance endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamdashboardbyteamperformance')

    table_names = example_team.data.keys()

    assert 'OverallTeamDashboard' in table_names
    assert 'ScoreDifferentialTeamDashboard' in table_names
    assert 'PointsScoredTeamDashboard' in table_names
    assert 'PontsAgainstTeamDashboard' in table_names

    example_overall = example_team.data['OverallTeamDashboard'][0]
    example_scorediff = example_team.data['ScoreDifferentialTeamDashboard'][0]
    example_scored = example_team.data['PointsScoredTeamDashboard'][0]
    example_against = example_team.data['PontsAgainstTeamDashboard'][0]

    columns = ['GROUP_SET',
               'GROUP_VALUE_ORDER',
               'GROUP_VALUE',
               'GROUP_VALUE_2',
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
               'PLUS_MINUS_RANK',
               'CFID',
               'CFPARAMS']

    assert list(example_overall.keys()) == ['GROUP_SET',
                                            'GROUP_VALUE',
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
                                            'PLUS_MINUS_RANK',
                                            'CFID',
                                            'CFPARAMS']

    assert list(example_scorediff.keys()) == columns

    assert list(example_scored.keys()) == columns

    assert list(example_against.keys()) == columns

def test_team_yoy():
    """ tests the teamdashboardbyyearoveryear endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamdashboardbyyearoveryear')

    table_names = example_team.data.keys()

    assert 'OverallTeamDashboard' in table_names
    assert 'ByYearTeamDashboard' in table_names

    example_overall = example_team.data['OverallTeamDashboard'][0]
    example_yoy = example_team.data['ByYearTeamDashboard'][0]

    columns = ['GROUP_SET',
               'GROUP_VALUE',
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
               'PLUS_MINUS_RANK',
               'CFID',
               'CFPARAMS']

    assert list(example_overall.keys()) == columns
    assert list(example_yoy.keys()) == columns

def test_team_lineups():
    """ tests the teamdashlineups endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamdashlineups',
                        game_id='0021700608',
                        team_id='1610612745',
                        player_id='2772')

    table_names = example_team.data.keys()

    assert 'Overall' in table_names
    assert 'Lineups' in table_names

    example_overall = example_team.data['Overall'][0]
    example_lineups = example_team.data['Lineups'][0]

    assert list(example_overall.keys()) == ['GROUP_SET',
                                            'GROUP_VALUE',
                                            'TEAM_ID',
                                            'TEAM_ABBREVIATION',
                                            'TEAM_NAME',
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

    assert list(example_lineups.keys()) == ['GROUP_SET',
                                            'GROUP_ID',
                                            'GROUP_NAME',
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

def test_team_pass():
    """ tests the teamdashptpass endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamdashptpass')

    table_names = example_team.data.keys()

    assert 'PassesMade' in table_names
    assert 'PassesReceived' in table_names

    example_made = example_team.data['PassesMade'][0]
    example_received = example_team.data['PassesReceived'][0]

    assert list(example_made.keys()) == ['TEAM_ID',
                                         'TEAM_NAME',
                                         'PASS_TYPE',
                                         'G',
                                         'PASS_FROM',
                                         'PASS_TEAMMATE_PLAYER_ID',
                                         'FREQUENCY',
                                         'PASS',
                                         'AST',
                                         'FGM',
                                         'FGA',
                                         'FG_PCT',
                                         'FG2M',
                                         'FG2A',
                                         'FG2_PCT',
                                         'FG3M',
                                         'FG3A',
                                         'FG3_PCT']

    assert list(example_received.keys()) == ['TEAM_ID',
                                             'TEAM_NAME',
                                             'PASS_TYPE',
                                             'G',
                                             'PASS_TO',
                                             'PASS_TEAMMATE_PLAYER_ID',
                                             'FREQUENCY',
                                             'PASS',
                                             'AST',
                                             'FGM',
                                             'FGA',
                                             'FG_PCT',
                                             'FG2M',
                                             'FG2A',
                                             'FG2_PCT',
                                             'FG3M',
                                             'FG3A',
                                             'FG3_PCT']

def test_team_reb():
    """ tests the teamdashptreb endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamdashptreb')

    table_names = example_team.data.keys()

    assert 'OverallRebounding' in table_names
    assert 'ShotTypeRebounding' in table_names
    assert 'NumContestedRebounding' in table_names
    assert 'ShotDistanceRebounding' in table_names
    assert 'RebDistanceRebounding' in table_names

    example_overall = example_team.data['OverallRebounding'][0]
    example_type = example_team.data['ShotTypeRebounding'][0]
    example_num = example_team.data['NumContestedRebounding'][0]
    example_shotdist = example_team.data['ShotDistanceRebounding'][0]
    example_rebdist = example_team.data['RebDistanceRebounding'][0]

    assert list(example_overall.keys()) == ['TEAM_ID',
                                            'TEAM_NAME',
                                            'G',
                                            'OVERALL',
                                            'REB_FREQUENCY',
                                            'OREB',
                                            'DREB',
                                            'REB',
                                            'C_OREB',
                                            'C_DREB',
                                            'C_REB',
                                            'C_REB_PCT',
                                            'UC_OREB',
                                            'UC_DREB',
                                            'UC_REB',
                                            'UC_REB_PCT']

    assert list(example_type.keys()) == ['TEAM_ID',
                                         'TEAM_NAME',
                                         'SORT_ORDER',
                                         'G',
                                         'SHOT_TYPE_RANGE',
                                         'REB_FREQUENCY',
                                         'OREB',
                                         'DREB',
                                         'REB',
                                         'C_OREB',
                                         'C_DREB',
                                         'C_REB',
                                         'C_REB_PCT',
                                         'UC_OREB',
                                         'UC_DREB',
                                         'UC_REB',
                                         'UC_REB_PCT']

    assert list(example_num.keys()) == ['TEAM_ID',
                                        'TEAM_NAME',
                                        'SORT_ORDER',
                                        'G',
                                        'REB_NUM_CONTESTING_RANGE',
                                        'REB_FREQUENCY',
                                        'OREB',
                                        'DREB',
                                        'REB',
                                        'C_OREB',
                                        'C_DREB',
                                        'C_REB',
                                        'C_REB_PCT',
                                        'UC_OREB',
                                        'UC_DREB',
                                        'UC_REB',
                                        'UC_REB_PCT']

    assert list(example_shotdist.keys()) == ['TEAM_ID',
                                             'TEAM_NAME',
                                             'SORT_ORDER',
                                             'G',
                                             'SHOT_DIST_RANGE',
                                             'REB_FREQUENCY',
                                             'OREB',
                                             'DREB',
                                             'REB',
                                             'C_OREB',
                                             'C_DREB',
                                             'C_REB',
                                             'C_REB_PCT',
                                             'UC_OREB',
                                             'UC_DREB',
                                             'UC_REB',
                                             'UC_REB_PCT']

    assert list(example_rebdist.keys()) == ['TEAM_ID',
                                            'TEAM_NAME',
                                            'SORT_ORDER',
                                            'G',
                                            'REB_DIST_RANGE',
                                            'REB_FREQUENCY',
                                            'OREB',
                                            'DREB',
                                            'REB',
                                            'C_OREB',
                                            'C_DREB',
                                            'C_REB',
                                            'C_REB_PCT',
                                            'UC_OREB',
                                            'UC_DREB',
                                            'UC_REB',
                                            'UC_REB_PCT']

def test_team_shot():
    """ tests the teamdashptshots endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamdashptshots')

    table_names = example_team.data.keys()

    assert 'GeneralShooting' in table_names
    assert 'ShotClockShooting' in table_names
    assert 'DribbleShooting' in table_names
    assert 'ClosestDefenderShooting' in table_names
    assert 'ClosestDefender10ftPlusShooting' in table_names
    assert 'TouchTimeShooting' in table_names

    example_gen = example_team.data['GeneralShooting'][0]
    example_clock = example_team.data['ShotClockShooting'][0]
    example_dribble = example_team.data['DribbleShooting'][0]
    example_defender = example_team.data['ClosestDefenderShooting'][0]
    example_defender10 = example_team.data['ClosestDefender10ftPlusShooting'][0]
    example_touch = example_team.data['TouchTimeShooting'][0]

    assert list(example_gen.keys()) == ['TEAM_ID',
                                       'TEAM_NAME',
                                       'SORT_ORDER',
                                       'G',
                                       'SHOT_TYPE',
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

    assert list(example_clock.keys()) == ['TEAM_ID',
                                          'TEAM_NAME',
                                          'SORT_ORDER',
                                          'G',
                                          'SHOT_CLOCK_RANGE',
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

    assert list(example_dribble.keys()) == ['TEAM_ID',
                                            'TEAM_NAME',
                                            'SORT_ORDER',
                                            'G',
                                            'DRIBBLE_RANGE',
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

    assert list(example_defender.keys()) == ['TEAM_ID',
                                             'TEAM_NAME',
                                             'SORT_ORDER',
                                             'G',
                                             'CLOSE_DEF_DIST_RANGE',
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

    assert list(example_defender10.keys()) == ['TEAM_ID',
                                               'TEAM_NAME',
                                               'SORT_ORDER',
                                               'G',
                                               'CLOSE_DEF_DIST_RANGE',
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

    assert list(example_touch.keys()) == ['TEAM_ID',
                                          'TEAM_NAME',
                                          'SORT_ORDER',
                                          'G',
                                          'TOUCH_TIME_RANGE',
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
    
def test_team_gamelog():
    """ tests the teamgamelog endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamgamelog')

    table_names = example_team.data.keys()

    assert 'TeamGameLog' in table_names

    example_log = example_team.data['TeamGameLog'][0]

    assert list(example_log.keys()) == ['Team_ID',
                                        'Game_ID',
                                        'GAME_DATE',
                                        'MATCHUP',
                                        'WL',
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
                                        'STL',
                                        'BLK',
                                        'TOV',
                                        'PF',
                                        'PTS']

def test_team_info():
    """ tests the teaminfocommon endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teaminfocommon')

    table_names = example_team.data.keys()

    assert 'TeamInfoCommon' in table_names
    assert 'TeamSeasonRanks' in table_names
    assert 'AvailableSeasons' in table_names

    example_info = example_team.data['TeamInfoCommon'][0]
    example_ranks = example_team.data['TeamSeasonRanks'][0]
    example_season = example_team.data['AvailableSeasons'][0]

    assert list(example_info.keys()) == ['TEAM_ID',
                                         'SEASON_YEAR',
                                         'TEAM_CITY',
                                         'TEAM_NAME',
                                         'TEAM_ABBREVIATION',
                                         'TEAM_CONFERENCE',
                                         'TEAM_DIVISION',
                                         'TEAM_CODE',
                                         'W',
                                         'L',
                                         'PCT',
                                         'CONF_RANK',
                                         'DIV_RANK',
                                         'MIN_YEAR',
                                         'MAX_YEAR']

    assert list(example_ranks.keys()) == ['LEAGUE_ID',
                                          'SEASON_ID',
                                          'TEAM_ID',
                                          'PTS_RANK',
                                          'PTS_PG',
                                          'REB_RANK',
                                          'REB_PG',
                                          'AST_RANK',
                                          'AST_PG',
                                          'OPP_PTS_RANK',
                                          'OPP_PTS_PG']

    assert list(example_season.keys()) == ['SEASON_ID']

def test_team_player():
    """ tests the teamplayerdashboard endpoint of the Player class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                            player_id='203954',
                            endpoint='teamplayerdashboard')

    table_names = example_team.data.keys()

    assert 'TeamOverall' in table_names
    assert 'PlayersSeasonTotals' in table_names

    example_info = example_team.data['TeamOverall'][0]
    example_players = example_team.data['PlayersSeasonTotals'][0]

    columns = ['GROUP_SET',
               'TEAM_ID',
               'TEAM_NAME',
               'GROUP_VALUE',
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
    
    assert list(example_info.keys()) == columns

    assert list(example_players.keys()) == ['GROUP_SET',
                                            'PLAYER_ID',
                                            'PLAYER_NAME',
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
                                            'TD3_RANK']

def test_team_onoff_details():
    """ tests the teamplayeronoffdetails endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamplayeronoffdetails')

    table_names = example_team.data.keys()

    assert 'OverallTeamPlayerOnOffDetails' in table_names
    assert 'PlayersOnCourtTeamPlayerOnOffDetails' in table_names
    assert 'PlayersOffCourtTeamPlayerOnOffDetails' in table_names

    example_overall = example_team.data['OverallTeamPlayerOnOffDetails'][0]
    example_on = example_team.data['PlayersOnCourtTeamPlayerOnOffDetails'][0]
    example_off = example_team.data['PlayersOffCourtTeamPlayerOnOffDetails'][0]

    assert list(example_overall.keys()) == ['GROUP_SET',
                                            'GROUP_VALUE',
                                            'TEAM_ID',
                                            'TEAM_ABBREVIATION',
                                            'TEAM_NAME',
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

    assert list(example_on.keys()) == ['GROUP_SET',
                                       'TEAM_ID',
                                       'TEAM_ABBREVIATION',
                                       'TEAM_NAME',
                                       'VS_PLAYER_ID',
                                       'VS_PLAYER_NAME',
                                       'COURT_STATUS',
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

    assert list(example_off.keys()) == ['GROUP_SET',
                                       'TEAM_ID',
                                       'TEAM_ABBREVIATION',
                                       'TEAM_NAME',
                                       'VS_PLAYER_ID',
                                       'VS_PLAYER_NAME',
                                       'COURT_STATUS',
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
    
def test_team_onoff_summary():
    """ tests the teamplayeronoffsummary endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamplayeronoffsummary')

    table_names = example_team.data.keys()

    assert 'OverallTeamPlayerOnOffSummary' in table_names
    assert 'PlayersOnCourtTeamPlayerOnOffSummary' in table_names
    assert 'PlayersOffCourtTeamPlayerOnOffSummary' in table_names

    example_overall = example_team.data['OverallTeamPlayerOnOffSummary'][0]
    example_on = example_team.data['PlayersOnCourtTeamPlayerOnOffSummary'][0]
    example_off = example_team.data['PlayersOffCourtTeamPlayerOnOffSummary'][0]

    assert list(example_overall.keys()) == ['GROUP_SET',
                                            'GROUP_VALUE',
                                            'TEAM_ID',
                                            'TEAM_ABBREVIATION',
                                            'TEAM_NAME',
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

    assert list(example_on.keys()) == ['GROUP_SET',
                                       'TEAM_ID',
                                       'TEAM_ABBREVIATION',
                                       'TEAM_NAME',
                                       'VS_PLAYER_ID',
                                       'VS_PLAYER_NAME',
                                       'COURT_STATUS',
                                       'GP',
                                       'MIN',
                                       'PLUS_MINUS',
                                       'OFF_RATING',
                                       'DEF_RATING',
                                       'NET_RATING']

    assert list(example_off.keys()) == ['GROUP_SET',
                                       'TEAM_ID',
                                       'TEAM_ABBREVIATION',
                                       'TEAM_NAME',
                                       'VS_PLAYER_ID',
                                       'VS_PLAYER_NAME',
                                       'COURT_STATUS',
                                       'GP',
                                       'MIN',
                                       'PLUS_MINUS',
                                       'OFF_RATING',
                                       'DEF_RATING',
                                       'NET_RATING']

def test_team_v_player():
    """ tests the teamvsplayer endpoint of the Player class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamvsplayer')

    table_names = example_team.data.keys()

    assert 'Overall' in table_names
    assert 'vsPlayerOverall' in table_names
    assert 'OnOffCourt' in table_names
    assert 'ShotDistanceOverall' in table_names
    assert 'ShotDistanceOnCourt' in table_names
    assert 'ShotDistanceOffCourt' in table_names
    assert 'ShotAreaOverall' in table_names
    assert 'ShotAreaOnCourt' in table_names
    assert 'ShotAreaOffCourt' in table_names

    example_overall = example_team.data['Overall'][0]
    example_vs_overall = example_team.data['vsPlayerOverall'][0]
    example_on_off = example_team.data['OnOffCourt'][0]
    example_dist = example_team.data['ShotDistanceOverall'][0]
    example_dist_on = example_team.data['ShotDistanceOnCourt'][0]
    example_dist_off = example_team.data['ShotDistanceOffCourt'][0]
    example_area = example_team.data['ShotAreaOverall'][0]
    example_area_on = example_team.data['ShotAreaOnCourt'][0]
    example_area_off = example_team.data['ShotAreaOffCourt'][0]

    assert list(example_overall.keys()) == ['GROUP_SET',
                                            'GROUP_VALUE',
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
                                            'PLUS_MINUS_RANK',
                                            'CFID',
                                            'CFPARAMS']

    assert list(example_vs_overall.keys()) == ['GROUP_SET',
                                               'GROUP_VALUE',
                                               'PLAYER_ID',
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
    
    assert list(example_on_off.keys()) == ['GROUP_SET',
                                           'TEAM_ID',
                                           'TEAM_ABBREVIATION',
                                           'TEAM_NAME',
                                           'VS_PLAYER_ID',
                                           'VS_PLAYER_NAME',
                                           'COURT_STATUS',
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
                                           'PLUS_MINUS_RANK',
                                           'CFID',
                                           'CFPARAMS']

    assert list(example_dist.keys()) == ['GROUP_SET',
                                         'GROUP_VALUE',
                                         'TEAM_ID',
                                         'TEAM_ABBREVIATION',
                                         'TEAM_NAME',
                                         'FGM',
                                         'FGA',
                                         'FG_PCT',
                                         'CFID',
                                         'CFPARAMS']

    assert list(example_dist_on.keys()) == ['GROUP_SET',
                                            'TEAM_ID',
                                            'TEAM_ABBREVIATION',
                                            'TEAM_NAME',
                                            'VS_PLAYER_ID',
                                            'VS_PLAYER_NAME',
                                            'COURT_STATUS',
                                            'GROUP_VALUE',
                                            'FGM',
                                            'FGA',
                                            'FG_PCT',
                                            'CFID',
                                            'CFPARAMS']

    assert list(example_dist_off.keys()) == ['GROUP_SET',
                                            'TEAM_ID',
                                            'TEAM_ABBREVIATION',
                                            'TEAM_NAME',
                                            'VS_PLAYER_ID',
                                            'VS_PLAYER_NAME',
                                            'COURT_STATUS',
                                            'GROUP_VALUE',
                                            'FGM',
                                            'FGA',
                                            'FG_PCT',
                                            'CFID',
                                            'CFPARAMS']

    assert list(example_area.keys()) == ['GROUP_SET',
                                         'GROUP_VALUE',
                                         'TEAM_ID',
                                         'TEAM_ABBREVIATION',
                                         'TEAM_NAME',
                                         'FGM',
                                         'FGA',
                                         'FG_PCT',
                                         'CFID',
                                         'CFPARAMS']

    assert list(example_area_on.keys()) == ['GROUP_SET',
                                            'TEAM_ID',
                                            'TEAM_ABBREVIATION',
                                            'TEAM_NAME',
                                            'VS_PLAYER_ID',
                                            'VS_PLAYER_NAME',
                                            'COURT_STATUS',
                                            'GROUP_VALUE',
                                            'FGM',
                                            'FGA',
                                            'FG_PCT',
                                            'CFID',
                                            'CFPARAMS']

    assert list(example_area_off.keys()) == ['GROUP_SET',
                                            'TEAM_ID',
                                            'TEAM_ABBREVIATION',
                                            'TEAM_NAME',
                                            'VS_PLAYER_ID',
                                            'VS_PLAYER_NAME',
                                            'COURT_STATUS',
                                            'GROUP_VALUE',
                                            'FGM',
                                            'FGA',
                                            'FG_PCT',
                                            'CFID',
                                            'CFPARAMS']

def test_team_stats():
    """ tests the teamyearbyyearstats endpoint of the Team class
    """

    time.sleep(1)
    example_team = Team(headers=HEADERS,
                        endpoint='teamyearbyyearstats')

    table_names = example_team.data.keys()

    assert 'TeamStats' in table_names

    example_stats = example_team.data['TeamStats'][0]

    assert list(example_stats.keys()) == ['TEAM_ID',
                                          'TEAM_CITY',
                                          'TEAM_NAME',
                                          'YEAR',
                                          'GP',
                                          'WINS',
                                          'LOSSES',
                                          'WIN_PCT',
                                          'CONF_RANK',
                                          'DIV_RANK',
                                          'PO_WINS',
                                          'PO_LOSSES',
                                          'CONF_COUNT',
                                          'DIV_COUNT',
                                          'NBA_FINALS_APPEARANCE',
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
                                          'PF',
                                          'STL',
                                          'TOV',
                                          'BLK',
                                          'PTS',
                                          'PTS_RANK']
