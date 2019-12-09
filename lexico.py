# -*- coding: utf-8 -*-

import ply.lex as lex
import os

# resultado del analisis
resultado_lexema = []

reservada = [
    # Palabras Reservadas
    'INCLUDE',
   'CADENA',
    'INT',
    'comentarios'
]
tokns = {
    #Condicionales
    'ari' : 'ARI',
    'wak' : "WAK",
    #Ciclos
    'unay' : 'UNAY',
    'rayku' : 'RAYKU',
    #Mostrar
    'rikuchiy':'RIKUCHIY',
    'tantay':'TANTAY',
    'qupuy' : 'QUPUY',
    #En de rayku
    'pi':'PI',
    #inicio de programa
    'qhapaq':'QHAPAQ',
    'sayarichiy':'SAYARICHIY',
    #entrada
    'yaykuy':'YAYKUY'
}

tokens = reservada + [
    'IDENTIFICADOR',
    'ENTERO',
    'ASIGNAR',

    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',

   'MINUSMINUS',
   'PLUSPLUS',

    #logica
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    # Symbolos
    'NUMERAL',

    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    
    # Otros
    'PUNTOCOMA',
    'COMA',
    'COMDOB',
    'MAYORDER', #>>
    'MAYORIZQ', #<<
    'DPUNTOS',
    'GBAJO',
    'LOGICA',
]
tokens += tokns.values()

# Reglas de Expresiones Regualres para token de Contexto simple

t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
# t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'

t_ASIGNAR = r'='
# Expresiones Logicas
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = ';'
t_COMA = r'\,'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_COMDOB = r'\"'
t_DPUNTOS = r"\:"
t_GBAJO = r'\_'
t_LOGICA= r'(\! | \& | \| )'


def t_IDENTIFICADOR(t):
    r'([jwaeioucchhkllmnñpqrsty])+\d*(\'\w+)*'
    if t.value in tokns:
        t.type = tokns[ t.value ]
    return t

def t_INCLUDE(t):
    r'yaykuchiy'
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
#    r'\"(([aeioucchhkllmnñpqrsty])+ \ *([aeioucchhkllmnñpqrsty])*\d* \ *)\"'
    r'\"(([jwaeioucchhkllmnñpqrsty])+ \ *([jwaeioucchhkllmnñpqrsty])*\d* \ *)\"'
    return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_MAYORDER(t):
    r'<<'
    return t

def t_MAYORIZQ(t):
    r'>>'
    return t

def t_DISTINTO(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_comentarios(t):
     r'\+(\w\d*\s*)+\*+'
     t.lexer.lineno += 1
     print("Comentario en una linea")
     
t_ignore =' \t\n'

def t_error( t):
    global resultado_lexema
    estado = "** Token no valido para el Valor {:16} Posicion {:4}".format( str(t.value),str(t.lexpos))
    #resultado_lexema.append(estado)
    print (estado)
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema
    # instanciamos el analizador lexico
    analizador = lex.lex()
    analizador.input(data)
    #resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        print("|token->",tok.type,", | Valor->",tok.value,"|")
        estado = "|token->",tok.type,", | Valor->",tok.value,"|"
        #print(estado)
    
analizador = lex.lex()
if __name__ == '__main__':
    #name = input("Nombre del Archivo de Codigo : ")
    f = open('code.qch','r+')
    data = f.readlines()
    for res in data:
        prueba(res)
    os.system("pause")
