import requests
API_KEY = "87aba3cfe16d25e95af26264a8a44c24"


def get_detail(place, frequency):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    data = requests.get(url).json()
    print(data)
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
