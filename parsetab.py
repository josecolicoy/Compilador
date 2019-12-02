
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNARleftSUMARESTAleftMULTDIVrightUMINUSAND ARI ASIGNAR CADENA COMA COMDOB CORDER CORIZQ DISTINTO DIV DPUNTOS ENTERO GBAJO IDENTIFICADOR IGUAL INCLUDE INT LLADER LLAIZQ LOGICA MAYORDER MAYORIGUAL MAYORIZQ MAYORQUE MENORIGUAL MENORQUE MINUSMINUS MODULO MULT NOT NUMERAL OR PARDER PARIZQ PLUSPLUS POTENCIA PUNTOCOMA QUPUY RAYKU RESTA RIKUCHIY SUMA TANTAY UNAY WAK comentariosdeclaracion : IDENTIFICADOR ASIGNAR expresiondeclaracion : expresionexpresion : RESTA expresion %prec UMINUS\n    expresion  : PARIZQ expresion PARDER\n                | LLAIZQ expresion LLADER\n                | CORIZQ expresion CORDER\n    \n    expresion   :  expresion MENORQUE expresion \n                |  expresion MAYORQUE expresion \n                |  expresion MENORIGUAL expresion \n                |   expresion MAYORIGUAL expresion \n                |   expresion IGUAL expresion \n                |   expresion DISTINTO expresion\n                |  PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER \n                |  PARIZQ  expresion PARDER MAYORIGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER IGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER DISTINTO PARIZQ expresion PARDER\n    \n    expresion   :   expresion AND expresion \n                |   expresion OR expresion \n                |   expresion NOT expresion \n                |  PARIZQ expresion AND expresion PARDER\n                |  PARIZQ expresion OR expresion PARDER\n                |  PARIZQ expresion NOT expresion PARDER\n    expresion : ENTEROexpresion : COMDOB expresion COMDOBexpresion : IDENTIFICADOR'
    
