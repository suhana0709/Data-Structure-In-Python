#defying a function for word matching
def word_match(words):
    crt = 0 #variable for storing the number of words matched
    lst = [] #list for storing the words matched
    #making the conditions
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            crt+=1
            lst.append(word)
    print("List of words with first and last characters same:-\n", lst)
    return crt
count = word_match(['acaca', 'dad', 'mom', 'gfk', 'pol'])
print("Number of words having first and last characters same: ", count)