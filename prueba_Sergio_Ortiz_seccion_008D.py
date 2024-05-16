import os
import time
clean = "cls"
os.system(clean)
cil5=5
cil11=11
cil15=15
cil45=45
cam=0
sw=1
estandar=765000
saldo1=0
kg=450
totalap=0
tkg=0
cil=1700
tkgc=450
tcam=0
tkg1=0
while sw==1:
    try:
        nombre=input("Porfavor ingresa tun nombre: ")
        len(nombre)
        if len(nombre)>=3:
            telefono_str=input("Porfavor ingresa tu numero de telefono: ")
            if len(telefono_str)<=9 and len(telefono_str)>=8:
                time.sleep(2)
                os.system(clean)
                while True:
                    print("Bienvenido "+ nombre+ " Porfavor selecciona una opcion")
                    print("1. Compra estandar(Detallar cantidad de camiones)")
                    print("2. Compra entrega carga especifiva (Especificar cantidad de cilindros)")
                    opc=int(input("Porfavor selecciona una opcion: "))
                    try:
                        if opc >=1 and opc <=2:
                            if opc==1:
                                print(f"Has selecionado la opcion estandar valor: ${estandar}")
                                cam=int(input("Porfavor indica la cantidad de camiones a utilizar:  "))
                                if cam >=1:
                                    tcam=(tcam+cam)
                                    tkg1=(tkgc*cam+tkg)
                                    totalap=(totalap+estandar)
                                    continu=int(input("Desea realizar otra compra? si/1 no/2: "))
                                    time.sleep(2)
                                    os.system(clean)
                                    if continu==2:
                                        print("Procediento a la boleta")
                                        time.sleep(2)
                                        os.system(clean)
                                        print("Boleta")
                                        print("Cliente: "+nombre)
                                        print("Telefono: "+telefono_str)
                                        print(f"Cantidad de kilos: {tkg1}")
                                        print(f"Camiones: {tcam}")
                                        print(f"Valor total: ${totalap}")
                                        continu=int(input("Desea relizar otra compra? si/1 no/2: "))
                                        time.sleep(2)
                                        os.system(clean)
                                        if continu==2:
                                            print("Gracias por escojernos")
                                            break
                                else:
                                    cam<= 0
                                    print("No puedes comprar 0 camiones")
                            if opc==2:
                                print("Has seleccionado la opcion entrega especifica")
                                kg5=int(input("Cuantos cilindros de 5kg deseas?: "))
                                tkg1=(5*kg5)
                                totalap1=(cil*kg5)
                                kg11=int(input("Cuantos cilindros de 11kg deseas?: "))
                                tkg2=(11*kg11)
                                totalap2=(cil*kg11)
                                kg15=int(input("Cuantos cilindros de 15kg deseas?: "))
                                tkg3=(15*kg15)
                                totalap3=(cil*kg15)
                                kg45=int(input("Cuantos cilindros de 45kg deseas?: "))
                                tkg4=(45*kg45)
                                totalap4=(cil*kg45)
                                tkg=(tkg1+tkg2+tkg3+tkg4+tkg1)
                                totalap=(totalap1+totalap2+totalap3+totalap4)
                                if tkg== 450:
                                    print("Solo se ocupara 1 camion no se cobra multa")
                                    tcam=(tcam+1)
                                    continu=int(input("Desea realizar otra compra? si/1 no/2: "))
                                    time.sleep(2)
                                    os.system(clean)
                                    if continu==2:
                                        print("Procediento a la boleta")
                                        time.sleep(2)
                                        os.system(clean)
                                        print("Boleta")
                                        print("Cliente: "+nombre)
                                        print("Telefono: "+telefono_str)
                                        print(f"Cantidad de kilos: {tkg}")
                                        print(f"Camiones: {tcam}")
                                        print(f"Valor total: ${totalap}")
                                        continu=int(input("Desea relizar otra compra? si/1 no/2: "))
                                        time.sleep(2)
                                        os.system(clean)
                                        if continu==2:
                                            print("Gracias por escojernos")
                                            break
                                if tkg > 450:
                                    cam2=int(input(f"La cantidad de kg({tkg}) es mayor a la de un camion(450kg) especifica cuantos camiones necesitas ocupar: "))
                                    tcam=(tcam+cam2)
                                    llen=int(input("Vas a llenar los 450kg? de cada camion? 1/si 2/no"))
                                    if llen==1:
                                        print("No se crobra multa")
                                    if llen==2:
                                        print("Se cobra 1700+ por kg y una multa de 100.000")
                                        totalap=(totalap*1700+100000)
                                        continu=int(input("Desea realizar otra compra? si/1 no/2: "))
                                    time.sleep(2)
                                    os.system(clean)
                                    if continu==2:
                                        print("Procediento a la boleta")
                                        time.sleep(2)
                                        os.system(clean)
                                        print("Boleta")
                                        print("Cliente: "+nombre)
                                        print("Telefono: "+telefono_str)
                                        print(f"Cantidad de kilos: {tkg}")
                                        print(f"Camiones: {tcam}")
                                        print(f"Valor total: ${totalap}")
                                        continu=int(input("Desea relizar otra compra? si/1 no/2: "))
                                        time.sleep(2)
                                        os.system(clean)
                                        if continu==2:
                                            print("Gracias por escojernos")
                                            break
                                if tkg< 450:
                                    print("No vas a llenar el 100% del camcion se cobra 1700+por kg y una multa de 100.000")
                                    tcam=(tcam+1)
                                    totalap=(totalap*1700+100000)

                                    continu=int(input("Desea realizar otra compra? si/1 no/2: "))
                                    time.sleep(2)
                                    os.system(clean)
                                    if continu==2:
                                        print("Procediento a la boleta")
                                        time.sleep(2)
                                        os.system(clean)
                                        print("Boleta")
                                        print("Cliente: "+nombre)
                                        print("Telefono: "+telefono_str)
                                        print(f"Cantidad de kilos: {tkg}")
                                        print(f"Camiones: {tcam}")
                                        print(f"Valor total: ${totalap}")
                                        continu=int(input("Desea relizar otra compra? si/1 no/2: "))
                                        time.sleep(2)
                                        os.system(clean)
                                        if continu==2:
                                            print("Gracias por escojernos")
                                            break
                                else:
                                    tkg==0
                                    print("No puedes comprar 0 cilindros")
                        else:
                            print("Opcion fuera de rango")
                    except:
                          print("Ingresa solo numeros Porfavor")
            else:
                print("El numero no puede tener menos de 8 numeros ni mas de 9 intenta otra vez")
                time.sleep(2)
                os.system(clean)
        else:
            len(nombre)<3
            print("El nombre no puede tener menos de 3 Letras intenta otra vez")
            time.sleep(2)
            os.system(clean)
    except:
        print("valor fuera de rango")


