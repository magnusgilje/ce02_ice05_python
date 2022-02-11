import sys
import getopt
import logging
import requests

sys.path.insert(0,"..")
import get_weather_info

def main(argv):
    """Main function for circle code to process the file arguments """

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.WARNING)

    region = None # float(input('your region'))
    try:
        opts, _args = getopt.getopt(argv, "r:", ["region="])
    except getopt.GetoptError:
        print('circle_demo.py -r <region>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('get_weather_info_demo.py -r <region>')
            sys.exit()
        elif opt in ("-r", "--region"):
            region = arg

    if region is None:
       print('get_weather_info.py -r <region>')
    else:
        try:       
            myW = get_weather_info.Get_weather_info(region)
            print(myW.description())
            # print(myW.scraping())
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)

if __name__ == "__main__":
    main(sys.argv[1:])