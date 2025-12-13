import requests
import argparse

from httplib2.auth import params
from typing_extensions import ParamSpec

url = 'https://api.openbrewerydb.org/v1/breweries'
noBreweries = 20

class Brewery:
    id: str
    name: str
    brewery_type = ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor', 'closed']
    address_1:str
    address_2:str
    address_3:str
    city:str
    state_province:str
    postal_code:str
    country:str
    longitude:int
    latitude:int
    phone:str
    website_url:str
    state:str
    street:str

    def __init__(self, brewery):
        self.id=brewery["id"]
        self.name=brewery["name"]
        self.brewery_type=brewery["brewery_type"]
        self.address_1=brewery["address_1"]
        self.address_2=brewery["address_2"]
        self.address_3=brewery["address_3"]
        self.city=brewery["city"]
        self.state_province=brewery["state_province"]
        self.postal_code=brewery["postal_code"]
        self.country=brewery["country"]
        self.longitude=brewery["longitude"]
        self.latitude=brewery["latitude"]
        self.phone=brewery["phone"]
        self.website_url=brewery["website_url"]
        self.state=brewery["state"]
        self.street=brewery["street"]

    def __str__(self):
        res = ""
        for p, w in self.__dict__.items():
            res = res + f"{p} = {w}\n"
        return res

def main():
    parser=argparse.ArgumentParser(description="Skrypt pobierający dane o browarach w wybranym mieście")
    parser.add_argument("-city", help="masto w którym funkcjonuje browar")
    args = parser.parse_args()
    params = {}

    if args.city:
        params['by_city'] = args.city
    else:
        params['per_page'] = str(noBreweries)

    res = requests.get(url, params)
    breweries = res.json()
    bw = []
    i = 0

    for b in breweries[:noBreweries]:
        bw.append(Brewery(brewery=b))
        # print(bw[i],["name"])
        # print(f"{chr(27)}[4m {i + 1} - {bw[i],["name"]} {chr(27)}[0m \n" + str(bw[i]))
        print(f"{chr(27)}[4m {i + 1} - {str(b["name"])} {chr(27)}[0m \n" + str(bw[i]))
        i = i + 1

if __name__ == "__main__":
    main()