#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:59:39 2018

@author: patrickmcfarlane

league.py contains the League class that
enables API calls for general league related endpoints
"""

from .utils import api_call, parse_api_call, get_season_year

class League:
    """ The League class contains all resources needed to use the league-
    related API calls. `stats.nba.com <https://stats.nba.com>`_
    has the following league-related API endpoints:

        - **commonallplayers**: Current roster information if the \
        **current_season** flag is '1', historical player information \
        if the **current_season** flag is '0'.
        - **commonteamyears**: Start and end dates for teams in league \
        history.
        - **commonplayoffseries**: Playoff series matchup breakdown by game.
        - **franchisehistory**: Current and defunct franchise histories, \
        including performance and franchise metadata.
        - **playoffpicture**: Current state of the playoff picture by \
        conference.
        - **playerindex**: Historical player metadata for all players \
        in league history
        - **alltimeleadersgrids**: All time leaders across various \
        metrics
        - **leaguegamelog**: Game logs for players or teams across the \
        league

    The League class has the following required parameters:

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

        @param **season** (*str*): Season in the API. String of a two-year
            season in a YYYY-ZZ format, where the ZZ are the last two \
            digits of the following year. For example, '2017-18' is a valid \
            value of **season** and represents the 2017-18 NBA season. \
            **season** is required by the 'commonallplayers' and \
            'commonplayoffseries' endpoints.

        @param **season_id** (*str*): SeasonID in the API. String of a year \
            season in a XYYYY format. X indicates the season type \
            ('1' for preseason, '2' for regular season, '4' for the playoffs). \
            For example, '22017' is a valid \
            value of **season_id** and represents the 2017-18 NBA regular
            season. **season_id** is required by the 'playoffpicture' \
            endpoint.

        @param **current_season** (*str*): IsOnlyCurrentSeason in the API. \
            Boolean value ('1' or '0') indicating whether only the current \
            season should be returned ('1'). A value of '0' returns all \
            players in league history. **current_season** is required by the \
            'commonallplayers' endpoint.

        @param **college** (*str*): College in the API. String of the college \
            desired. "Kansas" is an example

        @param **country** (*str*): Country in the API. String of the country \
            desired. "Cameroon" is an example

        @param **draft_pick** (*str*): DraftPick in the API. String of the overall \
            draft pick number

        @param **draft_round** (*str*): DraftRound in the API. String of the \
            draft round number

        @param **draft_year** (*str*): DraftYear in the API. String of the \
            draft year in YYYY format

        @param **height** (*str*): Height in the API. Height in Feet-Inches \
            format

        @param **weight** (*str*): Weight in the API. Weight in pounds

        @param **historical** (*str*): Historical in the API. Unclear what \
            this corresponds to, but it takes boolean values. Hardcoded to 1 \
            as a default

        @param **season_type** (*str*): SeasonType in the API. String \
            indicating the type of season for data to be returned. \
            Valid values include:

                - 'Regular Season', 'Pre Season', 'Playoffs', 'All Star'

        @param **team_id** (*str*): TeamID in the API. String of a 10-digit \
            integer that uniquely identifies a team for which data is to \
            be returned.

        @param **per_mode** (*str*): PerMode in the API. String indicating \
            the type of rate stats to be returned. Valid values include:

                - 'Totals', 'PerGame', 'MinutesPer', 'Per48', 'Per40', \
                'Per36', 'PerMinute', 'PerPossession', 'PerPlay', \
                'Per100Possessions', 'Per100Plays'

        @param **top_x** (*str*): TopX in the API. String of the number \
            of top players to return

        @param **counter** (*str*): Counter in the API. String of the \
            number of records to return. Defaults to 1000

        @param **date_from** (*str*): DateFrom in the API. String of a date \
            in a MM/DD/YYYY format indicating the start date for which \
            data is to be returned.

        @param **date_to** (*str*): DateTo in the API. String of a date \
            in a MM/DD/YYYY format indicating the end date for which \
            data is to be returned.

        @param **direction** (*str*): Direction in the API. String of \
            ASC or DESC corresponding to how the returned data should be sorted

        @param **player_or_team** (*str*): PlayerOrTeam in the API. String \
            indicating whether data returned is for 'P' or 'T' \
            leaders.

        @param **sorter** (*str*): Sorter in the API. String of the field \
            to sort the returned data

    Attributes:

        **api_resp** (*dict*): JSON object of the API response. The API \
            response has three keys. The 'resource' key describes the type of \
            response returned (the endpoint in this instance). The 'parameters' \
            key describes the parameters provided in the API call. The \
            'resultSets' key contains the data returned in the API call.

        **data** (*dict*): A dictionary of response names. Each response \
            name is a key to a list of dictionaries containing the \
            corresponding data.
    """

    def __init__(self, headers, endpoint='commonallplayers',
                 league_id='00', season=get_season_year("00"),
                 season_id='22017', current_season='1',
                 college='', country='', draft_pick='',
                 draft_round='', draft_year='', height='',
                 weight='', historical='1',
                 season_type='Regular Season', team_id='0',
                 per_mode='Totals', top_x='10', counter='1000',
                 date_from='', date_to='', direction='DESC',
                 player_or_team='P', sorter='DATE'):

        # Controlling the parameters depending on the endpoint
        if endpoint in ['commonteamyears', 'franchisehistory']:
            params = {'LeagueID': league_id}
        elif endpoint in ['commonplayoffseries']:
            params = {'LeagueID': league_id,
                      'Season': season}
        elif endpoint in ['playoffpicture']:
            params = {'LeagueID': league_id,
                      'SeasonID': season_id}
        elif endpoint == "playerindex":
            params = {'LeagueID': league_id,
                      'Season': season,
                      'College': college,
                      'Country': country,
                      'DraftPick': draft_pick,
                      'DraftRound': draft_round,
                      'DraftYear': draft_year,
                      'Height': height,
                      'Weight': weight,
                      'Historical': historical,
                      'SeasonType': season_type,
                      'TeamID': team_id}
        elif endpoint == 'alltimeleadersgrids':
            params = {'LeagueID': league_id,
                      'SeasonType': season_type,
                      'PerMode': per_mode,
                      'TopX': top_x}
        elif endpoint == "leaguegamelog":
            params = {'LeagueID': league_id,
                      'Season': season,
                      'SeasonType': season_type,
                      'Counter': counter,
                      'DateFrom': date_from,
                      'DateTo': date_to,
                      'Direction': direction,
                      'PlayerOrTeam': player_or_team,
                      'Sorter': sorter}
        else:
            params = {'LeagueID': league_id,
                      'Season': season,
                      'IsOnlyCurrentSeason': current_season}

        self.api_resp = api_call(endpoint=endpoint,
                                 params=params,
                                 headers=headers)

        # Storing the API response in a dictionary called data
        # The results can come in different formats, namely a
        # dictionary keyed by either resultSets or resultSet
        self.data = parse_api_call(self.api_resp)


