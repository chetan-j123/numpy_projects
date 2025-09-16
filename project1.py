import numpy as np
import random

# Menu for user   
def main():
 while True:
  print("🌦️ What would you like to calculate?")
  print("1. Average Temperature of the Month")
  print("2. Hottest Day of the Month")
  print("3. Days with Significant Rainfall (≥ 10 mm)")
  print("4. Correlation between Humidity and Rainfall")
  print("5. exit")
  userinput = str(input("\n👉 Enter your choice (1-4): "))

  # Extract required columns
  temp_of_month = new_data[1:len(new_data), 1].astype(float)
  rainfall = new_data[1:len(new_data), 3].astype(float)
  humidity = new_data[1:, 2].astype(float)

  # Option 1: Average temperature
  if userinput == "1":
    print("\n🌡️ The average temperature of the month is:",
          round(np.mean(temp_of_month), 2), "°C")

  # Option 2: Hottest day
  if userinput == "2":
    hottest_day = np.where(temp_of_month == np.max(temp_of_month))
    print("\n🔥 The hottest day is Day", hottest_day[0][0] + 1,
          "with a temperature of", np.max(temp_of_month), "°C")
 
  # Option 3: Rainy days
  if userinput == "3":
    rainy_days = np.where(rainfall >= 10)[0] + 1
    if len(rainy_days) > 0:
        print("\n☔ Days with significant rainfall (≥ 10 mm):")
        for day in rainy_days:
            print("   - Day", day)
        main()
    else:
        print("\n☀️ No significant rainfall recorded this month.")
        main()
 # Option 4: Correlation
  if userinput == "4":
    corr = np.corrcoef(humidity, rainfall)[0, 1]
    print("\n📈 The correlation between humidity and rainfall is:",
          round(corr, 3))
    if corr > 0:
        print("   ➡️ Positive correlation: As humidity increases, rainfall tends to increase.")
        main()  
    elif corr < 0:
        print("   ➡️ Negative correlation: As humidity increases, rainfall tends to decrease.")
        main()     
    else:
        print("   ➡️ No correlation between humidity and rainfall.")
        main()
  if(userinput=="5"):
     break   
   


# Initialize dataset with headers
weather_data = np.array([
    ["Day", "Temperature (°C)", "Humidity (%)", "Rainfall (mm)"]
])
columns = len(weather_data[0])

# Generate data for 30 days
days = 31
for i in range(0, days - 1, 1):
    data = ["Day:" + str(i + 1),
            round(random.uniform(20, 40), 1),     # Temperature
            random.randint(40, 90),               # Humidity
            random.randint(0, 20)]                # Rainfall
    added_weather_data = np.append(weather_data, data)
    weather_data = added_weather_data

print("✅ Weather data generated successfully!\n")
                
# Reshape into proper table
new_data = added_weather_data.reshape(days, columns)
uc=str(input("do you want to start =(yes or no)"))
if(uc=="yes"):
   main()

