# import numpy as np
# import cv2
# from skimage import io
# from PIL import Image
# import requests
# import matplotlib.pylab as plt


# urls = [
#     "https://drive.google.com/file/d/19_1Coz-RA-QqMjMql3mNIoZm6aPuxGap/view?usp=sharing"
# ]
# for url in urls:

#     response = requests.get(url)

#     # Verifica se a requisição foi bem-sucedida
#     if response.status_code == 200:
#         # Lê os dados binários da imagem
#         image_array = np.frombuffer(response.content, dtype=np.uint8)

#         # Decodifica os dados binários em uma imagem OpenCV
#         image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

#         # image = io.imread(url)
#         if image is not None:

#             image_2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#             final_frame = cv2.hconcat((image, image_2))
#             cv2.imshow(f"imagem {urls.index(url)+1}", final_frame)
#             cv2.waitKey(0)
#             # Fechar todas as janelas
#             cv2.destroyAllWindows()
#             print("\n")


import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# URL da imagem
url = "https://drive.google.com/uc?id=19_1Coz-RA-QqMjMql3mNIoZm6aPuxGap"

# Baixar a imagem usando o requests
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Abrir a imagem usando a PIL
    image = Image.open(BytesIO(response.content))

    # Exibir a imagem
    image.show()
else:
    print("Falha ao baixar a imagem.")
