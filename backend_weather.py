import requests
import os
api_key = os.environ["API"]
def get_detail(place, frequency):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    data = requests.get(url).json()
    if data['cod'] == '200':
        index = 8*frequency
        filtered_data = [data['list'][i]['main']for i in range(index)]
        date = [data['list'][i]['dt_txt']for i in range(index)]
        sky_data = [data['list'][i]['weather']for i in range(index)]
        return filtered_data, date, sky_data
    else:
        return data['message'],None,None



if __name__ == "__main__":
    get_detail(place="patna", frequency=1)
