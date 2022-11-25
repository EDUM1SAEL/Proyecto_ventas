print("Bienvenido al almacen de ventas para dar inicio ingrese :");
nombre=str(input("ingrese su nombre:"));
año_nac=int(input("Ingrese el año de nacimiento:"));
año=2022-año_nac;
if(año>18):
    print("has comprobado que ere mayor de edad");
    venta_1=float(input("ingrese las ventas del primer semestre del año 2021 :"));
    venta_2 = float(input("ingrese las ventas del segundo semestre del año 2021 :"));
    venta_anual=venta_1+venta_2;
    print("su venta anual es:",venta_anual);
    if(venta_1==venta_2):
        semestre=("Ambas ventas son iguales");
    elif (venta_1>venta_2):
        semestre=("1ro");
    else:
        semestre=("2do");

    print("******************Metas Alcanzadas**********************")
    if (venta_anual<=100000.0):
        medalla=("Bronce");
        premio=("un dia libre")
    elif(venta_anual<=500000.0):
        medalla = ("Plata");
        premio = ("un dia libre y un bono de Q250")
    elif(venta_anual<=1000000.00):
        medalla = ("Oro");
        premio = ("un dia libre y un bono de Q500")
    else:
        medalla =("Diamante");
        premio=("Dos dias libres y un bono de Q1000");
    print("*************************Datos calculados*******************");
    print("vendedor:",nombre);
    print("Ventas anuales:",venta_anual);
    print("Mejor Semestre",semestre);
    print("Medalla Acreditada:",medalla);
    print("Premio",premio);
else:
    print("se ha detectado que es menor de edad");
    exit()