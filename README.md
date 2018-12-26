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

Classes
- [BoxScore](https://github.com/basketballrelativity/py_ball/wiki/BoxScore)
- [Draft](https://github.com/basketballrelativity/py_ball/wiki/Draft)
- [Image](https://github.com/basketballrelativity/py_ball/wiki/Image)
- [LeaderBoard](https://github.com/basketballrelativity/py_ball/wiki/LeaderBoard)
- [League](https://github.com/basketballrelativity/py_ball/wiki/League)
- [LeagueDash](https://github.com/basketballrelativity/py_ball/wiki/LeagueDash)
- [PlayByPlay](https://github.com/basketballrelativity/py_ball/wiki/PlayByPlay)
- [Player](https://github.com/basketballrelativity/py_ball/wiki/Player)
- [ScoreBoard](https://github.com/basketballrelativity/py_ball/wiki/ScoreBoard)
- [Team](https://github.com/basketballrelativity/py_ball/wiki/Team)

## Development

1. ~~Initially map [stats.nba.com](https://stats.nba.com) API and fully document code.~~
2. ~~Refactor code to generate a more consistent structure across classes.~~
3. ~~Document endpoints and parameters with definitions.~~ (See Wiki [here](https://github.com/basketballrelativity/py_ball/wiki))
4. Research other basketball-related APIs to map.
5. ~Write unit tests for the package.~
6. Begin introductory basketball analytics analyses.
