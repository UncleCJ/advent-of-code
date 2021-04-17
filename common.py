import os
import sys
import re

try:
    import requests
except ImportError:
    sys.exit("You need requests module."
             + " Install it by running pip install requests.")

PROPERTIES = dict()


# By "Roberto" from https://stackoverflow.com/a/31852401
def load_properties(filepath, sep='=', comment_char='#'):
    """
    Read the file passed as parameter as a properties file.
    """
    props = {}
    try:
        with open(filepath, "rt") as f:
            for line in [line.strip() for line in f]:
                if line and not line.startswith(comment_char):
                    key_value = line.split(sep)
                    key = key_value[0].strip()
                    value = sep.join(key_value[1:]).strip().strip('"')
                    props[key] = value
    except Exception as e:
        print("Failed to read properties: " + str(e))
        return None
    return props


def load_config_ini(configfile='../../config.ini'):
    global PROPERTIES
    if 'USER_SESSION_ID' in PROPERTIES.keys():
        return None

    PROPERTIES = load_properties(filepath=configfile)
    if PROPERTIES:
        return True
    else:
        return None


def which_day():
    cwd_year, day_str = os.path.split(os.getcwd())
    _, year_str = os.path.split(cwd_year)

    try:
        year, day = int(year_str), int(day_str)
        return year, day
    except Exception as e:
        print("We do not seem to be in a calendar folder: " + str(e))
        return None


def download_helper(url: str, USER_SESSION_ID: str, USER_AGENT: str) -> str:
    # print(f'download_helper({url}, {USER_SESSION_ID}, {USER_AGENT})')
    try:
        with requests.get(url=url,
                          cookies={'session': USER_SESSION_ID},
                          headers={'User-Agent': USER_AGENT}) as response:
            if response.ok:
                return response.text
    except requests.exceptions.RequestException:
        print("Error while requesting statement from server."
              + " Request probably timed out.")
        return None
    except Exception as e:
        print("Non handled error while requesting statement from server. "
              + str(e))
        return None


def download_aoc_statement(year: int, day: int,
                           USER_SESSION_ID='',
                           USER_AGENT='adventofcode_notebook_helper',
                           baseurl='https://adventofcode.com/') -> str:

    html = download_helper(baseurl + str(year) + '/day/' + str(day),
                           USER_SESSION_ID, USER_AGENT)
    if not html:
        return None

    statement_pattern = '''
<article.*?>(?P<part1>.+?)</article>      # The contents of any first <article> is part1
(?P<part1_footer>.+?)                     # Then, depending on whether there is a second <article>, 
                                          # part1_footer is from </article> to it, or until </main>
(
    <article.*?>(?P<part2>.+?)</article>  # Same as before, though optional, match part2
    (?P<part2_footer>.+?)                 # and part2_footer
)?
</main>
'''
    matches = re.search(statement_pattern,
                        html,
                        flags=re.MULTILINE|re.DOTALL|re.VERBOSE)
    
    if not matches:
        return None
    
    output = matches.groupdict()

    if USER_SESSION_ID == '':
        return output
    
    input = download_helper(baseurl + str(year) + '/day/'
                            + str(day) + '/input',
                            USER_SESSION_ID, USER_AGENT)
    if input:
        output['input'] = input.rstrip('\n')

    return output


def refresh():
    year_day = which_day()
    if not year_day:
        return None
    else:
        year, day = year_day

    USER_SESSION_ID = ''
    global PROPERTIES
    if 'USER_SESSION_ID' not in PROPERTIES.keys():
        load_config_ini()

    if 'USER_SESSION_ID' in PROPERTIES.keys():
        USER_SESSION_ID = PROPERTIES['USER_SESSION_ID']

    return download_aoc_statement(year, day, USER_SESSION_ID=USER_SESSION_ID)