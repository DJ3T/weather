# Discord Weather Bot 🌦️

![Python](https://img.shields.io/badge/Python-3.10-blue)

## Description

A simple Discord bot that provides real-time weather information for a specified city using the OpenWeatherMap API. Users can request weather updates by sending a command in Discord, and the bot will respond with the current weather conditions, temperature, and more. 🌍

## Features

- 🌤️ Fetches weather data from OpenWeatherMap.
- ⏳ Supports commands with cooldowns to prevent spam.
- 📊 User-friendly responses with temperature and weather descriptions.

## Requirements

- 🐍 Python 3.10 or higher
- 📦 `discord.py` library
- 📦 `requests` library
- 📦 `asyncio` library

## Installation

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/DJ3T/weather-bot
   cd weather-bot
2. **Install required packages:**
   
   ```bash
   pip install -r requirements.txt
3. **Set up environment variables:** Edit the Python file to replace the API key and the Discord bot token:
   
   ```bash
   DISCORD_TOKEN = 'your_discord_bot_token'
   
   WEATHER_API_KEY = 'your_openweathermap_api_key'

## ⚠️ Warning ⚠️
When setting up your Discord bot, make sure to grant the following permissions:

✉️ Send Messages: Allows the bot to send weather updates in the channel.

📖 Read Messages: Enables the bot to read user commands.

🔗 Embed Links: Allows the bot to send rich embedded messages with formatting.

4. **Run the bot:**
   
   ```bash
   python weather_bot.py

## Usage
To get the weather information for a city, use the command:
   ```bash
   !weather <city_name>
   ```
## Example:
   ```bash
   !weather New York
   ```
   The bot will respond with the current weather conditions for the specified city.

## Cooldown
To prevent spam and to stay within the limit of 100 free requests per minutes, the weather command has a cooldown of 20 seconds. ⏳ If the command is used again before the cooldown period ends, the bot will respond with a message indicating how much time remains. If it's for personal use or if you don't mind paying, you can edit the python file.

## Contributing 🤝
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch:
   
   ```bash
   git checkout -b feature/YourFeature
3. Make your changes and commit them:
   
   ```bash
   git commit -m 'Add your message'
4. Push to the branch:
   
   ```bash
   git push origin feature/YourFeature
5. Create a new Pull Request.

## License 📜
This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgments 🙏
OpenWeatherMap for the weather data API.
Discord.py for the Discord bot framework. EOF
