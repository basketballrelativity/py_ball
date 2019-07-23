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
from cairosvg import svg2png

BASE_NBA_URL = 'https://ak-static.cms.nba.com/wp-content/uploads/' + \
                'headshots/nba/{team}/{season}/260x190/{player_id}.png'
BASE_WNBA_URL = 'https://ak-static.cms.nba.com/wp-content/uploads/' + \
                'headshots/wnba/{player_id}.png'
BASE_G_LEAGUE_URL = 'https://ak-static.cms.nba.com/wp-content/uploads/' + \
                    'headshots/dleague/{player_id}.png'

BASE_NBA_LOGO_URL = 'https://stats.nba.com/media/img/teams/' + \
                    'logos/season/{year}/{team}_logo.svg'
                    
BASE_WNBA_LOGO_URL = 'https://ak-static.cms.nba.com/wp-content/' + \
                     'themes/wnba-child/img/logos/' + \
                     '{team}-primary-logo.svg'

BASE_G_LEAGUE_LOGO_URL = 'https://stats.gleague.nba.com/media/' + \
                         'img/teams/logos/{team}.svg'
                     
ID_TO_TEAM_NBA = {'1610612761': 'TOR', '1610612743': 'DEN',
                  '1610612765': 'DET', '1610612740': 'NOP',
                  '1610612749': 'MIL', '1610612744': 'GSW',
                  '1610612759': 'SAS', '1610612757': 'POR',
                  '1610612746': 'LAC', '1610612742': 'DAL',
                  '1610612763': 'MEM', '1610612755': 'PHI',
                  '1610612738': 'BOS', '1610612750': 'MIN',
                  '1610612766': 'CHA', '1610612754': 'IND',
                  '1610612753': 'ORL', '1610612748': 'MIA',
                  '1610612745': 'HOU', '1610612758': 'SAC',
                  '1610612762': 'UTA', '1610612751': 'BKN',
                  '1610612737': 'ATL', '1610612756': 'PHX',
                  '1610612764': 'WAS', '1610612752': 'NYK',
                  '1610612760': 'OKC', '1610612747': 'LAL',
                  '1610612739': 'CLE', '1610612741': 'CHI'}

ID_TO_TEAM_WNBA = {'1611661330': 'dream', '1611661321': 'wings',
                   '1611661320': 'sparks', '1611661317': 'mercury',
                   '1611661329': 'sky', '1611661325': 'fever',
                   '1611661324': 'lynx', '1611661328': 'storm',
                   '1611661323': 'sun', '1611661319': 'aces',
                   '1611661313': 'liberty', '1611661322': 'mystics'}

ID_TO_TEAM_G_LEAGUE = {'1612709908': 'RGV', '1612709902': 'SCW',
                       '1612709926': 'MHU', '1612709914': 'STO',
                       '1612709903': 'SLC', '1612709921': 'LIN',
                       '1612709889': 'OKL', '1612709925': 'LAK',
                       '1612709920': 'RAP', '1612709919': 'WES',
                       '1612709917': 'GRD', '1612709923': 'WCB',
                       '1612709913': 'ERI', '1612709904': 'SXF',
                       '1612709909': 'DEL', '1612709928': 'CAP',
                       '1612709911': 'IWA', '1612709924': 'ACC',
                       '1612709910': 'FWN', '1612709905': 'SBL',
                       '1612709918': 'TEX', '1612709927': 'WIS',
                       '1612709922': 'GBO', '1612709915': 'MNE',
                       '1612709890': 'AUS', '1612709893': 'CTN',
                       '1612709900': 'NAS'}

class Headshot:
    """ The Headshot class contains all resources needed to pull
    headshot images for NBA, G-League, and WNBA players.

    The Headshot class has the following required parameters:

        @param **league** (*str*): String, either 'WNBA', 'G', or 'NBA',
            to the league in which the desired player or team plays.

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
        if league == 'WNBA':
            response = requests.get(BASE_WNBA_URL.format(player_id=player_id))
        elif league == 'NBA':
            response = requests.get(BASE_NBA_URL.format(player_id=player_id,
                                                        team=team_id,
                                                        season=season))
        elif league == 'G':
            response = requests.get(BASE_G_LEAGUE_URL.format(player_id=player_id))

        im = Image.open(BytesIO(response.content))
        self.image = im


class Logo:
    """ The Logo class contains all resources needed to pull
    logo images for NBA, G-League, and WNBA players.

    The Logo class has the following required parameters:

        @param **league** (*str*): String, either 'WNBA', 'G', or 'NBA',
            to the league in which the desired player plays.

        @param **team_id** (*str*): String of a 10-digit \
            integer that uniquely identifies a team for which data \
            is to be returned.

        @param **season_year** (*str*): String of a two-year season \
            year in a YYYY-ZZ format, where the ZZ are the \
            last two digits of the following year. For example, \
            '2017-18' is a valid value of **season_year** and \
            represents the 2017-18 NBA season. **season_year** is \
            only required for NBA logos.

    Attributes:

        **image** (*PngImageFile*): Image file of the desired headshot.
            Note that this image file is not saved locally, but stored
            in the Headshot class object.

    """

    def __init__(self, league='WNBA',
                 team_id='1611661319',
                 season_year='2017-18'):

        # Controlling the parameters depending on the endpoint
        if league == 'WNBA':
            team_str = ID_TO_TEAM_WNBA[team_id]
            response = requests.get(BASE_WNBA_LOGO_URL.format(team=team_str))
        elif league == 'NBA':
            team_str = ID_TO_TEAM_NBA[team_id]
            response = requests.get(BASE_NBA_LOGO_URL.format(team=team_str,
                                                             year=season_year))
        elif league == 'G':
            team_str = ID_TO_TEAM_G_LEAGUE[team_id]
            response = requests.get(BASE_G_LEAGUE_LOGO_URL.format(team=team_str))

        new_bites = svg2png(bytestring=response.content,
                            write_to=None)
        im = Image.open(BytesIO(new_bites))
        self.image = im
