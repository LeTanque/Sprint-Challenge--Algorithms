'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''



def count_th(word, counter=0):
    # print('word: ', word)
    
    found = word.find("th", 0, len(word))
    if found < 0:
        return counter
    else:
        return count_th(word[found + 2:], counter + 1)
    




# * Your function should take in a signle parameter (a string `word`)
# * Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
# * Your function must utilize recursion. 
#   * It cannot contain any loops.