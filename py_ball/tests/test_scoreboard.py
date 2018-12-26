#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:54:48 2018

@author: patrickmcfarlane

test_scoreboard.py

This function contains the tests for
functions in the scoreboard.py file
"""

import time

from .__init__ import HEADERS
from ..scoreboard import ScoreBoard

def test_scoreboard():
    """ tests the scoreboard endpoint of the ScoreBoard class
    """

    time.sleep(1)
    example_board = ScoreBoard(headers=HEADERS,
                               game_date='12/22/2018')

    table_names = example_board.data.keys()

    assert 'GameHeader' in table_names
    assert 'LineScore' in table_names
    assert 'SeriesStandings' in table_names
    assert 'LastMeeting' in table_names
    assert 'EastConfStandingsByDay' in table_names
    assert 'WestConfStandingsByDay' in table_names
    assert 'Available' in table_names

    example_game = example_board.data['GameHeader'][0]
    example_line = example_board.data['LineScore'][0]
    example_series = example_board.data['SeriesStandings'][0]
    example_last = example_board.data['LastMeeting'][0]
    example_east = example_board.data['EastConfStandingsByDay'][0]
    example_west = example_board.data['WestConfStandingsByDay'][0]
    example_avail = example_board.data['Available'][0]

    assert list(example_game.keys()) == ['GAME_DATE_EST',
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

    assert list(example_line.keys()) == ['GAME_DATE_EST',
                                         'GAME_SEQUENCE',
                                         'GAME_ID',
                                         'TEAM_ID',
                                         'TEAM_ABBREVIATION',
                                         'TEAM_CITY_NAME',
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
                                         'PTS',
                                         'FG_PCT',
                                         'FT_PCT',
                                         'FG3_PCT',
                                         'AST',
                                         'REB',
                                         'TOV']

    assert list(example_series.keys()) == ['GAME_ID',
                                           'HOME_TEAM_ID',
                                           'VISITOR_TEAM_ID',
                                           'GAME_DATE_EST',
                                           'HOME_TEAM_WINS',
                                           'HOME_TEAM_LOSSES',
                                           'SERIES_LEADER']

    assert list(example_last.keys()) == ['GAME_ID',
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

    assert list(example_east.keys()) == ['TEAM_ID',
                                         'LEAGUE_ID',
                                         'SEASON_ID',
                                         'STANDINGSDATE',
                                         'CONFERENCE',
                                         'TEAM',
                                         'G',
                                         'W',
                                         'L',
                                         'W_PCT',
                                         'HOME_RECORD',
                                         'ROAD_RECORD']

    assert list(example_west.keys()) == ['TEAM_ID',
                                         'LEAGUE_ID',
                                         'SEASON_ID',
                                         'STANDINGSDATE',
                                         'CONFERENCE',
                                         'TEAM',
                                         'G',
                                         'W',
                                         'L',
                                         'W_PCT',
                                         'HOME_RECORD',
                                         'ROAD_RECORD']

    assert list(example_avail.keys()) == ['GAME_ID', 'PT_AVAILABLE']

def test_scoreboardv2():
    """ tests the scoreboardv2 endpoint of the ScoreBoard class
    """

    time.sleep(1)
    example_board = ScoreBoard(headers=HEADERS,
                               endpoint='scoreboardv2',
                               game_date='12/22/2018')

    table_names = example_board.data.keys()

    assert 'GameHeader' in table_names
    assert 'LineScore' in table_names
    assert 'SeriesStandings' in table_names
    assert 'LastMeeting' in table_names
    assert 'EastConfStandingsByDay' in table_names
    assert 'WestConfStandingsByDay' in table_names
    assert 'Available' in table_names
    assert 'TeamLeaders' in table_names
    assert 'TicketLinks' in table_names
    assert 'WinProbability' in table_names

    example_game = example_board.data['GameHeader'][0]
    example_line = example_board.data['LineScore'][0]
    example_series = example_board.data['SeriesStandings'][0]
    example_last = example_board.data['LastMeeting'][0]
    example_east = example_board.data['EastConfStandingsByDay'][0]
    example_west = example_board.data['WestConfStandingsByDay'][0]
    example_avail = example_board.data['Available'][0]
    example_lead = example_board.data['TeamLeaders'][0]
    example_tick = example_board.data['TicketLinks'][0]

    assert list(example_game.keys()) == ['GAME_DATE_EST',
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
                                         'HOME_TV_BROADCASTER_ABBREVIATION',
                                         'AWAY_TV_BROADCASTER_ABBREVIATION',
                                         'LIVE_PERIOD_TIME_BCAST',
                                         'ARENA_NAME',
                                         'WH_STATUS']

    assert list(example_line.keys()) == ['GAME_DATE_EST',
                                         'GAME_SEQUENCE',
                                         'GAME_ID',
                                         'TEAM_ID',
                                         'TEAM_ABBREVIATION',
                                         'TEAM_CITY_NAME',
                                         'TEAM_NAME',
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
                                         'PTS',
                                         'FG_PCT',
                                         'FT_PCT',
                                         'FG3_PCT',
                                         'AST',
                                         'REB',
                                         'TOV']

    assert list(example_series.keys()) == ['GAME_ID',
                                           'HOME_TEAM_ID',
                                           'VISITOR_TEAM_ID',
                                           'GAME_DATE_EST',
                                           'HOME_TEAM_WINS',
                                           'HOME_TEAM_LOSSES',
                                           'SERIES_LEADER']

    assert list(example_last.keys()) == ['GAME_ID',
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

    assert list(example_east.keys()) == ['TEAM_ID',
                                         'LEAGUE_ID',
                                         'SEASON_ID',
                                         'STANDINGSDATE',
                                         'CONFERENCE',
                                         'TEAM',
                                         'G',
                                         'W',
                                         'L',
                                         'W_PCT',
                                         'HOME_RECORD',
                                         'ROAD_RECORD']

    assert list(example_west.keys()) == ['TEAM_ID',
                                         'LEAGUE_ID',
                                         'SEASON_ID',
                                         'STANDINGSDATE',
                                         'CONFERENCE',
                                         'TEAM',
                                         'G',
                                         'W',
                                         'L',
                                         'W_PCT',
                                         'HOME_RECORD',
                                         'ROAD_RECORD']

    assert list(example_avail.keys()) == ['GAME_ID', 'PT_AVAILABLE']

    assert list(example_lead.keys()) == ['GAME_ID',
                                         'TEAM_ID',
                                         'TEAM_CITY',
                                         'TEAM_NICKNAME',
                                         'TEAM_ABBREVIATION',
                                         'PTS_PLAYER_ID',
                                         'PTS_PLAYER_NAME',
                                         'PTS',
                                         'REB_PLAYER_ID',
                                         'REB_PLAYER_NAME',
                                         'REB',
                                         'AST_PLAYER_ID',
                                         'AST_PLAYER_NAME',
                                         'AST']

    assert list(example_tick.keys()) == ['GAME_ID', 'LEAG_TIX']
