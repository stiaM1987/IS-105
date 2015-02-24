# Module based on the poker game Five Card Stud.

# poker function takes a list of hands and determines the highest ranked hand.
def poker(hands):
    return max(hands, key=hand_rank)

# hand_rank function takes a hand and returns the hands rank.
def hand_rank(hand):
    ranks = card_ranks(hand)
    # Check if hand has five cards of the same suit in sequence, straight flush.
    if straight(ranks) and flush(hand):
       return (8, max(ranks))
    # Check if hand has four cards of the same rank, four of a kind.
    elif kind(4, ranks):
       return (7, kind(4, ranks), kind(1, ranks))
    # Check if hand has two and three cards of the same rank, full house.
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    # Check if hand includes five cards of the same suit, flush.
    elif flush(hand):
        return (5, ranks)
    # Check if card ranks in hand are in sequence, straight.
    elif straight(ranks):
        return (4, max(ranks))
    # Check if hand has three cards of the same rank, three of a kind.
    elif kind(3, ranks):
        return (3, kinds(3, ranks), ranks)
    # Check if hand has two pairs of cards of the same rank, two pair.
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    # Check if hand has two cards of the same rank, two of a kind.
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    # Check of highest card rank.
    else:
        return (0, ranks)

# card_ranks function takes a hand and returns the rank of each card in that hand.
def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    # To accuratly check for straight, we need to account for a hand that goes
    # from ace to five.
    if ranks == [14,5,4,3,2]:
        return [5,4,3,2,1]
    return ranks

# straight function checks if card ranks are in sequence, returns boolean value.
def straight(ranks):
    prev = ranks[0] - 1 # Keep track of prevois value
    inseq = 0 # Keep track of cards in sequence
    # Iterate over ranks in ranks.
    for r in ranks:
        # Check if card ranks is one higher than the last
        if(r == prev+1):
            inseq += 1
            prev = r
    if inseq == 5:
        return True
    return False

# flush function checks if hand holds five cards of the same suit, returns boolean value.
def flush(hand):
    # Iterate over suits of hand.
    suits= [s for r,s in hand]
        # Checks if suit occurs five times in hand
    if suits.count(s) == 5:
        return True
    return False

def straight_udacity(ranks):
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def flush_udacity(hand):
    suits = [s for r,s in hand]
    return (len(set(suits)) == 1)

# kind function checks if card rank occurs n amount of times.
def kind(n, ranks):
    # Iterate over ranks of hand.
    for r in ranks:
        # Checks if card rank occurs n amount of times
        if ranks.count(r) == n:
            return r
    return None

# two_pair function checks if hand includes two pairs of different ranks.
def two_pair(ranks):
    highpair = kind(2, ranks) # Get highest ranked pair.
    lowpair = kind(2, list(reversed(ranks))) # Get lowest ranked pair.
    # Make sure hand is not four of a kind.
    if highpair != lowpair:
        return (lowpair, highpair)
    return None

# Test function to test poker module.
def test():
    sf = "6C 7C 8C 9C TC".split() # straigh flush
    fk = "9D 9H 9S 9C 7D".split() # four of a kind
    fh = "TD TC TH 7C 7D".split() # full house
    f = "2H 5H 6H 9H 8H".split() # two pair
    s = "1H 2C 3H 4H 5H".split() # A-5 straight
    tp = "5S 5D 9H 9H 6S".split() # two pair
    
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    fhranks = card_ranks(fh)

    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9,5)

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([fh]) == fh
    assert poker([sf] + 99*[fh]) == sf

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)    

    assert card_ranks(sf) == [6, 7, 8, 9, 10]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    
    assert straight([1, 2, 3, 4, 5]) == True
    assert straight([1, 6, 3, 5, 4]) == False

    assert flush(sf) == True
    assert flush(fk) == False 

    print "Tests passed"

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("straight([9, 8, 7, 6, 5])", setup="from __main__ import straight"))
    print(timeit.timeit("straight_udacity([9, 8, 7, 6, 5])", setup="from __main__ import straight_udacity"))
    print(timeit.timeit("flush('6C 7C 8C 9C TC'.split())", setup="from __main__ import flush"))
    print(timeit.timeit("flush_udacity('6C 7C 8C 9C TC'.split())", setup="from __main__ import flush_udacity"))

test()



