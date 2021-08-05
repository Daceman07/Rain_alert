import requests
from twilio.rest import Client

API_KEY = "API KEY"
MY_LAT = 45.171730
MY_LONG = -93.304329
T_NUMBER = 'number'
MY_NUMBER = 'my number'
account_sid = "SID"
auth_token = "TOKEN"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {"lat": MY_LAT,
                  "lon": MY_LONG,
                  "appid": API_KEY,
                  "exclude": "current,minutely,daily"
                  }

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain/show today. Bring an ☔",
        from_=T_NUMBER,
        to=MY_NUMBER,
    )

    print(message.status)
