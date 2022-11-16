# A trie data tree in Python is really just a dictionary with nested dictionaries inside it witch are the tree branches.
# Using a variable 'cur', witch is our "current node", cur can be set equal to dictionary d. Making changes to 'cur' will also change dictionary d.
# So now "cur" can be set equal to nested parts of d to make changes in that part of d at any time.
# We dont need to create a class to do this. Just three simple functions - insert, search, and erase.

d = {}                       # We start with empty dictionary d


def insert_tree(word):
    print('inserting', word)
    cur = d                   # We set cur equal to d, so now we can use cur as a tool to move around in the dictionary
                              # and make changes inside. So right now cur is an empty dictionary like d.

    for l in word:

        if l in cur:         # If the letter is already present in cur then we set cur equal to that letter.
            cur = cur[l]     # This brings cur down a nested level in the dictionary witch is a branch in the tree

        if l not in cur:      #  if the letter is not in cur then we insert it as a new entry into cur (and d) with another
                              # empty dictionary as its value so we can then insert more letters under it.
            cur[l] = {}

            cur = cur[l]      # As before we now set value of cur equal to the letter we just put inside itself. This is how we
                              # go down one level into the nested dictionary to insert more letters

            print(d)          # We will print out d as it was updated by cur.


insert_tree('apply')          # We now call our insert function and load up the dictionary with words.
insert_tree('play')           # Feel free to change the words and watch the dictionary load up.
insert_tree('apple')
insert_tree('pliers')


def search_tree(word):             # the search function is almost the same as insert, except if letter
                                   # is not there we don't insert anything. We just break out of it and print word not found.
    print('searching for', word)
    cur = d                        # We always reset cur back to the main dictionary before we start the function.
                                   # That gets cur out of any nested parts it was in before

    for l in word:
        if l not in cur:
            print(word, 'not found')
            break

        if l in cur:                # if letter in word is found, then we go another level deeper into the nested dictionary to check
            cur = cur[l]            # the next letter down, again by setting cur equal to cur l witch is the key of the nested dict
            print(l, 'found')


search_tree('apply')
search_tree('apple')              # you will notice that the search finds 'apply' but then does not find 'apples'. This is because
                                   # cur goes down the branch of "apply" but then doesn't come back out to the main dictionary
                                   # to search elsewhere for 'apple', so this has to be fixed to handle these cases
search_tree('play')
search_tree('ape')


def erase_tree(word):     # To erase a word from the tree we have to find it first, so the first part of this function
                          # is the same as the search function above

    cur = d
    print('erasing', word)

    i = 0                 # i is an integer letter counter used to find a specific letter in word.  Word is
                          # actually an array in python that can be number indexed. I tried just using 'l' but its string not int.
    for l in word:

        i = i + 1

        if l not in cur:   # If the first letter in word is not present then we already know its not in the tree so break
            print(word, 'not present')
            break

        if l in cur:
            cur = cur[l]        # If letter is in cur then we go down a level as before

            if len(cur) <= 1:   # if the length of cur is 1 or less then we know there are no other branches
                                # that can be lost when we delete. So this is a good place to cut it.
                                # however it might leave a letter or two hanging in the dictionary

                print(l, 'found,', 'cur dict is',cur, 'lenght is', len(cur), 'so deleting')

                del cur[word[i]]     # So now we delete the letter in word of counter i, and all nested dictionaries below it a erased


erase_tree('play')
print('present dictionary',d)



