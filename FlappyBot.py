import random

class FlappyBot():
    def act(self):
    def act(self, horizontal_difference, vertical_difference, player_velocity):
        print("Horizontal difference: {} Vertical difference: {} Player velocity: {}".format(horizontal_difference, vertical_difference, player_velocity))
        return random.randint(0,1)