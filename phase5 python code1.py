import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'Cases': [100, 150, 200, 250],
    'Deaths': [5, 10, 15, 20],
}

df = pd.DataFrame(data)

print("COVID-19 Data:")
print(df)

total_cases = df['Cases'].sum()
total_deaths = df['Deaths'].sum()

print("\nTotal Cases:", total_cases)
print("Total Deaths:", total_deaths)
