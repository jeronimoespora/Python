
def compararListas ( l1 , l2 ):
    if (  len(l1) != len (l2) ):
        return False
    
    else:
        for i in range(1,len(l1)):
            if(l1[i]!=l2[i]):
                return False
    return True

l1=[1,2,3,4,5,6,7,8,9]
l2=[1,2,3,4,5,6,7,8,9]
l3=[3,24,35,46,57,68,79,80,9]

print(compararListas(l1,l3))
