"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    datos = [
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "A\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "B\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "C\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "D\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "A\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "A\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "A\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "A\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "A\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "A\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "A\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "B\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "D\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "B\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "D\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "B\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "D\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "B\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "D\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "B\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "D\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "B\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "C\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "C\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "C\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "C\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        
    ]
    
    # Extraer la primera columna (letra inicial)
    letras = [linea.split("\t")[0] for linea in datos]
    
    # Contar ocurrencias de cada letra
    from collections import Counter
    conteo = Counter(letras)
    
    # Ordenar alfabéticamente y convertir a lista de tuplas
    resultado = sorted(conteo.items())
    return resultado
print(pregunta_02())