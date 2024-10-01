une_chaine = "123"
une_list = [1, 2, 3]
un_tuple = (1, 2, 3)
un_tuple_2D = ([1, 2, 3], [4, 5, 6])
une_list_3D = [[[1, 2], [3, 4]], [[5, 6]]]

def iter(L):
    c=0
    while c<len(L):
        if type(L[c]) in (list,tuple) or (type(L[c])==str and len(L[c])>1):iter(L[c])
        else: 
            print(L[c])
        c+=1

print("Éléments de une_chaine :")
iter(une_chaine)

print("Éléments de une_list :")
iter(une_list)

print("Éléments de un_tuple :")
iter(un_tuple)

print("Éléments de un_tuple_2D :")
iter(un_tuple_2D) 
 
print("Éléments de une_list_3D :")
iter(une_list_3D)                  
