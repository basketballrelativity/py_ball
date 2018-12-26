#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 12:46:48 2018

@author: patrickmcfarlane

test_image.py

This function contains the tests for
functions in the image.py file
"""

import PIL
from ..image import Headshot, Logo

def test_headshot():
    """ tests the Headshot class
    """

    example_wnba_headshot = Headshot()
    example_nba_headshot = Headshot(league='NBA',
                                    player_id='2544',
                                    team_id='1610612747',
                                    season='2018')

    assert type(example_wnba_headshot.image) == PIL.PngImagePlugin.PngImageFile
    assert type(example_nba_headshot.image) == PIL.PngImagePlugin.PngImageFile

def test_logo():
    """ tests the Logo class
    """

    example_wnba_logo = Logo()
    example_nba_logo = Logo(league='NBA',
                            team_id='1610612755',
                            season_year='2018-19')

    assert type(example_wnba_logo.image) == PIL.PngImagePlugin.PngImageFile
    assert type(example_nba_logo.image) == PIL.PngImagePlugin.PngImageFile
