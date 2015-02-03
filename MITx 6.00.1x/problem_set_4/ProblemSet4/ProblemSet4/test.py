hand =  {'h': 1, 'e': 1, 'l': 2, 'o': 1}
hand2 = {'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}
WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def loadWords():

    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    valid = True
    new_hand = hand.copy()
    if word in wordList:
        for letter in word:
            try:
                if letter in new_hand and new_hand[letter] > 0:
                    new_hand[letter] = new_hand[letter] - 1
                    continue
                else:
                    valid = False
            except:
                valid = False
    else:
            valid = False

    return valid

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # Keep track of the total score
    score = 0
    points = getWordScore(word, len(word))

    # As long as there are still letters left in the hand:
    if (len(hand)) > 0:

        # Display the hand
        print displayHand(hand)

        # Ask user for input
        print "Enter word, or a '.' to indicate that you are finished: "
        word = raw_input()

        # If the input is a single period:
        if word == '.' :
            
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not a single period):
        else:

            # If the word is not valid:
            if isValidWord == False:

                # Reject invalid word (print a message followed by a blank line)
                print "Invalid word, please try again."

            # Otherwise (the word is valid):
            else:

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += points
                print '"' + word+'" earned' + points + ' points.  Total: ' + score + 'points'
                print
                # Update the hand
                updateHand(hand, word)


    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if word == '.':
                    print 'Goodbye! Total score: ' + score
    else:
                    print 'Run out of letters. Total score: ' + score + '.'

wordList = loadWords()
playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)

