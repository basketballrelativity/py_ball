#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 13:04:35 2018

@author: patrickmcfarlane

test_leaderboard.py

This function contains the tests for
functions in the leaderboard.py file
"""

from .__init__ import HEADERS
from ..leaderboard import LeaderBoard

def test_homepage_leaders():
    """ tests the homepageleaders endpoint of the LeaderBoard class
    """

    example_leaderboard = LeaderBoard(headers=HEADERS)

    table_names = example_leaderboard.data.keys()

    assert 'HomePageLeaders' in table_names
    assert 'LeagueAverage' in table_names
    assert 'LeagueMax' in table_names

    example_leaders = example_leaderboard.data['HomePageLeaders'][0]
    example_average = example_leaderboard.data['LeagueAverage'][0]
    example_max = example_leaderboard.data['LeagueMax'][0]

    assert list(example_leaders.keys()) == ['RANK',
                                            'PLAYERID',
                                            'PLAYER',
                                            'TEAM_ID',
                                            'TEAM_ABBREVIATION',
                                            'TEAM_NAME',
                                            'PTS',
                                            'FG_PCT',
                                            'FG3_PCT',
                                            'FT_PCT',
                                            'EFG_PCT',
                                            'TS_PCT',
                                            'PTS_PER48']

    assert list(example_average.keys()) == ['PTS',
                                            'FG_PCT',
                                            'FG3_PCT',
                                            'FT_PCT',
                                            'EFG_PCT',
                                            'TS_PCT',
                                            'PTS_PER48']

    assert list(example_max.keys()) == ['PTS',
                                        'FG_PCT',
                                        'FG3_PCT',
                                        'FT_PCT',
                                        'EFG_PCT',
                                        'TS_PCT',
                                        'PTS_PER48']
    
def test_homepage():
    """ tests the homepagev2 endpoint of the LeaderBoard class
    """

    example_leaderboard = LeaderBoard(headers=HEADERS,
                                      endpoint='homepagev2')

    table_names = example_leaderboard.data.keys()

    assert 'HomePageStat1' in table_names
    assert 'HomePageStat2' in table_names
    assert 'HomePageStat3' in table_names
    assert 'HomePageStat4' in table_names
    assert 'HomePageStat5' in table_names
    assert 'HomePageStat6' in table_names
    assert 'HomePageStat7' in table_names
    assert 'HomePageStat8' in table_names

    example_homestat1 = example_leaderboard.data['HomePageStat1'][0]
    example_homestat2 = example_leaderboard.data['HomePageStat2'][0]
    example_homestat3 = example_leaderboard.data['HomePageStat3'][0]
    example_homestat4 = example_leaderboard.data['HomePageStat4'][0]
    example_homestat5 = example_leaderboard.data['HomePageStat5'][0]
    example_homestat6 = example_leaderboard.data['HomePageStat6'][0]
    example_homestat7 = example_leaderboard.data['HomePageStat7'][0]
    example_homestat8 = example_leaderboard.data['HomePageStat8'][0]

    assert list(example_homestat1.keys()) == ['RANK',
                                              'PLAYER_ID',
                                              'PLAYER',
                                              'TEAM_ID',
                                              'TEAM_ABBREVIATION',
                                              'TEAM_NAME',
                                              'JERSEY_NUM',
                                              'PLAYER_POSITION',
                                              'DIST_MILES']

    assert list(example_homestat2.keys()) == ['RANK',
                                              'PLAYER_ID',
                                              'PLAYER',
                                              'TEAM_ID',
                                              'TEAM_ABBREVIATION',
                                              'TEAM_NAME',
                                              'JERSEY_NUM',
                                              'PLAYER_POSITION',
                                              'AST_POINTS_CREATED']

    assert list(example_homestat3.keys()) == ['RANK',
                                              'PLAYER_ID',
                                              'PLAYER',
                                              'TEAM_ID',
                                              'TEAM_ABBREVIATION',
                                              'TEAM_NAME',
                                              'JERSEY_NUM',
                                              'PLAYER_POSITION',
                                              'DRIVES']

    assert list(example_homestat4.keys()) == ['RANK',
                                              'PLAYER_ID',
                                              'PLAYER',
                                              'TEAM_ID',
                                              'TEAM_ABBREVIATION',
                                              'TEAM_NAME',
                                              'JERSEY_NUM',
                                              'PLAYER_POSITION',
                                              'NUM_TOUCHES']

    assert list(example_homestat5.keys()) == ['RANK',
                                              'PLAYER_ID',
                                              'PLAYER',
                                              'TEAM_ID',
                                              'TEAM_ABBREVIATION',
                                              'TEAM_NAME',
                                              'JERSEY_NUM',
                                              'PLAYER_POSITION',
                                              'POST_TOUCHES']

    assert list(example_homestat6.keys()) == ['RANK',
                                              'PLAYER_ID',
                                              'PLAYER',
                                              'TEAM_ID',
                                              'TEAM_ABBREVIATION',
                                              'TEAM_NAME',
                                              'JERSEY_NUM',
                                              'PLAYER_POSITION',
                                              'REB_CONTEST']

    assert list(example_homestat7.keys()) == ['RANK',
                                              'PLAYER_ID',
                                              'PLAYER',
                                              'TEAM_ID',
                                              'TEAM_ABBREVIATION',
                                              'TEAM_NAME',
                                              'JERSEY_NUM',
                                              'PLAYER_POSITION',
                                              'CATCH_SHOOT_PTS']

    assert list(example_homestat8.keys()) == ['RANK',
                                              'PLAYER_ID',
                                              'PLAYER',
                                              'TEAM_ID',
                                              'TEAM_ABBREVIATION',
                                              'TEAM_NAME',
                                              'JERSEY_NUM',
                                              'PLAYER_POSITION',
                                              'PULL_UP_PTS']

def test_leaderstiles():
    """ tests the leaderstiles endpoint of the LeaderBoard class
    """

    example_leaderboard = LeaderBoard(headers=HEADERS, endpoint='leaderstiles')

    table_names = example_leaderboard.data.keys()

    assert 'LeadersTiles' in table_names
    assert 'AllTimeSeasonHigh' in table_names
    assert 'LastSeasonHigh' in table_names
    assert 'LowSeasonHigh' in table_names

    example_leaders = example_leaderboard.data['LeadersTiles'][0]
    example_all_high = example_leaderboard.data['AllTimeSeasonHigh'][0]
    example_high = example_leaderboard.data['LastSeasonHigh'][0]
    example_low = example_leaderboard.data['LowSeasonHigh'][0]

    assert list(example_leaders.keys()) == ['RANK',
                                            'PLAYER_ID',
                                            'PLAYER',
                                            'TEAM_ID',
                                            'TEAM_ABBREVIATION',
                                            'TEAM_NAME',
                                            'PTS']

    assert list(example_all_high.keys()) == ['PLAYER_ID',
                                             'PLAYER_NAME',
                                             'PTS',
                                             'SEASON_YEAR',
                                             'TEAM_ID',
                                             'TEAM_ABBREVIATION',
                                             'TEAM_NAME']

    assert list(example_high.keys()) == ['RANK',
                                         'PLAYER_ID',
                                         'PLAYER',
                                         'TEAM_ID',
                                         'TEAM_ABBREVIATION',
                                         'TEAM_NAME',
                                         'PTS']

    assert list(example_low.keys()) == ['PLAYER_ID',
                                        'PLAYER_NAME',
                                        'PTS',
                                        'SEASON_YEAR',
                                        'TEAM_ID',
                                        'TEAM_ABBREVIATION',
                                        'TEAM_NAME']

def test_leaders():
    """ tests the leagueleaders endpoint of the LeaderBoard class
    """

    example_leaderboard = LeaderBoard(headers=HEADERS,
                                      endpoint='leagueleaders')

    table_names = example_leaderboard.data.keys()

    assert 'LeagueLeaders' in table_names

    example_leaders = example_leaderboard.data['LeagueLeaders'][0]

    assert list(example_leaders.keys()) == ['PLAYER_ID',
                                            'RANK',
                                            'PLAYER',
                                            'TEAM',
                                            'GP',
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
                                            'PTS',
                                            'EFF']
