import os 
class Nodo:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.siguiente = None
        self.anterior = None
        

class Lista:
    def __init__(self):
        self.primero = None
        #self.ultimo = None

    ### Verificar si ya existe el numero de telefono que estamos guardando
    def existe(self, telefono):
        existe = False
        actual = self.primero
        while actual != None:
            if str(actual.telefono) == str(telefono):
                existe = True
            actual = actual.siguiente
        if existe:
            return True
        else:
            return False

    ### guardar cada contacto con su informacion dentro de la lista al final
    #def insertar(self, nombre, apellido, telefono):
    def insertar(self, nombre,apellido,telefono):
        nuevo = Nodo(nombre,apellido,telefono)
        if self.primero == None:
            self.primero = nuevo
        elif self.existe(nuevo.telefono):
            print('-*-*-*-El numero '+telefono+' Ya existe')
        elif nuevo.apellido < self.primero.apellido:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente != None:
                if nuevo.apellido <actual.siguiente.apellido:
                    nuevo.siguiente = actual.siguiente
                    actual.siguiente.anterior = nuevo
                    nuevo.anterior = actual
                    actual.siguiente = nuevo
                    break
                actual = actual.siguiente
            if actual.siguiente == None:
                actual.siguiente = nuevo
                nuevo.anterior = actual
        



    ### imprimir los datos de contacto primeros
    def imprimir_primero(self):
        actual = self.primero
        print('\n----- LISTADO DE CONTACTOS PRIMERO-----')
        while actual != None:
            print(' NOMBRE  : '+ str(actual.nombre))
            print(' APELLIDO: '+ str(actual.apellido))
            print(' TELEFONO: '+ str(actual.telefono)+'\n')
            actual = actual.siguiente

        actual = self.primero
        while actual.siguiente is not None:
            actual = actual.siguiente
        print('\n----- LISTADO DE CONTACTOS ULTIMOS-----')
        while actual != None:
            print(' NOMBRE  : '+ str(actual.nombre))
            print(' APELLIDO: '+ str(actual.apellido))
            print(' TELEFONO: '+ str(actual.telefono+'\n'))
            actual = actual.anterior

        return 0

    
   


    # opcion para buscar la informacion de un numero de telefono
    def buscar(self, telefono):
        encontrado = False
        actual = self.primero
        while actual != None:
            if actual.telefono == telefono:
                encontrado = True
                break
            actual = actual.siguiente

        if encontrado :
            print(' **** NUMERO ENCONTRADO -*-*-*-*-')
            print(' **** Informacion del numero '+str(actual.telefono))
            print(' **** Nombre:   ' +str(actual.nombre))
            print(' **** Apellido: ' +str(actual.apellido))
            return 1
        else:
            return None




    ### crear graphviz
    def crear_graphviz(self):
        dot_file = open('file_dot.dot','w+')

        dot_file.write ('digraph A{\n')
        dot_file.write ('\tsubgraph cluster_O{\n')
        dot_file.write ('\t\tlabel ="Agenda de&#92;nContactos";\n')
        dot_file.write ('\t\tstyle = filled;\n')
        dot_file.write ('\t\tbgcolor="grey52";\n')
        
        #### Nodos de Contactos
        dot_file.write ('\n\t\t/* Entidades */\n')
        dot_file.write ('\t\tnode [shape=box,color= cornflowerblue,style=filled,fillcolor=darkseagreen1];\n\n')

        actual = self.primero
        while actual != None:
            label = "NOMBRE: "+actual.nombre+"&#92;nAPELLIDO: "+actual.apellido+"&#92;nTELEFONO: "+actual.telefono
            dot_file.write ('\t\t'+actual.telefono+' [ label="' +label+'"];\n\n')
            actual = actual.siguiente
        
        #### Relaciones de los nodos
        dot_file.write('\t\t/* Relationships */\n')
        #dot_file.write('\t\tedge [dir="both"]')
        actual = self.primero

        while actual.siguiente != None:
            dot_file.write ('\t\t{} -> {};\n'.format(
                actual.telefono,
                actual.siguiente.telefono
            ))

            dot_file.write ('\t\t{} -> {};\n'.format(
                actual.siguiente.telefono,
                actual.telefono
            ))
            actual = actual.siguiente


        
        dot_file.write ('\t}\n')
        dot_file.write ('}')
        dot_file.close()
        os.system('dot -Tpng file_dot.dot -o file_dot.png')    
        os.system('file_dot.png')
        pass
    

    #### agregar si no se encontro el numero
    def insertar_extra(self,telefono):

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

        self.insertar(nombre,apellido,telefono)

        return 0