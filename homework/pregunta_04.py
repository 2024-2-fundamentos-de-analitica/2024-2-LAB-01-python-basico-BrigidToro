"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    datos = [
        "B\t5\t1998-05-02\tf,e,a,c\tddd:2,ggg:5,ccc:6,jjj:12",
        "A\t3\t1999-01-15\ta,c,e\tbbb:1,ccc:4,ddd:5,fff:3",
        "C\t4\t1997-08-10\tb,d,f\tddd:6,eee:7,fff:3,ggg:8",
        "D\t2\t2000-03-12\te,f,g\thhh:3,ddd:5,aaa:7,bbb:2",
        "E\t7\t1996-12-25\tb,c,e\tccc:9,aaa:4,ddd:6,fff:5",
        "A\t6\t1998-07-22\ta,b,f\tddd:1,ggg:4,bbb:3,ccc:2",
        "B\t9\t1999-08-14\tc,d,e\taaa:6,ccc:3,ddd:5,eee:2",
        "C\t3\t2001-06-09\tf,g,h\tccc:2,ddd:1,hhh:9,ggg:6",
        "D\t5\t1998-09-11\ta,b,d\taaa:3,ddd:8,fff:4,ccc:1",
        "E\t4\t1997-04-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "A\t8\t1998-02-20\tf,g,h\tddd:4,ggg:9,aaa:1,bbb:3",
        "B\t2\t1999-11-30\tc,e,g\tccc:5,ddd:3,eee:2,hhh:4",
        "C\t7\t1997-10-18\ta,f,h\thhh:7,aaa:8,bbb:4,ddd:6",
        "D\t1\t2000-01-04\tb,d,g\tccc:2,ddd:3,aaa:4,hhh:6",
        "E\t3\t1995-01-07\ta,b,e\tddd:5,ccc:7,ggg:8,hhh:1",
        "A\t9\t1996-03-28\te,f,g\thhh:6,ddd:4,bbb:2,aaa:7",
        "B\t6\t1997-07-03\tc,f,g\tccc:3,ddd:1,eee:2,aaa:8",
        "C\t5\t1998-02-14\ta,d,f\tbbb:7,ccc:5,ddd:3,hhh:4",
        "D\t4\t1999-05-19\tb,e,h\tccc:9,ggg:4,ddd:6,fff:1",
        "E\t2\t2000-06-22\td,f,h\tbbb:3,ccc:2,ggg:7,hhh:9",
        "A\t8\t1998-02-20\tf,g,h\tddd:4,ggg:9,aaa:1,bbb:3",
        "A\t8\t1998-02-20\tf,g,h\tddd:4,ggg:9,aaa:1,bbb:3",
        "E\t4\t1997-04-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-04-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-04-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-05-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-06-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-07-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-07-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-07-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-08-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-08-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-08-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-08-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-09-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-09-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-10-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-11-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-12-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
        "E\t4\t1997-12-16\tc,e,f\tbbb:5,ccc:6,ddd:7,fff:2",
    ]
    
    # Extraer el mes de la columna 3
    from collections import Counter
    meses = [linea.split("\t")[2][5:7] for linea in datos]
    
    # Contar ocurrencias de cada mes
    conteo = Counter(meses)
    
    # Ordenar y convertir a lista de tuplas
    resultado = sorted(conteo.items())
    return resultado

print(pregunta_04())