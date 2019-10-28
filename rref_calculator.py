#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#This calculator makes any matrix of dimensions n by n+1 into reduced row echelon form. 
#Reduced row echelon form is very useful for solving large systems of equations.
#I used Gauss-Jordan elinination to make this calculator
#Uses NumPy; custom matrix
#Includes step by step instructions
#I have a Java version as well without any matrix library
#Note: The : means all the entries in that dimension. So inputMatrix[3,:] means the third row.
#Created by Hamza Patwa (11th grade)
#Happy reduced row echeloning!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import numpy as np

#Lets the user input the # of rows and makes # columns = # rows +1.
r = int(input("Number of rows: "))
inputMatrix = np.empty ([r, r+1], dtype = 'float')
NUMROWS = np.size(inputMatrix, 0)
NUMCOLS = NUMROWS + 1

#Sets every entry in the array equal to the user input 
for i in range(NUMROWS):
    for j in range(NUMCOLS):
        userInputEntry = input("Enter entry in row {} and column {}: ".format(i, j))
        inputMatrix[i][j] = userInputEntry
        
#Multiplies a row and a scalar
def multiplyRow(multiplier, rowNum):
    inputMatrix[rowNum,:] *= multiplier
    
#Adds two rows and replaces that sum into the row inputed last
def addRows(sourceRow, targetRow):
    inputMatrix[targetRow,:] += inputMatrix[sourceRow,:]

#Checks a certain column if it is in RREF form
def checkValueRREF(row, column):
    #Makes a column matrix equal to the correct RREF form it should be 
    RREFCol = np.empty ([NUMROWS, 1], dtype = 'float')
    #Makes a column matrix equal to the values of inputMatrix in a specific column
    columnMatrix = np.empty ([NUMROWS, 1], dtype = 'float')
    for i in range(NUMROWS):
        columnMatrix[i][0] = inputMatrix[i][column]
        if i == column:
            RREFCol[i][0] = 1
        else:
            RREFCol[i][0] = 0
    if columnMatrix[row][0] == RREFCol[row][0]:
        return True
    else:
        return False

def checkColRREF(column):
    #Makes a column matrix equal to the correct RREF form it should be 
    RREFCol = np.empty ([NUMROWS, 1], dtype = 'float')
    #Makes a column matrix equal to the values of inputMatrix in a specific column
    columnMatrix = np.empty ([NUMROWS, 1], dtype = 'float')
    for i in range(NUMROWS):
        columnMatrix[i][0] = inputMatrix[i][column]
        if i == column:
            RREFCol[i][0] = 1
        else:
            RREFCol[i][0] = 0
    if columnMatrix.all() == RREFCol.all():
        return True
    else:
        return False
    
#Makes an input column into RREF
def RREF (colNum):
    for i in range(NUMCOLS-1):
        #Makes the diagonal entry 1 in that column
        if inputMatrix[colNum][colNum] != 1.0:
            if (np.count_nonzero(inputMatrix[i,:])) == 0:
                return "zerorow"
            #If the diagonal entry is 0
            if inputMatrix[colNum][colNum] == 0:
                for i in range(NUMCOLS-1):
                    #If there is any diagonal entry that isn't 0, add the 0 column and that other column
                    if inputMatrix[i][colNum] != 0:
                        print("Add row {} to row {} and replace it into row {}: ".format(i, colNum, colNum))
                        addRows(i, colNum)
                        print(inputMatrix)
                        break
                if inputMatrix[colNum][colNum] == 0:
                    return "zerocol"
            print ("Divide row {} by {}(beginning): ".format(colNum, inputMatrix[colNum][colNum]))
            multiplyRow(1/inputMatrix[colNum][colNum], colNum)
            print(inputMatrix)
        #The if statement says that if the [colNum][colNum] is not 1 or any other value is not 0, run the RREF code
        if checkValueRREF(i, colNum) == False:
            #Checks if there is a row of zeros
            if (np.count_nonzero(inputMatrix[i,:])) == 0:
                return "zerorow"
            if inputMatrix[colNum][colNum] == -1:
                multiplyRow(-1, colNum)
            #Multiplies the row with a 1 by the negative of the entry you are trying to make 0
            print ("Multiply row {} by {}: ".format(colNum, -inputMatrix[i][colNum]))
            multiplyRow(-inputMatrix[i][colNum], colNum)
            print (inputMatrix)
            #Adds the two rows, making one entry zero
            print ("Add row {} and row {} and replace that into row {}: ".format(i, colNum, i))
            addRows(colNum, i)
            print (inputMatrix)
        #Makes the diagonal entry 1 again
        if inputMatrix[colNum][colNum] != 1.0 and inputMatrix[colNum][colNum] != 0.0:
            if (np.count_nonzero(inputMatrix[i,:])) == 0:
                return "zerorow"
            if ((np.count_nonzero(inputMatrix[i,:])) == 1 and inputMatrix[NUMROWS-1][NUMCOLS-1] != 0):
                return "zerocol"
            print ("Divide row {} by {}(end): ".format(colNum, inputMatrix[colNum][colNum]))
            multiplyRow((1/inputMatrix[colNum][colNum]), colNum)
            print(inputMatrix)
        if i == (NUMCOLS-2):
            return 1
def matrixFunction():
    counter = 97
    for i in range(NUMROWS):
        if (np.count_nonzero(inputMatrix[i,:])) == 0:
            return
        for j in range(NUMCOLS - 1):
            if j != 0:
                print("{0:+}{1} ".format(inputMatrix[i][j], chr(counter)), end = '')
            if j == 0:
                print("{}{} ".format(inputMatrix[i][j], chr(counter)), end = '')
            counter = counter + 1
        print("= {}".format(inputMatrix[i][NUMCOLS-1]))
        counter = 97
def variablesEqual():
    counter = 97
    for i in range(NUMROWS):
        print("{} ≈ {} ".format(chr(counter), round(inputMatrix[i][NUMCOLS-1], 4)))
        counter = counter + 1
    

#Main function where everything is run
def main():
    print("Your Matrix is: \n{}".format(inputMatrix))
    print("This matrix represents the system of equations: ")
    matrixFunction()
    for i in range(NUMCOLS-1):
        ret = RREF(i)
        if ret == "zerorow":
            print("The matrix doesn't have a RREF, since there is a row of all zeros")
            print()
            print("This represents a system of equations with more variables than unknowns: ")
            matrixFunction()
            break
        if ret == "zerocol":
            print("The matrix does not have a RREF, since there is a column of all zeros")
            print()
            print("This represents a system of equations with no solutions: ")
            matrixFunction()
            break
    if ret == 1:
        print("RREF of your Matrix is: \n{}".format(inputMatrix))
        variablesEqual()

#Calls the main function
if __name__ == "__main__":
    main()
