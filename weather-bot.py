import discord
from discord.ext import commands
import requests
import asyncio

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

DISCORD_TOKEN = 'DISCORD_BOT_TOKEN'
WEATHER_API_KEY = 'OPENWEATHERMAP_API_KEY'

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        return (
            f"Weather in **{city}**: {weather_desc}\n"
            f"🌡️ Temperature: {temp}°C\n"
            f"🤔 Feels like: {feels_like}°C"
        )
    elif response.status_code == 404:
        return "❌ City not found. Please check the name."
    else:
        return "⚠️ Unable to fetch weather data. Try again later."

@bot.command(name="weather")
@commands.cooldown(1, 20, commands.BucketType.default)
async def weather(ctx, *, city: str):
    """Command to get weather information for a given city."""
    weather_info = get_weather(city)
    await ctx.send(weather_info)

@weather.error
async def weather_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"⏳ Please wait {int(error.retry_after)} seconds before using this command again.")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

bot.run(DISCORD_TOKEN)
