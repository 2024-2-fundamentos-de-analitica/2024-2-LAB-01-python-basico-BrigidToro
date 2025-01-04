"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    datos = [
        ['E', 1, '1999-02-28', 'b,g,f', 'jjj:12,bbb:3,ddd:9,ggg:8,hhh:2'],
        ['A', 9, '1999-02-28', 'a,d,e', 'aaa:3,bbb:7,ccc:2,ddd:5'],
        ['B', 9, '1999-02-28', 'c,e,f', 'aaa:4,bbb:8,ccc:1'],
        ['A', 2, '1999-02-28', 'a,b,c', 'bbb:6,ccc:3,ddd:2'],
        ['C', 0, '1999-02-28', 'd,e,f', 'aaa:1,ddd:4,eee:5'],
        ['B', 1, '1999-02-28', 'a,e,g', 'aaa:2,ccc:3,ddd:6'],
        ['D', 8, '1999-02-28', 'b,f,h', 'bbb:9,eee:4,fff:7'],
        ['E', 9, '1999-02-28', 'a,d,f', 'aaa:5,bbb:2,ccc:8'],
        ['C', 9, '1999-02-28', 'a,e,f', 'aaa:7,ccc:0,ddd:9'],
        ['B', 3, '1999-02-28', 'b,c,d', 'ccc:4,ddd:5,eee:6'],
        ['D', 3, '1999-02-28', 'c,e,f', 'aaa:9,ddd:1,fff:3'],
        ['A', 7, '1999-02-28', 'b,e,f', 'bbb:5,ccc:2,ddd:4'],
    ]
    
    resultados = {}
    for fila in datos:
        letra = fila[0]
        valor = int(fila[1])
        if letra in resultados:
            resultados[letra].append(valor)
        else:
            resultados[letra] = [valor]
    
    rta = [(k, max(v), min(v)) for k, v in sorted(resultados.items())]
    return rta

print(pregunta_05())