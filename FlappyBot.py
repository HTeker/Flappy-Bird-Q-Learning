import random
import json
from itertools import chain

class FlappyBot():
    def __init__(self):
        self.q_values = {}
        self.load_q_values()

        if self.q_values == {}:
            self.initialize_q_values()

    def initialize_q_values(self):
        print('Creating and initializing q_values.json file...')
        for x in chain(list(range(-40, 140, 10)), list(range(140, 421, 70))):
            for y in chain(list(range(-300, 180, 10)), list(range(180, 421, 60))):
                for v in range(-10, 11):
                    self.q_values[str(x) + '_' + str(y) + '_' + str(v)] = [0, 0]

        fd = open('q_values.json', 'w')
        json.dump(self.q_values, fd)
        fd.close()

    def load_q_values(self):
        try:
            file = open('q_values.json', 'r')
        except IOError:
            return
        self.q_values = json.load(file)

    def act(self, horizontal_difference, vertical_difference, player_velocity):
        print("Horizontal difference: {} Vertical difference: {} Player velocity: {}".format(horizontal_difference, vertical_difference, player_velocity))
        return random.randint(0,1)