import requests
import json
import schedule
from twilio.rest import Client

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

    # Find the max/min temperature for the day
    for tempdata in data['hourly']['data']:
        temperatures.append(tempdata['temperature'])

    max_temperature = max(temperatures)
    min_temperature = min(temperatures)

    weather_info['max'] = str(max_temperature)
    weather_info['min'] = str(min_temperature)
    return weather_info

def send_text(twilio_accountsid, twilio_authtoken, twilio_phone, user_phone, weather_info, unit):
    client = Client(twilio_accountsid, twilio_authtoken)

    # Message to send to phone
    weather_text = ""
    if unit == "Fahrenheit":
        weather_text = weather_info['summary'] + " High: " + weather_info['max'] + "°F. Low: " + weather_info['min'] + "°F."
    elif unit == "Celsius":
        weather_text = weather_info['summary'] + " High: " + weather_info['max'] + "°C. Low: " + weather_info['min'] + "°C."

    message = client.messages.create(
        body=weather_text,
        from_=twilio_phone,
        to=user_phone
    )

    message.sid


def read_config():
    # config_information_map is a dictionary that stores all values within the config file
    config_information_map = {}

    # Read the config file and store data into config_information_map
    with open('config.json') as config_file:
        data = json.load(config_file)
    config_information_map['weather_apikey'] = data['weather_apikey']
    config_information_map['google_apikey'] = data['google_apikey']
    config_information_map['twilio_accountsid'] = data['twilio_accountsid']
    config_information_map['twilio_authtoken'] = data['twilio_authtoken']
    config_information_map['twilio_phone'] = data['twilio_phone']
    return config_information_map

def get_latitude_longitude(google_apikey, address):
    # latitude_longitude is a dictionary that stores the user's latitude and longitude
    latitude_longitude = {}

    # Google's Geocoding API endpoint
    geocoding_endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'

    # Google's Geocoding API requires two parameters: address and API key
    payload = {
        'address': address,
        'key': google_apikey
    }

    response = requests.get(geocoding_endpoint, params=payload)
    data = json.loads(response.text)

    latitude_longitude['latitude'] = str(data['results'][0]['geometry']['location']['lat'])
    latitude_longitude['longitude'] = str(data['results'][0]['geometry']['location']['lng'])
    return latitude_longitude

def get_user_info():
    # user_info is a dictionary that stores the user's address and phone number
    user_info = {}

    # Ask for user's country and store the associated country code
    print("To get the most accurate temperature readings, enter your address.")
    print("Please use the following format: 123 Example St, Los Angeles, CA 90089")
    address_input = input("\t> ")
    user_info['address'] = address_input
    print("Enter the phone number you wish to receive daily notifications from.")
    print("Please use the following format: +15558675310")
    phone_input = input("\t> ")
    user_info['phone'] = phone_input
    print("Enter the time of day you would like to receive the daily weather notification.")
    print("Please use the military time format (e.g. enter \"13:00\" for 1pm).")
    time_input = input("\t> ")
    user_info['time'] = time_input
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
    twilio_accountsid = config_information_map['twilio_accountsid']
    twilio_authtoken = config_information_map['twilio_authtoken']
    twilio_phone = config_information_map['twilio_phone']

    # Ask for user's address and unit preference
    user_info = get_user_info()

    # Get user's latitude and longitude based on the specified address
    latitude_longitude = get_latitude_longitude(google_apikey, user_info['address'])

    weather_info = get_weather(weather_apikey, latitude_longitude['latitude'], latitude_longitude['longitude'], user_info['unit'])

    send_text(twilio_accountsid, twilio_authtoken, twilio_phone, user_info['phone'], weather_info, user_info['unit'])

    # def job():
    #     # Get the weather info
    #     weather_info = get_weather(weather_apikey, latitude_longitude['latitude'], latitude_longitude['longitude'], user_info['unit'])
    #
    # # Get updated weather information and send text messages every day at specified time
    # schedule.every().day.at(user_info['time']).do(job)
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

main()

