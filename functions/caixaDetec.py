import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(
  cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
);

unknown_text = 'Desconhecido';

def caixaDetec(video):
  imagem_cinza = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY);
  rostos = face_cascade.detectMultiScale(imagem_cinza, 1.3, 5, minSize=(30, 30));
  for (x, y, w, h) in rostos:
    cv2.rectangle(video, (x, y), (x+w, y+h), (0, 255, 0), 2);
    
    # escreve texto abaixo do retângulo
    fonte = cv2.FONT_HERSHEY_SIMPLEX;
    cv2.putText(video, unknown_text , (x, y+h+30), fonte, 1, (255, 0, 0), 2, cv2.LINE_AA);

    return