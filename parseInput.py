import nltk
nltk.data.path.append('/home/ganesh/Desktop/FYP/Voice2Code')
from nltk import pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer
from rules import rules
import time

stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()

def isArray(variableName):
    symbolTableFile = open('./VariableTable.txt',"r")
    content = symbolTableFile.read()
    content = content.split('\n')
    it = 0
    while it < len(content):
        innercontent = content[it].split(' ')
        if(len(innercontent)>1 and innercontent[1] == variableName):
            if(len(innercontent) == 3):
                return True
            else:
                return False
        it = it +1
    symbolTableFile.close()
    return False
def getVariableDataType(variableName):
    symbolTableFile = open("./VariableTable.txt","r")
    content = symbolTableFile.read()
    content = content.split('\n')
    it = 0
    while it < len(content):
        innercontent = content[it].split(' ')
        if(len(innercontent)>1 and innercontent[1]==variableName):
            return innercontent[0]
        it = it + 1
    symbolTableFile.close()
    return "-1"
def replaceText(inputText):
    inputText = inputText.replace('of','[]')
    inputText = inputText.replace('function','')
    inputText = inputText.replace('increment','')
    inputText = inputText.replace('initialize','')
    inputText = inputText.replace('condition','')
    inputText = inputText.replace('math','')
    inputText = inputText.replace('equals','=')
    inputText = inputText.replace('plus','+')
    inputText = inputText.replace('multiplies','*')
    inputText = inputText.replace('minus','-')
    inputText = inputText.replace('divides','/')
    inputText = inputText.replace('by','/')
    inputText = inputText.replace('xor','^')
    inputText = inputText.replace('and','&')
    inputText = inputText.replace('or','|')
    inputText = inputText.replace('percent','%')
    inputText = inputText.replace('less than','<')
    inputText = inputText.replace('greater than','>')
    inputText = inputText.replace('less than or equals','<=')
    inputText = inputText.replace('greater than or equals','>=')
    inputText = inputText.replace('not equals','!=')
    inputText = inputText.replace('zero',"0")
    inputText = inputText.replace('one',"1")
    inputText = inputText.replace('two',"2")
    inputText = inputText.replace('three',"3")
    inputText = inputText.replace('four',"4")
    inputText = inputText.replace('five',"5")
    inputText = inputText.replace('six',"6")
    inputText = inputText.replace('seven',"7")
    inputText = inputText.replace('eight',"8")
    inputText = inputText.replace('nine',"9")
    inputText = inputText.replace('ten',"10")
    inputText = inputText.replace('hundered',"100")
    inputText = inputText.replace('thousand',"1000")
    inputText = inputText.replace('integer','int')
    inputText = inputText.replace('character','char')
    if(inputText.find('[]') != -1):
        inputText  = inputText.strip()
        symbolArray = inputText.split(' ')
        symbolArrayIterator = 0
        while(symbolArrayIterator < len(symbolArray)):
            if(symbolArray[symbolArrayIterator] == "[]"):
                symbolArray[symbolArrayIterator] = "["+symbolArray[symbolArrayIterator+1]+"]"
                del symbolArray[symbolArrayIterator+1]
            symbolArrayIterator +=1
        inputText = ''.join(symbolArray)
    return inputText
