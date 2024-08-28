''' Se ha creado una class llamada Game con funciones
- def __init__() para iniciar el constructor de la class Game
_ def run(self) funcion para iniciar
- def__process(self) para el proceso'''

# Importamos las librerias de mayor a menor jerarquia
import os
import cv2
import keyboard
from fun_get_shapes import get_shapes

# Definimos la class
class Game:


    def __init__(self):
        # Es el constructor
        pass
    def run(self):
        print("Precaución Iniciando Operaciones")
        self.__process()

    def __process(self):
        # leer el path donde estan las imagenes
        _path = "resources"
        #Lista con los nombres de las imagenes
        files_names = os.listdir(_path)

        _running = True

        # Bucle infinito mientras running este en True
        while _running:
            # Recorriendo la lista donde esta las imagenes
            for file_name in files_names:
                image = cv2.imread(_path + "/" + file_name)
                # Para dibujar los contornos pero mantener la imagen original hacemos una copia de la misma
                image_contour = image.copy()
                # Cambio de espacio de color de BGR a escala de grises
                _image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # Umbralización de la imagen - obtención de imagen binaria
                ret, image_thresh = cv2.threshold(_image_gray, 127, 255, cv2.THRESH_BINARY)

                if ret:
                    # Detector de bordes
                    image_canny = cv2.Canny(image_thresh, 50, 100)
                    # Instanciando la función get_shapes de la clase Game
                    get_shapes(image_canny, image_contour)
                    cv2.imshow('Image_thresh', image_contour)
                    cv2.waitKey(500)

                # Code para salir del bucle While pulsando la tecla q
                if keyboard.is_pressed("q"):
                    _running = False
                    break



