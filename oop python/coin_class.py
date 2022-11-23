import random

# The Coin class simulates a coin that can be flipped

class Coin:
    # The __init__ method initialises the
    # sideup data attribute with "Heads"

    def __init__(self):
        self.sideup = 'Head'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then the sideup is set to 'Head'
    # otherwise , sideup is set to 'Tail'

    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Head'
        else:
            self.sideup = 'Tail'

    # the get_sideup method returns the value
    # referenced by sideup

    def get_sideup(self):
        return self.sideup
