#!/usr/bin/python

import sys

def suma(Val1, Val2):
    print float(Val1) + int(Val2)
def resta(Val1, Val2): 
    print float(Val1) - int(Val2)
def mult(Val1, Val2):
    print float(Val1) * int (Val2)
def div(Val1, Val2):
    if int(Val2) == 0:
        print "NO SE PUEDE DIVIDIR ENTRE 0"
    else:
        print float(Val1) / int(Val2)

if __name__ == "__main__":
    try:
        if sys.argv[1] == "Sumar":
            suma(sys.argv[2], sys.argv[3])
        if sys.argv[1] == "Restar":
            resta(sys.argv[2], sys.argv[3])
        if sys.argv[1] == "Multiplicar":
            mult(sys.argv[2], sys.argv[3])
        if sys.argv[1] == "Dividir":
            div(sys.argv[2], sys.argv[3])
    except ValueError:
        print("Uno de los valores no es un numero")
    except IndexError:
        print("Falta al menos uno de los valores")
    
