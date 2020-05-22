import json
import string 
from source.utils import read_web, recursive_crawl, user_agent_list


try:
    with open('./data/atc_drug.json') as json_file: 
        atc_dict = json.load(json_file)
except:
    atc_dict = {}

url = 'https://www.whocc.no/atc_ddd_index/?code='

for alphabet in string.ascii_uppercase:
    root = read_web(url + alphabet + '&showdescription=no', user_agent_list)
    if root.find('div', attrs = {'id': 'content'}).find('b') == None:
        print('No ATC code starts with %s \n'%(alphabet))
        continue
    else:
        print('Download ATC code starts with %s ... \n'%(alphabet))
    atc_dict[alphabet] = root.find('div', attrs = {'id': 'content'}).find('b').text
    urls = root.find('div', attrs = {'id': 'content'}).find_all('p')[1].find_all('a')
    for site in urls:
        recursive_crawl('https://www.whocc.no/atc_ddd_index' + site['href'][1:], user_agent_list, atc_dict)

print('Done !\n')

with open('./data/atc_drug.json', 'w') as outfile:
    json.dump(atc_dict, outfile)
outfile.close()