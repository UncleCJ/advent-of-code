import os
import requests

PROPERTIES = dict()

# By "Roberto" from https://stackoverflow.com/a/31852401https://stackoverflow.com/a/31852401
def load_properties(filepath, sep='=', comment_char='#'):
    """
    Read the file passed as parameter as a properties file.
    """
    props = {}
    with open(filepath, "rt") as f:
        for line in f:
            l = line.strip()
            if l and not l.startswith(comment_char):
                key_value = l.split(sep)
                key = key_value[0].strip()
                value = sep.join(key_value[1:]).strip().strip('"') 
                props[key] = value 
    return props

def load_config_ini(configfile='../../config.ini')
    if 'USER_SESSION_ID' in PROPERTIES.keys():
        return None
    
    try:
        PROPERTIES = load_properties(configfile)
        return True
    except:
        return None

def which_day():
    cwd_year, day_str = os.path.split(os.getcwd())
    _, year_str = os.path.split(cwd_year)

    try:
        year, day = int(year_str), int(day_str)
        return year, day
    except:
        return None

def download_helper(url, USER_SESSION_ID, USER_AGENT):
    try:
        with requests.get(url=url,
                          cookies={'session': USER_SESSION_ID},
                          headers={'User-Agent': USER_AGENT}) as response:
            if response.ok:
                return response.text
    except requests.exceptions.RequestException:
        print("Error while requesting statement from server. Request probably timed out. Giving up.")
        return None
    except Exception as e:
        print("Non handled error while requesting statement from server. " + str(e))
        return None

def download(year, day,
             USER_SESSION_ID='',
             USER_AGENT='adventofcode_notebook_helper',
             baseurl='https://adventofcode.com/'):
    output = dict()

    # Download any problem statements and footers we can
    html = download_helper(baseurl + str(year) + '/day/' + str(day),
                           USER_SESSION_ID, USER_AGENT)    
    if html:
        p1_start = html.find('<article')
        # str.find returns -1 if not found, so this arithmetic is sloppy
        p1_end = html.find('</article>') + len('</article>')
        p1_footer_start = p1_end + 1
        bottom_end = html.find('</main>', p1_footer_start) - 1
        
        output['part1'] = html[p1_start:p1_end]

        if USER_SESSION_ID == '':
            p1_footer_end = bottom_end
        else:
            p2_start = html.find('<article', p1_footer_start)
            # str.find returns -1 if not found, so this arithmetic is sloppy
            p2_end = html.find('</article>', p1_footer_start) + len('</article>')
            if not p2_start:
                p1_footer_end = bottom_end
            else:
                p1_footer_end = p2_start - 1
                p2_footer_end = bottom_end

                p2_footer_start = p2_end + 1
                output['part2'] = html[p2_start:p2_end]
                output['part2_footer'] = html[p2_footer_start:p2_footer_end]
        output['part1_footer'] = html[p1_footer_start:p1_footer_end]

    # Download the input data if we can
    if USER_SESSION_ID != '':
        input = download_helper(baseurl + str(year) + '/day/' + str(day), '/input',
                                USER_SESSION_ID, USER_AGENT)    
        if input:
            output['input'] = input.rstrip('\n')

    return output