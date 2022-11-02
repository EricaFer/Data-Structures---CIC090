'''
See if you can improve upon the program in the self check by keeping letters 
that are correct and only modifying one character in the best string so far. 

This is a type of algorithm in the class of ‘hill climbing’ algorithms, 
that is we only keep the result if it is better than the previous one.

RESULT: The infinite monkey finally got the phrase right!
It only took it 403 tries!
'''

import random
import string

goalPhrase = 'methinks it is like a weasel'

def generate_random(lengthRandom):

    characters = string.ascii_lowercase + ' '
    randomBit = ''.join(random.choice(characters) for _ in range(lengthRandom))

    return randomBit

def calculate_score(randomPhrase):

    score = 0

    for i,goalLetter in enumerate(goalPhrase):
        if randomPhrase[i] == goalLetter:
            score += 1

    return score

def generate_and_score():

    score = 0
    bestScore = 0
    count = 0

    randomPhrase = generate_random(lengthRandom=len(goalPhrase))

    while score < len(goalPhrase):

        for i,goalLetter in enumerate(goalPhrase):
            while randomPhrase[i] != goalLetter:

                randomPhrase = randomPhrase[:i] + generate_random(1) + randomPhrase[i+1:]
                count += 1

            score = calculate_score(randomPhrase)

            if bestScore < score:
                bestString = randomPhrase
                bestScore = score

            if count%1000 == 0:
                print('The score this iteration was %d' %score)
                print('The best string generated so far was %s' %bestString)


    print('The infinite monkey finally got the phrase right!')
    print('It only took it %d tries!'%count)

generate_and_score()

