#!/usr/bin/env python3

voy="aeyuioéèàôù"
ct=0
NBR=int(input("Entrer le nombre maximal de voyelles:\n"))
ph=input("Entrer la phrase à analyser:")
for ch in ph:
    print(ch)
    if ch in voy:
        ct+=1
        print("Voyelle :",ch,"(",ct,"/",NBR,")")
        if ct==NBR:break
