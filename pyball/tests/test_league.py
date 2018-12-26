#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:37:05 2018

@author: patrickmcfarlane

test_league.py

This function contains the tests for
functions in the league.py file
"""

from .__init__ import HEADERS
from ..league import League

def test_all_players():
    """ tests the commonallplayers endpoint of the League class
    """

    example_league = League(headers=HEADERS)

    table_names = example_league.data.keys()

    assert 'CommonAllPlayers' in table_names

    example_players = example_league.data['CommonAllPlayers'][0]

    assert list(example_players.keys()) == ['PERSON_ID',
                                            'DISPLAY_LAST_COMMA_FIRST',
                                            'DISPLAY_FIRST_LAST',
                                            'ROSTERSTATUS',
                                            'FROM_YEAR',
                                            'TO_YEAR',
                                            'PLAYERCODE',
                                            'TEAM_ID',
                                            'TEAM_CITY',
                                            'TEAM_NAME',
                                            'TEAM_ABBREVIATION',
                                            'TEAM_CODE',
                                            'GAMES_PLAYED_FLAG']

def test_team_years():
    """ tests the commonteamyears endpoint of the League class
    """

    example_league = League(headers=HEADERS, endpoint='commonteamyears')

    table_names = example_league.data.keys()

    assert 'TeamYears' in table_names

    example_teams = example_league.data['TeamYears'][0]

    assert list(example_teams.keys()) == ['LEAGUE_ID',
                                          'TEAM_ID',
                                          'MIN_YEAR',
                                          'MAX_YEAR',
                                          'ABBREVIATION']

def test_playoff_series():
    """ tests the commonplayoffseries endpoint of the League class
    """

    example_league = League(headers=HEADERS, endpoint='commonplayoffseries')

    table_names = example_league.data.keys()

    assert 'PlayoffSeries' in table_names

    example_playoffs = example_league.data['PlayoffSeries'][0]

    assert list(example_playoffs.keys()) == ['GAME_ID',
                                             'HOME_TEAM_ID',
                                             'VISITOR_TEAM_ID',
                                             'SERIES_ID',
                                             'GAME_NUM']
def test_franchise_history():
    """ tests the franchisehistory endpoint of the League class
    """

    example_league = League(headers=HEADERS, endpoint='franchisehistory')

    table_names = example_league.data.keys()

    assert 'FranchiseHistory' in table_names
    assert 'DefunctTeams' in table_names

    example_franchise = example_league.data['FranchiseHistory'][0]
    example_defunct = example_league.data['DefunctTeams'][0]

    assert list(example_franchise.keys()) == ['LEAGUE_ID',
                                              'TEAM_ID',
                                              'TEAM_CITY',
                                              'TEAM_NAME',
                                              'START_YEAR',
                                              'END_YEAR',
                                              'YEARS',
                                              'GAMES',
                                              'WINS',
                                              'LOSSES',
                                              'WIN_PCT',
                                              'PO_APPEARANCES',
                                              'DIV_TITLES',
                                              'CONF_TITLES',
                                              'LEAGUE_TITLES']

    assert list(example_defunct.keys()) == ['LEAGUE_ID',
                                            'TEAM_ID',
                                            'TEAM_CITY',
                                            'TEAM_NAME',
                                            'START_YEAR',
                                            'END_YEAR',
                                            'YEARS',
                                            'GAMES',
                                            'WINS',
                                            'LOSSES',
                                            'WIN_PCT',
                                            'PO_APPEARANCES',
                                            'DIV_TITLES',
                                            'CONF_TITLES',
                                            'LEAGUE_TITLES']

def test_playoff_picture():
    """ tests the playoffpicture endpoint of the League class
    """

    example_league = League(headers=HEADERS, endpoint='playoffpicture')

    table_names = example_league.data.keys()

    assert 'EastConfPlayoffPicture' in table_names
    assert 'WestConfPlayoffPicture' in table_names
    assert 'EastConfStandings' in table_names
    assert 'WestConfStandings' in table_names
    assert 'EastConfRemainingGames' in table_names
    assert 'WestConfRemainingGames' in table_names

    example_east_pp = example_league.data['EastConfPlayoffPicture'][0]
    example_west_pp = example_league.data['WestConfPlayoffPicture'][0]
    example_east_stand = example_league.data['EastConfStandings'][0]
    example_west_stand = example_league.data['WestConfStandings'][0]
    example_east_rem = example_league.data['EastConfRemainingGames'][0]
    example_west_rem = example_league.data['WestConfRemainingGames'][0]

    assert list(example_east_pp.keys()) == ['CONFERENCE',
                                            'HIGH_SEED_RANK',
                                            'HIGH_SEED_TEAM',
                                            'HIGH_SEED_TEAM_ID',
                                            'LOW_SEED_RANK',
                                            'LOW_SEED_TEAM',
                                            'LOW_SEED_TEAM_ID',
                                            'HIGH_SEED_SERIES_W',
                                            'HIGH_SEED_SERIES_L',
                                            'HIGH_SEED_SERIES_REMAINING_G',
                                            'HIGH_SEED_SERIES_REMAINING_HOME_G',
                                            'HIGH_SEED_SERIES_REMAINING_AWAY_G']

    assert list(example_west_pp.keys()) == ['CONFERENCE',
                                            'HIGH_SEED_RANK',
                                            'HIGH_SEED_TEAM',
                                            'HIGH_SEED_TEAM_ID',
                                            'LOW_SEED_RANK',
                                            'LOW_SEED_TEAM',
                                            'LOW_SEED_TEAM_ID',
                                            'HIGH_SEED_SERIES_W',
                                            'HIGH_SEED_SERIES_L',
                                            'HIGH_SEED_SERIES_REMAINING_G',
                                            'HIGH_SEED_SERIES_REMAINING_HOME_G',
                                            'HIGH_SEED_SERIES_REMAINING_AWAY_G']

    assert list(example_east_stand.keys()) == ['CONFERENCE',
                                               'RANK',
                                               'TEAM',
                                               'TEAM_ID',
                                               'WINS',
                                               'LOSSES',
                                               'PCT',
                                               'DIV',
                                               'CONF',
                                               'HOME',
                                               'AWAY',
                                               'GB',
                                               'GR_OVER_500',
                                               'GR_OVER_500_HOME',
                                               'GR_OVER_500_AWAY',
                                               'GR_UNDER_500',
                                               'GR_UNDER_500_HOME',
                                               'GR_UNDER_500_AWAY',
                                               'RANKING_CRITERIA',
                                               'CLINCHED_PLAYOFFS',
                                               'CLINCHED_CONFERENCE',
                                               'CLINCHED_DIVISION',
                                               'ELIMINATED_PLAYOFFS',
                                               'SOSA_REMAINING']

    assert list(example_west_stand.keys()) == ['CONFERENCE',
                                               'RANK',
                                               'TEAM',
                                               'TEAM_ID',
                                               'WINS',
                                               'LOSSES',
                                               'PCT',
                                               'DIV',
                                               'CONF',
                                               'HOME',
                                               'AWAY',
                                               'GB',
                                               'GR_OVER_500',
                                               'GR_OVER_500_HOME',
                                               'GR_OVER_500_AWAY',
                                               'GR_UNDER_500',
                                               'GR_UNDER_500_HOME',
                                               'GR_UNDER_500_AWAY',
                                               'RANKING_CRITERIA',
                                               'CLINCHED_PLAYOFFS',
                                               'CLINCHED_CONFERENCE',
                                               'CLINCHED_DIVISION',
                                               'ELIMINATED_PLAYOFFS',
                                               'SOSA_REMAINING']

    assert list(example_east_rem.keys()) == ['TEAM',
                                             'TEAM_ID',
                                             'REMAINING_G',
                                             'REMAINING_HOME_G',
                                             'REMAINING_AWAY_G']

    assert list(example_west_rem.keys()) == ['TEAM',
                                             'TEAM_ID',
                                             'REMAINING_G',
                                             'REMAINING_HOME_G',
                                             'REMAINING_AWAY_G']
