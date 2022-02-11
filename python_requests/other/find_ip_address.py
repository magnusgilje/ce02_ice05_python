import requests
import sys

def main(argv):

    if len(argv) !=0:
        print('Usage: no parameters')
        exit(1)

    r = requests.get('https://api.ipify.org?format=json')

    if r.status_code != 200:
        print(f'Unable to perform request, status: {r.status_code}')
        exit(0)
    
    json = r.json()

    ip_address = json['ip']

    print(f'Public facing ip address is {ip_address}')

if __name__ == "__main__":
    main(sys.argv[1:])

# to run >python find_ip_address.py