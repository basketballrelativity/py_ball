#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:02:05 2019

@author: patrickmcfarlane
"""

from requests import get

SALARY_URL = "https://hoopshype.com/salaries/"

URL_TO_ID_NBA = {'https://hoopshype.com/salaries/toronto_raptors/': '1610612761',
                 'https://hoopshype.com/salaries/denver_nuggets/': '1610612743',
                 'https://hoopshype.com/salaries/detroit_pistons/': '1610612765',
                 'https://hoopshype.com/salaries/new_orleans_pelicans/': '1610612740',
                 'https://hoopshype.com/salaries/milwaukee_bucks/': '1610612749',
                 'https://hoopshype.com/salaries/golden_state_warriors/': '1610612744',
                 'https://hoopshype.com/salaries/san_antonio_spurs/': '1610612759',
                 'https://hoopshype.com/salaries/portland_trail_blazers/': '1610612757',
                 'https://hoopshype.com/salaries/los_angeles_clippers/': '1610612746',
                 'https://hoopshype.com/salaries/dallas_mavericks/': '1610612742',
                 'https://hoopshype.com/salaries/memphis_grizzlies/': '1610612763',
                 'https://hoopshype.com/salaries/philadelphia_76ers/': '1610612755',
                 'https://hoopshype.com/salaries/boston_celtics/': '1610612738',
                 'https://hoopshype.com/salaries/minnesota_timberwolves/': '1610612750',
                 'https://hoopshype.com/salaries/charlotte_hornets/': '1610612766',
                 'https://hoopshype.com/salaries/indiana_pacers/': '1610612754',
                 'https://hoopshype.com/salaries/orlando_magic/': '1610612753',
                 'https://hoopshype.com/salaries/miami_heat/': '1610612748',
                 'https://hoopshype.com/salaries/houston_rockets/': '1610612745',
                 'https://hoopshype.com/salaries/sacramento_kings/': '1610612758',
                 'https://hoopshype.com/salaries/utah_jazz/': '1610612762',
                 'https://hoopshype.com/salaries/brooklyn_nets/': '1610612751',
                 'https://hoopshype.com/salaries/atlanta_hawks/': '1610612737',
                 'https://hoopshype.com/salaries/phoenix_suns/': '1610612756',
                 'https://hoopshype.com/salaries/washington_wizards/': '1610612764',
                 'https://hoopshype.com/salaries/new_york_knicks/': '1610612752',
                 'https://hoopshype.com/salaries/oklahoma_city_thunder/': '1610612760',
                 'https://hoopshype.com/salaries/los_angeles_lakers/': '1610612747',
                 'https://hoopshype.com/salaries/cleveland_cavaliers/': '1610612739',
                 'https://hoopshype.com/salaries/chicago_bulls/': '1610612741'}


def salary_columns(html_text):
    """ salary_columns returns the column names
    for the team salary information

    @param **html_text** (*str*): String of the HTML response
    from SALARY_URL

    Returns:

        **html_text** (*str*): Truncated string of the HTML
            response from a Hoopshype URL with the column information
            removed

        **column_list** (*list*): List of column names for
            salary information
    """
    column_list = []
    for col_count in range(0, 6):
        start_ind = html_text.find('>') + 1
        end_ind = html_text.find('</td>')
        column_list.append(html_text[start_ind:end_ind])
        html_text = html_text[end_ind + 5:]

    return html_text, column_list


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
    value_str = 'data-value="'
    team_salaries = {}
    nba_teams = 30

    for teams in range(0, nba_teams):
        team_list = []
        start_ind = html_text.find('<a')
        end_ind = html_text.find('</a>')
        team_key = html_text[start_ind + 2: end_ind]
        team_key = team_key[team_key.find('href="') + 6:team_key.find('">\n')]
        html_text = html_text[end_ind + 4:]
        for col_count in range(0, 6):
            start_ind = html_text.find(value_str) + len(value_str)
            end_ind = html_text.find('">')
            team_list.append(int(html_text[start_ind:end_ind]))
            html_text = html_text[end_ind + 2:]
        team_list.append(team_key)
        team_salaries[URL_TO_ID_NBA[team_key]] = team_list

    return team_salaries


def get_team_salary():
    """ This function pulls team salary information for six seasons
    from `hoopshype.com <https://hoopshype.com/salaries/>`

    Returns:

        **team_salaries** (*dict*): Dictionary keyed by NBA
            team ID with a list of yearly salaries (followed
            by team salary URL) as values

        **column_list** (*list*): List of column names for team
            salary information
    """

    api_resp = get(SALARY_URL)
    html_text = api_resp.text
    sorted_str = 'hh-salaries-sorted'

    table_index = html_text.find(sorted_str)
    html_text = html_text[table_index:]
    html_text, column_list = salary_columns(html_text)
    column_list.append('url')

    team_salaries = team_salary_values(html_text)

    return team_salaries, column_list


def get_option(option):
    """ get_option returns the type of option (if any) applied
    to that year's salary
    """

    if option == 'color:black':
        option = ''
    elif option == 'color:rgb(255, 0, 0)':
        option = 'Team'
    elif option == 'color:rgb(0, 153, 0)':
        option = 'Qualifying'
    elif option == 'color:rgb(168, 0, 212)':
        option = 'Two-Way'
    elif option == 'color:rgb(4, 134, 176)':
        option = 'Player'
    else:
        option = ''

    return option
    

def player_salary_values(html_text):
    """ player_salary_values returns a dictionary of
    salary information keyed by Hoopshype player ID

    @param **html_text** (*str*): String of the HTML response
    from a Hoopshype team URL

    Returns:

        **player_salaries** (*dict*): Dictionary keyed by Hoopshype
            player ID with a list of yearly salaries (followed
            by player salary URL) as values
    """
    value_str = 'data-value="'
    option_str = 'style="'
    player_salaries = {}
    url_val = html_text.find('<a')
    total_val = html_text.find('class="name">Totals</td>')

    while url_val < total_val:
        player_list = []
        option_list = []
        start_ind = html_text.find('<a')
        end_ind = html_text.find('</a>')
        play_key = html_text[start_ind + 2: end_ind]
        play_key = play_key[play_key.find('href="') + 6:play_key.find('">\n')]
        player_key = play_key.split('/')[-3]
        html_text = html_text[end_ind + 4:]
        for col_count in range(0, 6):
            start_ind = html_text.find(option_str) + len(option_str)
            end_ind = html_text.find('" ')
            option = get_option(html_text[start_ind:end_ind])
            option_list.append(option)
            html_text = html_text[end_ind + 2:]

            start_ind = html_text.find(value_str) + len(value_str)
            end_ind = html_text.find('">')
            try:
                salary_value = int(html_text[start_ind:end_ind])
            except:
                salary_value = 0
            player_list.append(salary_value)
            html_text = html_text[end_ind + 2:]

        player_list.append(play_key)
        player_salaries[player_key] = {}
        player_salaries[player_key]['salary'] = player_list
        player_salaries[player_key]['options'] = option_list

        total_val = html_text.find('class="name">Totals</td>')
        url_val = html_text.find('<a')

    return player_salaries


def get_player_salary(team_url):
    """ This function pulls player salary information for six seasons
    from `hoopshype.com <https://hoopshype.com/salaries/>`

    Returns:

        **player_salaries** (*dict*): Dictionary keyed by Hoopshype
            player ID with a list of yearly salaries as values

        **column_list** (*list*): List of column names for team
            salary information
    """

    api_resp = get(team_url)
    html_text = api_resp.text
    sorted_str = 'hh-salaries-sorted'

    table_index = html_text.find(sorted_str)
    html_text = html_text[table_index:]
    html_text, column_list = salary_columns(html_text)
    column_list.append('url')

    player_salaries = player_salary_values(html_text)

    return player_salaries, column_list
      

class TeamSalaries:
    """ The TeamSalaries class contains all resources needed
    to scrape team salary information from
    `hoopshype.com <https://hoopshype.com/salaries/>`.
    This class contains both team total salary as well as individual
    player breakdowns.

    Attributes:

        **totals** (*dict*): Dictionary keyed by NBA
            team ID with a list of yearly salaries (followed
            by team salary URL) as values

        **totals_columns** (*list*): List of column names for team
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