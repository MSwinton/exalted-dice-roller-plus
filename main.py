import argparse
from roller import Roller


def get_params():
    parser = argparse.ArgumentParser()

    # Required
    parser.add_argument('dice_pool', type=int)

    # Successes
    parser.add_argument('--suc-base', dest='base_successes', type=int, default=[0]*6+[1]*4, nargs=10)
    parser.add_argument('--suc-mods', dest='adtl_successes', type=int, default=[0]*10, nargs=10)
    parser.add_argument('--suc-mults', dest='success_multipliers', type=int, default=[1]*9+[2], nargs=10)

    # Botches
    parser.add_argument('--btch-base', dest='base_botches', type=int, default=[1]+[0]*9, nargs=10)
    parser.add_argument('--btch-mods', dest='adtl_botches', type=int, default=[0]*10, nargs=10)
    parser.add_argument('--btch-mults', dest='botch_multipliers', type=int, default=[1]*10, nargs=10)

    # Normal extra options
    parser.add_argument('--casc', dest='cascading_nums', type=int, default=[], nargs='*')
    parser.add_argument('--rr', dest='reroll_nums', type=int, default=[], nargs='*')

    # Weird Options
    parser.add_argument('--botch-anyway', action='store_const', const=True, dest='botch_anyway')

    # Additional Options
    parser.add_argument('--no-sort', action='store_const', const=True, dest='no_sort')


    return parser.parse_args()


def __main__():

    params = get_params()

    roller = Roller(params)
    roller.determine_rolls()
    roller.determine_successes()
    roller.determine_botches()


__main__()