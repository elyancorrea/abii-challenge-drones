import cv2
import os

# Dicionário com as informações dos marcadores
marcadores_dict = {
    0: {'Quadrado': 'Início', 'Face': '-'},
    1: {'Quadrado': 1, 'Face': 1},
    2: {'Quadrado': 1, 'Face': 2},
    3: {'Quadrado': 1, 'Face': 3},
    4: {'Quadrado': 1, 'Face': 4},
    5: {'Quadrado': 2, 'Face': 1},
    6: {'Quadrado': 2, 'Face': 2},
    7: {'Quadrado': 2, 'Face': 3},
    8: {'Quadrado': 2, 'Face': 4},
    9: {'Quadrado': 3, 'Face': 1},
    10: {'Quadrado': 3, 'Face': 2},
    11: {'Quadrado': 3, 'Face': 3},
    12: {'Quadrado': 3, 'Face': 4},
    13: {'Quadrado': 4, 'Face': 1},
    14: {'Quadrado': 4, 'Face': 2},
    15: {'Quadrado': 4, 'Face': 3},
    16: {'Quadrado': 4, 'Face': 4},
    17: {'Quadrado': 5, 'Face': 1},
    18: {'Quadrado': 5, 'Face': 2},
    19: {'Quadrado': 5, 'Face': 3},
    20: {'Quadrado': 5, 'Face': 4},
}

# Cria a pasta "marcadores" se ela não existir
if not os.path.exists('marcadores'):
    os.makedirs('marcadores')

# Caminho para o diretório de saída
output_dir = 'marcadores/'

# Tamanho desejado para cada marcador (em pixels)
marker_size = 1000

# Criação dos marcadores ArUco e salvamento em arquivo
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_100)
parameters = cv2.aruco.DetectorParameters_create()

for marker_id, info in marcadores_dict.items():
    marker_image = cv2.aruco.drawMarker(aruco_dict, marker_id, marker_size)
    filename = f"{output_dir}marcador_{marker_id}.png"
    cv2.imwrite(filename, marker_image)

print("Marcadores gerados e salvos com sucesso.")
