import math
import json

class FlappyBot():
    def __init__(self):
        self.number_of_games = 0
        self.score = 0
        self.distance = 0
        self.learning_rate = .7
        self.gamma = 0.95
        self.last_state = "0_0_0"
        self.last_action = 0
        self.memory = []
        self.q_values = {}

        self.load_q_values()

    def load_q_values(self):
        """
        Loads the Q-values if the file exists, otherwise it creates a new file for the Q-values
        :return:
        """

        # Open the q_values.json file if it exists
        try:
            file = open('assets/q_values.json', 'r')
            self.q_values = json.load(file)
        # Create the q_values.json file if it does not exist
        except:
            file = open('assets/q_values.json', 'w')
            self.q_values = {"0_0_0": [0, 0]}
            json.dump(self.q_values, file)
            file.close()

    def act(self, horizontal_difference, vertical_difference, player_velocity):
        """
        Selects the best action for the given state based on the Q-values
        :param horizontal_difference:
        :param vertical_difference:
        :param player_velocity:
        :return:
        """

        # Get the string representation of the states
        state = self.convert_states_to_string(horizontal_difference, vertical_difference, player_velocity)

        # Append the last_state, last_action and state to the memory for later use in the update_q_values function
        self.memory.append([self.last_state, self.last_action, state])

        # Update the last state as the new state
        self.last_state = state

        # Check if Q-value exists for current state
        try:
            # Check which action is better to perform based on the Q-values
            if self.q_values[state][0] >= self.q_values[state][1]:
                self.last_action = 0
                return 0
            else:
                self.last_action = 1
                return 1
        except:
            # Create the Q-value if it does not exist among the Q-values
            self.q_values[state] = [0.0, 0.0]
            return 0

    def update_q_values(self):
        """
        Updates the Q-values for all states in the memory (per game) based on the rewards
        :return:
        """

        # Reverse the memory array so that the last state-action combination becomes the first
        history = list(reversed(self.memory))

        bird_died_on_top = True if int(history[0][2].split('_')[1]) > 120 else False

        i = 0
        for experience in history:
            state = experience[0]
            action = experience[1]
            resulting_state = experience[2]

            if i == 0:
                reward = -1000
            elif i == 1:
                reward = -750
            elif i == 2:
                reward = -500
            elif bird_died_on_top and action:
                reward = -1000
                bird_died_on_top = False
            else:
                reward = 1

            # Updating the Q-value for the given state-action combination
            self.q_values[state][action] = (1 - self.learning_rate) * (self.q_values[state][action]) + \
                                   self.learning_rate * (reward + self.gamma * max(self.q_values[resulting_state]))

            i += 1

        self.memory = []
        self.save_q_values()

    def convert_states_to_string(self, horizontal_difference, vertical_difference, player_velocity):
        """
        Converts the states into one single string value that is used as the key for the Q-values
        :param horizontal_difference:
        :param vertical_difference:
        :param player_velocity:
        :return:
        """

        # Round the states to the nearest 10 so that the state space becomes smaller
        horizontal_difference = int(math.ceil(horizontal_difference / 10.0)) * 10
        vertical_difference = int(math.ceil(vertical_difference / 10.0)) * 10

        return str(int(horizontal_difference)) + '_' + str(int(vertical_difference)) + '_' + str(player_velocity)

    def save_q_values(self):
        """
        Saves the Q-values array to the q_values.json file
        :return:
        """

        msg = 'Game #{} | Score: {} | Distance: {}'.format(self.number_of_games, self.score, self.distance)
        print(msg)

        file = open('assets/results.txt', 'a')
        file.write(msg + "\n")
        file.close()

        self.distance = 0
        self.score = 0
        self.reward = 0

        file = open('assets/q_values.json', 'w')
        json.dump(self.q_values, file)
        file.close()