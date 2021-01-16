# Advent of Code - in Jupyter Notebooks [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome#readme) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UncleCJ/advent-of-code/master)

This repository contains the problems and my personal solutions to [Advent of Code](https://adventofcode.com/) in Jupyter (Python) Notebooks. Similar to that of [Alexe Simon](https://github.com/AlexeSimon/adventofcode), I want to provide [boilerplates](https://en.wikipedia.org/wiki/Boilerplate_code) to attempt AoC as well as record my own progress. See also the [Awesome Advent of Code](https://github.com/Bogdanp/awesome-advent-of-code) collection of references.

Jupyter Notebooks read much like the high school "lab reports" I was so fond of creating. In particular, besides being a nice blend of text and code, you may open them in a place such as [mybinder](https://mybinder.org) and get an interactive development environment in any web browser! See a [Jupyter tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/), [Advanced Jupyter tutorial](https://www.dataquest.io/blog/advanced-jupyter-notebooks-tutorial/) and [tips and tricks](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/).

Note that [mybinder hardly work with GitHub](https://mybinder.readthedocs.io/en/latest/about/about.html) - if you want to commit to Git, you need to save changes from there and upload them manually. I use [VS Code](https://code.visualstudio.com/docs/python/jupyter-support) and should look into [nbdime](https://nbdime.readthedocs.io/en/latest) / [jupytext](https://towardsdatascience.com/introducing-jupytext-9234fdff6c57).

Note that I do things like this repository more than I code - [professionally](https://www.linkedin.com/in/carljohan) I want to be a '[Developer Experience Manager](https://twitter.com/annegentle/status/1326389253752975361)'. My Python solutions (in [the branch 'cj'](https://github.com/UncleCJ/advent-of-code/tree/cj)) are notoriously naive but a way for me to learn, and I look at the [solution megathreads on reddit](https://www.reddit.com/r/adventofcode/?f=flair_name%3A%22SOLUTION%20MEGATHREAD%22) for inspiration.

## Changelog
### 2021-01-16

Finished AoC 2020! Now I can get on with the even more fun and playful work, such as:

* Make this repository more presentable and useful as an AoC sandbox
* Study, discuss, refer to all the other great participants' solutions and improve my own accordingly
* Solve the problems from previous years

### 2020-12-11

Add flake8 style checking

### 2020-12-08

Speed up MyBinder launching by pre-building docker images using [.github/workflows/binder.yaml] *(could provide a reference on this eventually)*. It was convenient when fiddling on code from the corporate computer, but otherwise I've become well acquainted with Jupyter in VS Code.

### 2020-12-07

Learnt that [Eric Wastl doesn't want the community to redistribute](https://www.reddit.com/r/adventofcode/comments/k4e4lm/2020_day_1_solutions/geykew3/?utm_source=reddit&utm_medium=web2x&context=3) problems or input data - so stopped doing so, will take out what I already put in and aim for a programmatic solution which will only re-display the problems from the original site

### 2020-12-03

Created this repository and started participating in Advent of Code

## Contribute

Contributions are always welcome! I don't have any guidelines, but get in touch and/or send me a pull request and we can look at it.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [CJ Sveningsson](https://github.com/UncleCJ) has waived all copyright and related or neighboring rights to this work.
