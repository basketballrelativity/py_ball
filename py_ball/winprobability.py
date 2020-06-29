#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:59:39 2020

@author: Avyay Varadarajan

winprobability.py contains the WinProbability class that
calculates win probability from play-by-play data for
NBA games
"""

import json
from .utils import get_seconds_left, open_model
from . import playbyplay, boxscore, team
import matplotlib.pyplot as plt


def discern_possession_and_margin(event, current_margin, home_has_ball):
    """ This function determines whether
    or not the home team has the ball

    @param event (pd.Series): pandas Series
        containing a row from a play-by-play
        DataFrame
    @param current_margin (int): Current score margin
            relative to the home team
    @param home_has_ball (bool): True if the home
            team has possession, False otherwise

    Returns:

        home_has_ball (bool): True if the home
            team has possession, False otherwise
        current_margin (int): Current score margin
            relative to the home team
    """

    # Determine possession
    home_desc = (event['HOMEDESCRIPTION'] != None)
    visitor_desc = (event['VISITORDESCRIPTION'] != None)

    if home_desc and not visitor_desc:
        home_has_ball = True
    elif visitor_desc and not home_desc:
        home_has_ball = False
    elif home_desc and visitor_desc:
        if ('STEAL' in event['HOMEDESCRIPTION']) \
            or ('BLOCK' in event['HOMEDESCRIPTION']):
            home_has_ball = True
        else:
            home_has_ball = False

    # Determine score margin
    if event['SCOREMARGIN'] != None:
        current_margin = 0
        if event['SCOREMARGIN'] != 'TIE':
            current_margin = (int(event['SCOREMARGIN']))

    return home_has_ball, current_margin


def get_team_abr(headers, game_id):
    """ This function pulls the name
    abbreviations for the home and away teams

    @param headers (dict): Dictionary of request
        header information required by the API
    @param game_id (str): 10-digit string that
        represents a unique game

    Returns:

        - team_abr (list): List of team abbreviations
            with the home team in the first index and
            the away team in the second index
    """

    bxscore = boxscore.BoxScore(headers=headers,
                                game_id=game_id,
                                endpoint='boxscoresummaryv2').data

    game_summary = (bxscore['GameSummary'])[0]
    home_team_id = game_summary['HOME_TEAM_ID']
    visitor_team_id = game_summary['VISITOR_TEAM_ID']

    home_team_data = team.Team(headers=headers,
                               endpoint='teaminfocommon',
                               team_id=home_team_id).data
    visitor_team_data = team.Team(headers=headers,
                                  endpoint='teaminfocommon',
                                  team_id=visitor_team_id).data

    home = home_team_data['TeamInfoCommon'][0]['TEAM_ABBREVIATION']
    away = visitor_team_data['TeamInfoCommon'][0]['TEAM_ABBREVIATION']

    team_abr = [home, away]

    return team_abr


def plot_win_prob(times, diff, end_lim, probs, team_abr, bools):
    """ This function plots the win probability and
    score differential for the game

    @param times (list): list containing actual_times
        and times. times contains all of the times at
        which win probability was calculated
    @param diff (list): List of score differentials
        corresponding to all times in actual_times
    @param end_lim (int): Time at which the last win
        probability value is calculated
    @param probs (list): List of win probability
        lists (probs_home and probs_away). probs_home
        contains all of the home win probability
        values for all times in the times list.
        probs_away is the same, but for win probability
        for the away team
    @param team_abr (list): List contraining the
        home team abbreviation in the first index
        and the away team abbreviation in the
        second index
    @param bools (list): List of booleans controlling
        which figures are plotted

    Returns:

        - fig (matplotlib.figure.Figure): Figure
            containing score differential and/or
            win probability. None if all of the
            booleans are False
    """

    actual_times, times = times
    probs_home, probs_away = probs
    plot_diff, plot_home, plot_away = bools

    plt.rcParams["figure.figsize"] = (20,6)

    # Score differential
    if plot_diff:
        fig, pltting = \
            plot_score_differential(actual_times,
                                    diff,
                                    end_lim)
    else:
        fig,ax = plt.subplots()
        pltting = ax 

    # Quarter deliniation
    for normal_q in range(0,4):
        pltting.plot([2880-normal_q*12*60, 2880-normal_q*12*60],
                     [0,1], 'gray')

    # OT deliniation
    for ot in range(0,10):
        pltting.plot([-ot*5*60, -ot*5*60],
                     [0,1], 'gray')

    # Win probability
    if plot_home:
        pltting.plot(times, probs_home, 'blue', label=team_abr[0])
    if plot_away:
        pltting.plot(times, probs_away, 'orange', label=team_abr[-1])
    
    pltting.set_xlim(2880, end_lim)
    pltting.set_ylim(0.0, 1.0)
    pltting.set_title("Win Probability")
    plt.legend(loc='best')
    plt.show()

    return fig


def plot_score_differential(actual_times, diff, end_lim):
    """ This function plots the score differential
    throughout the game

    @param actualtimes (list): list that contains
        all of the times at which a score
        differential was calculated
    @param diff (list): List of score differentials
        corresponding to all times in actual_times
    @param end_lim (int): Time at which the last win
        probability value is calculated

    Returns:

        - fig (matplotlib.figure.Figure): Figure
            containing the score differential
        - ax (matplotlib.axes): Axis object
    """

    fig, ax = plt.subplots(1,2)
    ax[0].set_title("Point Differential")
    ax[0].plot(actual_times, diff)
    ax[0].set_xlim(2880, end_lim)
    for normal_q in range(0,4):
        ax[0].plot([2880-normal_q*12*60, 2880-normal_q*12*60], [min(diff),max(diff)], 'gray')
    for ot in range(0,10):
        ax[0].plot([-ot*5*60, -ot*5*60], [min(diff),max(diff)], 'gray')
    ax[0].set_ylim(min(diff), max(diff))
    pltting = ax[1]

    return fig, pltting


def organize_probabilities(probs, times, diff):
    """ This function organizes the predicted
    win probability into a form more amenable
    to visualization

    @param probs (list): list of win probability
        values relative to the home team
    @param times (list): list of times at which
        the win probability values are calculated
    @param diff (list): list of score differentials
        relative to the home team

    Returns:

        - times (list): list of times at which
        the win probability values are calculated
        - probs_home (list): list of win probability
        values relative to the home team
        - probs_away (list): list of win probability
        values relative to the away team
    """

    probs_home = [0.5] + probs
    probs_away = [1 - x for x in probs_home]

    times, probs_home, probs_away = zip(*sorted(zip(times, probs_home, probs_away)))
    probs_home = list(probs_home)
    probs_away = list(probs_away)
    times = list(times)

    home_won = int(diff[-1]>0)
    probs_home[0] = float(home_won)
    probs_away[0] = float(1-home_won)

    return times, probs_home, probs_away


class WinProbability:
    """ The WinProbability class contains all resources needed
    to compute win probability for an NBA game

    The WinProbability class has the following required parameters:

    @param **headers** (*dict*): Dictionary of request header information
        required by the API. Specifically, the API requires you to declare
        the 'User-Agent' key of the request header dictionary. More information
        can be found `here <https://stackoverflow.com/questions/46781563/
        how-to-obtain-a-json-response-from-the-stats-nba-com-api>`_ and
        an example request header dictionary can be found in the __init__.py
        file in the tests folder of this module.

    @param **game_id** (*str*): GameID in the API. 10-digit string \
        that represents a unique game. The format is two leading zeroes, \
        followed by a season indicator number ('1' for preseason, \
        '2' for regular season, '4' for the post-season), \
        then the trailing digits of the season in which the game \
        took place (e.g. '17' for the 2017-18 season). The following \
        5 digits increment from '00001' in order as the season progresses. \
        For example, '0021600001' is the **game_id** of the first game \
        of the 2016-17 NBA regular season.
    """
    def __init__(self, game_id, headers):
        """ Initializing object
        """
        self.game_id = game_id
        self.model = open_model()
        self.test_data = self.get_test(game_id, headers)
        self.home_win_probability = []
        self.home_won = 0

    def get_test(self, game_id, headers):
        """ This function pulls play-by-play and
        boxscore data to organize them in a format
        needed by the win probability model

        Returns:

            - game_x (dict): Dictionary keyed by three-second
                intervals with values of lists containing
                the current score margin and possession
            - times (list): List of keys in the game_x
                dictionary
            - diff (list): List of score margins for each
                play
            - actual_times (list): List of game times for
                each play
            - team_abr (list): List of team abbreviations
                with the home team in the first index and
                the away team in the second index
        """

        diff = []
        pbp = playbyplay.PlayByPlay(headers=headers, game_id=game_id).data
        team_abr = get_team_abr(headers, game_id)

        # Initializing game parameters
        jump_event = pbp['PlayByPlay'][1]
        home_has_ball = (jump_event['HOMEDESCRIPTION'] != None)
        current_quarter = 1
        current_margin = 0
        home_wins = int(pbp['PlayByPlay'][-1]['SCOREMARGIN']) > 0
        last_second = 2880
        game_x = {}
        actual_times = []
        added_this_game = []

        for event in pbp['PlayByPlay'][2:]:

            # This section covers the period of time between the last play
            # and this play. If any time period in that range qualifies for
            # inclusion (i.e. 3 second intervals), it is added to game_x
            seconds_left_in_game = get_seconds_left(event['PERIOD'], event['PCTIMESTRING'])
            for sec in range(seconds_left_in_game+1, last_second):
                if sec % 3 == 0 and (sec not in added_this_game):
                    game_x[sec] = [current_margin,
                                   home_has_ball]
                    added_this_game.append(sec)

            # This section covers the current play
            last_second = seconds_left_in_game
            home_has_ball, current_margin = \
                discern_possession_and_margin(event,
                                              current_margin,
                                              home_has_ball)

            if seconds_left_in_game % 3 == 0 and seconds_left_in_game not in added_this_game:
                game_x[seconds_left_in_game] = [current_margin,
                                                home_has_ball]
                added_this_game.append(int(seconds_left_in_game))

            times = (list(game_x.keys()))
            diff.append(current_margin)
            actual_times.append(seconds_left_in_game)

        return game_x, times, diff, actual_times, team_abr


    def probs(self, plot_home=True, plot_away=False, plot_diff=False, get_values=False):
        """ This function calculates the win probability throughout
        a game and plots the resulting win probability chart

        @param plot_home (bool): If True, the win probability
            of the home team is plotted
        @param plot_away (bool): If True, the win probability
            of the away team is plotted
        @param plot_diff (bool): If True, the point differential
            is plotted
        @param get_values (bool): This controls whether or not
            the win probability and associated objects are returned

        Results:

        If get_values == True:

            - times (list): List of times for which win probability
                is calculated
            - probs_home (list): List of win probability of the home
                team
            - probs_away (list): List of win probability of the away
                team
            - team_abr (list): List of team abbreviations
                with the home team in the first index and
                the away team in the second index
        """
        test_x, times, diff, actual_times, team_abr = self.test_data
        times = [2880] + times
        probs = []
        for time in times[1:]:
            training_key = time
            if training_key < 0:
                for ot in range(0,10):
                    if (ot*5*60)+training_key > 0:
                        training_key = (ot*5*60)+training_key
                        break
            time_prob = self.model[training_key].predict_proba([test_x[time]])[0][1]
            probs.append(time_prob)
        
        times, probs_home, probs_away = \
            organize_probabilities(probs, times, diff)
        
        end_lim = 2880-(len(probs_home)*3)

        if plot_home or plot_away:
        
            fig = plot_win_prob([actual_times, times],
                                diff,
                                end_lim,
                                [probs_home, probs_away],
                                team_abr,
                                [plot_diff, plot_home, plot_away])
        else:
            fig = None

        self.home_win_probability = probs_home
        self.home_won = int(diff[-1]>0)
        times.reverse()
        probs_home.reverse()
        probs_away.reverse()
        if get_values:
            return times, probs_home, probs_away, team_abr

        return fig

    def brier_score(self):
        """ This function calculates the Brier score
        for the game

        Returns:

            - brier_score (float): Brier score for
                the game
        """
        if len(self.home_win_probability) == 0:
            self.probs(plot_home=False)

        size_of_arr = len(self.home_win_probability)
        cum_brier_score = 0
        for ind_prob in self.home_win_probability:
            cum_brier_score += (self.home_won-ind_prob)**2

        brier_score = cum_brier_score/size_of_arr 
        return brier_score     
