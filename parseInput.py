import nltk
nltk.data.path.append('/home/ganesh/Desktop/FYP/Voice2Code')
from nltk import pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer
from rules import rules

stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()

def inputParseText(inputText):
    #inputText = input("Enter input : ")
    inputText = inputText.lower()

    stopwordFile = open("./stopwords/english")

    stopwords = stopwordFile.read()

    stopwordsList = stopwords.split('\n')

    stopwordFile.close()

    ignoreWordFile = open('ignoreWords.txt')

    ignorewords = ignoreWordFile.read()

    ignorewordsList = ignorewords.split('\n')

    ignoreWordFile.close()

    words = inputText.split()

    stopwordRemovedList = []

    for individualWord in words:
        #print(stemmer.stem(individualWord) + " " + lemmatiser.lemmatize(individualWord,pos="v") +"\n")
        
        if individualWord in ignorewordsList:
            stopwordRemovedList.append(individualWord)
        elif not(individualWord in stopwordsList):
            stopwordRemovedList.append(individualWord)

    print(stopwordRemovedList)

    posTagList = pos_tag(words)

    stopwordRemovedPOSTagList=[]

    for individualWord in stopwordRemovedList:
        for individualPOSTagWord in posTagList:
            if individualPOSTagWord[0] == individualWord:
                stopwordRemovedPOSTagList.append(individualPOSTagWord[1])
                break

    print(stopwordRemovedPOSTagList)


    currentRule = rules[stopwordRemovedPOSTagList[0]]

    currentRule = currentRule[stopwordRemovedList[0]]

    i=1

    while i < len(stopwordRemovedPOSTagList):
        #if(not currentRule[stopwordRemovedPOSTagList[i]]):
        #    break
        currentRule = currentRule[stopwordRemovedPOSTagList[i]]
        if currentRule == "-1" or currentRule == "print":
            break
        i = i + 1

    if currentRule == "-1":
        result = "#include<" + stopwordRemovedList[i-1] +">"
    elif currentRule == "print":
        result = "printf(\""
        i = 1
        while i < len(words):
            result = result + words[i] + " "
            i = i+1
        result = result + "\");\n"
    else:
        result = currentRule


    resultFile = open('intermediate.txt','w')

    resultFile.write(result)

    resultFile.close()

#inputParseText()