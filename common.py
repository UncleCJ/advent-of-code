import requests

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

def download(year, day, USER_SESSION_ID='', USER_AGENT='adventofcode_notebook_helper', baseurl='https://adventofcode.com/'):
    output = {}
    try:
        with requests.get(url=baseurl + str(year) + '/day/' + str(day),
                          cookies={'session': USER_SESSION_ID},
                          headers={'User-Agent': USER_AGENT}) as response:
            if response.ok:
                html = response.text

                p1_start = html.find('<article')
                p1_end = html.find('</article>') + len('</article>')
                
                output['part1'] = html[p1_start:p1_end]

                if USER_SESSION_ID != '':
                    p2_start = html.find('<article', p1_end + 1)
                    p2_end = html.find('</article>', p1_end + 1) + len('</article>')
                    if p2_start and p2_end:
                        output['part2'] = html[p2_start:p2_end]
        if USER_SESSION_ID != '':
            with requests.get(url=baseurl + str(year) + '/day/' + str(day) + '/input',
                              cookies={'session': USER_SESSION_ID},
                              headers={'User-Agent': USER_AGENT}) as response:
                if response.ok:
                    input = response.text
                    if input:
                        output['input'] = input.rstrip('\n')
        return output
    except requests.exceptions.RequestException:
        print("Error while requesting statement from server. Request probably timed out. Giving up.")
        return None
    except Exception as e:
        print("Non handled error while requesting statement from server. " + str(e))
        return None
