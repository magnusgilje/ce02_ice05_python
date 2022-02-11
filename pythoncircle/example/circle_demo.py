import sys
import getopt
import logging

sys.path.insert(0,"..")
import circle

def main(argv):
    """Main function for circle code to process the file arguments """

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.WARNING)

    radius = None
    try:
        opts, _args = getopt.getopt(argv, "r:", ["radius="])
    except getopt.GetoptError:
        print('circle_demo.py -r <radius>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('circle_demo.py -r <radius>')
            sys.exit()
        elif opt in ("-r", "--radius"):
            radius = arg

    if radius is None:
       print('circle_demo.py -r <radius>')
    else:
        try:                
            myC = circle.Circle(float(radius))
            print(myC.summary())
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)

if __name__ == "__main__":
    main(sys.argv[1:])
