"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    datos = [
        ['E', 1, '1999-02-28', 'b,g,f', 'jjj:5,bbb:3,ddd:9,ggg:3,hhh:0'],
        ['A', 9, '1999-02-28', 'a,d,e', 'aaa:3,bbb:7,ccc:2,ddd:5,iii:0'],
        ['B', 5, '1999-02-28', 'c,e,f', 'aaa:4,bbb:8,ccc:1'],
        ['A', 3, '1999-02-28', 'a,b,c', 'bbb:9,ccc:3,ddd:2'],
        ['C', 0, '1999-02-28', 'd,e,f', 'aaa:1,ddd:4,eee:5,ggg:10'],
        ['B', 1, '1999-02-28', 'a,e,g', 'aaa:2,ccc:3,ddd:6'],
        ['D', 8, '1999-02-28', 'b,f,h', 'bbb:1,eee:4,fff:9'],
        ['E', 9, '1999-02-28', 'a,d,f', 'aaa:5,bbb:2,ccc:10,ggg:7'],
        ['C', 9, '1999-02-28', 'a,e,f', 'aaa:7,ccc:1,ddd:9'],
        ['B', 3, '1999-02-28', 'b,c,d', 'ccc:4,ddd:5,eee:7'],
        ['D', 3, '1999-02-28', 'c,e,f', 'aaa:9,ddd:0,fff:0'],
        ['A', 7, '1999-02-28', 'b,e,f', 'bbb:6,ccc:2,ddd:4'],
        ['C', 6, '1999-12-01', 'f,g,d,a,2', 'iii:9,ddd:5,eee:1,jjj:17,hhh:9'],
    ]
    
    valores = {}
    for fila in datos:
        columna = fila[4].split(',')
        for par in columna:
            clave, valor = par.split(':')
            valor = int(valor)
            if clave in valores:
                valores[clave].append(valor)
            else:
                valores[clave] = [valor]
    
    rta = [(clave, min(valores[clave]), max(valores[clave])) for clave in sorted(valores.keys())]
    return rta

print(pregunta_06())
