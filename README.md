# Discord Weather Bot

![Python](https://img.shields.io/badge/Python-3.10-blue)

## Description

A simple Discord bot that provides real-time weather information for a specified city using the OpenWeatherMap API. Users can request weather updates by sending a command in Discord, and the bot will respond with the current weather conditions, temperature, and more.

## Features

- Fetches weather data from OpenWeatherMap.
- Supports commands with cooldowns to prevent spam.
- User-friendly responses with temperature and weather descriptions.

## Requirements

- Python 3.10 or higher
- `discord.py` library
- `requests` library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/weather-bot.git
   cd weather-bot
   
2. **Install required packages:**
```bash
pip install -r requirements.txt
Set up environment variables:
```
3. **Edit the python file to replace the API key and the discord bot token**

DISCORD_TOKEN = your_discord_bot_token
WEATHER_API_KEY = your_openweathermap_api_key

4. **Run the bot:**
```bash
python weather_bot.py
```
