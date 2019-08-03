import requests
import json

def get_weather(weather_apikey, latitude, longitude, unit):
    # weather_info is a dictionary that stores weather summary, highest temperature, and lowest temperature
    weather_info = {}

    # Weather API endpoint (https://darksky.net)
    weather_endpoint = 'https://api.darksky.net/forecast/' + weather_apikey + "/" + latitude + "," + longitude

    # Optional parameters
    if unit == "Fahrenheit":
        payload = {
            'exclude': 'currently,minutely,daily,alerts,flags'
        }
    elif unit == "Celsius":
        payload = {
            'exclude': 'currently,minutely,daily,alerts,flags',
            'unit': 'si'
        }

    response = requests.get(weather_endpoint, params=payload)
    data = json.loads(response.text)

    weather_info['summary'] = data['hourly']['summary']

    # temperatures is a list that stores all temperatures throughout the day; used to find max/min temperature
    temperatures = []

    for tempdata in data['hourly']['data']:
        temperatures.append(data['hourly']['data']['temperature'])

    max_temperature = max(temperatures)
    min_temperature = min(temperatures)

    weather_info['max'] = max_temperature
    weather_info['min'] = min_temperature
    return weather_info

def read_config():
    # config_information_map is a dictionary that stores all values within the config file
    config_information_map = {}

    # Read the config file and store data into config_information_map
    with open('config.json') as config_file:
        data = json.load(config_file)
    config_information_map['weather_apikey'] = data['weather_apikey']
    config_information_map['google_apikey'] = data['google_apikey']
    return config_information_map

def get_latitude_longitude(google_apikey, address):
    # latitude_longitude is a dictionary that stores the user's latitude and longitude
    latitude_longitude = {}

    # Google's Geocoding API endpoint
    geocoding_endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'

    # Google's Geocoding API requires the address and API key parameters
    payload = {
        'address': address,
        'key': google_apikey
    }

    response = requests.get(geocoding_endpoint, params=payload)
    data = json.loads(response.text)
    print(data)

    latitude_longitude['latitude'] = data['results'][0]['geometry']['location']['lat']
    latitude_longitude['longitude'] = data['results'][0]['geometry']['location']['lng']

def get_user_info():
    # user_info is a dictionary that stores the user's address and phone number
    user_info = {}

    # Ask for user's country and store the associated country code
    print("To get the most accurate temperature readings, enter your address.")
    print("Please use the following format: 123 Example St, Los Angeles, CA 90089")
    address_input = input("\t> ")
    user_info['address'] = address_input
    print("Enter the phone number you wish to receive daily notifications from.")
    print("Please use the following format: (123) 345-5678")
    phone_input = input("\t> ")
    user_info['phone'] = phone_input
    print("The default unit is Fahrenheit. Would you like to switch to Celsius? (y/n)")
    unit_input = input("\t> ")
    while unit_input.lower() != "y" and unit_input.lower() != "n":
        print("Invalid input.")
        unit_input = "\t> "
    if unit_input == "n":
        user_info['unit'] = "Fahrenheit"
    elif unit_input == "y":
        user_info['unit'] = "Celsius"

    return user_info


def main():
    print("Daily Weather Notification by Tran Ngo")
    print("Powered by Dark Sky (https://darksky.net/poweredby)")
    print("---------------------------------------------------")

    # Read the config file and store it into a dictionary
    config_information_map = read_config()

    # Assign the values of the config file to variables for use
    weather_apikey = config_information_map['weather_apikey']
    google_apikey = config_information_map['google_apikey']

    # Ask for user's country and postal code
    user_info = get_user_info()

    latitude_longitude = get_latitude_longitude(google_apikey, user_info['address'])



main()

