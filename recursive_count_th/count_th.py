'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if word.find("th") == -1:#Base Case: we stop when there's no more "th", .find() returns -1
        return 0
    else:
        first_th_index = word.find("th") #Find the index of first occurence of 'th'

        #Create new word minus everything including the first "th" and what came before first "th"
        new_word = word[first_th_index+2:] 
        return 1 + count_th(new_word) #  1 for the first "th" found, and recursive call for the remaining

