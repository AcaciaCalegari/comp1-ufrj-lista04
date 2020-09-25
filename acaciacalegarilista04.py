#Lista04
#Acacia Calegari

from math import *

#1-
def SIGA(alune):
    '''Funcao que recebe uma tupla com 4 parametros: o nome do aluno, e 3 notas,
    e retorna uma mensagem com o nome do aluno, a media das 3 notas, e mensagem de aprovado, ou reprovado, se a nota for maio que 7 também retona uma mensagem de parabens
    str,float,float,float -> str'''
    nomealune,p1,p2,p3 = alune
    media = (p1+p2+p3)/3
    if media >= 7.0 :
        return (nomealune, media,"aprovado", "Parabéns!")
    elif media >= 5:
        return (nomealune, media,"aprovado")
    else:
        return (nomealune, media,"reprovado")
    

#2-
def quadrante(angulo,graus):
    '''funcao que recebe 2 paramentros, um para o valor d um angulo, e retorna um inteiro
    entre 1 e 4 representando em qual quadrante do plano cartesiano este angulo
    se encontra, e outro parametro booleano, True para graus, False para radianos 
    float,bool -> int'''
    if graus:
        angulo = angulo % 360
        if angulo <= 90:
            return 1
        if angulo > 90 <= 180:
            return 2
        if angulo > 180 <= 270:
            return 3
        if angulo > 270 <= 360:
            return 4
    else:
        angulo = angulo % (2 * pi)
        if angulo <= pi/2:
            return 1
        if angulo > pi/2 <= pi:
            return 2
        if angulo > pi <= 3*pi/2:
            return 3
        if angulo > 3*pi/2 <= 2*pi:
            return 4
