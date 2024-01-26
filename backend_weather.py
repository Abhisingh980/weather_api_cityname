import requests
API_KEY = "87c1216ff2589ddeabc4353be7e52387"


def get_detail(place, frequency):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    data = requests.get(url).json()
    if data['cod'] == '404':
        return data['message'], None, None
    index = 8*frequency
    filtered_data = [data['list'][i]['main']for i in range(index)]
    date = [data['list'][i]['dt_txt']for i in range(index)]
    sky_data = [data['list'][i]['weather']for i in range(index)]
    return filtered_data, date, sky_data


if __name__ == "__main__":
    get_detail(place="patnax", frequency=1)