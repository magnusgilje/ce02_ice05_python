import requests
import sys

# x= int(input('what description do you want'))

class Get_weather_info:
    def __init__(self): #,x:int):
        print('running description search')
        #self.x = x

    def main(argv):

        if len(argv) !=0:
            print('Usage: no parameters')
            exit(1)

        r = requests.get('https://api.weather.gov/alerts/active?area=AN')

        if r.status_code != 200:
            print(f'Unable to perform request, status: {r.status_code}')
            exit(0)
        #lets get runnning the code 
        x= int(input('what description do you want'))
        description = r.json()['features'][x]['properties']['description']

        print(description)

        
    if __name__ == "__main__":
        main(sys.argv[1:])

# to run >python find_ip_address.py