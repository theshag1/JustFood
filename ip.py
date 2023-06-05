import requests
import ast
from pprint import pprint

ip = "82.215.92.158"
url = f'https://api.codinary.org/v1/geoLocation/?ip={ip}'

response = requests.get(url)
print(response.text)
my_dict = ast.literal_eval(response.text)
pprint(my_dict, indent=2)


print('\n', my_dict['lat'], my_dict['l17on'])
