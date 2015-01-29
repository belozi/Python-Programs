animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    if aDict == {}:
        return None
    most = aDict.keys()[0]
    for key in aDict:
        if len(aDict[key]) >= (len(aDict[most])):
            most = key
    return most


print biggest({'M': []})
print biggest({'a': [18, 12, 9, 19, 18, 2, 7, 1, 9, 1], 'c': [7, 16, 18, 5, 1], 'b': [20, 15], 'e': [16, 5, 10], 'd': [1, 9, 19, 6, 10, 13, 19, 8, 4]})
print biggest({})
