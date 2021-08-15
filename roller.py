import random


class Roller:

    def __init__(self, args):

        self.dice_pool = args.dice_pool
        self.extra_rules = args

        self.rolls = []

        # Rules to be expanded.
        self.reroll_nums = [1]
        self.cascading_nums = [10]
        self.success_nums = [7, 8, 9, 10]
        self.dbl_success_nums = [10]


    '''
    Rolls n dice.
    Returns a single result (1-10) if num_dice=1
    Otherwise returns a list of results.
    '''
    def roll_dice(self, num_dice=1):
        results = ["haven't rolled yet."] * num_dice
        for roll_num in range(len(results)):
            results[roll_num] = random.randrange(10) + 1

        if num_dice == 1:
            print(f'rolled a {results[0]}')
            return results
        else:
            return results


    '''
    Given out dice pool and rules, roll some dice.
    This is currently the only function that gets to roll dice.
    Currently supports:
        reroll_nums
        cascading_nums
    '''
    def determine_rolls(self):
        working_rolls = self.roll_dice(num_dice=self.dice_pool)
        added_rolls = []
        completed_rolls = []

        # As long as we have rolls to parse...
        while working_rolls:

            # Check each roll and apply rules.
            for roll_num in range(len(working_rolls)):
                roll = working_rolls[roll_num]
                
                # Reroll n's.
                while roll in self.reroll_nums:
                    print(f'Rerolling {roll}...')
                    new_roll = self.roll_dice()[0]
                    working_rolls[roll_num] = new_roll
                    roll = new_roll

                # Cascading n's
                if roll in self.cascading_nums:
                    print('Cascade!')
                    new_roll = self.roll_dice()[0]
                    added_rolls.append(new_roll)

            # Transition working rolls to completed, any added rolls become new working rolls.
            completed_rolls += working_rolls
            working_rolls = added_rolls
            added_rolls = []

        # Done.
        self.rolls = completed_rolls
        print(completed_rolls)



    '''
    Given our rolls, determine how many successes were achieved.
    '''
    def deterine_successes(self):
        pass



    '''
    Given our rolls, determine how many botches were achieved.
    '''
    def determine_botches(self):
        pass







