import pandas as pd

data = pd.read_csv("covid_data.csv")

print("COVID-19 Data:")
print(data.head())

total_cases = data['Cases'].sum()
total_deaths = data['Deaths'].sum()

print("\nTotal Cases:", total_cases)
print("Total Deaths:", total_deaths)
