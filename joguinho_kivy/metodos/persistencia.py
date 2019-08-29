#!VENV/bin/python3
# -*- coding: UTF-8 -*-

def salvarArquivo(scores):

    with open("Pontos/salvo.txt", 'w') as arquivo:
        for score in scores:
            arquivo.write(str(score)+" ")

        arquivo.close()

def lerArquivo():
    ponts = []

    try:
        with open("Pontos/salvo.txt", 'r') as arquivo:
            
            for score in arquivo.readline().split(' '):
                if score != " ":
                    ponts.append(score)
        
            arquivo.close()
        
        for i in ponts:
            if i == "":
                ponts.remove(i)

        return ponts
    
    except:pass