import argparse
from roller import Roller


def get_params():
    parser = argparse.ArgumentParser()

    # Normal default options.
    parser.add_argument('dice_pool', type=int)
    parser.add_argument('--btch', dest='botch_nums', type=int, default=[1], nargs='*')
    parser.add_argument('--suc', dest='success_nums', type=int, default=[7, 8, 9, 10], nargs='*')
    parser.add_argument('--dbl', dest='dbl_success_nums', type=int, default=[10], nargs='*')


    # Normal extra options
    parser.add_argument('--casc', dest='cascading_nums', type=int, default=[], nargs='*')
    parser.add_argument('--rr', dest='reroll_nums', type=int, default=[], nargs='*')


    # Faire Folk Bullshit
    parser.add_argument('--dbl-btch', dest='dbl_botch_nums', type=int, default=[10], nargs='*')

    return parser.parse_args()


def __main__():

    params = get_params()

    roller = Roller(params)
    roller.determine_rolls()
    roller.determine_successes()
    roller.determine_botches()


__main__()