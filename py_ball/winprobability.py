import numpy as np
import json
from sklearn import linear_model
from .utils import get_seconds_left, open_model
from . import playbyplay, boxscore, team
import matplotlib.pyplot as plt

class WinProbability:
    def __init__(self, game_id, headers):
        self.game_id = game_id
        self.model = open_model()
        self.test_data = self.get_test(game_id, headers)
    def get_test(self, game_id, headers):
        test_x = []
        test_y = []
        times = []
        diff = []
        pbp = playbyplay.PlayByPlay(headers=headers, game_id=game_id).data
        bxscore = boxscore.BoxScore(headers=headers, game_id=game_id, endpoint='boxscoresummaryv2').data
        team_abr = []
        game_summary = (bxscore['GameSummary'])[0]
        home_team_id = game_summary['HOME_TEAM_ID']
        visitor_team_id = game_summary['VISITOR_TEAM_ID']

        home_team_data = team.Team(headers=headers, endpoint='teaminfocommon', team_id=home_team_id).data
        visitor_team_data = team.Team(headers=headers, endpoint='teaminfocommon', team_id=visitor_team_id).data

        home = home_team_data['TeamInfoCommon'][0]['TEAM_ABBREVIATION']
        away = visitor_team_data['TeamInfoCommon'][0]['TEAM_ABBREVIATION']

        jump_event = pbp['PlayByPlay'][1]
        home_has_ball = (jump_event['HOMEDESCRIPTION'] != None)
        current_quarter = 1
        current_margin = 0
        home_wins = int(pbp['PlayByPlay'][-1]['SCOREMARGIN']) > 0
        last_second = 2880
        game_x = {}
        game_y = []
        added_this_game = []
        actual_times = []

        for event in pbp['PlayByPlay'][2:]:

            seconds_left_in_game = get_seconds_left(event['PERIOD'], event['PCTIMESTRING'])

            for sec in range(seconds_left_in_game+1, last_second):
                if sec % 10 == 0 and (sec not in added_this_game):
                    game_x[sec] = [current_margin, home_wins, home_has_ball]
                    game_y.append(int(home_wins))
                    added_this_game.append(sec)

            last_second = seconds_left_in_game

            home_desc = (event['HOMEDESCRIPTION'] != None)
            visitor_desc = (event['VISITORDESCRIPTION'] != None)

            if home_desc and not visitor_desc:
                home_has_ball = True

            if visitor_desc and not home_desc:
                home_has_ball = False

            if home_desc and visitor_desc:
                if ('STEAL' in event['HOMEDESCRIPTION']) or ('BLOCK' in event['HOMEDESCRIPTION']):
                    home_has_ball = True
                else:
                    home_has_ball = False

            if event['SCOREMARGIN'] != None:
                margin = 0
                if event['SCOREMARGIN'] != 'TIE':
                    margin = (int(event['SCOREMARGIN']))
                    current_margin = margin

            if seconds_left_in_game % 10 == 0 and seconds_left_in_game not in added_this_game:
                game_x[seconds_left_in_game] = [current_margin, home_wins, home_has_ball]
                game_y.append(int(home_wins))
                added_this_game.append(int(seconds_left_in_game))

            test_x = (game_x)
            times = (list(game_x.keys()))
            diff.append(current_margin)
            actual_times.append(seconds_left_in_game)

        return test_x, times, diff, actual_times, home, away

    def plot_probs_for_test(self,plot_wp=True):
        print(self.game_id)
        test_x, times, diff, actual_times, home, away = self.test_data
        times = np.insert(times, 0, 2880)
        probs = []
        for time in times[1:]:
            time_prob = self.model[time].predict_proba([[test_x[time][0], test_x[time][2]]])[0]
            probs.append(time_prob)
        
        probs = np.array(probs)
        
        probs_away = np.insert(probs[:,0], 0, 0.5)
        probs_home = np.insert(probs[:,1], 0, 0.5)
        
        end_lim = 2880-(len(probs_home)*10)
        
        if plot_wp:
            plt.rcParams["figure.figsize"] = (20,6)
            fig, ax = plt.subplots(1,2)
            ax[0].set_title("Point Differential")
            ax[0].plot(actual_times, diff)
            ax[0].set_xlim(2880, end_lim)
            ax[1].plot(times, probs_home, label=home)
            ax[1].plot(times, probs_away, label=away)
            ax[1].set_xlim(2880, end_lim)
            ax[1].set_ylim(0.0, 1.0)
            ax[1].set_title("Win Probability")
            plt.legend(loc='best')
            plt.show()
        
        return probs_home, probs_away, home, away
        
