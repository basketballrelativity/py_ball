#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:00:44 2019

@author: patrickmcfarlane

wnba_shots.py contains the Shots class that
enables API calls for WNBA shot-related
data
"""

from .utils import wnba_shot_call

class Shots:
    """ The Shots class contains all resources needed
    to use the shot-related WNBA data. `data.wnba.com <https://data.wnba.com>`_
    has the following endpoints:

        - **pbp**: Shot-related data, including location, player \
        and associated metadata.

    The Shots class has the following required parameters:

        @param **headers** (*dict*): Dictionary of request header information
            required by the API. Specifically, the API requires you to declare
            the 'User-Agent' key of the request header dictionary. More information
            can be found `here <https://stackoverflow.com/questions/46781563/
            how-to-obtain-a-json-response-from-the-stats-nba-com-api>`_ and
            an example request header dictionary can be found in the __init__.py
            file in the tests folder of this module.

        @param **season** (*str*): Season in the API. String of a one-year \
            season in a YYYY format. For example, '2017' is a valid \
            value of **season** and represents the 2017 WNBA season.

        @param **game_id** (*str*): GameID in the API. 10-digit string \
            that represents a unique game. The format is two leading digits \
            ('10'), followed by a season indicator number ('1' for preseason, \
            '2' for regular season, '4' for the post-season), \
            then the trailing digits of the season in which the game \
            took place (e.g. '17' for the 2017 season). The following \
            5 digits increment from '00001' in order as the season progresses. \
            For example, '1021600001' is the **game_id** of the first game \
            of the 2016 WNBA regular season.

    Attributes:

        **data** (*dict*): A list of dictionaries containing a play. Each list
        contains play-by-play data for one game.
    """
    def __init__(self, headers, season='2018', game_id='1021800050'):

        params = {'season': season, 'game_id': game_id}
        self.data = wnba_shot_call(params=params, headers=headers)