_lr_action_items = {'IDENTIFICADOR':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,37,38,39,52,53,54,55,56,57,],[2,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'RESTA':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,37,38,39,52,53,54,55,56,57,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'PARIZQ':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,37,38,39,43,44,45,46,47,48,52,53,54,55,56,57,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,52,53,54,55,56,57,5,5,5,5,5,5,]),'LLAIZQ':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,37,38,39,52,53,54,55,56,57,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'CORIZQ':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,37,38,39,52,53,54,55,56,57,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'ENTERO':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,37,38,39,52,53,54,55,56,57,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'COMDOB':([0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,52,53,54,55,56,57,58,59,60,67,68,69,70,71,72,],[9,9,9,9,9,-25,9,9,9,9,9,9,9,9,9,9,9,-3,-27,42,-7,-8,-9,-10,-11,-12,-19,-20,-21,-4,9,9,9,-5,-6,-26,9,9,9,9,9,9,-22,-23,-24,-13,-14,-15,-16,-17,-18,]),'$end':([1,2,3,8,20,21,26,27,28,29,30,31,32,33,34,35,36,40,41,42,58,59,60,67,68,69,70,71,72,],[0,-27,-2,-25,-3,-27,-1,-7,-8,-9,-10,-11,-12,-19,-20,-21,-4,-5,-6,-26,-22,-23,-24,-13,-14,-15,-16,-17,-18,]),'ASIGNAR':([2,],[10,]),'MENORQUE':([2,3,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,49,50,51,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[-27,11,-25,-3,-27,11,11,11,11,11,11,11,11,11,11,11,11,11,11,43,-5,-6,-26,11,11,11,-22,-23,-24,11,11,11,11,11,11,-13,-14,-15,-16,-17,-18,]),'MAYORQUE':([2,3,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,49,50,51,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[-27,12,-25,-3,-27,12,12,12,12,12,12,12,12,12,12,12,12,12,12,44,-5,-6,-26,12,12,12,-22,-23,-24,12,12,12,12,12,12,-13,-14,-15,-16,-17,-18,]),'MENORIGUAL':([2,3,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,49,50,51,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[-27,13,-25,-3,-27,13,13,13,13,13,13,13,13,13,13,13,13,13,13,45,-5,-6,-26,13,13,13,-22,-23,-24,13,13,13,13,13,13,-13,-14,-15,-16,-17,-18,]),'MAYORIGUAL':([2,3,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,49,50,51,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[-27,14,-25,-3,-27,14,14,14,14,14,14,14,14,14,14,14,14,14,14,46,-5,-6,-26,14,14,14,-22,-23,-24,14,14,14,14,14,14,-13,-14,-15,-16,-17,-18,]),'IGUAL':([2,3,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,49,50,51,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[-27,15,-25,-3,-27,15,15,15,15,15,15,15,15,15,15,15,15,15,15,47,-5,-6,-26,15,15,15,-22,-23,-24,15,15,15,15,15,15,-13,-14,-15,-16,-17,-18,]),'DISTINTO':([2,3,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,49,50,51,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[-27,16,-25,-3,-27,16,16,16,16,16,16,16,16,16,16,16,16,16,16,48,-5,-6,-26,16,16,16,-22,-23,-24,16,16,16,16,16,16,-13,-14,-15,-16,-17,-18,]),'AND':([2,3,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,49,50,51,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[-27,17,-25,-3,-27,37,17,17,17,17,17,17,17,17,17,17,17,17,17,-4,-5,-6,-26,17,17,17,-22,-23,-24,17,17,17,17,17,17,-13,-14,-15,-16,-17,-18,]),'OR':([2,3,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,49,50,51,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[-27,18,-25,-3,-27,38,18,18,18,18,18,18,18,18,18,18,18,18,18,-4,-5,-6,-26,18,18,18,-22,-23,-24,18,18,18,18,18,18,-13,-14,-15,-16,-17,-18,]),'NOT':([2,3,8,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,49,50,51,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[-27,19,-25,-3,-27,39,19,19,19,19,19,19,19,19,19,19,19,19,19,-4,-5,-6,-26,19,19,19,-22,-23,-24,19,19,19,19,19,19,-13,-14,-15,-16,-17,-18,]),'PARDER':([8,20,21,22,27,28,29,30,31,32,33,34,35,36,40,41,42,49,50,51,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,],[-25,-3,-27,36,-7,-8,-9,-10,-11,-12,-19,-20,-21,-4,-5,-6,-26,58,59,60,-22,-23,-24,67,68,69,70,71,72,-13,-14,-15,-16,-17,-18,]),'LLADER':([8,20,21,23,27,28,29,30,31,32,33,34,35,36,40,41,42,58,59,60,67,68,69,70,71,72,],[-25,-3,-27,40,-7,-8,-9,-10,-11,-12,-19,-20,-21,-4,-5,-6,-26,-22,-23,-24,-13,-14,-15,-16,-17,-18,]),'CORDER':([8,20,21,24,27,28,29,30,31,32,33,34,35,36,40,41,42,58,59,60,67,68,69,70,71,72,],[-25,-3,-27,41,-7,-8,-9,-10,-11,-12,-19,-20,-21,-4,-5,-6,-26,-22,-23,-24,-13,-14,-15,-16,-17,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,37,38,39,52,53,54,55,56,57,],[3,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,49,50,51,61,62,63,64,65,66,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> IDENTIFICADOR ASIGNAR expresion','declaracion',3,'p_declaracion_asignar','analizador_sintactico.py',20),
  ('declaracion -> expresion','declaracion',1,'p_declaracion_expr','analizador_sintactico.py',24),
  ('expresion -> RESTA expresion','expresion',2,'p_expresion_uminus','analizador_sintactico.py',48),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',53),
  ('expresion -> LLAIZQ expresion LLADER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',54),
  ('expresion -> CORIZQ expresion CORDER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',55),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',61),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',62),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',63),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',64),
  ('expresion -> expresion IGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',65),
  ('expresion -> expresion DISTINTO expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',66),
  ('expresion -> PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',67),
  ('expresion -> PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',68),
  ('expresion -> PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',69),
  ('expresion -> PARIZQ expresion PARDER MAYORIGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',70),
  ('expresion -> PARIZQ expresion PARDER IGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',71),
  ('expresion -> PARIZQ expresion PARDER DISTINTO PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',72),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',98),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',99),
  ('expresion -> expresion NOT expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',100),
  ('expresion -> PARIZQ expresion AND expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',101),
  ('expresion -> PARIZQ expresion OR expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',102),
  ('expresion -> PARIZQ expresion NOT expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',103),
  ('expresion -> ENTERO','expresion',1,'p_expresion_numero','analizador_sintactico.py',121),
  ('expresion -> COMDOB expresion COMDOB','expresion',3,'p_expresion_cadena','analizador_sintactico.py',125),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_expresion_nombre','analizador_sintactico.py',129),
]