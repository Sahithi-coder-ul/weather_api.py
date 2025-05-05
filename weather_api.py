

# Import the required libraries
import requests  # To make HTTP requests and fetch data from an API
import matplotlib.pyplot as plt  # To create charts and graphs

# Your city and OpenWeatherMap API key (you need to sign up at openweathermap.org to get one)
city = "Hyderabad"
api_key = "8b7fa2e63d7a8a7419b6851f536c544a"

# Create the API URL with the city and your API key
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

# Send a request to the weather API and get the response
response = requests.get(url)
weather_data = response.json()  # Convert the response into a Python dictionary

# Create empty lists to store temperature and time
temperatures = []
timestamps = []

# Loop through the first few entries in the forecast
print(weather_data)
for entry in weather_data["list"][:10]:  # Limit to 10 data points to keep it simple
    temperature = entry["main"]["temp"]
    time = entry["dt_txt"]
    temperatures.append(temperature)
    timestamps.append(time)

# Create a line graph
plt.figure(figsize=(10, 5))  # Set the graph size
plt.plot(timestamps, temperatures, marker='o', color='blue')  # Plot the temperature vs time
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.title(f"Weather Forecast for {city}")  # Add a title
plt.xlabel("Time")  # Label x-axis
plt.ylabel("Temperature (°C)")  # Label y-axis
plt.tight_layout()  # Adjust layout to prevent label overlap
plt.grid(True)  # Add a grid for easier reading
plt.show()  # Display the graph


