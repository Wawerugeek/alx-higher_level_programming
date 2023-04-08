#!/usr/bin/python3
"""text-indenttion function"""

def text_indentation(text):
    """
    its mandatory a text be a string
    No blank space at the beggining
    no blank space at the end of line
    raises ty[eERROR
    """
    
    element = 0
    
    while element < len(text) and text[element] == ' ':
        element += 1

    while element < len(text):
        print(text[element], end="")
        if text[element] in ".?:":
            print("\n")
        element += 1

        while element < len(text) and text[element] == ' ':
            element += 1
            continue
        element += 1
