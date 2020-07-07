#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:06:31 2018

@author: patrickmcfarlane

utils.py

Utilities for the py_ball package
"""

from requests import get
import pkgutil
import pickle

BASE_URL = 'http://stats.nba.com/stats/{endpoint}/'
BASE_WNBA_URL = 'http://data.wnba.com/data/5s/v2015/json/mobile_teams/' + \
    'wnba/{season}/scores/pbp/{game_id}_{quarter}_pbp.json'

def api_call(endpoint, params, headers):
    """ This function completes the API call at the given
    end point with the provided parameters.

    Args:
        - @param **endpoint** (*str*): string corresponding to a \
            `stats.nba.com <https://stats.nba.com>`_ API endpoint

    Returns:
        - JSON object of the API response
    """

    api_response = get(BASE_URL.format(endpoint=endpoint), params=params,
                       headers=headers)

    api_response.raise_for_status()
    json_resp = api_response.json()

    api_response.close()
    return json_resp


def wnba_shot_call(params, headers):
    """ This function completes the API call for WNBA
    shot data with the provided parameters.

    Args:
        - @param **params** (*str*): Dictionary containing required
            parameters for the WNBA shot data URL

    Returns:
        - **pbp_list** (*list*): list of play-by-play data
    """

    pbp_list = []
    for i in range(1, 10):
        try:
            api_response = get(BASE_WNBA_URL.format(season=params['season'],
                                                    game_id=params['game_id'],
                                                    quarter=i,
                                                    headers=headers))
        
            api_response.raise_for_status()
            json_resp = api_response.json()
            pbp_list += json_resp['g']['pla']
        except:
            break

    api_response.close()
    return pbp_list


def parse_api_call(api_resp):
    """ This function parses the API call returned from **api_call**
    and stores the response in a dictionary.

    Args:
        - @param **api_resp** (*dict*): JSON object of an API response. \
        This dictionary is keyed by 'resource', 'parameters', and \
        'resultSets'/'resultSet'. 'resource' contains the endpoint of the \
        API call. 'parameters' contains the parameters passed to the API call. \
        'resultSets'/'resultSet' contains the data returned from the \
        API call.

    Returns:
        - Dictionary keyed by all table names returned from the API call \
        containing all data in 'resultSets'/'resultSet'.
    """

    data = {}
    if 'resultSets' in api_resp:
        dictionary_key = 'resultSets'
    elif 'resultSet' in api_resp:
        dictionary_key = 'resultSet'

    if isinstance(api_resp[dictionary_key], list):
        for result_set in api_resp[dictionary_key]:
            headers = result_set['headers']
            if len(headers) > 0:
                if isinstance(headers[0], dict):
                    add_on = headers[0]['columnNames']
                    keep_header = headers[1]['columnNames']
                    col_ind = 0
                    col_count = 0
                    add_count = 0
                    for col_name in keep_header:
                        col_count += 1
                        if col_count <= 5:
                            continue
                        else:
                            keep_header[col_count] += '_' + add_on[col_ind]
                            add_count += 1
                            if add_count == 2:
                                add_count = 0
                                col_ind = 1
                    headers = keep_header
            values = result_set['rowSet']
            name = result_set['name']
            data[name] = [dict(zip(headers, value)) 
                          for value in values]
    else:
        result_set = api_resp[dictionary_key]
        headers = result_set['headers']
        if isinstance(headers[0], dict):
            add_on = headers[0]['columnNames']
            keep_header = headers[1]['columnNames']
            col_ind = 0
            col_count = -1
            add_count = 0
            for col_name in keep_header:
                col_count += 1
                if col_count <= 4:
                    continue
                else:
                    keep_header[col_count] += '_' + add_on[col_ind].replace(' ', '_')
                    add_count += 1
                    if add_count == 3:
                        add_count = 0
                        col_ind += 1
            headers = keep_header
                    
        values = result_set['rowSet']
        name = result_set['name']
        data[name] = [dict(zip(headers, value)) 
                      for value in values]

    return data


def get_seconds_left(period, time_string):
    """ get_seconds_left calculates the seconds
    remaining in the game

    @param period (int): Integer indicating which quarter
        the game is in
    @param time_string (str): String of the format
        MM:SS for the time remaining in the quarter

    Returns:

        - seconds_remaining (int): Number of seconds
        remaining in the game
    """

    time_in_quarter = 12 #normal quarter is 12 minutes long
    if period > 4:
        time_in_quarter=5 #if it's overtime, 5 mins long
    mins, seconds = time_string.split(':') #from a string like "11:20", we have 11 mins, 20 seconds
    extra_after_quarter = (4-period)*time_in_quarter*60 
    if period > 4:
        #if overtime, we go into negatives, so 10 seconds into overtime is -10 and so on
        extra_after_quarter = (5-period)*time_in_quarter*60 
        time_elapsed = (time_in_quarter*60) - ((int(mins)*60)+(int(seconds))) # convert to seconds
        seconds_remaining = extra_after_quarter-time_elapsed
    else:
        seconds_remaining = extra_after_quarter+(int(mins)*60)+(int(seconds)) #convert to seconds

    return seconds_remaining


def open_model(fname="models/model.pickle"):
    """ This function opens the win probability model

    @param fname (str): Name of the file containing
        the win probability model

    Returns:

        - time_to_model (sklearn.linear_model.Logistic_Regression):
            Win probability model
    """
    pickle_data = pkgutil.get_data(__name__, fname)
    time_to_model = pickle.loads(pickle_data)
    return time_to_model
