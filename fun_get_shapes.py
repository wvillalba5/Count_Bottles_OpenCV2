''' Analizando las formas de los objetos de una imagen'''

import cv2

'''Declarando la funcion get_shapes(input_image,image_contour) con sus
parametros de entrada'''
def get_shapes(input_image,image_contour):

    # Obtenemos los contornos
    contours, hierarchy = cv2.findContours(input_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #Inicializando Conteo de botellas
    number_bottles = 0
    # Ciclo for para recorrer la lista contours
    for contour in contours:
        # Se obtiene el perimetro
        perimeter = cv2.arcLength(contour, True)

        # Y se aproxima la curva poligonal, con un error del 1%
        poly = cv2.approxPolyDP(contour, 0.01 * perimeter, True)

        # Se obtiene la longitud del contorno
        x, y, w, h = cv2.boundingRect(poly)

        # Dibujamos el rectángulo
        cv2.rectangle(image_contour, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Y dibujamos un punto en el centro del rectángulo
        cv2.circle(image_contour, (x + w//2, y + h//2), 1, (0, 255, 0), 2, 1)

        # Conteo de corners
        corner_count = len(poly)
        # Si el corner_count es >= 10 entonces se le define como botella.
        if corner_count >= 10:

            number_bottles = number_bottles + 1
            obj_type = str(number_bottles)
        else:
            pass

        # Escribir en la imagen el número de botella
        cv2.putText(image_contour, obj_type, ((x+(w//2))-10, (y+(h//2))-10), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2)

        # Imprimimos los datos
    print(f' caja con :{number_bottles} botellas')
