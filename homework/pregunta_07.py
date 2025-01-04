"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    datos = [
        ['E', 1, '1999-02-28', 'b,g,f', 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2'],
        ['A', 2, '1999-10-28', 'a,f,c', 'ccc:2,ddd:0,aaa:3,hhh:9'],
        ['E', 2, '1999-06-01', 'a,f,g', 'ddd:8,ggg:4,hhh:2'],
        ['A', 3, '1999-12-01', 'b,e,g', 'aaa:5,bbb:9,ccc:8'],
        ['B', 3, '1999-06-01', 'a,f,g', 'ddd:8,ggg:4,hhh:2'],
        ['D', 3, '1999-06-01', 'a,f,g', 'ddd:8,ggg:4,hhh:2'],
        ['C', 0, '1999-01-15', 'a,b,c', 'aaa:1,ddd:4,eee:5'],
        ['E', 3, '1999-04-12', 'f,g,h', 'ddd:9,eee:6,fff:3'],
        ['E', 3, '1999-05-30', 'c,d,e', 'aaa:4,bbb:8,ccc:3'],
        ['D', 3, '1999-06-01', 'a,f,g', 'ddd:8,ggg:4,hhh:2'],
        ['E', 4, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['B', 4, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['B', 5, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['C', 5, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['D', 5, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['D', 5, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['E', 5, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['E', 5, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['E', 5, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['B', 1, '1999-07-14', 'b,e,f', 'aaa:2,bbb:5,ccc:9'],
        ['E', 1, '1999-06-01', 'a,f,g', 'ddd:8,ggg:4,hhh:2'],
        ['C', 6, '1999-09-20', 'f,g,h', 'ddd:5,eee:7,fff:8'],
        ['E', 6, '1999-09-20', 'f,g,h', 'ddd:5,eee:7,fff:8'],
        ['A', 6, '1999-09-20', 'f,g,h', 'ddd:5,eee:7,fff:8'],
        ['B', 6, '1999-09-20', 'f,g,h', 'ddd:5,eee:7,fff:8'],
        ['A', 7, '1999-11-10', 'a,d,f', 'ccc:3,ddd:6,hhh:9'],
        ['C', 7, '1999-11-10', 'a,d,f', 'ccc:3,ddd:6,hhh:9'],
        ['E', 7, '1999-11-10', 'a,d,f', 'ccc:3,ddd:6,hhh:9'],
        ['D', 7, '1999-11-10', 'a,d,f', 'ccc:3,ddd:6,hhh:9'],
        ['E', 8, '1999-11-10', 'a,d,f', 'ccc:3,ddd:6,hhh:9'],
        ['D', 8, '1999-11-10', 'a,d,f', 'ccc:3,ddd:6,hhh:9'],
        ['E', 8, '1999-11-10', 'a,d,f', 'ccc:3,ddd:6,hhh:9'],
        ['A', 8, '1999-11-10', 'a,d,f', 'ccc:3,ddd:6,hhh:9'],
        ['B', 8, '1999-11-10', 'a,d,f', 'ccc:3,ddd:6,hhh:9'],
        ['A', 9, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['B', 9, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['E', 9, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['A', 9, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['A', 9, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
        ['C', 9, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9'],
    ]
    
    asociaciones = {}
    for fila in datos:
        valor = fila[1]
        letra = fila[0]
        if valor in asociaciones:
            asociaciones[valor].append(letra)
        else:
            asociaciones[valor] = [letra]
    
    rta = sorted([(clave, asociaciones[clave]) for clave in asociaciones])
    return rta

print(pregunta_07())