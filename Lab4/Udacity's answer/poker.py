def poker(hands):
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

def hand_rank(hand):
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14,5,4,3,2):
        ranks = (5,4,3,2,1)
    straigh = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return max(count_rankings[counts], 4*straigh + 5*flush), ranks

count_rankings = {(5,):10, (4,1):7, (3, 2):6, (3, 1, 1):3, (2, 2, 1):2,
    (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0}

def group(items):
    groups = [(items.count(x),x) for x in set(items)]
    return sorted(groups, reverse=True)

def unzip(pairs): return zip(*pairs)

