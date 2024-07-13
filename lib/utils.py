from sage.combinat.permutation import Permutation


def all_transpositions(n):
    perms = []
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i != j:
                perms.append((i, j))
    return perm


def all_transpositions_of_elements(elements):
    perms = []
    n = len(elements)

    for i in range(n):
        for j in range(i, n):
            if i != j:
                perms.append((elements[i], elements[j]))

    return perms


def all_pairs(list_1, list_2):
    pairs = []
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            pairs.append((list_1[i], list_2[j]))

    return pairs


def compute_valid_perms(elements):
    n = len(elements)
    if n % 2 == 1:
        raise ValueError(
            'Can only compute valid permutations for an even number of elements.')

    # TODO: gotta be a better way of doing this
    evens = []
    odds = []
    for e in elements:
        if e % 2 == 0:
            evens.append(e)
        if e % 2 == 1:
            odds.append(e)

    if len(evens) != len(odds):
        raise ValueError('Number of even and odd elements were different.')

    if n == 2:
        return [[(odds[0], evens[0])]]

    valid_perms = []

    for i, e in enumerate(evens):
        first_perm = (odds[0], e)
        other_odds = odds[1:]
        other_evens = evens[:i] + evens[i+1:]
        other_elements = other_evens + other_odds
        other_perms = compute_valid_perms(other_elements)

        for perm in other_perms:
            valid_perms.append([first_perm]+perm)

    return valid_perms
