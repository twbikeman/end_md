

def loadDataSet():
    postingList=[['my', 'dog', 'has','flea','problem','help','please'],
                ['my', 'dog', 'has','flea','problem','help','please'],
                ['my', 'dog', 'has','flea','problem','help','please'],
                ['my', 'dog', 'has','flea','problem','help','please'],
                ['my', 'dog', 'has','flea','problem','help','please'],
                ['my', 'dog', 'has','flea','problem','help','please'],
                ['my', 'dog', 'has','flea','problem','help','please']]
    classVec = [0,1,0,1,0,1] #1 is abusive, 0 not
    return postingList, classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    returnVect = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print("the word: {} is not in my Vocabulary!".format(word))
    return returnVec

