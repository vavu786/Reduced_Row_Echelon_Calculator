#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#This calculator makes any matrix of dimensions m by n into reduced row echelon form. 
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
import fractions
import argparse

np.set_printoptions(suppress=True)
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

def parse_args():
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('-rownum', action='store', type=int)
    parser.add_argument('-colnum', action='store', type=int)
    parser.add_argument('-values', action='store', type=float, nargs='+')
    parser.add_argument('-show_equations', action='store_false')
    args = parser.parse_args()
    return args


#Multiplies a row and a scalar
def multiplyRow(multiplier, rowNum):
    if multiplier != 0.0:
        inputMatrix[rowNum,:] *= multiplier
    
#Adds two rows and replaces that sum into the row inputed last
def addRows(sourceRow, targetRow):
    inputMatrix[targetRow,:] += inputMatrix[sourceRow,:]
    
def switchRows(row1, row2):
    tempvar = inputMatrix[row1,:]
    inputMatrix[row1,:] = inputMatrix[row2,:]
    inputMatrix[row2,:] = tempvar

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
    
    
#Makes an input column into RREF
def RREF (colNum):
    for i in range(NUMROWS):
        #Makes the diagonal entry 1 in that column
        if inputMatrix[colNum][colNum] != 1.0 and inputMatrix[colNum][colNum] != 0:
            print ("Divide row {} by {}(beg): ".format(colNum, inputMatrix[colNum][colNum]))
            multiplyRow(1/inputMatrix[colNum][colNum], colNum)
            print(inputMatrix)
        #The if statement says that if the [colNum][colNum] is not 1 or any other value is not 0, run the RREF code
        if checkValueRREF(i, colNum) == False:
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
            print ("Divide row {} by {}(end): ".format(colNum, inputMatrix[colNum][colNum]))
            multiplyRow((1/inputMatrix[colNum][colNum]), colNum)
            print(inputMatrix)
        if i == (NUMROWS-1):
            return 1

def matrixFunction():
    counter = 97
    for i in range(NUMROWS):
        if (np.count_nonzero(inputMatrix[i,:])) == 0:
            return
        for j in range(NUMCOLS - 1):
            if j != 0 :
                if inputMatrix[i][j] != 0:
                    print("{0:+}{1} ".format(inputMatrix[i][j], chr(counter)), end = '')
            if j == 0:
                if inputMatrix[i][j] != 0:
                    print("{}{} ".format(inputMatrix[i][j], chr(counter)), end = '')
            counter = counter + 1
        print("= {}".format(inputMatrix[i][NUMCOLS-1]))
        counter = 97
def variablesEqual():
    counter = 97
    for i in range(NUMROWS):
        print("{} ≈ {} ≈ {}".format(chr(counter), fractions.Fraction(inputMatrix[i][NUMCOLS-1]).limit_denominator(), round(inputMatrix[i][NUMCOLS-1], 4)))
        counter = counter + 1
    
    
#Main function where everything is run
def main():
    global inputMatrix
    global deleted
    global NUMROWS
    global NUMCOLS
    deleted = 0
    args = parse_args()
    listofValues = args.values
    inputMatrix = np.empty([len(args.values)])
    for i in range(len(args.values)):
        inputMatrix[i] = listofValues[i]
    inputMatrix = inputMatrix.reshape(args.rownum, args.colnum)
    NUMROWS = args.rownum
    NUMCOLS = args.colnum
    
    print("Your Matrix is: \n{}".format(inputMatrix))
    print()
    if args.show_equations is not None:
        print("This matrix represents the system of equations: ")
        matrixFunction()
    for i in range(NUMROWS):
        ret = RREF(i)
    if ret == 1:
        print("RREF of your Matrix is: \n{}".format(inputMatrix))
        variablesEqual()

#Calls the main function
if __name__ == "__main__":
    main()
