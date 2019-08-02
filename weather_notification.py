import requests
import json

def get_weather(postalcode, countrycode):
    # Weather API endpoint (https://openweathermap.org)
    weather_endpoint = 'api.openweathermap.org/data/2.5/weather'

    # Parameter(s) needed to make the API call
    payload = {
        # 'zip' = postalcode
    }

    response = requests.get(url)

def read_config():
    # config_information_map is a dictionary that stores all values within the config file
    config_information_map = { }

    # Read the config file and store data into config_information_map
    with open('config.json') as config_file:
        data = json.load(config_file)
    config_information_map['weather_apikey'] = data['weather_apikey']
    return config_information_map

def print_welcome_text():
    # user_info is a dictionary that stores the user's country code and postal code
    user_info = { }

    # country_code_map is a dictionary that stores countries with their
    # corresponding 2 character ISO 3166 code
    country_code_map = {
        'Afghanistan': 'AF',
        'Algeria': 'DZ',
        'Argentina': 'AR',
        'Armenia': 'AM',
        'Australia': 'AU',
        'Austria': 'AT',
        'Bahamas': 'BS',
        'Bangladesh': 'BD',
        'Barbados': 'BB',
        'Belgium': 'BE',
        'Belize': 'BZ',
        'Bhutan': 'BT',
        'Bolivia': 'BO',
        'Bosnia and Herzegovina': 'BA',
        'Botswana': 'BW',
        'Brazil': 'BR',
        'Bulgaria': 'BG',
        'Cambodia': 'KH',
        'Cameroon': 'CM',
        'Canada': 'CA',
        'Chad': 'TD',
        'Chile': 'CL',
        'China': 'CN',
        'Colombia': 'CO',
        'Congo': 'CG',
        'Costa Rica': 'CR',
        'Croatia': 'HR',
        'Cuba': 'CU',
        'Czech Republic': 'CZ',
        'Denmark': 'DK',
        'Dominican Republic': 'DO',
        'Ecuador': 'EC',
        'Egypt': 'EG',
        'El Salvador': 'SV',
        'Estonia': 'EE',
        'Ethiopia': 'ET',
        'Finland': 'FI',
        'France': 'FR',
        'Germany': 'DE',
        'Ghana': 'GH',
        'Greece': 'GR',
        'Greenland': 'GL',
        'Guadeloupe': 'GP',
        'Guatemala': 'GT',
        'Guinea': 'GN',
        'Haiti': 'HT',
        'Honduras': 'HN',
        'Hong Kong': 'HK',
        'Hungary': 'HU',
        'Iceland': 'IS',
        'India': 'IN',
        'Indonesia': 'ID',
        'Iraq': 'IQ',
        'Ireland': 'IE',
        'Israel': 'IL',
        'Italy': 'IT',
        'Jamaica': 'JM',
        'Japan': 'JP',
        'Jordan': 'JO',
        'Kenya': 'KE',
        'Kuwait': 'KW',
        'Latvia': 'LV',
        'Lebanon': 'LB',
        'Liberia': 'LR',
        'Libya': 'LY',
        'Lithuania': 'LT',
        'Luxembourg': 'LU',
        'Macao': 'MO',
        'Madagascar': 'MG',
        'Malaysia': 'MY',
        'Mexico': 'MX',
        'Mongolia': 'MN',
        'Morocco': 'MA',
        'Myanmar': 'MM',
        'Nepal': 'NP',
        'Netherlands': 'NL',
        'New Zealand': 'NZ',
        'Nicaragua': 'NI',
        'Niger': 'NE',
        'Nigeria': 'NG',
        'Norway': 'NO',
        'Pakistan': 'PK',
        'Panama': 'PA',
        'Papua New Guinea': 'PG',
        'Paraguay': 'PY',
        'Peru': 'PE',
        'Philippines': 'PH',
        'Poland': 'PL',
        'Portugal': 'PT',
        'Puerto Rico': 'PR',
        'Romania': 'RO',
        'Russian Federation': 'RU',
        'Saudi Arabia': 'SA',
        'Serbia': 'RS',
        'Sierra Leone': 'SL',
        'Singapore': 'SG',
        'Slovakia': 'SK',
        'Slovenia': 'SI',
        'Somalia': 'SO',
        'South Africa': 'ZA',
        'South Korea': 'KR',
        'South Sudan': 'SS',
        'Spain': 'ES',
        'Sri Lanka': 'LK',
        'Sudan': 'SD',
        'Sweden': 'SE',
        'Switzerland': 'CH',
        'Taiwan': 'TW',
        'Thailand': 'TH',
        'Turkey': 'TR',
        'Uganda': 'UG',
        'Ukraine': 'UA',
        'United Kingdom': 'GB',
        'United States': 'US',
        'Uruguay': 'UY',
        'Uzbekistan': 'UZ',
        'Venezuela': 'VE',
        'Vietnam': 'VN',
        'Yemen': 'YE',
        'Zambia': 'ZM',
        'Zimbabwe': 'ZW'
    }

    # Putting the keys of the country_code_map dictionary into a list
    country_list = list(country_code_map.keys())

    print("Daily Weather Notification by Tran Ngo")
    print("-----------------------------------------------")
    # Ask for user's country and store the associated country code
    country_input = input("Please enter your country (to see a list of supported countries, type \"help\"): ")
    while country_input not in country_list and country_input != "help":
        print("Invalid input.")
        country_input = input("Please enter your country (to see a list of supported countries, type \"help\"): ")
    if country_input == "help":
        print("")
        for country in country_list:
            print(country)
    else:
        user_info['countrycode'] = country_code_map[country_input]
    # Ask for user's postal code and store it
    postalcode_input = input("Please enter your postal code: ")
    user_info['postalcode'] = postalcode_input
    return user_info


def main():
    # Read the config file and store it into a dictionary
    config_information_map = read_config()

    # Assign the values of the config file to variables for use
    weather_apikey = config_information_map['weather_apikey']
    print_welcome_text()

main()

