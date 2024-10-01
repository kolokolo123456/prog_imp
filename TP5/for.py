une_chaine = "123"
une_list = [1, 2, 3]
un_tuple = (1, 2, 3)
un_intervalle = range(1, 4)
une_list_2D = ["toto", range(3), ["t", "o", "t", "o"]]
un_tuple_2D = ([1, 2, 3], [4, 5, 6])
une_list_3D = [[[1, 2], [3, 4]], [[5, 6]]]


def iter(L):
    for i in L:
        if type(i) in (list,tuple) or (type(i)==str and len(i)>1):iter(i)
        else: 
            print(i)
            
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
    
