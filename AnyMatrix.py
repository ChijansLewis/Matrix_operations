import numpy as np
import sys
from fractions import Fraction as fn
# 设置矩阵输出用分数形式
np.set_printoptions(formatter={'all':lambda x:str(fn(x).limit_denominator())})

global a,b
a=np.array([
            [9,2,3],
            [2,3,4],
            [0,1,1]
                    ])

b=np.array([[9,2,3],
           [2,3,4],
           [0,1,1]])

global row_a,row_b,col_a,clo_b


def multi_(a,b):
    global mul_a_b
    mul_a_b=np.dot(a,b)

def transposition(a):
    global tsp_a_b
    tsp_a_b=a.T

def det(a):
    global det
    det=np.linalg.det(a)

def inverse(a):
    global inv_M
    inv_M =np.linalg.inv(a)

def adjoint(a):
    global ad 
    det(a)
    inverse(a)
    ad =det*inv_M


def main():
    if sys.argv[1]=="multi":
        multi_(a,b)
        print(mul_a_b)
    elif sys.argv[1]=="transposition":
        transposition(a)
        print(tsp_a_b)
    elif sys.argv[1]=="det":
        det(a)
        print(det)
    elif sys.argv[1]=="inv":
        if det(a)==0:
            print("det(a)==0")
        else:
            inverse(a)
            print(inv_M)
    elif sys.argv[1]=="adjoint":
        adjoint(a)
        print(ad)
    
if __name__=="__main__":
    try:
        main()
    except :
        print('\033[37;41m',"Please check matrixes you have input again,repython it.",end="")
        print('\033[0m',end="")
    sys.exit(0)


