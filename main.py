import cv2
from functions.caixaDetec import caixaDetec
from functions.connectToFeed import connectToFeed

captura = connectToFeed();
captura2 = cv2.VideoCapture(0);

while True:
  resultado, video = captura.read(); # lê os frames do vídeo
  resultado, video2 = captura2.read(); # lê os frames do vídeo
  if resultado is False:
    break;
  faces = caixaDetec(video);
  faces = caixaDetec(video2);
  video = cv2.resize(video, (640, 480));
  video2 = cv2.resize(video2, (640, 480));
  cv2.imshow('Video', video);
  cv2.imshow('Video2', video2);
  # define tamanho da janela
  cv2.resizeWindow('Video', 640, 480);
  cv2.resizeWindow('Video2', 640, 480);

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break;

captura.release();
captura2.release();
cv2.destroyAllWindows();
