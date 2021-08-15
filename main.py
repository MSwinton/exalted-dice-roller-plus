import argparse
from roller import Roller


def get_params():
    parser = argparse.ArgumentParser()

    # Normal default options.
    parser.add_argument('dice_pool', type=int)
    parser.add_argument('--btch', dest='botch_nums', type=list, default=[1])
    parser.add_argument('--suc', dest='success_nums', type=list, default=[7, 8, 9, 10])
    parser.add_argument('--dbl', dest='dbl_success_nums', type=list, default=[10])


    # Normal extra options


    # Faire Folk Bullshit

    return parser.parse_args()


def __main__():

    params = get_params()

    roller = Roller(params)
    roller.determine_rolls()


__main__()