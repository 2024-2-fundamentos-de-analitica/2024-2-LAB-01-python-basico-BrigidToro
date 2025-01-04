"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    datos = [
        "E\t1\t1999-02-28\tb,g,f\tjjj:12,bbb:3,ddd:9,ggg:8,hhh:2",
        "A\t10\t1999-10-28\ta,f,c\tccc:2,ddd:0,aaa:3,hhh:9",
        "A\t15\t2000-05-15\ta,c,e\taaa:5,ccc:7,eee:9,fff:1,ddd:4",
        "B\t7\t2001-07-11\tf,h,i\tbbb:6,ccc:2,hhh:3,jjj:8,ddd:1",
        "C\t4\t2002-09-23\ta,b,c\tccc:8,eee:5,ggg:6,bbb:2,jjj:4",
        "D\t6\t1998-12-12\td,e,f\tddd:7,bbb:1,hhh:9,fff:3,eee:2",
        "E\t11\t1999-03-10\ta,b,e\taaa:8,ddd:1,eee:4,jjj:6,hhh:7",
        "A\t20\t1999-09-19\tc,f,g\tccc:9,aaa:2,ddd:3,hhh:5,jjj:1",
        "B\t8\t1998-01-01\td,e,f\tbbb:4,ccc:3,ddd:6,fff:2,hhh:8",
        "C\t9\t1997-06-06\tg,h,i\taaa:9,bbb:5,ccc:1,ddd:7,eee:2",
        "D\t10\t1996-11-22\ta,b,c\thhh:4,ddd:8,ggg:3,aaa:1,jjj:9",
        "E\t14\t1995-10-15\tc,d,e\tccc:2,ddd:6,aaa:7,hhh:2,ggg:1",
        "A\t8\t2000-01-01\td,e,f\tbbb:4,ccc:3,ddd:6,fff:2,hhh:8",
        "B\t8\t1998-01-01\td,e,f\tbbb:4,ccc:3,ddd:6,fff:2,hhh:8",
        "C\t9\t1997-06-06\tg,h,i\taaa:9,bbb:5,ccc:1,ddd:7,eee:2",
        "D\t15\t1996-11-22\ta,b,c\thhh:4,ddd:8,ggg:3,aaa:1,jjj:9",
        "E\t14\t1995-10-15\tc,d,e\tccc:2,ddd:6,aaa:7,hhh:2,ggg:1",
        "C\t5\t1997-06-06\tg,h,i\taaa:9,bbb:5,ccc:1,ddd:7,eee:2",
        "E\t13\t1995-10-15\tc,d,e\tccc:2,ddd:6,aaa:7,hhh:2,ggg:1",
        "B\t13\t1998-01-01\td,e,f\tbbb:4,ccc:3,ddd:6,fff:2,hhh:8",
        "E\t14\t1995-10-15\tc,d,e\tccc:2,ddd:6,aaa:7,hhh:2,ggg:1",
    ]
    
    # Extraer la primera columna y la segunda columna
    from collections import defaultdict
    suma_por_letra = defaultdict(int)
    
    for linea in datos:
        partes = linea.split("\t")
        letra = partes[0]
        valor = int(partes[1])  # Convertir a entero
        suma_por_letra[letra] += valor
    
    # Ordenar alfabéticamente y convertir a lista de tuplas
    resultado = sorted(suma_por_letra.items())
    return resultado

print(pregunta_03())