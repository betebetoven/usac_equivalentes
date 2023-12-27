from ply.lex import lex
from ply.yacc import yacc
from asignacion import asignacion, serie, paralelo



class parsero:
    def __init__(self, tabla):
        self.TABLA_DE_SIMBOLOS = tabla
        tokens = ('NUMBER', 'VARIABLE', 'PARALELO', 'SERIE', 'RIGHTPAREN', 'COMA', 'PUNTOYCOMA', 'IGUAL', 'NUM_EXPONENCIAL')
        t_ignore = ' \t\r'
        t_COMA = r','
        t_PUNTOYCOMA = r';'
        t_RIGHTPAREN = r'\)'
        t_IGUAL = r'='

        def t_SERIE(t):
            r'ser\('
            return t
        def t_PARALELO(t):
            r'par\('
            return t




        def t_NUM_EXPONENCIAL(t):
            r'-?\d+(\.\d+)?e-?\d+'
            t.value = float(t.value)
            return t

        def t_NUMBER(t):
            r'-?\d+(\.\d+)?'
            t.value = float(t.value)
            return t


        def t_VARIABLE(t):
            r'[a-zA-Z_\*\?][a-zA-Z0-9_]*'
            t.value = t.value  # remove the '=' at the beginning
            return t
        def t_ignore_newline(t):
            r'\n+'
            t.lexer.lineno += t.value.count('\n')

        # Error handler for illegal characters
        def t_error(t):
            #print(f'Illegal character {t.value[0]!r}')
            t.lexer.skip(1)

        # Build the lexer object









        lexer = lex()

        def p_instrucciones(p):
            '''instrucciones : command_list'''
            for command in p[1]:
                #call each object as a funciton
                A = command(self.TABLA_DE_SIMBOLOS)
                self.TABLA_DE_SIMBOLOS['RESULTADO'] = A
            #print(self.TABLA_DE_SIMBOLOS)
            p[0] = self.TABLA_DE_SIMBOLOS


        def p_command_list(p):
            '''command_list : expression
                            | command_list expression'''
            if len(p) == 3:
                comandos = p[1]
                comandos.append(p[2])
                p[0] = comandos
            else:
                comandos = []
                comandos.append(p[1])
                p[0] = comandos
                
        def p_expression(p):
            '''expression : asignacion
                        | calculo PUNTOYCOMA
                        | error
                        '''
            p[0] = p[1]
        def p_asignacion(p):
            '''asignacion : VARIABLE IGUAL calculo PUNTOYCOMA'''
            p[0] = asignacion(p[1], p[3])
        def p_calculo(p):
            '''calculo : SERIE calculo COMA calculo RIGHTPAREN
                        | PARALELO calculo COMA calculo RIGHTPAREN
                        | VARIABLE
                        | NUMBER
                        | NUM_EXPONENCIAL'''
            if p[1] == 'ser(':
                p[0] = serie(p[2], p[4])
            elif p[1] == 'par(':
                p[0] = paralelo(p[2], p[4])
            else:
                p[0] = p[1]
        def p_error(p):
            print(f'Syntax error at {p.value!r}')
            p[0] =  {'error': f'Syntax error at {p.value!r}'}



        self.parser = yacc()


