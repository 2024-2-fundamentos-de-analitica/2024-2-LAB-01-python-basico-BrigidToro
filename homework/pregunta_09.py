"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    datos = [
        ['E', 1, '1999-02-28', 'b,g,f', 'aaa:3,aaa:3,aaa:3,aaa:3,aaa:3,aaa:3,aaa:3,aaa:3,bbb:9,ccc:8,ddd:0,eee:4,fff:3,ggg:4,hhh:2,iii:6,ggg:4,bbb:3,ddd:9,ggg:8,ggg:4'],
        ['A', 2, '1999-10-28', 'a,f,c', 'ccc:2,ddd:0,aaa:3,hhh:9,jjj:12,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2,ccc:2'],
        ['B', 3, '1999-12-01', 'b,e,g', 'aaa:5,bbb:9,ccc:8,bbb:9,bbb:9,bbb:9,bbb:9,bbb:9,bbb:9,bbb:9,bbb:9,bbb:9'],
        ['C', 0, '1999-01-15', 'a,b,c', 'aaa:1,ddd:4,eee:5,ggg:4,ggg:4,ggg:4,ggg:4,ggg:4,ggg:4,ggg:4'],
        ['A', 9, '1999-03-22', 'b,c,d', 'bbb:6,ccc:2,ddd:7'],
        ['E', 7, '1999-04-12', 'f,g,h', 'ddd:9,eee:6,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3,fff:3'],
        ['D', 3, '1999-05-30', 'c,d,e', 'aaa:4,bbb:8,ccc:3,hhh:2,hhh:2,hhh:2,hhh:2,hhh:2,hhh:2,hhh:2,hhh:2,hhh:2,hhh:2,hhh:2,hhh:2'],
        ['E', 5, '1999-06-01', 'a,f,g', 'ddd:8,ggg:4,hhh:2,jjj:12,jjj:12,jjj:12,jjj:12,jjj:12,ddd:8,ddd:8,ddd:8,ddd:8,ddd:8,ddd:8,ddd:8,ddd:8,ddd:8,ddd:8,ddd:8,ddd:8,ddd:8'],
        ['B', 1, '1999-07-14', 'b,e,f', 'aaa:2,bbb:5,ccc:9,eee:4,eee:4,eee:4,eee:4,eee:4,eee:4,eee:4,eee:4,eee:4,eee:4,eee:4'],
        ['C', 6, '1999-12-01', 'f,g,d,a', 'iii:6,ddd:5,eee:4,jjj:12,iii:6,iii:6,iii:6,iii:6,iii:6,iii:6,iii:6,iii:6,iii:6,iii:6,iii:6,iii:6,iii:6,iii:6,iii:6,iii:6'],
        ['A', 7, '1999-11-10', 'a,d,f', 'ccc:3,ddd:6,hhh:9'],
        ['D', 9, '1999-08-08', 'e,f,g', 'bbb:7,ddd:8,ggg:9,jjj:12,jjj:12,jjj:12,jjj:12,jjj:12,jjj:12,jjj:12,jjj:12,jjj:12,jjj:12,jjj:12'],
    ]
    
    conteo_claves = {}
    for fila in datos:
        columna = fila[4].split(',')
        for par in columna:
            clave, _ = par.split(':')
            if clave in conteo_claves:
                conteo_claves[clave] += 1
            else:
                conteo_claves[clave] = 1
    
    return conteo_claves

print(pregunta_09())