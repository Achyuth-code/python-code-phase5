import random
import time

def collect_covid_data():
    cases = random.randint(1, 100)
    deaths = random.randint(0, 10)
    return cases, deaths

total_cases = 0
total_deaths = 0

for day in range(1, 8):
    cases, deaths = collect_covid_data()
    
    print(f"Day {day}: Cases: {cases}, Deaths: {deaths}")
    
    total_cases += cases
    total_deaths += deaths
    
    time.sleep(1)

print("\nTotal Cases: ", total_cases)
print("Total Deaths: ", total_deaths)
