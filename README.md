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
- `asyncio`library

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

5. **Run the bot:**
   ```bash
   python weather_bot.py
   ```


Usage
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
To prevent spam, the weather command has a cooldown of 20 seconds. If the command is used again before the cooldown period ends, the bot will respond with a message indicating how much time remains.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

## Fork the repository.
1. Create a new branch (git checkout -b feature/YourFeature).
2. Make your changes and commit them (git commit -m 'Add your message').
3. Push to the branch (git push origin feature/YourFeature).
4. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgments
OpenWeatherMap for the weather data API.
Discord.py for the Discord bot framework.
