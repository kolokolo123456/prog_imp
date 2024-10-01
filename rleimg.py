#!/usr/bin/env python3

import sys

def compression(file):
    l1=file.readline()[:2]
    if l1!="P1":raise SyntaxError("Fichier non valide.")
    l2=file.readline().split(" ")
    largeur,hauteur=int(l2[0]),int(l2[1])
    data=str(largeur)+' '+str(hauteur)+"\n"
    p,act,longueur_file_source,sum_longueur_lignes=0,'0',0,0
    while True:
        li=file.readline()
        if li=='':
            sum_longueur_lignes+=p
            data+=str(p)
            break
        for ch in li:
            if ch=='\n':break
            longueur_file_source+=1
            if p==0:
                p,act=1,ch
            else:
                if ch==act:p+=1
                else:
                    sum_longueur_lignes+=p
                    data+=str(p)+'\n'
                    p,act=1,ch               
    if longueur_file_source!=largeur*hauteur:raise ValueError("longueur_file_source!=largeur*hauteur.")
    if longueur_file_source!=sum_longueur_lignes:raise ValueError("longueur_file_source!=sum_longueur_lignes.(nb répétitions)")
    print(data)

def decompression(file):
    data='P1\n'+file.readline()
    flag,p=0,0
    while True:
        line=file.readline()
        if line=='':break
        li=int(line)
        while li>=70:
            data+=str(flag)*(70-p)+'\n'
            li-=70-p
            p=0
        if p+li<=70:    
            data+=str(flag)*li
            p+=li
        else:
            data+=str(flag)*(70-p)+"\n"+str(flag)*(p+li-70) 
            p+=li-70
        flag=(flag+1)%2  
    print(data)    
          

def main():
    mode=sys.argv[1]
    if mode not in ("-c","-d"):raise SyntaxError("Argument d'utilisation non déclaré.")
    if len(sys.argv)<3:raise SyntaxError("Fichier non défini.")
    file=open(sys.argv[2],'r')
    if mode=="-c":compression(file)
    if mode=="-d":decompression(file)
    file.close()
main()    