import math
import logging
# import matplotlib.pyplot as plt

class Hailstone:
    def __init__(self, n: int):
        if (n <=0):
            logging.error('perimeter request for invalid starting value')
            raise ValueError("Invalid value for starting value")
        self.n = n
        logging.info('Hailstone sequence initiated')
        
    def plot(self):
        seq_list = [self.n]
        while self.n!=1:
            if self.n % 2 ==0:
                seq_list.append(self.n/2)
                self.n = self.n/2
            else:
                seq_list.append(3*self.n +1)
                self.n = 3*self.n +1
        logging.debug(f'Hailstone sequence starting with {self.n} generated')
        return (f"The seuquence starting with {seq_list[0]} results in: {seq_list}")
        