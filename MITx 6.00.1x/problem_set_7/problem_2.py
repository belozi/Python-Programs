'''
To avoid getting an error from the grader about using the class variables title,
subject, or summary, rename any variable you have used with these names to something else. 
'''

import string

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError
    
#Problem 2

class WordTrigger(Trigger):

    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        erase = set(string.punctuation)
        clean = []
        for char in text:

            if char in erase:
                clean.append(' ')
            else:
                clean.append(char)
        data = ''.join(clean)
        print data
        zzz = data.find(self.word)
        if zzz == -1:
            return False
        else:
            return True
        
               
#Problem 3

class TitleTrigger(WordTrigger):

    x = WordTrigger(self.word)

'''

#Problem 4

class SubjectTrigger(WordTrigger):

    super(WordTrigger.isWordIn(self.getSubject())).__init__()


#Problem 5

class SummaryTrigger(WordTrigger):

    super(WordTrigger.isWordIn(self.getSummary())).__init__()
'''

