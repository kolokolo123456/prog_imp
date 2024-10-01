def fact(val):
    if val==0:return 1
    out=1
    while val>0:
        out*=val
        val-=1
    return out
    
def main():
    try:
        n=int(input("n="))
        if n<0:raise ValueError()
        print("n!=",fact(n))
    except ValueError:
        print("n doit être un entier naturel.")     
        
main()   
