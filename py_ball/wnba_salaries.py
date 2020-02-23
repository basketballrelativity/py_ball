#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  23 13:02:05 2020

@author: patrickmcfarlane

wnba_salaries.py contains the functions
to gather NBA salary information
"""

from requests import get

SALARY_URL = "https://www.spotrac.com/wnba/cap/"

URL_TO_ID_WNBA = {'https://www.spotrac.com/redirect/team/347/cap/': '1611661324',
                  'https://www.spotrac.com/redirect/team/345/cap/': '1611661319',
                  'https://www.spotrac.com/redirect/team/348/cap/': '1611661313',
                  'https://www.spotrac.com/redirect/team/341/cap/': '1611661329',
                  'https://www.spotrac.com/redirect/team/346/cap/': '1611661320',
                  'https://www.spotrac.com/redirect/team/344/cap/': '1611661325',
                  'https://www.spotrac.com/redirect/team/340/cap/': '1611661330',
                  'https://www.spotrac.com/redirect/team/342/cap/': '1611661323',
                  'https://www.spotrac.com/redirect/team/349/cap/': '1611661317',
                  'https://www.spotrac.com/redirect/team/351/cap/': '1611661322',
                  'https://www.spotrac.com/redirect/team/350/cap/': '1611661328',
                  'https://www.spotrac.com/redirect/team/343/cap/': '1611661321'}


def team_salary_values(html_text):
    """ team_salary_values returns a dictionary of
    salary information keyed by NBA team ID

    @param **html_text** (*str*): String of the HTML response
    from SALARY_URL

    Returns:

        **team_salaries** (*dict*): Dictionary keyed by NBA
            team ID with a list of yearly salaries (followed
            by team salary URL) as values
    """
    value_str = '<td '
    team_salaries = {}
    wnba_teams = 12

    for teams in range(0, wnba_teams):
        team_list = []
        start_ind = html_text.find('<a')
        end_ind = html_text.find('</a>')
        team_key = html_text[start_ind + 2: end_ind]
        team_key = team_key[team_key.find('href="') + 6:team_key.find('">')]
        for col_count in range(0, 8):
            end_ind = html_text.find('">')
            html_text = html_text[end_ind + 2: ]
            end_ind = html_text.find('</td>')
            val = html_text[:end_ind]
            if '</a>' in val:
            	val = val.replace('</a>', '')
            if "<span style='display:none'>" in val:
            	val = val.replace("<span style='display:none'>", '')
            	end_val = val.find('</span>')
            	val = val[ :end_val]
            team_list.append(val)
            html_text = html_text[end_ind + 5:]
        start_ind = html_text.find(value_str) + len(value_str)
        html_text = html_text[start_ind: ]

        team_list.append(team_key)
        team_salaries[URL_TO_ID_WNBA[team_key]] = team_list

    return team_salaries


def get_team_salary():
    """ This function pulls team salary information
    from `spotrac.com <https://www.spotrac.com/wnba/cap/>`

    Returns:

        **team_salaries** (*dict*): Dictionary keyed by WNBA
            team ID with a list of yearly salaries (followed
            by team salary URL) as values

        **column_list** (*list*): List of column names for team
            salary information
    """

    api_resp = get(SALARY_URL)
    html_text = api_resp.text
    sorted_str = 'The total cap $ for a team">Total Cap'
    table_index = html_text.find(sorted_str)
    html_text = html_text[table_index:]

    sorted_str = '<td class="center">'
    table_index = html_text.find(sorted_str)
    html_text = html_text[table_index:]

    column_list = ['Rank', 'Team', 'Signed', 'Average Age',
    			   'Active Cap', 'Dead Cap', 'Total Cap',
    			   'Cap Space', 'URL']

    team_salaries = team_salary_values(html_text)

    return team_salaries, column_list


class TeamSalaries:
    """ The TeamSalaries class contains all resources needed
    to scrape team salary information from
    `spotrac.com <https://www.spotrac.com/wnba/cap/>`.
    This class contains both team total salary as well as individual
    player breakdowns

    Attributes:

        **totals** (*dict*): Dictionary keyed by WNBA
            team ID with a list of yearly salaries (followed
            by team salary URL) as values

        **totals_columns** (*list*): List of column names for team
            salary information

        **team_player_salaries** (*dict*): Dictionary keyed by both WNBA
            team ID and Hoopshype player ID with values containing both
            salary and option information

        **team_player_columns** (*list*): List of column names for team-player
            salary information
    """

    def __init__(self):

        # First, total team salary information is pulled
        team_salaries, column_list = get_team_salary()
        self.totals = team_salaries
        self.totals_columns = column_list
        team_player_salary = {}
        for team_id in team_salaries:
            team_url = team_salaries[team_id][-1]
            player_salaries, column_list = get_player_salary(team_url)
            team_player_salary[team_id] = player_salaries

        self.team_player_salaries = team_player_salary
        self.team_player_columns = column_list