import requests

data = requests.get("https://raw.githubusercontent.com/chrislopez24/corona-parser/master/cases.json").json()

while True:
    try:
        country = input("Country name (empty input to exit): ")
        if country == "":
            break
        totalCases = data[country]["Total Cases"]
        newCases = data[country]["New Cases"]
        totalDeath = data[country]["Total Deaths"]
        newDeath = data[country]["New Deaths"]
        totalRecovered = data[country]["Total Recovered"]
        activeCases = data[country]["Active Cases"]

        print("""
=========================================================
Total cases: {}
New cases: {}
Total death: {}
New death: {}
Total recovered: {}
Active cases: {}
=========================================================""".format(totalCases, newCases, totalDeath, newDeath, totalRecovered, activeCases))
    except:
        print("Incorrect input!")