import math
import logging

class Circle:
    def __init__(self, radius: float):
        if (radius <= 0.0):
            logging.error('perimeter request for invalid radius value')
            raise ValueError("Invalid value for radius")
        self.radius = radius
        logging.info('Circle created with radius {:.2f}'.format(self.radius))

    def area(self) -> float:
        logging.debug('area request for circle with {:.2f}'.format(self.radius))
        return math.pi * self.radius * self.radius
    
    def perimeter(self) -> float:
        logging.debug('perimeter request for circle with {:.2f}'.format(self.radius))
        return 2.0 * math.pi * self.radius

    def summary(self) -> str:
        logging.debug('summary request for circle with {:.2f}'.format(self.radius))
        return ("area={area}, perimeter={perimeter}".format(area=round(self.area(),2), perimeter=round(self.perimeter(),2)))

