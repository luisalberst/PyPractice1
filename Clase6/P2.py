
## Clase alumno con evaluación e impresión
class alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

        ## Se evalua la calificacion del 1 al 20, donde una nota > 10 significa que el alumno esta aprobado
        if int(self.nota) > 10:
            print('El alumno {} ha aprobado con la nota de {}'.format(self.nombre,self.nota))
        else:
            print('El alumno {} ha sido aplazado con la nota de {}'.format(self.nombre,self.nota))

print('-- Impresion de datos sin definir metodos --')
a1 = alumno('Juan','11')
a2 = alumno('Maria','9')
## Fin de la clase alumno
print()
## Inicio de la clase alumno1, definiendo metodos
class alumno1:
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print('Nombre del alumno: {}'.format(self.nombre))
        print('Nota del alumno: {}'.format(self.nota))

    def resultados(self):
        ## Se evalua la calificacion del 1 al 20, donde una nota > 10 significa que el alumno esta aprobado
        if float(self.nota) > 10:
            print('El alumno ha aprobado')
        else:
            print('El alumno ha sido aplazado')

a3 = alumno1()
a4 = alumno1()
print('-- Impresión de datos definiendo metodos --')
a3.inicializar('Juanito','7')
a4.inicializar('Angelica','15')

a3.imprimir()
a3.resultados()
print()
a4.imprimir()
a4.resultados()