import random
import json
from itertools import chain

class FlappyBot():
    def __init__(self):


        self.q_values = {}
        self.load_q_values()

    def load_q_values(self):
        try:
            file = open('q_values.json', 'r')
            self.q_values = json.load(file)
        except IOError:
            file = open('q_values.json', 'w')
            file.write('{}')

    def act(self, horizontal_difference, vertical_difference, player_velocity):
        print("Horizontal difference: {} Vertical difference: {} Player velocity: {}".format(horizontal_difference, vertical_difference, player_velocity))
        return random.randint(0,1)