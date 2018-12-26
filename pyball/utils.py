#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:06:31 2018

@author: patrickmcfarlane

utils.py

Utilities for the py_ball package
"""

from requests import get

BASE_URL = 'http://stats.nba.com/stats/{endpoint}/'

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

    