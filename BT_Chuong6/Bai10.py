from random import randrange

def nhapMaTran(n, m):
    return [[randrange(-99, 100) for i in range(m)] for i in range(n)]

def congMaTran(A, B):
    if(len(A) != len(B) or len(A[0]) != len(B[0])):
        print("Ma tran khong hop le!")
        return []
    return [[a + b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]

A = nhapMaTran(3, 4)
B = nhapMaTran(3, 4)
print("Ma tran A: ", *A, sep='\n')
print("Ma tran B: ", *B, sep='\n')
AB = congMaTran(A, B)
print("Ma tran A + B =", *AB, sep='\n')
