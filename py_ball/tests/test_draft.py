#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 12:29:35 2018

@author: patrickmcfarlane

test_draft.py

This function contains the tests for
functions in the draft.py file
"""

from .__init__ import HEADERS
from ..draft import Draft

def test_draft_combine():
    """ tests the draftcombinestats endpoint of the Draft class
    """

    example_draft = Draft(headers=HEADERS)

    table_names = example_draft.data.keys()

    assert 'DraftCombineStats' in table_names

    example_player_stats = example_draft.data['DraftCombineStats'][0]

    assert list(example_player_stats.keys()) == ['SEASON',
                                                 'PLAYER_ID',
                                                 'FIRST_NAME',
                                                 'LAST_NAME',
                                                 'PLAYER_NAME',
                                                 'POSITION',
                                                 'HEIGHT_WO_SHOES',
                                                 'HEIGHT_WO_SHOES_FT_IN',
                                                 'HEIGHT_W_SHOES',
                                                 'HEIGHT_W_SHOES_FT_IN',
                                                 'WEIGHT',
                                                 'WINGSPAN',
                                                 'WINGSPAN_FT_IN',
                                                 'STANDING_REACH',
                                                 'STANDING_REACH_FT_IN',
                                                 'BODY_FAT_PCT',
                                                 'HAND_LENGTH',
                                                 'HAND_WIDTH',
                                                 'STANDING_VERTICAL_LEAP',
                                                 'MAX_VERTICAL_LEAP',
                                                 'LANE_AGILITY_TIME',
                                                 'MODIFIED_LANE_AGILITY_TIME',
                                                 'THREE_QUARTER_SPRINT',
                                                 'BENCH_PRESS',
                                                 'SPOT_FIFTEEN_CORNER_LEFT',
                                                 'SPOT_FIFTEEN_BREAK_LEFT',
                                                 'SPOT_FIFTEEN_TOP_KEY',
                                                 'SPOT_FIFTEEN_BREAK_RIGHT',
                                                 'SPOT_FIFTEEN_CORNER_RIGHT',
                                                 'SPOT_COLLEGE_CORNER_LEFT',
                                                 'SPOT_COLLEGE_BREAK_LEFT',
                                                 'SPOT_COLLEGE_TOP_KEY',
                                                 'SPOT_COLLEGE_BREAK_RIGHT',
                                                 'SPOT_COLLEGE_CORNER_RIGHT',
                                                 'SPOT_NBA_CORNER_LEFT',
                                                 'SPOT_NBA_BREAK_LEFT',
                                                 'SPOT_NBA_TOP_KEY',
                                                 'SPOT_NBA_BREAK_RIGHT',
                                                 'SPOT_NBA_CORNER_RIGHT',
                                                 'OFF_DRIB_FIFTEEN_BREAK_LEFT',
                                                 'OFF_DRIB_FIFTEEN_TOP_KEY',
                                                 'OFF_DRIB_FIFTEEN_BREAK_RIGHT',
                                                 'OFF_DRIB_COLLEGE_BREAK_LEFT',
                                                 'OFF_DRIB_COLLEGE_TOP_KEY',
                                                 'OFF_DRIB_COLLEGE_BREAK_RIGHT',
                                                 'ON_MOVE_FIFTEEN',
                                                 'ON_MOVE_COLLEGE']

def test_draft_history():
    """ tests the drafthistory endpoint of the Draft class
    """

    example_draft = Draft(headers=HEADERS, endpoint='drafthistory')

    table_names = example_draft.data.keys()

    assert 'DraftHistory' in table_names

    example_history = example_draft.data['DraftHistory'][0]

    assert list(example_history.keys()) == ['PERSON_ID',
                                            'PLAYER_NAME',
                                            'SEASON',
                                            'ROUND_NUMBER',
                                            'ROUND_PICK',
                                            'OVERALL_PICK',
                                            'TEAM_ID',
                                            'TEAM_CITY',
                                            'TEAM_NAME',
                                            'TEAM_ABBREVIATION',
                                            'ORGANIZATION',
                                            'ORGANIZATION_TYPE']

