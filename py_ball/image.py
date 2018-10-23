#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:22:00 2018

@author: patrickmcfarlane

image.py contains the Headshot and Logo classes that
enables API calls for two score board endpoints
"""

from PIL import Image
import requests
from io import BytesIO

BASE_NBA_URL = 'https://ak-static.cms.nba.com/wp-content/uploads/' + \
                'headshots/nba/{team}/{season}/260x190/{player_id}.png'
BASE_WNBA_URL = 'https://ak-static.cms.nba.com/wp-content/uploads/' + \
                'headshots/wnba/{player_id}.png'

class Headshot:
    """ The Headshot class contains all resources needed to pull
    headshot images for NBA and WNBA players.

    The Headshot class has the following required parameters:

        @param **league** (*str*): String, either 'WNBA' or 'NBA',
            to the league in which the desired player plays.

        @param **player_id** (*str*): String of an \
            integer corresponding to a player ID for a given player.

        @param **team_id** (*str*): String of a 10-digit \
            integer that uniquely identifies a team for which data \
            is to be returned.

        @param **season** (*str*): String of a year in YYYY format \
            corresponding to the year in which the NBA season begins.

    Attributes:

        **image** (*PngImageFile*): Image file of the desired headshot.
            Note that this image file is not saved locally, but stored
            in the Headshot class object.

    """

    def __init__(self, league='WNBA',
                 player_id='203400', team_id='',
                 season=''):
        
        # Controlling the parameters depending on the endpoint
        if league=='WNBA':
            response = requests.get(BASE_WNBA_URL.format(player_id=player_id))
        elif league=='NBA':
            response = requests.get(BASE_NBA_URL.format(player_id=player_id,
                                                        team=team_id,
                                                        season=season))
        im = Image.open(BytesIO(response.content))
        self.image = im
