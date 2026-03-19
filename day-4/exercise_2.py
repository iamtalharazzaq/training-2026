import sys
import urllib.request
import urllib.error
import urllib.parse
import json

def get_weather_description(code):
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Drizzle: Light",
        53: "Drizzle: Moderate",
        55: "Drizzle: Dense",
        56: "Freezing Drizzle: Light",
        57: "Freezing Drizzle: Dense",
        61: "Rain: Slight",
        63: "Rain: Moderate",
        65: "Rain: Heavy",
        66: "Freezing Rain: Light",
        67: "Freezing Rain: Heavy",
        71: "Snow fall: Slight",
        73: "Snow fall: Moderate",
        75: "Snow fall: Heavy",
        77: "Snow grains",
        80: "Rain showers: Slight",
        81: "Rain showers: Moderate",
        82: "Rain showers: Violent",
        85: "Snow showers: Slight",
        86: "Snow showers: Heavy",
        95: "Thunderstorm: Slight or moderate",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }
    return weather_codes.get(code, f"Unknown weather code ({code})")

def fetch_weather(city):
    # Step 1: Geocoding API to get coordinates
    city_encoded = urllib.parse.quote(city)
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_encoded}&count=1&language=en&format=json"
    
    try:
        req_geo = urllib.request.Request(geocoding_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req_geo) as response_geo:
            geo_data = json.loads(response_geo.read().decode())
            
            # print("--- Raw Geocoding JSON ---")
            # print(json.dumps(geo_data, indent=2))
            
            if not geo_data.get('results'):
                print(f"Error: City '{city}' not found.")
                return
            
            location = geo_data['results'][0]
            lat = location.get('latitude')
            lon = location.get('longitude')
            city_name = location.get('name')
            country = location.get('country', '')
            
    except urllib.error.URLError as e:
        print(f"Network Error during geocoding: {e.reason}")
        return
    except Exception as e:
        print(f"An error occurred during geocoding: {e}")
        return

    # Step 2: Weather API to get current weather
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,weather_code"
    
    try:
        req_weather = urllib.request.Request(weather_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req_weather) as response_weather:
            weather_data = json.loads(response_weather.read().decode())
            
            # print("--- Raw Weather JSON ---")
            # print(json.dumps(weather_data, indent=2))
            
            current = weather_data.get('current', {})
            temp_c = current.get('temperature_2m')
            temp_f = (temp_c * 9/5) + 32 if temp_c is not None else None
            wind_speed = current.get('wind_speed_10m')
            weather_code = current.get('weather_code')
            description = get_weather_description(weather_code)
            
            print(f"Weather for {city_name}, {country}:")
            if temp_c is not None:
                print(f"Temperature: {temp_c}°C ({temp_f:.1f}°F)")
            else:
                print("Temperature: N/A")
            print(f"Wind Speed: {wind_speed} km/h")
            print(f"Description: {description}")
            
    except urllib.error.URLError as e:
        print(f"Network Error during weather fetch: {e.reason}")
    except Exception as e:
        print(f"An error occurred during weather fetch: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        city_input = " ".join(sys.argv[1:])
    else:
        city_input = input("Enter city name: ")
    fetch_weather(city_input)
