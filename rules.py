
rules = {
    "NN" : {
        "create": {
            "JJ": {
                "NN": "int main(){ \n \n }"
            }
        },
        "print":{
            "NN": "print",
            "JJ": "print"
        }
    },
    "VB" : {
        "create": {
            "JJ": {
                "NN": "int main(){ \n \n }"
            }
        },
    },
    "VBP" : {
        "include": {
            "NN":{
                "NN":{
                    "NN": "-1"
                },
                "NNS": "#include<stdio.h>"
            },
            "JJ":{
                "NN":{
                    "NNS":"#include<stdio.h>",
                    "NN": "#include<stdio.h>"
                }
            }
        }
    }
}