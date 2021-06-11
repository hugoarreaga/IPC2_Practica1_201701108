### Practica 1
from tda import *

# instanciamos el objeto lista donde guardaremos toda la infomracion
contactos = Lista()


'''     DATOS DE PRUEBA'''
contactos.insertar('usuario5','eapellido5', '5')
contactos.insertar('usuario6','fapellido6', '6')
contactos.insertar('usuario7','gapellido7', '7')

contactos.insertar('cusuario1','aapellido1', '1')
contactos.insertar('busuario2','aapellido2', '2')
contactos.insertar('ausuario3','aapellido3', '3')

contactos.insertar('usuario1','apellido1', '1')
contactos.insertar('usuario2','bpellido2', '2')
contactos.insertar('usuario4','dpellido4', '4')


### metodo para guardar contactos
def ingresar_contacto():
    print('\nIngresar Nuevo Contacto')
    nombre ="     "
    while True:
        nombre   = input('Ingrese el nombre del contacto: ')
        if nombre and nombre.strip(): break
        else:  print('\tDEBE DE INGRESAR UN NOMBRE ADECUADO')
        
    apellido="     "
    while True:
        apellido   = input('Ingrese el apellido del contacto: ')
        if apellido and apellido.strip(): break
        else: print('\tDEBE DE INGRESAR UN APELLIDO ADECUADO')

    telefono = "error"
    while telefono.isdigit()==False :
        telefono = input('Ingrese el numero de telefono: ')
        if telefono.isdigit()==False:
            print("\t''Solo debe ingresar numero enteros ")

    contactos.insertar(nombre,apellido,telefono)
    return 0







### metodo para buscar contactos existentes
def buscar_contacto():
    print('\nBuscar Contacto')

    telefono = "error"
    while telefono.isdigit()==False :
        telefono = input('Ingrese el numero de telefono: ')
        if telefono.isdigit()==False:
            print("\t''Solo debe ingresar numero enteros ")

    contacto = contactos.buscar(telefono)
    if contacto is None:
        opcion = input('El numero no se encuentra registrado ¿Desea Agregarlo? ( y / n ): ')
        if opcion == 'y':
            contactos.insertar_extra(telefono)
    return 0


### metodo para visualizar la lista de contactos
def visualizar_agenda():
    print('\nVisualizar agenda')
    if contactos.primero is None:
        print('''\n        ****************************************
        ** El listado de Contactos esta vacio **
        ****************************************''')
    else:
        contactos.crear_graphviz()
    return 0






### imprimir datos
def imprimirdatos():
    contactos.imprimir_primero()
    return 0






### metodo para correr el programa
def app():
    paso = True
    while paso:
        
        print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print('*-*-*-*-*-AGENDA DE CONTACTOS-*-*-*-*-*')
        print('1) Ingresar nuevo Contacto')
        print('2) Buscar Contacto')
        print('3) Visualizar agenda')
        print('4) Salir')
        opcion = input('Seleccione una opcion: ')

        if  opcion == '1':
            ingresar_contacto()
        elif opcion =='2':
            buscar_contacto()
        elif opcion =='3':
            visualizar_agenda()
        elif opcion =='4':
            paso = False
            print('\nGracias por utilizar el programa')
        elif opcion =='5':
            imprimirdatos()
        else:
            print('\nDebe de seleccionar una de las opciones disponibles: ;( ')

app()

