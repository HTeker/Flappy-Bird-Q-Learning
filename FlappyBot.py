import random
import math
import json
from itertools import chain

class FlappyBot():
    def __init__(self):
        self.number_of_games = 0
        self.score = 0
        self.reward = 0

        self.learning_rate = .7
        self.gamma = 0.95
        self.chance_of_flapping_on_unknown = 0.1

        self.last_move = []
        self.last_state = "0_0_0"
        self.last_action = 0

        self.memory = []
        self.q_values = {}
        self.load_q_values()

    def load_q_values(self):
        try:
            file = open('q_values.json', 'r')
            self.q_values = json.load(file)
        except IOError:
            file = open('q_values.json', 'w')
            self.q_values = {"0_0_0": [0, 0]}
            json.dump(self.q_values, file)
            file.close()

    def act(self, horizontal_difference, vertical_difference, player_velocity):
        state = self.convert_states_to_string(horizontal_difference, vertical_difference, player_velocity)

        self.last_move = [self.last_state, self.last_action, state]

        # Update the last state as the new state
        self.last_state = state

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
            self.q_values[state] = [0.0, 0.0]
            if(random.uniform(0, 1) <= self.chance_of_flapping_on_unknown):
                return 1
            else:
                return 0

    def update_last_q_value_based_on_reward(self):
        state = self.last_move[0]
        action = self.last_move[1]
        resulting_state = self.last_move[2]

        self.q_values[state][action] = (1 - self.learning_rate) * (self.q_values[state][action]) + \
                                   self.learning_rate * (self.reward + self.gamma * max(self.q_values[resulting_state]))

    def convert_states_to_string(self, horizontal_difference, vertical_difference, player_velocity):
        # Round to the nearest 10
        horizontal_difference = int(math.ceil(horizontal_difference / 10.0)) * 10
        vertical_difference = int(math.ceil(vertical_difference / 10.0)) * 10

        return str(int(horizontal_difference)) + '_' + str(int(vertical_difference)) + '_' + str(player_velocity)

    def save_q_values(self):
        self.number_of_games += 1
        print('Game #{} | Reward: {} | Score: {}'.format(self.number_of_games, self.reward, self.score))
        self.score = 0
        self.reward = 0

        file = open('q_values.json', 'w')
        json.dump(self.q_values, file)
        file.close()