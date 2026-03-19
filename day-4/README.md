# Day 4: API Integration & JSON Parsing

This repository contains Python exercises focusing on API interactions, fetching data from public APIs, handling different HTTP response codes, and processing JSON data.

---

## Exercise 1 — `exercise_1.py` (GitHub Profile Fetcher)
- Fetches any user's profile from the GitHub public API.
- Retrieves and displays the user's username, biography, number of public repositories, and follower count.
- Fetches the user's public repositories and displays the top 5 sorted by star count (including name, stars, and language).
- **Error Handling**: Handles user not found (404), API rate bounds (403), and network errors gracefully.
- **Usage**: You can pass the GitHub username as a command-line argument, or simply run the script and enter it when prompted:
  ```bash
  python3 exercise_1.py torvalds
  # OR
  python3 exercise_1.py
  ```
- **Output:**
  ```text
  Username: torvalds
  Bio: None
  Public Repos: 11
  Followers: 291493
  
  Top 5 Repositories by Stars:
  - linux | 223948 stars | C
  - AudioNoise | 4291 stars | C
  - uemacs | 1938 stars | C
  - GuitarPedal | 1824 stars | C
  - test-tlb | 955 stars | C
  ```

---

## Exercise 2 — `exercise_2.py` (Weather CLI)
- Retrieves the current weather for a specified city using the free Open-Meteo API.
- Reaches out to the Open-Meteo Geocoding API to secure latitude and longitude for the given city name.
- Connects to the Open-Meteo Weather API to retrieve the `temperature_2m`, `wind_speed_10m`, and `weather_code`.
- Calculates Fahrenheit from the Celsius return value, maps the weather code to a descriptive string via the WMO interpretation codes, and nicely prints the result.
- **Usage**: You can pass the city name as command-line arguments, or simply run the script and enter it when prompted:
  ```bash
  python3 exercise_2.py "London"
  # OR
  python3 exercise_2.py
  ```
- **Output:**
  ```text
  Weather for London, United Kingdom:
  Temperature: 11.3°C (52.3°F)
  Wind Speed: 9.0 km/h
  Description: Clear sky
  ```

---

## API Reflection: What was the hardest part of reading the API response?
The hardest part of reading the API response was **understanding the nested JSON structure and the pagination mechanics**. For example, when fetching weather data, deciding which parts of the `current` object map to specific requirements like Celsius vs Fahrenheit. Knowing exactly when to parse floats or check for default API rate limit bounds (and interpreting Open-Meteo's weather codes into human-readable definitions via WMO codes) required studying the API shape visually before blindly looping over the responses.

---

## Run

```bash
python3 exercise_1.py
python3 exercise_2.py
```
