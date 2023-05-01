import os
from scr.functions import advisor_API, convert_data
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

paramts_city_id = {
    "name": "Jardim do Seridó",
    "state": "RN",
    "token": TOKEN
}
paramts = {
    "token": TOKEN
}

data = advisor_API.fetch_city_id(paramts_city_id)

list_city = []
for i in range(len(data)):
    id = data[i]['id']
    list_city.append(advisor_API.meteorological_data(id, paramts))

data_json = {}
data_json = convert_data.format_data(list_city)


