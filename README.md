[![Downloads](https://pepy.tech/badge/py-ball)](https://pepy.tech/project/py-ball)

# py_ball
Python API wrapper for stats.nba.com with a focus on NBA and WNBA applications

## Introduction

The motivation for this stems from [nba_py](https://github.com/seemethere/nba_py) by [seemethere](https://github.com/seemethere) and [nbastatsR](https://github.com/abresler/nbastatR) by [abresler](https://github.com/abresler). The work towards a Python API wrapper in `nba_py` is a great start, but the documentation of the [stats.nba.com](https://stats.nba.com) API is lacking. `nbastatsR` is an extremely valuable resource for the R community, and this work hopes to extend the breadth and depth of that package. In my research, I have also come across the recent effort of [nba_api](https://github.com/swar/nba_api) by [swar](https://github.com/swar). This looks similar to `nba_py` and I am hoping to collaborate.

## Goals

If successful, `py_ball` should accomplish the following:
- By working with the community, improve the quality of documentation for [stats.nba.com](https://stats.nba.com).
- Further enable the dissemination of basketball statistics to increase the understanding of the sport and encourage the practice of basketball analytics.
- Produce introductory analyses leveraging NBA and WNBA data to reduce the barrier of entry to basketball analytics through demonstration.
- Focus on the WNBA in an effort to stress inclusivity and contribute to women's basketball analytics.

## Documentation

While `nba_api` improves greatly upon the documentation of the [stats.nba.com](https://stats.nba.com) API in `nba_py`, `py_ball` strives to take documentation further through the following:
- Fully documented code, including function, class, and script docstrings.
- Extend endpoint and parameter documentation to include feature definitions.

### [Current Documentation](https://github.com/basketballrelativity/py_ball/wiki)

Classes:

The functionality of the classes within the package are documented in both the docstrings and [this site](https://basketballrelativity.github.io/py_ball/_build/html/index.html). The endpoints, parameters, and tables are documented in the Wiki (linked below):

- [BoxScore](https://github.com/basketballrelativity/py_ball/wiki/BoxScore)
- [Draft](https://github.com/basketballrelativity/py_ball/wiki/Draft)
- [Image](https://github.com/basketballrelativity/py_ball/wiki/Image)
- [LeaderBoard](https://github.com/basketballrelativity/py_ball/wiki/LeaderBoard)
- [League](https://github.com/basketballrelativity/py_ball/wiki/League)
- [LeagueDash](https://github.com/basketballrelativity/py_ball/wiki/LeagueDash)
- [PlayByPlay](https://github.com/basketballrelativity/py_ball/wiki/PlayByPlay)
- [Player](https://github.com/basketballrelativity/py_ball/wiki/Player)
- [Salaries](https://github.com/basketballrelativity/py_ball/wiki/Salaries) (using [Hoopshype](https://hoopshype.com/))
- [ScoreBoard](https://github.com/basketballrelativity/py_ball/wiki/ScoreBoard)
- [Shots](https://github.com/basketballrelativity/py_ball/wiki/Shots)
- [Team](https://github.com/basketballrelativity/py_ball/wiki/Team)
- [WinProbability](https://github.com/basketballrelativity/py_ball/wiki/WinProbability)

## Development

1. ~~Initially map [stats.nba.com](https://stats.nba.com) API and fully document code.~~
2. ~~Refactor code to generate a more consistent structure across classes.~~
3. ~~Document endpoints and parameters with definitions.~~ (See Wiki [here](https://github.com/basketballrelativity/py_ball/wiki))
4. Research other basketball-related APIs to map.
5. ~~Write unit tests for the package.~~
6. ~~Begin introductory basketball analytics analyses.~~
    - ~~Franchise History~~ ([here!](https://github.com/basketballrelativity/franchise_history))
    - ~~Draft Combine Player Sheet~~ ([here!](https://github.com/basketballrelativity/draft_combine))
    - ~~Live NBA/WNBA scoreboard~~ ([here!](https://github.com/basketballrelativity/scoreboard))
    - ~~Shot Probability Model~~ ([here!](https://github.com/basketballrelativity/shot_probability))
    - ~~Location Data Exploration~~ ([here!](https://github.com/basketballrelativity/location_data))
    - ~~Assist Networks~~ ([here!](https://github.com/basketballrelativity/assist_networks))
    - ~Win Probability Model~ ([here!](https://github.com/basketballrelativity/py_ball/wiki/WinProbability))

## Installation

The package is built for Python 3 and leverages the packages in the `requirements.txt` file. `py_ball` can be installed via pip (more info [here](https://pypi.org/project/py-ball/)):
```
pip install py_ball
```

## Usage

The [stats.nba.com](https://stats.nba.com) API requires a request header for all API calls. A good discussion on this, including steps to obtain a proper request header, can be found [here](https://stackoverflow.com/questions/46781563/how-to-obtain-a-json-response-from-the-stats-nba-com-api). With a request header in `HEADER`, the example below demonstrates usage of the package to pull franchise history for the WNBA:

```
from py_ball import league, image

league_id = '10' #WNBA
franchises = league.League(headers=HEADERS,
                           endpoint='franchisehistory',
                           league_id=league_id)
```

Each class, with the exception of the `Headshot` and `Logo` classes, has a `data` attribute. This is a dictionary containing table names as keys and a list of dictionaries of table data as values. The `Headshot` and `Logo` classes have an `image` attribute that is a PNG object.

## Contact

Follow along for updates or reach out on Twitter [@py_ball_](https://twitter.com/py_ball_)!
