import argparse
from roller import Roller


def get_params():
    parser = argparse.ArgumentParser()

    # Normal default options.
    parser.add_argument('dice_pool', type=int)


    # Normal extra options


    # Faire Folk Bullshit

    return parser.parse_args()


def __main__():

    params = get_params()

    roller = Roller(params)
    roller.determine_rolls()
    roller.determine_successes()
    roller.determine_botches()




__main__()