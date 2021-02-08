from bs4 import BeautifulSoup
import requests

url = "https://pittsburgh.craigslist.org/d/cars-trucks/search/cta"

response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')

cars = soup.findAll('a', {'class': 'result-title'})

for car in cars:
    car_url = car.get('href')
    response = requests.get(car_url)
    car_soup_data = BeautifulSoup(response.text, 'html.parser')
    spans = car_soup_data.findAll('span')
    odo = -1
    for span in spans:
        if "odometer" in span.text:
            odo = span.text.replace("odometer", "")
    print(car.text, odo)
