import face_recognition
import os
import cv2

Rostos_Conhecidos_Dir = "Rostos_conhecidos"
Rostos_Desconhecidos_Dir = "Rostos_desconhecidos"

Tolerancia = 0.6
# Quanto menor a tolerância, menos chances de termos falsos-positivos
# Com uma tolerância maior, podemos dar "match" nas imagens erradas ~ Com cerca de 0.1 de tolerância.

Grossura_moldura = 3 
Grossura_fonte = 2
Modelo = "cnn"

# Carregando as imagens conhecidas para caso termos uma imagem não conhecida, ela pode ser comparada com a conhecida.

print("Carregando as imagens conhecidas")

Rostos_conhecidos = []
Nomes_conhecidos = []

for nome in os.listdir(Rostos_Conhecidos_Dir):
    for nomeArq in os.listdir(f"{Rostos_Conhecidos_Dir}/{nome}"):
        imagem = face_recognition.load_image_file(f"{Rostos_Conhecidos_Dir}/{nome}/{nomeArq}")
        encoding = face_recognition.face_encodings(imagem)
        Rostos_conhecidos.append(encoding)
        Nomes_conhecidos.append(nome)

print("Processando rostos desconhecidos")

for nomeArq in os.listdir(Rostos_Desconhecidos_Dir):
    print(nomeArq)
    imagem = face_recognition.load_image_file(f"{Rostos_Desconhecidos_Dir}/{nomeArq}")
    