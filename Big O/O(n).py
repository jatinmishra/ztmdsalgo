import timeit

wordList = ['dory', 'bruce', 'marlin', 'gill', 'bloat', 'nigel', 'squirt', 'nemo']
largeList = ['darla' for i in range(100000)]
# O(n) -> takes linear number of steps i.e takes 10 steps to find in list of 10 items, 1000 steps in list of 1000, etc.
def findNemo(wordList):
    begin = timeit.default_timer()
    for item in wordList:
        if item == 'nemo':
            print('Found Nemo!!')
    print(f"Time took to find nemo = {timeit.default_timer() - begin}")

findNemo(wordList)
findNemo(largeList)


