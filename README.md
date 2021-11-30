# AdventOfCodeTemplate

This is my modification of Simon's Advent of Code template, spiced up with solution timings, copy-paste answers, tests,
an improved template, and many utility functions. Shoutouts to the r/python Discord for giving me template/utility
function ideas and helping me through tough puzzles.

Note that **Python 3.10** is required.

## Copying the template

You can use `init.py`, `runner.py`, and `aocutil.py` if you want to copy this repo template and answer the problems by yourself. 
Its functionnalities include making directories, downloading statements, downloading inputs, making code templates and making url links.

### Running `init.py`

To run `init.py`, follow these steps:
* Create a new folder.
* Download `init.py` and put it into the folder.
* Create a file called `session.txt` and put it into the same folder.
* Put your session into `session.txt` (see below).
* Open `init.py` in a text editor and change other user parameters as desired (see below).
* Change the date of the last advent of code year and day if needed.
* Run `init.py` from within the folder with
```shell
python init.py
```

### User Parameters

The `init.py` parameters are as follows:
```python
# USER SPECIFIC PARAMETERS
base_pos = "./"            # Folders will be created here. If you want to make a parent folder, change this to ex "./adventofcode/"
USER_SESSION_ID = ""       # Get your session by inspecting the session cookie content in your web browser while connected to adventofcode and paste it here as plain text in between the ". Leave at is to not download inputs.
DOWNLOAD_STATEMENTS = True # Set to false to not download statements. Note that only part one is downloaded (since you need to complete it to access part two)
DOWNLOAD_INPUTS = True     # Set to false to not download inputs. Note that if the USER_SESSION_ID is wrong or left empty, inputs will not be downloaded.
MAKE_CODE_TEMPLATE = True  # Set to false to not make code templates. Note that even if OVERWRITE is set to True, it will never overwrite codes.
MAKE_URL = True            # Set to false to not create a direct url link in the folder.
author = "?"               # Name automatically put in the code templates.
OVERWRITE = False          # If you really need to download the whole thing again, set this to true. As the creator said, AoC is fragile; please be gentle. Statements and Inputs do not change. This will not overwrite codes.

# DATE SPECIFIC PARAMETERS
date = "December 2020"               # Date automatically put in the code templates.
starting_advent_of_code_year = 2020  # You can go as early as 2015.
last_advent_of_code_year = 2020      # The setup will download all advent of code data up until that date included
starting_advent_of_code_day = 1      # You can go as early as 1 and as late as 25
last_advent_of_code_day = 25         # If the year isn't finished, the setup will download days up until that day included for the last year
```
The only important parameter is **USER_SESSION_ID**, which has to be set correctly for the script to download your personnal problems input.
To recover your session:
* Go to [AdventOfCode](https://adventofcode.com/).
* Log in by any means (GitHub, Google, ...).
* Check for a cookie named **session**. This step depends on the browser used. It can be done through network inspection or, in advanced browser like Chrome, by simply clicking on the **View site information** button directly left of the url (shown as a padlock), then clicking **Cookies**.
* Copy this cookie content and paste it in init.py in between the ". It might be automatically formated upon being copied and look different, do not worry.
Other parameters are self explanatory.
  
## AOCUtil

Before coding a solution, look over `aocutil.py` to see all the utility functions (and add your own). The template imports `aocutil` and many other useful functions.

## Running this repo code

Simply download the wanted solution folders.
Script can be run from the same directory:
```shell
cd 2020/2
python code.py
```
Note that the solution looks for files named `code.py` and `input.txt` and renaming them will not work.

### Runner

The runner will run both parts (`return None` at the start of the solve function to disable that part)
and time how long it takes. Then the return value of the **last not-`None` part** will be copied to clipboard for easy
pasting. The runner also has `pretty_errors` enabled, simply comment out its import statement to disable.

### Tests

Tests can be run by running `test.py` instead of `code.py`. They will only run if you specifically request it.

## Contributing

Any constructive pull request directly correcting errors or improving the code is welcomed.
