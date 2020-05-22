import json
import string 
from source.utils import read_web, recursive_crawl, user_agent_list


try:
    with open('./data/ATC_alteration.json') as json_file: 
        atc_dict = json.load(json_file)
except:
    atc_dict = {}

url = 'https://www.whocc.no/atc_ddd_alterations__cumulative/atc_alterations/'

root = read_web(url, user_agent_list)

atc_alteration = {}

for k in root.find_all('tr', attrs = {'valign': 'top'}):
    try:
        index = k.find_all('td')[2].text.find('\xa0')
        if index < 0:
            val = k.find_all('td')[2].text.split()[0]
        else:
            val = k.find_all('td')[2].text[:index]
        atc_alteration[k.find_all('td')[0].text[:7]] = val
        print(k.find_all('td')[0].text[:7], val)
    except:
        pass
    print('\n')

print('Done !\n')

with open('./data/atc_alteration.json', 'w') as outfile:
    json.dump(atc_alteration, outfile)
outfile.close()