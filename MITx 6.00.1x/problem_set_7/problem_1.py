'''To avoid getting an error from the grader about using
the class variables title, subject, or summary, rename any variable you have used with these names to something else.
'''
class NewsStory:

    def __init__(self, guid, title, subject, summary, link):
        self.id = guid
        self.headline = title
        self.about = subject
        self.gist = summary
        self.url = link

    def getGuid(self):
        return self.id

    def getTitle(self):
        return self.headline

    def getSubject(self):
        return self.about

    def getSummary(self):
        return self.gist

    def getLink(self):
        return self.url

x = NewsStory(1,2,3,4,5)

print x
