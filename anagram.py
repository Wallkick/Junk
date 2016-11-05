#anagram solver
#produce a list of possible solutions to an anagram presented.

def getDictionary():
    return [w.lower().rstrip('\n') for w in open('dictfile.txt', 'r')]

def solveSingleWord(anagram):
    ana = sorted(list(anagram.lower()), key=str.lower)
    solutions = []
    for attempt in getDictionary():
        if sorted(list(attempt), key=str.lower) == ana:
            print(attempt)
            solutions.append(attempt)
    return solutions

def solveSingleWordA(anagram):
    # anagram = the current anagram being worked on
    # attempt = the word that is being matched against
    # prog = progress aginst current attempt
    # solutions = list of possible solutions
    solutions = []
    for attempt in getDictionary():
        prog = list(anagram)
        for c in attempt:
            if c in prog:
                del prog[prog.index(c)]
            else:
                break
        if prog == '':
            print(attempt)
            solutions.append(attempt)

def solveMultiWord(anagram):
    pass

if __name__ == '__main__':
    import sys
    solveSingleWord(sys.argv[1])

