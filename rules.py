
rules = {
    "NN" : {
        "create": {
            "JJ": {
                "NN": "int main(){ \n \n }"
            },
            "IN":"conditionalStatements",
            "RB":"conditionalElse",
            "NN":"conditionalIfElse"
        },
        "print":{
            "NN": "printVariable",
            "JJ": "printVariable",
            "VBP": "print",
            "VB": "print",
            "RBR": "print"
        },
        "assign":{
            "NN": "assignVariable",
            "JJ": "assignVariable",
            "VB": "assignVariable",
            "PRP": "assignVariableLatest"
        },
        "return": "returnStatementHandler",
        "math":"expr",
        "condition":"conditionalStatementsCondition",
        "end": "end"
    },
    "VB" : {
        "create": {
            "JJ": {
                "NN": "int main(){ \n "
            },
            "IN":"conditionalStatements",
            "RB":"conditionalElse",
            "NN":"conditionalStatements"
        },
        "declare":{
            "NN": "variableDataType",
            "JJ": "var"
        },
        "input":{
            "JJ": "variableInput",
            "NN": "variableInput"
        },
        "end":"end",
        "initialize": "initializationFor"
    },
    "VBP" : {
        "include": {
            "NN":{
                "NN":{
                    "NN": "-1",
                    "NNS": "-1"
                },
                "NNS": "#include<stdio.h>\n"
            },
            "JJ":{
                "NN":{
                    "NNS":"#include<stdio.h>\n",
                    "NN": "#include<stdio.h>\n"
                }
            }
        }
    },
    "JJ":{
        "increment": "incrementFor"
    }
}