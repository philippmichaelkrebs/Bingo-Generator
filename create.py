'''Creates Bingo Fields'''
import random
import math
import sys

words = []

# read words
with open("wordlist.txt", "r",encoding='utf8') as file:
    for line in file:
        if len(line) > 0:
            words.append(line.replace('\r', '').replace('\n', ''))


def permutate() -> list[int]:
    '''creates permutation for given words as indexes'''
    permutation = []

    # fill permutation list with indexes to words
    while len(permutation) < 16:
        new_random = math.floor(random.random()*len(words))
        if new_random not in permutation:
            permutation.append(new_random)

    return permutation

def create_bingo_card() -> list[str]:
    '''creates permutation for given words'''
    permutation = permutate()
    bingo_card = []
    for word_index in permutation:
        bingo_card.append(words[word_index])
    return bingo_card

def list_to_csv(data:list[str], sep=';') -> str:
    '''generates the bingo csv string'''
    csv_string = ""
    counter = 0
    for word in data:
        if len(csv_string) == 0:
            csv_string = csv_string + word
        elif counter % 4 == 0:
            csv_string = csv_string + "\n" + word
        else:
            csv_string = csv_string + f"{sep}" + word
        counter += 1
    return csv_string

if "__main__":

    iterations = 32
    seperator = ';'

    if len(sys.argv) > 1:
        iterations = int(sys.argv[1])
    if len(sys.argv) > 2:
        seperator = str(sys.argv[2])

    for i in range(iterations):
        field = create_bingo_card()
        print(list_to_csv(field,seperator))
        print('')
