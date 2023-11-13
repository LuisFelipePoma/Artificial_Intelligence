# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:59:26 2021

@author: preye
"""

import cv2
import mediapipe as mp
# instalar via pip install imutils
import imutils 

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Video streaming
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture("video/video_01.mp4")

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        
           
        #Configuramos ancho del frame para el video.mp4
        frame = imutils.resize(frame, width=720)
        frame = cv2.flip(frame, 1)
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultados = face_detection.process(frame_rgb)
        
        # Dibujamos el recuadro sobre el rostro asi como los 6 puntos de referencia      
       
        if resultados.detections is not None:
            for detection in resultados.detections:
                mp_drawing.draw_detection(frame, detection,
                    mp_drawing.DrawingSpec(color=(0, 255, 255), circle_radius=2),
                    mp_drawing.DrawingSpec(color=(255, 0, 255)))
        
        cv2.imshow("Frame", frame)
        
        # Cambiamos el waitkey 10 en lugar de 1 para disminuir la velocidad del video
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
cap.release()
cv2.destroyAllWindows()