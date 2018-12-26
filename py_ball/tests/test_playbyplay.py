#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:37:02 2018

@author: patrickmcfarlane

test_playbyplay.py

This function contains the tests for
functions in the playbyplay.py file
"""

from .__init__ import HEADERS
from ..playbyplay import PlayByPlay

def test_playbyplay():
    """ tests the playbyplay endpoint of the PlayByPlay class
    """

    example_pbp = PlayByPlay(headers=HEADERS,
                             game_id='0021500002')

    table_names = example_pbp.data.keys()

    assert 'PlayByPlay' in table_names
    assert 'AvailableVideo' in table_names

    example_game = example_pbp.data['PlayByPlay'][0]
    example_video = example_pbp.data['AvailableVideo'][0]

    assert list(example_game.keys()) == ['GAME_ID',
                                         'EVENTNUM',
                                         'EVENTMSGTYPE',
                                         'EVENTMSGACTIONTYPE',
                                         'PERIOD',
                                         'WCTIMESTRING',
                                         'PCTIMESTRING',
                                         'HOMEDESCRIPTION',
                                         'NEUTRALDESCRIPTION',
                                         'VISITORDESCRIPTION',
                                         'SCORE',
                                         'SCOREMARGIN']

    assert list(example_video.keys()) == ['VIDEO_AVAILABLE_FLAG']
    
def test_playbyplayv2():
    """ tests the playbyplayv2 endpoint of the PlayByPlay class
    """

    example_pbp = PlayByPlay(headers=HEADERS,
                             endpoint='playbyplayv2',
                             game_id='0021500002')

    table_names = example_pbp.data.keys()

    assert 'PlayByPlay' in table_names
    assert 'AvailableVideo' in table_names

    example_game = example_pbp.data['PlayByPlay'][0]
    example_video = example_pbp.data['AvailableVideo'][0]

    assert list(example_game.keys()) == ['GAME_ID',
                                         'EVENTNUM',
                                         'EVENTMSGTYPE',
                                         'EVENTMSGACTIONTYPE',
                                         'PERIOD',
                                         'WCTIMESTRING',
                                         'PCTIMESTRING',
                                         'HOMEDESCRIPTION',
                                         'NEUTRALDESCRIPTION',
                                         'VISITORDESCRIPTION',
                                         'SCORE',
                                         'SCOREMARGIN',
                                         'PERSON1TYPE',
                                         'PLAYER1_ID',
                                         'PLAYER1_NAME',
                                         'PLAYER1_TEAM_ID',
                                         'PLAYER1_TEAM_CITY',
                                         'PLAYER1_TEAM_NICKNAME',
                                         'PLAYER1_TEAM_ABBREVIATION',
                                         'PERSON2TYPE',
                                         'PLAYER2_ID',
                                         'PLAYER2_NAME',
                                         'PLAYER2_TEAM_ID',
                                         'PLAYER2_TEAM_CITY',
                                         'PLAYER2_TEAM_NICKNAME',
                                         'PLAYER2_TEAM_ABBREVIATION',
                                         'PERSON3TYPE',
                                         'PLAYER3_ID',
                                         'PLAYER3_NAME',
                                         'PLAYER3_TEAM_ID',
                                         'PLAYER3_TEAM_CITY',
                                         'PLAYER3_TEAM_NICKNAME',
                                         'PLAYER3_TEAM_ABBREVIATION']

    assert list(example_video.keys()) == ['VIDEO_AVAILABLE_FLAG']
