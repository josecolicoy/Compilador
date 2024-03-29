# -*- coding: utf-8 -*-

import random
import ply.yacc as yacc
from lexico import tokens
from lexico import analizador



# resultado del analisis
resultado_gramatica = []

precedence = (
    ('right','ASIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)
nombres = {}

def p_declaracion_expresion(t):
    'expresion : declaracion'
    t[0] = t[1]

def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNAR expresion'
    nombres[t[1]] = t[3]

def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion
                |   expresion RESTA expresion
                |   expresion MULT expresion
                |   expresion DIV expresion
                |   expresion POTENCIA expresion
                |   expresion MODULO expresion
    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        if p[3] == 0:
            print("No es posible dividir por zero")
        else:
            t[0] = t[1] / t[3]

    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1

def p_expresion_uminus(t):
    'expresion : RESTA expresion %prec UMINUS'
    t[0] = -t[2]

def p_expresion_grupo(t):
    '''
    expresion  :  PARIZQ expresion PARDER
                | LLAIZQ expresion LLADER
                | CORIZQ expresion CORDER
    '''
    t[0] = t[2]
# sintactico de expresiones logicas
def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENORQUE expresion 
                |  expresion MAYORQUE expresion 
                |  expresion MENORIGUAL expresion 
                |   expresion MAYORIGUAL expresion 
                |   expresion IGUAL expresion 
                |   expresion DISTINTO expresion
                |  PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER
                |  PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER
                |  PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER 
                |  PARIZQ  expresion PARDER MAYORIGUAL PARIZQ expresion PARDER
                |  PARIZQ  expresion PARDER IGUAL PARIZQ expresion PARDER
                |  PARIZQ  expresion PARDER DISTINTO PARIZQ expresion PARDER
    '''
    if t[2] == "<": t[0] = t[1] < t[3]
    elif t[2] == ">": t[0] = t[1] > t[3]
    elif t[2] == "<=": t[0] = t[1] <= t[3]
    elif t[2] == ">=": t[0] = t[1] >= t[3]
    elif t[2] == "==": t[0] = t[1] is t[3]
    elif t[2] == "!=": t[0] = t[1] != t[3]
    elif t[3] == "<":
        t[0] = t[2] < t[4]
    elif t[2] == ">":
        t[0] = t[2] > t[4]
    elif t[3] == "<=":
        t[0] = t[2] <= t[4]
    elif t[3] == ">=":
        t[0] = t[2] >= t[4]
    elif t[3] == "==":
        t[0] = t[2] is t[4]
    elif t[3] == "!=":
        t[0] = t[2] != t[4]

    # print('logica ',[x for x in t])

# gramatica de expresiones booleanadas
def p_expresion_booleana(t):
    '''
    expresion   :   expresion AND expresion 
                |   expresion OR expresion 
                |   expresion NOT expresion 
                |  PARIZQ expresion AND expresion PARDER
                |  PARIZQ expresion OR expresion PARDER
                |  PARIZQ expresion NOT expresion PARDER
    '''
    if t[2] == "&&":
        t[0] = t[1] and t[3]
    elif t[2] == "||":
        t[0] = t[1] or t[3]
    elif t[2] == "!":
        t[0] =  t[1] is not t[3]
    elif t[3] == "&&":
        t[0] = t[2] and t[4]
    elif t[3] == "||":
        t[0] = t[2] or t[4]
    elif t[3] == "!":
        t[0] =  t[2] is not t[4]



def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = t[1]

def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido ", t[1])
        t[0] = 0

def p_expresion_mostrar_rikuchiy(t):
    '''
    expresion   :   RIKUCHIY PARIZQ expresion PARDER
                |   RIKUCHIY PARIZQ CADENA CADENA PARDER
                |   RIKUCHIY PARIZQ CADENA SUMA expresion PARDER
    '''
    t[0]=t[3]

def p_expresion_incluir_tantay(t):
    'expresion : TANTAY CADENA'
    t[0]=t[2]

def p_expresion_ciclo_unay(t):
    '''
    expresion : UNAY PARIZQ expresion PARDER LLAIZQ
              | UNAY PARIZQ expresion PARDER
              | UNAY PARIZQ expresion PARDER LLAIZQ expresion LLADER
              | UNAY PARIZQ expresion PARDER LLAIZQ CADENA LLADER
              | UNAY CHIQA LLAIZQ expresion LLADER
              | UNAY CHIQA LLAIZQ
    '''
    if(t[2]) == 'chiqa':
        t[0]=t[2]
    else:
        t[0]=t[3]

def p_expresion_ciclo_rayku(t):
    '''
    expresion : RAYKU IDENTIFICADOR PI expresion LLAIZQ
              | RAYKU IDENTIFICADOR PI expresion
              | RAYKU IDENTIFICADOR PI expresion LLAIZQ expresion LLADER
              | RAYKU IDENTIFICADOR PI expresion LLAIZQ CADENA LLADER
    '''
    t[0]=t[4]


def p_expresion_diccionario(t):
    'expresion : IDENTIFICADOR ASIGNAR LLAIZQ terminologia LLADER'
    nombres[t[1]]=t[4]

def p_expresion_terminologia(t):
    'expresion : terminologia'
    t[0]=t[1]

def p_terminologia_clave(t):
    'terminologia : CADENA DPUNTOS valor'
    t[0]=t[3]

valores = {}
def p_expresion_valor(t):
    '''
    valor : expresion
          | expresion COMA expresion
          | LLAIZQ expresion LLADER
    '''
    if t[1]=='{':
        valores[t[0]]=t[2]
    else:
        valores[t[0]]=t[1]

def p_expresion_arreglo(t):
    'expresion : IDENTIFICADOR ASIGNAR CORIZQ term CORDER'
    t[0]=t[4]

def p_term_expresion(t):
    'term : expresion'
    t[0]=t[1]

def p_expresion_term(t):
    'expresion : expresion COMA term'
    t[0]=t[1]

def p_condicion_ari(t): #condicion if 
    '''
    expresion : ARI PARIZQ expresion PARDER LLAIZQ
              | ARI PARIZQ expresion PARDER LLAIZQ expresion LLADER
    '''
    t[0]=t[3]

def p_condicion_wak(t): #condicion else
    '''
    expresion : WAK PARIZQ expresion PARDER LLAIZQ
              | WAK PARIZQ expresion PARDER LLAIZQ expresion LLADER
    '''
    t[0]=t[3]

def p_comentario(t): #comentarios
    'expresion : NUMERAL expresion'
    t[0]=t[2]

def p_funciones(t):
    'expresion : SAYARICHIY IDENTIFICADOR PARIZQ IDENTIFICADOR PARDER LLAIZQ expresion LLADER' 
    t[0]=t[7] 

def p_expresion_ingreso_yaykut(t):
    '''
    expresion : IDENTIFICADOR ASIGNAR YAYKUY PARIZQ PARDER
    '''
    nombres[t[1]]=input()

def p_expresion_azar_sami(t):
    'expresion : SAMI PARIZQ ENTERO COMA ENTERO PARDER'
    t[0]=random.randint(t[3],t[5])

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)

# instanciamos el analizador sistactico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica = []

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica

if __name__ == '__main__':
        f = open('code_trueque.qch','r+')

        # gram = parser.parse(s)
        # print("Resultado ", gram)

        data = f.readlines()
        for res in data:
            prueba_sintactica(res)
        #os.system("pause")
        #prueba_sintactica(s)

        