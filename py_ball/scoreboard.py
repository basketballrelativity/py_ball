#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 20:45:03 2018

@author: patrickmcfarlane

scoreboard.py contains the ScoreBoard class that
enables API calls for two score board endpoints
"""

from .utils import api_call, parse_api_call
from datetime import datetime

class ScoreBoard:
    """ The ScoreBoard class contains all resources needed to use the
    score board API calls. `stats.nba.com <https://stats.nba.com>`_
    has the following score board API endpoints:

        - **scoreboard**: Live scores across the league, with series metadata \
        and standings information.
        - **scoreboardv2**: Live scores across the league, with series metadata \
        and standings information. Also, scoreboardv2 has ticket, win \
        probability, and team leader information.

    The ScoreBoard class has the following required parameters:

        @param **headers** (*dict*): Dictionary of request header information
            required by the API. Specifically, the API requires you to declare
            the 'User-Agent' key of the request header dictionary. More information
            can be found `here <https://stackoverflow.com/questions/46781563/
            how-to-obtain-a-json-response-from-the-stats-nba-com-api>`_ and
            an example request header dictionary can be found in the __init__.py
            file in the tests folder of this module.

        @param **league_id** (*str*): LeagueID in the API. String of a \
            two-digit number corresponding to the league. '00' is the NBA, \
            '10' is the WNBA, '01' is the ABA, and '20' is the G-League.

        @param **game_date** (*str*): GameDate in the API. String of a \
            date formatted as 'MM/DD/YYYY' representing the date for \
            which data is desired.

        @param **day_offset** (*str*): DayOffset in the API. String of an \
            integer representing days from or before the date given in \
            **game_date** for which data is desired. Positive values \
            indicate days into the future, zero represents the current \
            day, and negative values indicate days into the past.

    Attributes:

        **api_resp** (*dict*): JSON object of the API response. The API \
            response has three keys. The 'resource' key describes the \
            type of response returned (the endpoint in this instance). \
            The 'parameters' key describes the parameters provided in \
            the API call. The 'resultSets' key contains the data returned \
            in the API call.

        **data** (*dict*): A dictionary of response names. Each response \
            name is a key to a list of dictionaries containing the \
            corresponding data.
    """

    cur_day = datetime.today().day
    cur_month = datetime.today().month
    cur_year = str(datetime.today().year)
    if cur_day < 10:
        cur_day = '0' + str(cur_day)
    else:
        cur_day = str(cur_day)

    if cur_month < 10:
        cur_month = '0' + str(cur_month)
    else:
        cur_month = str(cur_month)

    current_date = cur_month + '/' + \
                   cur_day + '/' + \
                   cur_year

    def __init__(self, headers, endpoint='scoreboard',
                 league_id='00', game_date=current_date,
                 day_offset='0'):
        
        # Controlling the parameters depending on the endpoint
        params = {'LeagueID': league_id,
                  'GameDate': game_date,
                  'DayOffset': day_offset}

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params,
                                 headers=headers)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)
