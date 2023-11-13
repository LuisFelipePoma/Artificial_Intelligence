# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:59:26 2021

@author: preye
"""

import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection

mp_drawing = mp.solutions.drawing_utils

with mp_face_detection.FaceDetection(min_detection_confidence = 0.5) as  face_detection:
    #leemos la imagen de entrada
    image = cv2.imread("images/image_05.jpg")
    # Almacenamos el alto y ancho de nuestra imagen a traves de shape (no necesitamos los canales)
    alto, ancho, _ = image.shape
    # Antes de aplicar la transformacion de rsotros Transformamos la imagen de BGR a RGB pq por defecto opencv la carga en BGR
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    #Aplicamos la deteccion de rostros con la imagen en RGB
    
    resultados = face_detection.process(image_rgb)
    
    # Visualizamos el resultado (las coordenadas de los 6 puntos del rostro)
    print("Resultados:", resultados.detections)
    
    
    #Accedemos a cada una de las detecciones pe. a xmin=0.33
    if resultados.detections is not None:
        for detection in resultados.detections:
            #Caja delimitadora de rostro o Bounding Box
            print(int(detection.location_data.relative_bounding_box.xmin * ancho))
            
            xmin = int(detection.location_data.relative_bounding_box.xmin * ancho)
            ymin = int(detection.location_data.relative_bounding_box.ymin * alto)
            w = int(detection.location_data.relative_bounding_box.width * ancho)
            h = int(detection.location_data.relative_bounding_box.height * alto)
            cv2.rectangle(image, (xmin, ymin), (xmin + w, ymin + h), (0, 255, 0), 5)
            
            # Ojo derecho (circulo en rojo)
            x_RE = int(detection.location_data.relative_keypoints[0].x * ancho)
            y_RE = int(detection.location_data.relative_keypoints[0].y * alto)
            cv2.circle(image, (x_RE, y_RE), 3, (0, 0, 255), 5)
            # Ojo izquierdo (circulo en rosado)
            x_LE = int(detection.location_data.relative_keypoints[1].x * ancho)
            y_LE = int(detection.location_data.relative_keypoints[1].y * alto)
            cv2.circle(image, (x_LE, y_LE), 3, (255, 0, 255), 5)
            # Punta de la nariz (circulo en azul)
            x_NT = int(detection.location_data.relative_keypoints[2].x * ancho)
            y_NT = int(detection.location_data.relative_keypoints[2].y * alto)
            cv2.circle(image, (x_NT, y_NT), 3, (255, 0, 0), 5)
            # Centro de la boca (circulo en verde)
            x_MC = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.MOUTH_CENTER).x * ancho)
            y_MC = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.MOUTH_CENTER).y * alto)
            cv2.circle(image, (x_MC, y_MC), 3, (0, 255, 0), 5)
            
            # Tambien podemos acceder a estos puntos por su nombre (ya no por su indice)
            # Trago de la oreja derecha (circulo en amarillo)
            x_RET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.RIGHT_EAR_TRAGION).x * ancho)
            y_RET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.RIGHT_EAR_TRAGION).y * alto)
            cv2.circle(image, (x_RET, y_RET), 3, (0, 255, 255), 5)
            # Trago de la oreja izquierda (circulo en celeste)
            x_LET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.LEFT_EAR_TRAGION).x * ancho)
            y_LET = int(mp_face_detection.get_key_point(detection, mp_face_detection.FaceKeyPoint.LEFT_EAR_TRAGION).y * alto)
            cv2.circle(image, (x_LET, y_LET), 3, (255, 255, 0), 5)
      
      
    '''
    # Ahora Visualizamos los resultados con mediapipe
    # validamos que la imagen tenga un rostro resultados.detection nos devuelve una lista con todos los rostros detectados
    
    if resultados.detections is not None:
        for detection in resultados.detections:
            mp_drawing.draw_detection(image,detection),
        
    #Podemos cambiar el color/grosor de linea del cuadro delimitar como a los puntos de referencia de mediapipe
            mp_drawing.DrawingSpec(color=(255,0,255), thickness=3,circle_radius=3),
            mp_drawing.DrawingSpec(color=(0,255,255), thickness=3)
    '''
            
    #La visualizamos
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()