def inputParseText(inputText):
    inputText = input("Enter input : ")
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

    if(words[0]=="editor"):
        resultFile = open('intermediate.txt','w')

        resultFile.write(inputText)

        resultFile.close()
        return

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
        if(currentRule == 'expr' or currentRule == "functionCall" or currentRule == "functionParameters" or currentRule == "incrementFor" or currentRule == "initializationFor" or currentRule == "returnStatementHandler" or currentRule == "conditionalStatementsCondition" or currentRule == "conditionalIfElse" or currentRule == "conditionalElse" or currentRule == "end" or currentRule == "conditionalStatements"):
            break
        currentRule = currentRule[stopwordRemovedPOSTagList[i]]
        if currentRule == "-1" or currentRule == "functionCall" or currentRule == "assignVariableLatest" or currentRule == "assignVariable" or currentRule == "printVariable" or currentRule == "variableInput" or currentRule == "print" or currentRule == "var" or currentRule == "variableDataType":
            break
        i = i + 1

    result = ""
    if currentRule == "printVariable" or currentRule == "variableInput":
        j=2
        if words[1]=="break":
            result = "break;\n"
        elif words[j]=="variable":
            j = j+1
            printVariableDataType = getVariableDataType(words[j])
            printVariableArrayStatus = isArray(words[j])
            if(printVariableDataType == "-1"):
                print("Variable not found")
            else:
                if(printVariableDataType == "i"):
                    formatSpecifier = "%d"
                elif(printVariableDataType == "s"):
                    formatSpecifier = "%s"
                elif(printVariableDataType == "f"):
                    formatSpecifier = "%f"
                elif(printVariableDataType == "d"):
                    formatSpecifier = "%lf"
                elif(printVariableDataType == "c"):
                    formatSpecifier = "%c"
                if(currentRule == "variableInput" and printVariableArrayStatus == False):
                    result = "scanf(\"" + formatSpecifier + "\",&" + words[j] +");\n"
                elif(currentRule =="printVariable" and printVariableArrayStatus == False):
                    result = "printf(\"" + formatSpecifier + "\\n\","+words[j]+");\n"
                elif(currentRule == "variableInput" and printVariableArrayStatus == True):
                    if(len(words)<=4):
                        result = "scanf(\"" + formatSpecifier + "\"," + words[j] +"[0]);\n"
                    else:
                        result = "scanf(\"" + formatSpecifier + "\"," + words[j] +"["+words[len(words)-1]+"]);\n"                        
                elif(currentRule == "printVariable" and printVariableArrayStatus == True):
                    if(len(words)<=4):
                        result = "printf(\"" + formatSpecifier + "\\n\","+words[j]+"[0]);\n"
                    else:
                        result = "printf(\"" + formatSpecifier + "\\n\","+words[j]+"["+words[len(words)-1]+"]);\n"
                print(result)
        else:
            currentRule = "print"
    if currentRule == "-1":
        result = "#include<" + stopwordRemovedList[i] +".h>\n"
    elif currentRule == "expr":
        inputText = replaceText(inputText)
        result = inputText + ';\n'
    elif currentRule == "functionParameters":
        latestDeclarationFile = open('./LatestDeclaration.txt',"r")
        content = latestDeclarationFile.read()
        content = content.split(',')
        if(content[0]=="function"):
            functionDetails = open('./FunctionDetails.txt',"a+")
            inputText = replaceText(inputText)
            inputText = inputText.strip()
            words = inputText.split(' ')
            functionDetailsWriteValue = content[1]+","+content[2]+","
            result = content[2] + " " + content[1] + "("
            wordIterator = 1
            while(wordIterator<len(words)):
                result = result + words[wordIterator] +" "
                functionDetailsWriteValue = functionDetailsWriteValue + words[wordIterator]
                result = result + words[wordIterator + 1]
                wordIterator = wordIterator + 2
                if(wordIterator < len(words)):
                    result = result + ","
                    functionDetailsWriteValue = functionDetailsWriteValue +','
            result = result + ") {\n"
            functionDetailsWriteValue = functionDetailsWriteValue + "\n"
            functionDetails.write(functionDetailsWriteValue)
            functionDetails.close()
            latestDeclarationFile = open('./LatestDeclaration.txt',"w")
            latestDeclarationFile.write("")
            latestDeclarationFile.close()
            #prompt parameters
        else:
            functionCallDetailsFile = open('./FunctionCallDetails.txt',"r")
            content = functionCallDetailsFile.read()
            functionCallDetailsFile.close()
            content = content.split(',')
            if(content[0]=="function"):
                inputText = replaceText(inputText)
                inputText = inputText.strip()
                words = inputText.split(' ')
                wordIterator = 1
                result = content[1]+"("
                while(wordIterator < len(words)):
                    result = result + words[wordIterator]
                    wordIterator = wordIterator + 1
                    if(wordIterator < len(words)):
                        result = result + ","
                result = result+");\n"
                if(len(content) > 2):
                    result = content[2] + " = " + result
                functionCallDetailsFile = open('./FunctionCallDetails.txt',"w")
                functionCallDetailsFile.write("")
                functionCallDetailsFile.close()
            else:
                print("INVALID")
            #expecting function here
    elif currentRule == "functionCall":
        assignFunctionCallVariableName = ""
        if(words[1]=="function" or words[2] == "function"):
            if(words[1] == "function"):
                functionCallName = words[2]
            else:
                functionCallName = words[3]
            if(len(words)>4):
                assignFunctionCallVariableName = words[len(words)-1]
            functionCallFile = open('./FunctionCallDetails.txt',"w")
            if(assignFunctionCallVariableName == ""):
                functionCallFile.write("function,"+functionCallName)
            else:
                functionCallFile.write("function,"+functionCallName+","+assignFunctionCallVariableName)
            functionCallFile.close()
            #prompt parameters and return assignment
    elif currentRule == "conditionalStatementsCondition":
        latestDeclarationFile = open('./LatestDeclaration.txt',"r")
        content = latestDeclarationFile.read()
        latestDeclarationFile.close()
        inputText = replaceText(inputText)
        if(content.find("for") == -1):
            content = content.split(' ')
            if(content[0]=="if"):
                result = "if("+ inputText.strip() + '){\n'
            elif(content[0]=="elseif"):
                result = "else if("+ inputText.strip() + '){\n'
            elif(content[0]=="while"):
                result = "while("+inputText.strip()+'){\n'
            else:
                #Prompt "ONLY VALID IN IF"
                print("Not valid")
        else:
            #FOR CONDITION PART
            content = content.split(',')
            latestDeclarationFile = open('./LatestDeclaration.txt','w')
            latestDeclarationFile.write('for,'+content[1]+","+inputText)
            latestDeclarationFile.close()
    elif currentRule == "initializationFor":
        latestDeclarationFile = open('./LatestDeclaration.txt',"r")
        content = latestDeclarationFile.read()
        latestDeclarationFile.close()
        content = content.split(' ')
        inputText = replaceText(inputText)
        if(content[0] == "for"):
            latestDeclarationFile = open('./LatestDeclaration.txt',"w")
            latestDeclarationFile.write("for,"+inputText)
            latestDeclarationFile.close()
        else:
            #Prompt "ONLY VALID IN FOR"
            print("Not Valid")
    elif currentRule == "incrementFor":
        latestDeclarationFile = open('./LatestDeclaration.txt',"r")
        content = latestDeclarationFile.read()
        latestDeclarationFile.close()
        content = content.split(',')
        inputText = replaceText(inputText)
        if(content[0]=="for"):
            latestDeclarationFile = open('./LatestDeclaration.txt',"w")
            latestDeclarationFile.write("")
            latestDeclarationFile.close()
            result = "for("+content[1].strip()+";"+content[2].strip()+";"+inputText.strip()+"){\n"
    elif currentRule == "print":
        result = "printf(\""
        i = 1
        while i < len(words):
            result = result + words[i] + " "
            i = i+1
        result = result + "\");\n"
    elif currentRule == "var":
        symbolTableFile = open("./VariableTable.txt","a+")
        i = 2
        if(words[3]=="array"):
            if(words[2] == "double"):
                result = "double "
                dataType = "d"
                value = words[4]
                size = replaceText(words[len(words)-1])
                result = result + value + "[" + size + "];\n"
        elif(words[i]=="double"):
            result = "double "
            dataType = "d"
            i=4
        else:
            result = "int "
            dataType = "i"
            i=3
        if(words[3]!= "array"):
            while i < len(words):
                result = result + words[i]
                value = words[i]
                i=i+1
            symbolTableFile.write(dataType+" "+value+"\n")
            symbolTableFile.close()
            result += ";"
            result +="\n"
            latestDeclarationFile = open('./LatestDeclaration.txt',"w")
            latestDeclarationFile.write("variable "+value)
            latestDeclarationFile.close()
        else:
            symbolTableFile.write(dataType+" "+value+" "+size+"\n")
            symbolTableFile.close()
    elif currentRule == "variableDataType":
        symbolTableFile = open("./VariableTable.txt","a+")
        i=2
        if(words[3] == "array"):
            if(words[i]=="integer"):
                result = "int "
                dataType = "i"
            elif(words[i] == "float"):
                result = "float "
                dataType = "f"
            elif(words[i] == "character"):
                result = "char "
                dataType = "c"
        elif(words[i] == "integer"):
            result = "int "
            dataType = "i"
            i=i+2
        elif(words[i] == "float"):
            result = "float "
            dataType = "f"
            i=i+2
        elif(words[i] == "character"):
            result = "char "
            dataType = "c"
            i=i+2
        elif(words[i] == "string"):
            result = "string "
            dataType = "s"
            i=i+2
        elif(words[i] == "variable"):
            result = "int "
            dataType = "i"
            i = i+1
        if(words[3]!="array"):
            result = result + words[i] +";\n"
            value = words[i]
            symbolTableFile.write(dataType+" "+value+"\n")
            symbolTableFile.close()
            latestDeclarationFile = open('./LatestDeclaration.txt',"w")
            latestDeclarationFile.write("variable "+value)
            latestDeclarationFile.close()
        else:
            result = result + words[4] + "[" + replaceText(words[len(words)-1]) +"];\n"
            symbolTableFile.write(dataType+" "+words[4]+" "+replaceText(words[len(words)-1])+"\n")
            symbolTableFile.close()

    elif currentRule == "assignVariableLatest":
        latestDeclarationFile = open('./LatestDeclaration.txt',"r")
        content = latestDeclarationFile.read()
        latestDeclarationFile.close()
        content = content.split(' ')
        if content[0] != "variable":
            print("Cannot be resolved,Tell the correct variable")
        else:
            assignVariableName = content[1]
            assignVariableValue = words[3]
            assignVariableDataType = getVariableDataType(assignVariableName)
            if(assignVariableDataType == "i" or assignVariableDataType == "f" or assignVariableDataType == "d"):
                result = assignVariableName + " = " + assignVariableValue +";\n"
            elif(assignVariableDataType == "s"):
                result = assignVariableName + " = \"" + assignVariableValue + "\";\n"
            elif(assignVariableDataType == "c"):
                result = assignVariableName + " = '" + assignVariableValue +"';\n"                
    elif currentRule == "assignVariable":
        variableAlreadyDeclared = False
        assignVariableName = words[2]
        assignVariableValue  = words[4]
        assignVariableDataType = getVariableDataType(words[2])
        symbolTableFile = open("./VariableTable.txt","r")
        content = symbolTableFile.read()
        content = content.split('\n')
        symbolTableFileCounter = 0
        while symbolTableFileCounter < len(content):
            innercontent = content[symbolTableFileCounter].split(' ')
            symbolTableFileCounter = symbolTableFileCounter + 1
            if(len(innercontent)>1 and innercontent[1] == assignVariableName):
                variableAlreadyDeclared = True
                break
        symbolTableFile.close()
        if(variableAlreadyDeclared == True):
            if(assignVariableDataType == "i" or assignVariableDataType == "d" or assignVariableDataType == "f"):
                result = assignVariableName + "=" + assignVariableValue + ";\n"
            elif(assignVariableDataType == "s"):
                result = assignVariableName + "= \"" + assignVariableValue + "\";\n"
            elif(assignVariableDataType == "c"):
                result = assignVariableName + "= '" + assignVariableValue + "';\n"
        else:
            print("Variable not declared")
    elif currentRule == "conditionalStatements":
        if words[2] == "if" or words[1] == "if":
            #promptCondition
            latestDeclarationFile = open('./LatestDeclaration.txt',"w")
            latestDeclarationFile.write("if "+"-1")
            latestDeclarationFile.close()
        elif words[2] == "for" or words[1] == "for":
            #promptCondition
            latestDeclarationFile = open('./LatestDeclaration.txt',"w")
            latestDeclarationFile.write("for")
            latestDeclarationFile.close()
        elif words[2] == "while" or words[1] == "while":
            latestDeclarationFile = open('./LatestDeclaration.txt',"w")
            latestDeclarationFile.write("while "+"-1")
            latestDeclarationFile.close()
        elif words[2] == "function" or words[1] == "function":
            #prompt parameters
            latestDeclarationFile = open("./LatestDeclaration.txt","w")
            if(words[2] == "function"):
                if(len(words)>4):
                    latestDeclarationFile.write("function,"+words[3]+","+replaceText(words[len(words)-1]).strip())
                else:
                    latestDeclarationFile.write("function,"+words[3]+",void")
            else:
                if(len(words)>4):
                    latestDeclarationFile.write("function,"+words[3]+","+replaceText(words[len(words)-1]).strip())
                else:
                    latestDeclarationFile.write("function,"+words[2]+",void")
            latestDeclarationFile.close()
    elif currentRule == "conditionalElse":
        latestDeclarationFile = open('./LatestDeclaration.txt',"w")
        latestDeclarationFile.write("else "+"-1")
        latestDeclarationFile.close()
        result = "else {\n"
    elif currentRule == "conditionalIfElse":
        #prompt condition
        latestDeclarationFile = open('./LatestDeclaration.txt',"w")
        latestDeclarationFile.write("elseif "+"-1")
        latestDeclarationFile.close()
    elif currentRule == "end":
        result = "}\n"
    elif currentRule == "returnStatementHandler":
        inputText = replaceText(inputText).strip()
        result = inputText + ";\n"
    else:
        if(currentRule != "printVariable" and currentRule != "variableInput"):
            result = currentRule


    resultFile = open('intermediate.txt','w')

    resultFile.write(result)

    resultFile.close()

    if(currentRule == "end"):
        time.sleep(1.1)
        resultFile = open('intermediate.txt','w')
        resultFile.write("")
        resultFile.close()

inputParseText("")