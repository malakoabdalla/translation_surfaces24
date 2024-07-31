from sage.combinat.permutation import Permutation #, SymmetricGroup
from sage.all import SymmetricGroup


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

##this is an example of a for loop that goes through a list of numbers 
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

    for i, e in enumerate(evens): #enumerate gives you both the element and the index 
        first_perm = (odds[0], e)
        other_odds = odds[1:]
        other_evens = evens[:i] + evens[i+1:]
        other_elements = other_evens + other_odds
        other_perms = compute_valid_perms(other_elements)

        for perm in other_perms:
            valid_perms.append([first_perm]+perm)

    return valid_perms

# pair is a list of tuples
# want to convert it to a Permutation type from the sage SymmetricGroup library
# e.g. pair = [[(1,2),(3,4)], [(1,3), (2,4)]]
# return (Permutation('(12)(34)'), Permutation('(14)(23)))
def convert_pair(n, pair):
    Sn = SymmetricGroup(n)
    top = Sn(pair[0])
    bottom = Sn(pair[1])
    return (top,bottom)



# we dont want there to be the same pairings ie cannot have T and B (14) and (14), dont wanna include 
#goal is to output a list of pairs of permutations 
#two permutations create a pair and check if they share any permutations, if they do share discard, dont.. keep
def compute_valid_pairs(n, valid_perms):
    valid_pairings= []
    for i,v in enumerate(valid_perms):
        for j,w in enumerate(valid_perms):
            first_pair=(v,w)
            # print(f"v is {v}") #this is to check whats going on in the for loop. f is a formatted print combines text w variable v 
            # print(f"w is {w}")
            #enumerate for index and element of list
            if check_if_perms_share_transposition(v,w):
                # print("they're equal")
                continue #use continue to say "dont include"
            if j< i: 
                continue 
            else : 
                # print(f"they're not equal, appending: {first_pair}")
                pair = convert_pair(n, first_pair)
                valid_pairings.append(pair)

    return valid_pairings

def check_if_perms_share_transposition(perm1, perm2):
    # e.g. perm1 = [(1, 2), (3, 4), (5, 6)]
    #      perm2 = [(1, 4), (3, 2), (5, 6)]

    for t1 in perm1:
        for t2 in perm2:
            if t1== t2 :
                return True
    
    return False 
        

# This function takes in two inputs:
# - n which is the number of dots (permutation group)
# - bottom which is the bottom permutation 
# It returns a permutation which is the shift of bottom

def shift_bottom(n, bottom):
    Sn = SymmetricGroup(n)
    s=''
    for i in range(1,n+1):    
        if i==1:
            s=s+'(1,'
        elif i<n : 
            s=s+ f'{n-i+2},'
        if i==n:
            s=s+ '2)'
      
    si= ''
    for i in range(1,n+1):
        if i==1:
            si= si+'(1,'
        elif i<n:
            si= si+ f'{i},'
        if i==n:
            si= si+ f'{n})'
   
    s = Sn(s)
    si = Sn(si)
    new = s*bottom*si # TODO: is this correct? ... i believe it is 
    return new