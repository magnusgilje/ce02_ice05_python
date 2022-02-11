import requests
import sys
import logging


class Get_weather_info:
    def __init__(self,region:str,pos=0): 
        self.pos = pos
        self.region = region

    def description(self):
        self.r = requests.get(f'https://api.weather.gov/alerts/active?area={self.region}')
        desc = self.r.json()['features'][self.pos]['properties']['description']
        logging.debug(f'Description at position {self.pos} returned')
        return desc
    
    def extract_weather_description(self,json):

        features = json['features']
        '''If no weather warning'''
        if len(features)==0:
            return "All looks good"

        return features[self.pos]['properties']['description']

    def scraping(self):
        #r =requests.get('https://api.weather.gov/alerts/active?area=AN')
        logging.debug(f'weather request initialised')
        if(self.r.status_code !=200):
            logging.info(f'Unsuccessful status code')
            print(f'Status code error: {self.r.status_code}')
            exit(0)

        self.weather_desc = self.extract_weather_description(self.r.json())

        return(f"\n\nDescription for region '{self.region}':\n\n{self.weather_desc}\n\n")
