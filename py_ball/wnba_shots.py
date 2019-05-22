#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:00:44 2019

@author: patrickmcfarlane

wnba_shots.py contains the Shots class that
enables XML downloads for WNBA shot-related
data
"""

from .utils import wnba_shot_call, parse_wnba_shot_call

class Shots:
    """ The Shots class contains all resources needed
    to use the shot-related WNBA data. `data.wnba.com <https://data.wnba.com>`_
    has the following shot XML files:

        - **shotchart_all.xml**: Shot-related data, including location, player \
        and associated metadata.

    The Shots class has the following required parameters:

        @param **headers** (*dict*): Dictionary of request header information
            required by the API. Specifically, the API requires you to declare
            the 'User-Agent' key of the request header dictionary. More information
            can be found `here <https://stackoverflow.com/questions/46781563/
            how-to-obtain-a-json-response-from-the-stats-nba-com-api>`_ and
            an example request header dictionary can be found in the __init__.py
            file in the tests folder of this module.

        @param **date** (*str*): String of a date \
            in a YYYMMDD format indicating the date on which a game has been \
            played.

        @param **teams** (*str*): String of a three-letter team abbreaviations \
            in a AAAHHH format indicating the away (AAA) and home (HHH) teams \
            in a game.

    Attributes:

        **api_resp** (*dict*): JSON object of the API response. The API \
            response has three keys. The 'resource' key describes the \
            type of response returned (the endpoint in this instance). \
            The 'parameters' key describes the parameters provided in the \
            API call. The 'resultSets' key contains the data returned in \
            the API call.

        **data** (*dict*): A dictionary of response names. Each response \
            name is a key to a list of dictionaries containing the \
            corresponding data.
    """
    def __init__(self, date='20150616', teams='MINLAS'):

        params = {'date': date, 'teams': teams}
        self.api_resp = wnba_shot_call(params=params)

        # Storing the API response in a dictionary called data
        self.data = parse_wnba_shot_call(self.api_resp)
