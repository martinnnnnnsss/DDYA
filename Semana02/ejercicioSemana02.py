def insertsort(L):

    for j in range ( 1, len (L)):
        key = L [j]
        i = j - 1
        while i  >= 0 and L[i] < key:
            L[i + 1] = L[i]
            i = i - 1 
        L[i + 1] = key
    return L

def main():

    L = [5, 9, 3, 7, 1, 8, 2, 4, 6, 10]
    print (insertsort(L))
    
main () 
