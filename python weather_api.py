import requests

api_key = "6d26688638a93aa41eda0ae08c023dc4"
city = "Chennai"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print(data)  # DEBUG LINE

if "main" in data:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Pressure:", pressure)
else:
    print("Error:", data)
import matplotlib.pyplot as plt

labels = ["Temperature", "Humidity", "Pressure"]
values = [temperature, humidity, pressure]

plt.bar(labels, values)
plt.title("Weather Data Visualization")
plt.xlabel("Weather Parameters")
plt.ylabel("Values")
plt.show()
