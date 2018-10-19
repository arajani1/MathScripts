import math

#prints out instructions to make program easier to run
def manual():
    print("Use parentheses to make propositions as clear as possible")
    print("Use ¬ as a 'not' operation")
    print("Use ∧ between two propositions as an 'and' operation")
    print("Use v between two propositions as an 'or' operation")
    print("Use → between a hypothesis and a conclusion to form a conditional proposition")
    print("Use ↔ between two propositions for use as a biconditional operation")
    

#calls methods to actually build table
def tablecreator():
    proposition = input("Enter in a proposition: ")
    columns, variables = tablesetup(proposition)
    tablebuild(columns, variables)

#simplifies proposition
def simplification1():
    proposition = input("Enter in a proposition: ")
    



#whgen calles prints out table with True and False values for proposition
def tablebuild(columns, variables):
    variablecount = len(variables)
    rowcount = 2**variablecount
    columncount = len(columns)
    rowcounter = 0
    rowcounter2 = 0
    columncounter = 0
    variablecounter = 0
    check = False
    vswitch = 0
    blank = ""
    true = "T"
    false = "F"
    variableboolean = "T"
    boolls = []
    curvariables = []
    answer = ""
    for row in range(rowcount+1):
        rowcounter += 1
        for col in columns:
            if len(col) == 1:
                variablecounter += 1
                boolls = vboolean(variablecount,variablecounter)
                curvariables.append(boolls[rowcounter-2])
            columncounter += 1
            if rowcounter == 1:
                print('%15s'%col+"\t|",end = "")
            else:
                if len(col) == 1:
                    #boolls changes to array of T 
                    print("%15s"%(boolls[(rowcounter-2)])+"\t|",end = "")
                elif columncounter > variablecounter:
                    answer = propevaluator(curvariables, col,variables)
                    print("%15s"%answer+"\t|",end = "")
                else:
                    print("%15s"%blank+"\t|",end = "")
        curvariables.clear()
        variableboolean = "T"
        vswitch = 0
        columncounter = 0
        variablecounter = 0
        print('')


#fully evaluates phrases or propositions
def propevaluator(curvariables,proposition, variables):
    varkey = {}
    count = 0
    for var in variables:
        if curvariables[count] == "T":
            curvariables[count] = "<"
        elif curvariables[count] == "F":
            curvariables[count] = ">"
        varkey[var] = curvariables[count]
        count += 1
    #print(proposition,end = "")
    for char in proposition:
        for key in varkey:
            if char == key:
                proposition = proposition.replace(char,str(varkey[key]))
    proposition = proposition.replace("v","or")
    proposition = proposition.replace("∧","and")
    proposition = proposition.replace("<","True")
    proposition = proposition.replace(">","False")
    proposition = proposition.replace("↔","==")
    proposition = proposition.replace("¬True","False")
    proposition = proposition.replace("¬False","True")
    proposition = proposition.replace("(True and True)","True")
    proposition = proposition.replace("(True and False)","False")
    proposition = proposition.replace("(False and True)","False")
    proposition = proposition.replace("(False and False)","False")
    proposition = proposition.replace("(True or True)","True")
    proposition = proposition.replace("(True or False)","True")
    proposition = proposition.replace("(False or True)","True")
    proposition = proposition.replace("(False or False)","False")
    proposition = proposition.replace("True → True","True")
    proposition = proposition.replace("True → False","False")
    proposition = proposition.replace(" True → False","False")
    proposition = proposition.replace("True → False ","False")
    proposition = proposition.replace("False → True","True")
    proposition = proposition.replace("False → False","True")
    proposition = proposition.replace("↔","==")
    solution = eval(proposition)
    return solution


    
#returns array of true and false values for column using formula A(x,y) = 2**(x-y)
def vboolean(totalvariables,currentcolumn):
    rowcount = 2**totalvariables
    boollist = []
    variableboolean = "T"
    colcount = 0
    rowcounter = 0
    alternation = 2**(totalvariables - currentcolumn)
    for row in range(rowcount):
        rowcounter +=1
        boollist.append(variableboolean)
        if rowcounter == alternation:
            if variableboolean == "T":
                variableboolean = "F"
            else:
                variableboolean = "T"
            rowcounter = 0
    return (boollist)


 
#takes user input and returns variables and table headers for truth table
def tablesetup(proposition):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVXYZabcdefghiklmnopqrstuxwyz v∧¬→↔'
    check = False
    check2 = False
    check3 = False
    column = []
    phrases = []
    variables = []
    deleted = []
    phrase = ""
    for char in proposition:
        for letter in alphabet:
            if char == letter and char != ' ' and char != 'v' and char != '∧' and char != '¬' and char != '→' and char != '↔':
                column.append(letter)
                variables.append(letter)
                deleted.append(letter)
                alphabet = alphabet.replace(letter, '')
            if char == "(":
                check = True
                break
            if char == ")" and check == True:
                check = False
                phrases.append(phrase)
                phrase = ""
                break
            if check == True:
                if check3 == False:
                    for val in deleted:
                        if char == val:
                            check2 = True
                            check3 = True
                if char == letter or check2 == True:
                    phrase += char
                    check2 = False
        check3 = False
    for par in phrases:
        column.append(par)
    column.append(proposition)
    rowcount = 2**len(variables)
    return column, variables



print("Type and enter in the number of the function you would like to apply:")
print("\t0. Manual")
print("\t1. Draw table of all combinations for proposition")


functionchoice = input()


while functionchoice.isdigit() == False:
    print("Please just type in the number of your function of choice: ")
    functionchoice = input()

if functionchoice.isdigit():
    functionchoice = int(functionchoice)

if functionchoice == 0:
    manual()
elif functionchoice == 1:
    tablecreator()
    


