#!/usr/bin/env python3

# Advent of code working directories creator
# IMPORTANT Remember to edit the USER_SESSION_ID & author values with yours
# uses requests module. If not present use pip install requests
# Author = Alexe Simon
# Date = 06/12/2018

# Imports
import os
import datetime

import common


# Code
PROPERTIES = common.load_properties(filepath='config.ini')
locals().update(PROPERTIES)
# Set the default values if they are not in config.ini
base_pos = './' if 'base_pos' not in locals().keys() else base_pos
USER_SESSION_ID = '' if 'USER_SESSION_ID' not in locals().keys() else USER_SESSION_ID
# common.load_properties will load only as strings, so we need to cast some of them here
DOWNLOAD_STATEMENTS = True if 'DOWNLOAD_STATEMENTS' not in locals().keys() else bool(DOWNLOAD_STATEMENTS)
DOWNLOAD_INPUTS = True if 'DOWNLOAD_INPUTS' not in locals().keys() else bool(DOWNLOAD_INPUTS)
MAKE_CODE_TEMPLATE = True if 'MAKE_CODE_TEMPLATE' not in locals().keys() else bool(MAKE_CODE_TEMPLATE)
MAKE_URL = True if 'MAKE_URL' not in locals().keys() else bool(MAKE_URL)
# author = "CJ Sveningsson"
OVERWRITE = False if 'OVERWRITE' not in locals().keys() else bool(OVERWRITE)
# date = "December 2018"
starting_advent_of_code_year = 2015 if 'starting_advent_of_code_year' not in locals().keys() else int(starting_advent_of_code_year)
last_advent_of_code_year = 2015 if 'last_advent_of_code_year' not in locals().keys() else int(last_advent_of_code_year)
last_advent_of_code_day = 25 if 'last_advent_of_code_day' not in locals().keys() else int(last_advent_of_code_day)
MAX_RECONNECT_ATTEMPT = 2 if 'MAX_RECONNECT_ATTEMPT' not in locals().keys() else int(MAX_RECONNECT_ATTEMPT)
baseurl = 'https://adventofcode.com/' if 'baseurl' not in locals().keys() else baseurl
USER_AGENT = 'adventofcode_working_directories_creator' if 'USER_AGENT' not in locals().keys() else USER_AGENT

years = range(starting_advent_of_code_year, last_advent_of_code_year + 1)
days = range(1, 26)

print("Setup will download data and create working directories and files for adventofcode.")
if not os.path.exists(base_pos):
    os.mkdir(base_pos)
for y in years:
    print("Year "+str(y))
    if not os.path.exists(base_pos+str(y)):
        os.mkdir(base_pos+str(y))
    year_pos = base_pos + str(y)
    for d in (d for d in days if (y < last_advent_of_code_year or d <= last_advent_of_code_day)):
        print("    Day "+str(d));
        if not os.path.exists(year_pos+"/"+str(d)):
            os.mkdir(year_pos+"/"+str(d))
        day_pos = year_pos+"/"+str(d)
        if MAKE_CODE_TEMPLATE and not os.path.exists(day_pos+"/code.py"):
            with open(day_pos+"/code.py", "w+") as code:
                code.write("# Advent of code Year "+str(y)+" Day "+str(d)+" solution\n# Author = "+author+"\n# Date = "+date+"\n\nwith open((__file__.rstrip(\"code.py\")+\"input.txt\"), 'r') as input_file:\n    input = input_file.read()\n\n\n\nprint(\"Part One : \"+ str(None))\n\n\n\nprint(\"Part Two : \"+ str(None))")
        # if DOWNLOAD_INPUTS and (not os.path.exists(day_pos+"/input.txt") or OVERWRITE)and USER_SESSION_ID != "":
        #     done = False
        #     error_count = 0
        #     while(not done):
        #         try:
        #             with requests.get(url=baseurl+str(y)+"/day/"+str(d)+"/input", cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT}) as response:
        #                 if response.ok:
        #                     data = response.text
        #                     input = open(day_pos+"/input.txt", "w+")
        #                     input.write(data.rstrip("\n"))
        #                     input.close()
        #                 else:
        #                     print("        Server response for input is not valid.")
        #             done = True
        #         except requests.exceptions.RequestException:
        #             error_count += 1
        #             if error_count > MAX_RECONNECT_ATTEMPT:
        #                 print("        Giving up.")
        #                 done = True
        #             elif error_count == 0:
        #                 print("        Error while requesting input from server. Request probably timed out. Trying again.")
        #             else:
        #                 print("        Trying again.")
        #         except Exception as e:
        #             print("        Non handled error while requesting input from server. " + str(e))
        #             done = True
        if DOWNLOAD_STATEMENTS and (not os.path.exists(day_pos+"/statement.html") or OVERWRITE):
            done = False
            error_count = 0
            while(not done):
                html = common.download_helper(url=baseurl + str(y) + "/day/" + str(d),
                                              USER_SESSION_ID=USER_SESSION_ID,
                                              USER_AGENT=USER_AGENT)
                # with requests.get(url=baseurl+str(y)+"/day/"+str(d), cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT}) as response:
                if html:
                    start = html.find("<article")
                    end = html.rfind("</article>")+len("</article>")
                    end_success = html.rfind("</code>")+len("</code>")
                    with open(day_pos+"/statement.html", "w+") as statement:
                        statement.write(html[start:max(end, end_success)])
                    done = True
                else:
                    error_count += 1
                    if error_count > MAX_RECONNECT_ATTEMPT:
                        print("        Giving up.")
                        done = True
                    else:
                        print("        Trying again.")
        # if MAKE_URL and (not os.path.exists(day_pos+"/baseurl.url") or OVERWRITE):
        #     url = open(day_pos+"/baseurl.url", "w+")
        #     url.write("[InternetShortcut]\nURL="+baseurl+str(y)+"/day/"+str(d)+"\n")
        #     url.close()
print("Setup complete : adventofcode working directories and files initialized with success.")
