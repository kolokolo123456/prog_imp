def pgcd(val1,val2):
    while val2!=0:val1,val2=val2,val1%val2
    return val1
    
def main():
    try:
        a=int(input("a="))
        b=int(input("b="))
        if a<=0 or b<=0:raise ValueError()
        print("pgcd(",a,",",b,")=",pgcd(a,b))
    except ValueError:
        print("Les valeurs d'entrée doivent être des entiers naturels non nuls.")     
        
main()       
