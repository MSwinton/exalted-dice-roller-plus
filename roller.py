import random


class Roller:

    def __init__(self, args):

        self.rules = args

        self.rolls = None
        self.successes = None
        self.botches = None

        # Rules to be expanded.
        self.reroll_nums = [int(num) for num in args.reroll_nums]
        self.cascading_nums = [int(num) for num in args.cascading_nums]

        # Set successes and botch values
        self.set_success_botch_vals()


    '''
    Determines how many successes/botches each number is worth.
    Sets self.success_vals and self.botch_vals
    '''
    def set_success_botch_vals(self):

        # Successes
        base_successes = [int(num) for num in self.rules.base_successes]
        adtl_successes = [int(num) for num in self.rules.adtl_successes]
        success_multipliers = [int(num) for num in self.rules.success_multipliers]
        self.success_vals = [(base_successes[i] + adtl_successes[i]) * success_multipliers[i] for i in range(10)]

        # Successes
        base_botches = [int(num) for num in self.rules.base_botches]
        adtl_botches = [int(num) for num in self.rules.adtl_botches]
        botch_multipliers = [int(num) for num in self.rules.botch_multipliers]
        self.botch_vals = [(base_botches[i] + adtl_botches[i]) * botch_multipliers[i] for i in range(10)]


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
        working_rolls = self.roll_dice(num_dice=self.rules.dice_pool)
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
        if not self.rules.no_sort:
            completed_rolls.sort()
        self.rolls = completed_rolls
        print(completed_rolls)
        print("Total dice rolled:", len(completed_rolls))



    '''
    Given our rolls, determine how many successes were achieved.
    '''
    def determine_successes(self):
        num_of_successes = 0

        for roll in self.rolls:
            num_of_successes += self.success_vals[roll - 1]

        print(num_of_successes, ' successes.')
        self.successes = num_of_successes



    '''
    Given our rolls, determine how many botches were achieved.
    '''
    def determine_botches(self):
        num_of_botches = 0

        if self.successes == 0 or self.rules.botch_anyway:
            for roll in self.rolls:
                num_of_botches += self.botch_vals[roll - 1]


        print(num_of_botches, ' botches.')
        self.botches = num_of_botches







