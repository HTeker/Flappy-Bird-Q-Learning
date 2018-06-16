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
        state = self.convert_states_to_string(horizontal_difference, vertical_difference, player_velocity)

        print(state)


        try:
            # Check which action is better to perform based on the Q-values
            if self.q_values[state][0] >= self.q_values[state][1]:
                self.last_action = 0
                return 0
            else:
                self.last_action = 1
                return 1
        except:
            # Create q-value if it does not exist among the q-values
            self.q_values[state] = [0, 0]
            return random.randint(0, 1)

    def convert_states_to_string(self, horizontal_difference, vertical_difference, player_velocity):
        return str(int(horizontal_difference)) + '_' + str(int(vertical_difference)) + '_' + str(player_velocity)
