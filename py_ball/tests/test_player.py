#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:51:00 2018

@author: patrickmcfarlane

test_player.py

This function contains the tests for
functions in the player.py file
"""

import time

from .__init__ import HEADERS
from ..player import Player

def test_playercareer():
    """ tests the playercareerstats	 endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            player_id='203954')

    table_names = example_player.data.keys()

    assert 'SeasonTotalsRegularSeason' in table_names
    assert 'CareerTotalsRegularSeason' in table_names
    assert 'SeasonTotalsPostSeason' in table_names
    assert 'CareerTotalsPostSeason' in table_names
    assert 'SeasonTotalsAllStarSeason' in table_names
    assert 'CareerTotalsAllStarSeason' in table_names
    assert 'SeasonTotalsCollegeSeason' in table_names
    assert 'CareerTotalsCollegeSeason' in table_names
    assert 'SeasonRankingsRegularSeason' in table_names
    assert 'SeasonRankingsPostSeason' in table_names

    example_season_reg = example_player.data['SeasonTotalsRegularSeason'][0]
    example_career_reg = example_player.data['CareerTotalsRegularSeason'][0]
    example_season_post = example_player.data['SeasonTotalsPostSeason'][0]
    example_career_post = example_player.data['CareerTotalsPostSeason'][0]
    example_season_star = example_player.data['SeasonTotalsAllStarSeason'][0]
    example_career_star = example_player.data['CareerTotalsAllStarSeason'][0]
    example_season_col = example_player.data['SeasonTotalsCollegeSeason'][0]
    example_career_col = example_player.data['CareerTotalsCollegeSeason'][0]
    example_seasonrank_reg = example_player.data['SeasonRankingsRegularSeason'][0]
    example_seasonrank_post = example_player.data['SeasonRankingsPostSeason'][0]

    assert list(example_season_reg.keys()) == ['PLAYER_ID',
                                               'SEASON_ID',
                                               'LEAGUE_ID',
                                               'TEAM_ID',
                                               'TEAM_ABBREVIATION',
                                               'PLAYER_AGE',
                                               'GP',
                                               'GS',
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

    assert list(example_career_reg.keys()) == ['PLAYER_ID',
                                               'LEAGUE_ID',
                                               'Team_ID',
                                               'GP',
                                               'GS',
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

    assert list(example_season_post.keys()) == ['PLAYER_ID',
                                                'SEASON_ID',
                                                'LEAGUE_ID',
                                                'TEAM_ID',
                                                'TEAM_ABBREVIATION',
                                                'PLAYER_AGE',
                                                'GP',
                                                'GS',
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

    assert list(example_career_post.keys()) == ['PLAYER_ID',
                                                'LEAGUE_ID',
                                                'Team_ID',
                                                'GP',
                                                'GS',
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

    assert list(example_season_star.keys()) == ['PLAYER_ID',
                                                'SEASON_ID',
                                                'LEAGUE_ID',
                                                'TEAM_ID',
                                                'TEAM_ABBREVIATION',
                                                'PLAYER_AGE',
                                                'GP',
                                                'GS',
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

    assert list(example_career_star.keys()) == ['PLAYER_ID',
                                                'LEAGUE_ID',
                                                'Team_ID',
                                                'GP',
                                                'GS',
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

    assert list(example_season_col.keys()) == ['PLAYER_ID',
                                               'SEASON_ID',
                                               'LEAGUE_ID',
                                               'ORGANIZATION_ID',
                                               'SCHOOL_NAME',
                                               'PLAYER_AGE',
                                               'GP',
                                               'GS',
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

    assert list(example_career_col.keys()) == ['PLAYER_ID',
                                               'LEAGUE_ID',
                                               'ORGANIZATION_ID',
                                               'GP',
                                               'GS',
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

    assert list(example_seasonrank_reg.keys()) == ['PLAYER_ID',
                                                   'SEASON_ID',
                                                   'LEAGUE_ID',
                                                   'TEAM_ID',
                                                   'TEAM_ABBREVIATION',
                                                   'PLAYER_AGE',
                                                   'GP',
                                                   'GS',
                                                   'RANK_PG_MIN',
                                                   'RANK_PG_FGM',
                                                   'RANK_PG_FGA',
                                                   'RANK_FG_PCT',
                                                   'RANK_PG_FG3M',
                                                   'RANK_PG_FG3A',
                                                   'RANK_FG3_PCT',
                                                   'RANK_PG_FTM',
                                                   'RANK_PG_FTA',
                                                   'RANK_FT_PCT',
                                                   'RANK_PG_OREB',
                                                   'RANK_PG_DREB',
                                                   'RANK_PG_REB',
                                                   'RANK_PG_AST',
                                                   'RANK_PG_STL',
                                                   'RANK_PG_BLK',
                                                   'RANK_PG_TOV',
                                                   'RANK_PG_PTS',
                                                   'RANK_PG_EFF']

    assert list(example_seasonrank_post.keys()) == ['PLAYER_ID',
                                                    'SEASON_ID',
                                                    'LEAGUE_ID',
                                                    'TEAM_ID',
                                                    'TEAM_ABBREVIATION',
                                                    'PLAYER_AGE',
                                                    'GP',
                                                    'GS',
                                                    'RANK_PG_MIN',
                                                    'RANK_PG_FGM',
                                                    'RANK_PG_FGA',
                                                    'RANK_FG_PCT',
                                                    'RANK_PG_FG3M',
                                                    'RANK_PG_FG3A',
                                                    'RANK_FG3_PCT',
                                                    'RANK_PG_FTM',
                                                    'RANK_PG_FTA',
                                                    'RANK_FT_PCT',
                                                    'RANK_PG_OREB',
                                                    'RANK_PG_DREB',
                                                    'RANK_PG_REB',
                                                    'RANK_PG_AST',
                                                    'RANK_PG_STL',
                                                    'RANK_PG_BLK',
                                                    'RANK_PG_TOV',
                                                    'RANK_PG_PTS',
                                                    'RANK_PG_EFF']

def test_playercompare():
    """ tests the playercompare endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playercompare')

    table_names = example_player.data.keys()

    assert 'OverallCompare' in table_names
    assert 'Individual' in table_names

    example_overall = example_player.data['OverallCompare'][0]
    example_individual = example_player.data['Individual'][0]

    assert list(example_overall.keys()) == ['GROUP_SET',
                                            'DESCRIPTION',
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
                                            'PLUS_MINUS']

    assert list(example_individual.keys()) == ['GROUP_SET',
                                               'DESCRIPTION',
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
                                               'PLUS_MINUS']

def test_player_clutch():
    """ tests the playerdashboardbyclutch endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashboardbyclutch')

    table_names = example_player.data.keys()

    assert 'OverallPlayerDashboard' in table_names
    assert 'Last5Min5PointPlayerDashboard' in table_names
    assert 'Last3Min5PointPlayerDashboard' in table_names
    assert 'Last1Min5PointPlayerDashboard' in table_names
    assert 'Last30Sec3PointPlayerDashboard' in table_names
    assert 'Last10Sec3PointPlayerDashboard' in table_names
    assert 'Last5MinPlusMinus5PointPlayerDashboard' in table_names
    assert 'Last3MinPlusMinus5PointPlayerDashboard' in table_names
    assert 'Last1MinPlusMinus5PointPlayerDashboard' in table_names
    assert 'Last30Sec3Point2PlayerDashboard' in table_names
    assert 'Last10Sec3Point2PlayerDashboard' in table_names

    example_overall = example_player.data['OverallPlayerDashboard'][0]
    example_last5_5 = example_player.data['Last5Min5PointPlayerDashboard'][0]
    example_last3_5 = example_player.data['Last3Min5PointPlayerDashboard'][0]
    example_last1_5 = example_player.data['Last1Min5PointPlayerDashboard'][0]
    example_last30_3 = example_player.data['Last30Sec3PointPlayerDashboard'][0]
    example_last10_3 = example_player.data['Last10Sec3PointPlayerDashboard'][0]
    example_last5 = example_player.data['Last5MinPlusMinus5PointPlayerDashboard'][0]
    example_last3 = example_player.data['Last3MinPlusMinus5PointPlayerDashboard'][0]
    example_last1 = example_player.data['Last1MinPlusMinus5PointPlayerDashboard'][0]
    example_last30_3_2 = example_player.data['Last30Sec3Point2PlayerDashboard'][0]
    example_last10_3_2 = example_player.data['Last10Sec3Point2PlayerDashboard'][0]

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


def test_player_gamesplits():
    """ tests the playerdashboardbygamesplits endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashboardbygamesplits')

    table_names = example_player.data.keys()

    assert 'OverallPlayerDashboard' in table_names
    assert 'ByHalfPlayerDashboard' in table_names
    assert 'ByPeriodPlayerDashboard' in table_names
    assert 'ByScoreMarginPlayerDashboard' in table_names
    assert 'ByActualMarginPlayerDashboard' in table_names

    example_overall = example_player.data['OverallPlayerDashboard'][0]
    example_half = example_player.data['ByHalfPlayerDashboard'][0]
    example_period = example_player.data['ByPeriodPlayerDashboard'][0]
    example_score = example_player.data['ByScoreMarginPlayerDashboard'][0]
    example_margin = example_player.data['ByActualMarginPlayerDashboard'][0]

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

    assert list(example_overall.keys()) == columns

    assert list(example_half.keys()) == columns

    assert list(example_period.keys()) == columns

    assert list(example_score.keys()) == columns

    assert list(example_margin.keys()) == columns

def test_player_generalsplits():
    """ tests the playerdashboardbygeneralsplits endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashboardbygeneralsplits')

    table_names = example_player.data.keys()

    assert 'OverallPlayerDashboard' in table_names
    assert 'LocationPlayerDashboard' in table_names
    assert 'WinsLossesPlayerDashboard' in table_names
    assert 'MonthPlayerDashboard' in table_names
    assert 'PrePostAllStarPlayerDashboard' in table_names
    assert 'StartingPosition' in table_names
    assert 'DaysRestPlayerDashboard' in table_names

    example_overall = example_player.data['OverallPlayerDashboard'][0]
    example_location = example_player.data['LocationPlayerDashboard'][0]
    example_wl = example_player.data['WinsLossesPlayerDashboard'][0]
    example_month = example_player.data['MonthPlayerDashboard'][0]
    example_star = example_player.data['PrePostAllStarPlayerDashboard'][0]
    example_starter = example_player.data['StartingPosition'][0]
    example_rest = example_player.data['DaysRestPlayerDashboard'][0]

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

    assert list(example_overall.keys()) == columns

    assert list(example_location.keys()) == columns

    assert list(example_wl.keys()) == columns

    assert list(example_month.keys()) == columns

    assert list(example_star.keys()) == columns

    assert list(example_starter.keys()) == columns

    assert list(example_rest.keys()) == columns

def test_player_lastngames():
    """ tests the playerdashboardbylastngames endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashboardbylastngames')

    table_names = example_player.data.keys()

    assert 'OverallPlayerDashboard' in table_names
    assert 'Last5PlayerDashboard' in table_names
    assert 'Last10PlayerDashboard' in table_names
    assert 'Last15PlayerDashboard' in table_names
    assert 'Last20PlayerDashboard' in table_names
    assert 'GameNumberPlayerDashboard' in table_names

    example_overall = example_player.data['OverallPlayerDashboard'][0]
    example_last5 = example_player.data['Last5PlayerDashboard'][0]
    example_last10 = example_player.data['Last10PlayerDashboard'][0]
    example_last15 = example_player.data['Last15PlayerDashboard'][0]
    example_last20 = example_player.data['Last20PlayerDashboard'][0]
    example_game = example_player.data['GameNumberPlayerDashboard'][0]

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

    assert list(example_overall.keys()) == columns

    assert list(example_last5.keys()) == columns

    assert list(example_last10.keys()) == columns

    assert list(example_last15.keys()) == columns

    assert list(example_last20.keys()) == columns

    assert list(example_game.keys()) == columns
    
def test_player_opponent():
    """ tests the playerdashboardbyopponent endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashboardbyopponent')

    table_names = example_player.data.keys()

    assert 'OverallPlayerDashboard' in table_names
    assert 'ConferencePlayerDashboard' in table_names
    assert 'DivisionPlayerDashboard' in table_names
    assert 'OpponentPlayerDashboard' in table_names

    example_overall = example_player.data['OverallPlayerDashboard'][0]
    example_conference = example_player.data['ConferencePlayerDashboard'][0]
    example_division = example_player.data['DivisionPlayerDashboard'][0]
    example_opponent = example_player.data['OpponentPlayerDashboard'][0]

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

    assert list(example_overall.keys()) == columns

    assert list(example_conference.keys()) == columns

    assert list(example_division.keys()) == columns

    assert list(example_opponent.keys()) == columns

def test_player_shootingsplits():
    """ tests the playerdashboardbyshootingsplits endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashboardbyshootingsplits')

    table_names = example_player.data.keys()

    assert 'OverallPlayerDashboard' in table_names
    assert 'Shot5FTPlayerDashboard' in table_names
    assert 'Shot8FTPlayerDashboard' in table_names
    assert 'ShotAreaPlayerDashboard' in table_names
    assert 'AssitedShotPlayerDashboard' in table_names
    assert 'ShotTypeSummaryPlayerDashboard' in table_names
    assert 'ShotTypePlayerDashboard' in table_names
    assert 'AssistedBy' in table_names

    example_overall = example_player.data['OverallPlayerDashboard'][0]
    example_5ft = example_player.data['Shot5FTPlayerDashboard'][0]
    example_8ft = example_player.data['Shot8FTPlayerDashboard'][0]
    example_area = example_player.data['ShotAreaPlayerDashboard'][0]
    example_assisted = example_player.data['AssitedShotPlayerDashboard'][0]
    example_typesummary = example_player.data['ShotTypeSummaryPlayerDashboard'][0]
    example_type = example_player.data['ShotTypePlayerDashboard'][0]
    example_assistedby = example_player.data['AssistedBy'][0]

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

    assert list(example_typesummary.keys()) == ['GROUP_SET',
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
                                                'CFID',
                                                'CFPARAMS']

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

def test_player_teamperformance():
    """ tests the playerdashboardbyteamperformance endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashboardbyteamperformance')

    table_names = example_player.data.keys()

    assert 'OverallPlayerDashboard' in table_names
    assert 'ScoreDifferentialPlayerDashboard' in table_names
    assert 'PointsScoredPlayerDashboard' in table_names
    assert 'PontsAgainstPlayerDashboard' in table_names

    example_overall = example_player.data['OverallPlayerDashboard'][0]
    example_scorediff = example_player.data['ScoreDifferentialPlayerDashboard'][0]
    example_scored = example_player.data['PointsScoredPlayerDashboard'][0]
    example_against = example_player.data['PontsAgainstPlayerDashboard'][0]

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

    assert list(example_scorediff.keys()) == columns

    assert list(example_scored.keys()) == columns

    assert list(example_against.keys()) == columns

def test_player_yoy():
    """ tests the playerdashboardbyyearoveryear endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashboardbyyearoveryear')

    table_names = example_player.data.keys()

    assert 'OverallPlayerDashboard' in table_names
    assert 'ByYearPlayerDashboard' in table_names

    example_overall = example_player.data['OverallPlayerDashboard'][0]
    example_yoy = example_player.data['ByYearPlayerDashboard'][0]

    columns = ['GROUP_SET',
               'GROUP_VALUE',
               'TEAM_ID',
               'TEAM_ABBREVIATION',
               'MAX_GAME_DATE',
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

    assert list(example_overall.keys()) == columns
    assert list(example_yoy.keys()) == columns

def test_player_pass():
    """ tests the playerdashptpass endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashptpass')

    table_names = example_player.data.keys()

    assert 'PassesMade' in table_names
    assert 'PassesReceived' in table_names

    example_made = example_player.data['PassesMade'][0]
    example_received = example_player.data['PassesReceived'][0]

    assert list(example_made.keys()) == ['PLAYER_ID',
                                         'PLAYER_NAME_LAST_FIRST',
                                         'TEAM_NAME',
                                         'TEAM_ID',
                                         'TEAM_ABBREVIATION',
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

    assert list(example_received.keys()) == ['PLAYER_ID',
                                             'PLAYER_NAME_LAST_FIRST',
                                             'TEAM_NAME',
                                             'TEAM_ID',
                                             'TEAM_ABBREVIATION',
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

def test_player_reb():
    """ tests the playerdashptreb endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashptreb')

    table_names = example_player.data.keys()

    assert 'OverallRebounding' in table_names
    assert 'ShotTypeRebounding' in table_names
    assert 'NumContestedRebounding' in table_names
    assert 'ShotDistanceRebounding' in table_names
    assert 'RebDistanceRebounding' in table_names

    example_overall = example_player.data['OverallRebounding'][0]
    example_type = example_player.data['ShotTypeRebounding'][0]
    example_num = example_player.data['NumContestedRebounding'][0]
    example_shotdist = example_player.data['ShotDistanceRebounding'][0]
    example_rebdist = example_player.data['RebDistanceRebounding'][0]

    assert list(example_overall.keys()) == ['PLAYER_ID',
                                            'PLAYER_NAME_LAST_FIRST',
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

    assert list(example_type.keys()) == ['PLAYER_ID',
                                         'PLAYER_NAME_LAST_FIRST',
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

    assert list(example_num.keys()) == ['PLAYER_ID',
                                        'PLAYER_NAME_LAST_FIRST',
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

    assert list(example_shotdist.keys()) == ['PLAYER_ID',
                                             'PLAYER_NAME_LAST_FIRST',
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

    assert list(example_rebdist.keys()) == ['PLAYER_ID',
                                           'PLAYER_NAME_LAST_FIRST',
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

def test_player_defend():
    """ tests the playerdashptshotdefend endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashptshotdefend')

    table_names = example_player.data.keys()

    assert 'DefendingShots' in table_names

    example_defend = example_player.data['DefendingShots'][0]

    assert list(example_defend.keys()) == ['CLOSE_DEF_PERSON_ID',
                                           'GP',
                                           'G',
                                           'DEFENSE_CATEGORY',
                                           'FREQ',
                                           'D_FGM',
                                           'D_FGA',
                                           'D_FG_PCT',
                                           'NORMAL_FG_PCT',
                                           'PCT_PLUSMINUS']

def test_player_shot():
    """ tests the playerdashptshots endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playerdashptshots')

    table_names = example_player.data.keys()

    assert 'Overall' in table_names
    assert 'GeneralShooting' in table_names
    assert 'ShotClockShooting' in table_names
    assert 'DribbleShooting' in table_names
    assert 'ClosestDefenderShooting' in table_names
    assert 'ClosestDefender10ftPlusShooting' in table_names
    assert 'TouchTimeShooting' in table_names

    example_overall = example_player.data['Overall'][0]
    example_gen = example_player.data['GeneralShooting'][0]
    example_clock = example_player.data['ShotClockShooting'][0]
    example_dribble = example_player.data['DribbleShooting'][0]
    example_defender = example_player.data['ClosestDefenderShooting'][0]
    example_defender10 = example_player.data['ClosestDefender10ftPlusShooting'][0]
    example_touch = example_player.data['TouchTimeShooting'][0]

    columns = ['PLAYER_ID',
               'PLAYER_NAME_LAST_FIRST',
               'SORT_ORDER',
               'GP',
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

    assert list(example_overall.keys()) == columns
    assert list(example_gen.keys()) == columns
    assert list(example_clock.keys()) == ['PLAYER_ID',
                                          'PLAYER_NAME_LAST_FIRST',
                                          'SORT_ORDER',
                                          'GP',
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

    assert list(example_dribble.keys()) == ['PLAYER_ID',
                                           'PLAYER_NAME_LAST_FIRST',
                                           'SORT_ORDER',
                                           'GP',
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

    assert list(example_defender.keys()) == ['PLAYER_ID',
                                             'PLAYER_NAME_LAST_FIRST',
                                             'SORT_ORDER',
                                             'GP',
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

    assert list(example_defender10.keys()) == ['PLAYER_ID',
                                               'PLAYER_NAME_LAST_FIRST',
                                               'SORT_ORDER',
                                               'GP',
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

    assert list(example_touch.keys()) == ['PLAYER_ID',
                                          'PLAYER_NAME_LAST_FIRST',
                                          'SORT_ORDER',
                                          'GP',
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
    
def test_player_gamelog():
    """ tests the playergamelog endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playergamelog')

    table_names = example_player.data.keys()

    assert 'PlayerGameLog' in table_names

    example_log = example_player.data['PlayerGameLog'][0]

    assert list(example_log.keys()) == ['SEASON_ID',
                                        'Player_ID',
                                        'Game_ID',
                                        'GAME_DATE',
                                        'MATCHUP',
                                        'WL',
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
                                        'PTS',
                                        'PLUS_MINUS',
                                        'VIDEO_AVAILABLE']
    
def test_playerprofile():
    """ tests the playerprofilev2 endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            player_id='203954',
                            endpoint='playerprofilev2')

    table_names = example_player.data.keys()

    assert 'SeasonTotalsRegularSeason' in table_names
    assert 'CareerTotalsRegularSeason' in table_names
    assert 'SeasonTotalsPostSeason' in table_names
    assert 'CareerTotalsPostSeason' in table_names
    assert 'SeasonTotalsAllStarSeason' in table_names
    assert 'CareerTotalsAllStarSeason' in table_names
    assert 'SeasonTotalsCollegeSeason' in table_names
    assert 'CareerTotalsCollegeSeason' in table_names
    assert 'SeasonRankingsRegularSeason' in table_names
    assert 'SeasonRankingsPostSeason' in table_names

    example_season_reg = example_player.data['SeasonTotalsRegularSeason'][0]
    example_career_reg = example_player.data['CareerTotalsRegularSeason'][0]
    example_season_post = example_player.data['SeasonTotalsPostSeason'][0]
    example_career_post = example_player.data['CareerTotalsPostSeason'][0]
    example_season_star = example_player.data['SeasonTotalsAllStarSeason'][0]
    example_career_star = example_player.data['CareerTotalsAllStarSeason'][0]
    example_season_col = example_player.data['SeasonTotalsCollegeSeason'][0]
    example_career_col = example_player.data['CareerTotalsCollegeSeason'][0]
    example_seasonrank_reg = example_player.data['SeasonRankingsRegularSeason'][0]
    example_seasonrank_post = example_player.data['SeasonRankingsPostSeason'][0]
    example_season_high = example_player.data['SeasonHighs'][0]
    example_career_high = example_player.data['CareerHighs'][0]
    example_next = example_player.data['NextGame'][0]

    columns = ['PLAYER_ID',
               'SEASON_ID',
               'LEAGUE_ID',
               'TEAM_ID',
               'TEAM_ABBREVIATION',
               'PLAYER_AGE',
               'GP',
               'GS',
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

    assert list(example_season_reg.keys()) == columns

    assert list(example_career_reg.keys()) == ['PLAYER_ID',
                                               'LEAGUE_ID',
                                               'TEAM_ID',
                                               'GP',
                                               'GS',
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

    assert list(example_season_post.keys()) == columns

    assert list(example_career_post.keys()) == ['PLAYER_ID',
                                                'LEAGUE_ID',
                                                'TEAM_ID',
                                                'GP',
                                                'GS',
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

    assert list(example_season_star.keys()) == columns

    assert list(example_career_star.keys()) == ['PLAYER_ID',
                                                'LEAGUE_ID',
                                                'TEAM_ID',
                                                'GP',
                                                'GS',
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

    assert list(example_season_col.keys()) == ['PLAYER_ID',
                                               'SEASON_ID',
                                               'LEAGUE_ID',
                                               'ORGANIZATION_ID',
                                               'SCHOOL_NAME',
                                               'PLAYER_AGE',
                                               'GP',
                                               'GS',
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

    assert list(example_career_col.keys()) == ['PLAYER_ID',
                                               'LEAGUE_ID',
                                               'ORGANIZATION_ID',
                                               'GP',
                                               'GS',
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

    assert list(example_seasonrank_reg.keys()) == ['PLAYER_ID',
                                                   'SEASON_ID',
                                                   'LEAGUE_ID',
                                                   'TEAM_ID',
                                                   'TEAM_ABBREVIATION',
                                                   'PLAYER_AGE',
                                                   'GP',
                                                   'GS',
                                                   'RANK_PG_MIN',
                                                   'RANK_PG_FGM',
                                                   'RANK_PG_FGA',
                                                   'RANK_FG_PCT',
                                                   'RANK_PG_FG3M',
                                                   'RANK_PG_FG3A',
                                                   'RANK_FG3_PCT',
                                                   'RANK_PG_FTM',
                                                   'RANK_PG_FTA',
                                                   'RANK_FT_PCT',
                                                   'RANK_PG_OREB',
                                                   'RANK_PG_DREB',
                                                   'RANK_PG_REB',
                                                   'RANK_PG_AST',
                                                   'RANK_PG_STL',
                                                   'RANK_PG_BLK',
                                                   'RANK_PG_TOV',
                                                   'RANK_PG_PTS',
                                                   'RANK_PG_EFF']

    assert list(example_seasonrank_post.keys()) == ['PLAYER_ID',
                                                    'SEASON_ID',
                                                    'LEAGUE_ID',
                                                    'TEAM_ID',
                                                    'TEAM_ABBREVIATION',
                                                    'PLAYER_AGE',
                                                    'GP',
                                                    'GS',
                                                    'RANK_PG_MIN',
                                                    'RANK_PG_FGM',
                                                    'RANK_PG_FGA',
                                                    'RANK_FG_PCT',
                                                    'RANK_PG_FG3M',
                                                    'RANK_PG_FG3A',
                                                    'RANK_FG3_PCT',
                                                    'RANK_PG_FTM',
                                                    'RANK_PG_FTA',
                                                    'RANK_FT_PCT',
                                                    'RANK_PG_OREB',
                                                    'RANK_PG_DREB',
                                                    'RANK_PG_REB',
                                                    'RANK_PG_AST',
                                                    'RANK_PG_STL',
                                                    'RANK_PG_BLK',
                                                    'RANK_PG_TOV',
                                                    'RANK_PG_PTS',
                                                    'RANK_PG_EFF']

    assert list(example_season_high.keys()) == ['PLAYER_ID',
                                                'GAME_ID',
                                                'GAME_DATE',
                                                'VS_TEAM_ID',
                                                'VS_TEAM_CITY',
                                                'VS_TEAM_NAME',
                                                'VS_TEAM_ABBREVIATION',
                                                'STAT',
                                                'STAT_VALUE',
                                                'STAT_ORDER',
                                                'DATE_EST']

    assert list(example_career_high.keys()) == ['PLAYER_ID',
                                                'GAME_ID',
                                                'GAME_DATE',
                                                'VS_TEAM_ID',
                                                'VS_TEAM_CITY',
                                                'VS_TEAM_NAME',
                                                'VS_TEAM_ABBREVIATION',
                                                'STAT',
                                                'STAT_VALUE',
                                                'STAT_ORDER',
                                                'DATE_EST']

    assert list(example_next.keys()) == ['GAME_ID',
                                         'GAME_DATE',
                                         'GAME_TIME',
                                         'LOCATION',
                                         'PLAYER_TEAM_ID',
                                         'PLAYER_TEAM_CITY',
                                         'PLAYER_TEAM_NICKNAME',
                                         'PLAYER_TEAM_ABBREVIATION',
                                         'VS_TEAM_ID',
                                         'VS_TEAM_CITY',
                                         'VS_TEAM_NICKNAME',
                                         'VS_TEAM_ABBREVIATION']

def test_player_v_player():
    """ tests the playervsplayer endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='playervsplayer')

    table_names = example_player.data.keys()

    assert 'Overall' in table_names
    assert 'OnOffCourt' in table_names
    assert 'ShotDistanceOverall' in table_names
    assert 'ShotDistanceOnCourt' in table_names
    assert 'ShotDistanceOffCourt' in table_names
    assert 'ShotAreaOverall' in table_names
    assert 'ShotAreaOnCourt' in table_names
    assert 'ShotAreaOffCourt' in table_names
    assert 'PlayerInfo' in table_names
    assert 'VsPlayerInfo' in table_names

    example_overall = example_player.data['Overall'][0]
    example_on_off = example_player.data['OnOffCourt'][0]
    example_dist = example_player.data['ShotDistanceOverall'][0]
    example_dist_on = example_player.data['ShotDistanceOnCourt'][0]
    example_dist_off = example_player.data['ShotDistanceOffCourt'][0]
    example_area = example_player.data['ShotAreaOverall'][0]
    example_area_on = example_player.data['ShotAreaOnCourt'][0]
    example_area_off = example_player.data['ShotAreaOffCourt'][0]
    example_player_inf = example_player.data['PlayerInfo'][0]
    example_vs_player_inf = example_player.data['VsPlayerInfo'][0]

    assert list(example_overall.keys()) == ['GROUP_SET',
                                            'GROUP_VALUE',
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
                                            'CFID',
                                            'CFPARAMS']

    assert list(example_on_off.keys()) == ['GROUP_SET',
                                           'PLAYER_ID',
                                           'PLAYER_NAME',
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
                                           'NBA_FANTASY_PTS',
                                           'CFID',
                                           'CFPARAMS']

    assert list(example_dist.keys()) == ['GROUP_SET',
                                         'GROUP_VALUE',
                                         'PLAYER_ID',
                                         'PLAYER_NAME',
                                         'FGM',
                                         'FGA',
                                         'FG_PCT',
                                         'CFID',
                                         'CFPARAMS']

    assert list(example_dist_on.keys()) == ['GROUP_SET',
                                            'PLAYER_ID',
                                            'PLAYER_NAME',
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
                                             'PLAYER_ID',
                                             'PLAYER_NAME',
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
                                         'PLAYER_ID',
                                         'PLAYER_NAME',
                                         'FGM',
                                         'FGA',
                                         'FG_PCT',
                                         'CFID',
                                         'CFPARAMS']

    assert list(example_area_on.keys()) == ['GROUP_SET',
                                            'PLAYER_ID',
                                            'PLAYER_NAME',
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
                                             'PLAYER_ID',
                                             'PLAYER_NAME',
                                             'VS_PLAYER_ID',
                                             'VS_PLAYER_NAME',
                                             'COURT_STATUS',
                                             'GROUP_VALUE',
                                             'FGM',
                                             'FGA',
                                             'FG_PCT',
                                             'CFID',
                                             'CFPARAMS']

    assert list(example_player_inf.keys()) == ['PERSON_ID',
                                               'FIRST_NAME',
                                               'LAST_NAME',
                                               'DISPLAY_FIRST_LAST',
                                               'DISPLAY_LAST_COMMA_FIRST',
                                               'DISPLAY_FI_LAST',
                                               'BIRTHDATE',
                                               'SCHOOL',
                                               'COUNTRY',
                                               'LAST_AFFILIATION']

    assert list(example_vs_player_inf.keys()) == ['PERSON_ID',
                                                  'FIRST_NAME',
                                                  'LAST_NAME',
                                                  'DISPLAY_FIRST_LAST',
                                                  'DISPLAY_LAST_COMMA_FIRST',
                                                  'DISPLAY_FI_LAST',
                                                  'BIRTHDATE',
                                                  'SCHOOL',
                                                  'COUNTRY',
                                                  'LAST_AFFILIATION']

def test_player_shotchart():
    """ tests the shotchartdetail endpoint of the Player class
    """

    time.sleep(1)
    example_player = Player(headers=HEADERS,
                            endpoint='shotchartdetail',
                            game_id='0021700608',
                            player_id='2772')

    table_names = example_player.data.keys()

    assert 'Shot_Chart_Detail' in table_names
    assert 'LeagueAverages' in table_names

    example_shotchart = example_player.data['Shot_Chart_Detail'][0]
    example_avg = example_player.data['LeagueAverages'][0]

    assert list(example_shotchart.keys()) == ['GRID_TYPE',
                                              'GAME_ID',
                                              'GAME_EVENT_ID',
                                              'PLAYER_ID',
                                              'PLAYER_NAME',
                                              'TEAM_ID',
                                              'TEAM_NAME',
                                              'PERIOD',
                                              'MINUTES_REMAINING',
                                              'SECONDS_REMAINING',
                                              'EVENT_TYPE',
                                              'ACTION_TYPE',
                                              'SHOT_TYPE',
                                              'SHOT_ZONE_BASIC',
                                              'SHOT_ZONE_AREA',
                                              'SHOT_ZONE_RANGE',
                                              'SHOT_DISTANCE',
                                              'LOC_X',
                                              'LOC_Y',
                                              'SHOT_ATTEMPTED_FLAG',
                                              'SHOT_MADE_FLAG',
                                              'GAME_DATE',
                                              'HTM',
                                              'VTM']

    assert list(example_avg.keys()) == ['GRID_TYPE',
                                        'SHOT_ZONE_BASIC',
                                        'SHOT_ZONE_AREA',
                                        'SHOT_ZONE_RANGE',
                                        'FGA',
                                        'FGM',
                                        'FG_PCT']
