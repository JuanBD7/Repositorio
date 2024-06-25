import os
os.system('cls')
planilla_sueldos={'CEO': '1.200.000','Desarrollador': '900.000', 'Analista':'600.000' }
def registro():
    
    print('Trabajador'.ljust(15),'Cargo'.ljust(10),'Sueldo'.rjust(15),'Salud'.rjust(15),'AFP'.rjust(15),'Liquido'.rjust(15))
    print(f'{nombre}'.ljust(15), f'{cargo}'.ljust(10),f'{sueldo}'.rjust(15),f'{salud}'.rjust(15),f'{afp}'.rjust(15),f'{liquido}'.rjust(15))

lista_trabajadores=[]
print('Opciones')
print('1Registrar trabajador')
print('2.Lista de trabajadores')
print('3.Imprimir planilla de sueldos')
print('4.Salir')
opcion=input('Elije una opcion: ')
inicio=0
while inicio==0:
    if opcion=='1':
        try:    
            nombre=input('Ingrese nombre de trabajador: ')
            apellido=input('Ingrese apellido de trabajador: ')
            cargo=input('Ingrese cargo de trabajador: ')
            sueldo=int(input('Ingrese sueldo bruto: '))
            salud=(sueldo*0.07)
            afp=(sueldo*0.12)
            liquido=sueldo-salud-afp
            inicio=1
            registro()
        except ValueError:
            print('Ingresa numero entero')
            inicio=0
    elif opcion=='2':
        print('Lista de trabajadores',lista_trabajadores)
        inicio=1
    elif opcion=='3':
        print('Imprimir planilla de sueldos: a=(todos los cargos)/b = (cargo especifico)')
        consulta= input('¿Como lo quiere imprimir?: ')
        if consulta=='a':
            print(planilla_sueldos)
            inicio=1
        elif consulta== 'b':
            print('Cargos: Analista (an), Desarrollador (de), CEO (ce)')
            eleccion=input('Elige un cargo: ')
            inicio=1

            if eleccion=='an':
                print('Cargo Analista', planilla_sueldos['Analista'])
                inicio=1
            elif eleccion=='de':
                print('Cargo Desarrollador',planilla_sueldos['Desarrollador'])
                inicio=1
            elif eleccion=='ce':
                print('Cargo CEO',planilla_sueldos['CEO'])
                inicio=1

    elif opcion=='4':
        print('Haz salido del programa ')
        inicio=1

