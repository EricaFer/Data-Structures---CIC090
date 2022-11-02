'''
Here’s a self check that really covers everything so far. 
You may have heard of the infinite monkey theorem? 
The theorem states that a monkey hitting keys at random on a typewriter keyboard
for an infinite amount of time will almost surely type a given text, 
such as the complete works of William Shakespeare. 
Well, suppose we replace a monkey with a Python function. 
How long do you think it would take for a Python function to generate just one 
sentence of Shakespeare? 
The sentence we’ll shoot for is: “methinks it is like a weasel”

You’re not going to want to run this one in the browser, so fire up your 
favorite Python IDE. 
The way we’ll simulate this is to write a function that generates a string that 
is 27 characters long by choosing random letters from the 26 letters in the 
alphabet plus the space. 

We’ll write another function that will score each 
generated string by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score, 
then if 100% of the letters are correct we are done. 
If the letters are not correct then we will generate a whole new string.
To make it easier to follow your program’s progress this third function should 
print out the best string generated so far and its score every 1000 tries.
'''

import random
import string

goalPhrase = 'methinks it is like a weasel'

def generate_phrase():

    characters = string.ascii_lowercase + ' '
    randomPhrase = ''.join(random.choice(characters) for i in range(27))

    return randomPhrase

def calculate_score(randomPhrase):

    score = 0

    for i,randomLetter in enumerate(randomPhrase):
        if goalPhrase[i] == randomLetter:
            score += 1

    return score

def generate_and_score():

    score = 0
    bestScore = 0
    count = 0

    while score < len(goalPhrase):

        randomPhrase = generate_phrase()
        score = calculate_score(randomPhrase)

        if bestScore < score:
            bestString = randomPhrase
            bestScore = score

        if count%1000 == 0:
            print('The score this iteration was %d' %score)
            print('The best string generated so far was %s with score %d' %(bestString,bestScore))

        count += 1

    print('The infinite monkey finally got the phrase right!')
    print('It only took it %d tries!'%count)

generate_and_score()