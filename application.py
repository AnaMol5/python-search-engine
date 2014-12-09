#coding:utf-8
"En este programa simularemos un buscador de palabras"
import urllib2 #me sirve para los Urls
import re #me ayuda para usar expresiones regulares
import os #trabaja con sistema operativo

class Conectar(object):

    def __init__(self):
        self.link = ""
        self.link2 = ""
        self.palabra = ""

    def inicio(self):
        print"""
         \t\t  _   _   _   _   _   _   _   _   _   _
        \t\t / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ 
       \t\t\t( B ( I ( E ( N ( V ( E ( N ( I ( D ( O )
        \t\t \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/
                  """
        print"""
         \t\t  _     _   _   _   _   _   _   _   _   _
        \t\t / \\   / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ 
       \t\t\t( A ) ( B ( U ( S ( C ( A ( W ( O ( R ( D )
        \t\t \\_/   \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/"""
        print """
              \rEn este búscador deberá ingrésar, 2 URL's para su generar búsqueda
              \rde una palabra, el mismo hará una comparación y le recomedará el URL
              \ren el que encuentré  la mayor cantidad de palabras"""
        raw_input("\nPRESIONE ENTER PARA CONTINUAR...")
        os.system("clear")
        self.contar()

    def contar(self):
        os.system('reset')
        self.link = raw_input("Ingrése un URL: ")
        self.link2 = raw_input("Ingrése otro URL: ")
        self.palabra = str(raw_input("Ingrése la palabra que desea búscar: "))
        if self.link[4:0] != "http" or self.link2[4:0] != "http":
            self.link = "https://" + self.link
            self.link2 = "https://" + self.link2
            try:
                pagina = urllib2.urlopen(self.link)
                archivo = pagina.read()
                pagina2 = urllib2.urlopen(self.link2)
                archivo2 = pagina2.read()
                if len(re.findall(self.palabra, archivo)) == 0:
                #findall devuelve las palabras encontradas en las urls
                    print "Palabra no encontrada"
                else:
                    primera = len(re.findall(self.palabra, archivo))
                    print "\nNúmero de palabras encontradas en la primera página: " + str(primera)
                    segunda = len(re.findall(self.palabra, archivo2))
                    print "\nNúmero de palabras encontradas en la segunda página: " + str(segunda)

                if primera == segunda:
                    print "Cantidad de palabras encontras en la primera URL es igual a la segunda\n"
                    print "                          \nGRACIAS POR UTILIZAR"
                    print"""
                    \r\t\t   _   _   _   _   _   _   _   _   _
                    \r\t\t  / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ 
                    \r\t\t ( B ( U ( S ( C ( A ( W ( O ( R ( D )
                    \r\t\t  \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/"""
                    raw_input("\nPRESIONE ENTER PARA CONTINUAR...")
                    self.contar()

                elif primera > segunda:
                    print "\nCantidad de palabras encontras en la primera página es mayor", primera
                    print "\nle recomedamos ingrésar a ella"
                    print str(self.link)
                    print "                          \nGRACIAS POR UTILIZAR"
                    print"""
                    \r\t\t   _   _   _   _   _   _   _   _   _
                    \r\t\t  / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ 
                    \r\t\t ( B ( U ( S ( C ( A ( W ( O ( R ( D )
                    \r\t\t  \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/"""
                    raw_input("\nPRESIONE ENTER PARA CONTINUAR...")
                    self.contar()

                elif primera < segunda:
                    print "La cantidad de palabras encontras en la primera página es mayor", segunda
                    print "Recomiendo que ingrese a ella"
                    print str(self.link2)
                    print "                          \nGRACIAS POR UTILIZAR"
                    print"""
                    \r\t\t   _   _   _   _   _   _   _   _   _
                    \r\t\t  / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ 
                    \r\t\t ( B ( U ( S ( C ( A ( W ( O ( R ( D )
                    \r\t\t  \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/"""
                    raw_input("\nPRESIONE ENTER PARA CONTINUAR...")
                    self.contar()

            except urllib2.URLError as error:
                print error.reason
                print "URL's no válidas"
                raw_input("\nPRESIONE ENTER PARA CONTINUAR...")
                self.contar()
BUSCAR = Conectar()
BUSCAR.inicio()
