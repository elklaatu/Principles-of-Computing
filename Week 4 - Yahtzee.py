# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    if hand == ():
        return 0
    total = []
    for num_sides in hand:
        total.append(hand.count(num_sides) * num_sides)
                                   
    return max(total)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    
    gen_outcomes = range(1, num_die_sides + 1)
    #generate outcomes list for gen_all_sequence function
    
    all_outcomes = gen_all_sequences(gen_outcomes, num_free_dice)
    #gets set of possible combinations
    
    values = 0.0
    for points in all_outcomes:
        values += score(points + held_dice)   
    
    return values / len(all_outcomes)
    





def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    #hand = (1, 1, 2, 3, 5)
    answer_set = [()]
    for current in hand:
        for sub_set in answer_set:
            answer_set = answer_set + [tuple(sub_set) + (current, )]
          
    return set(answer_set)

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_value = 0
    for held_dice in gen_all_holds(hand):
        value = expected_value(held_dice, num_die_sides, len(hand) - len(held_dice))
        if value > max_value:
            decision = held_dice
            max_value = value
    
    
    return (max_value, decision)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()

#hand = (1, 1, 2, 3, 5)
#print score(hand)
#print len(hand)
#print gen_all_holds(hand)

#print expected_value((1, 2), 6, 3)


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
  