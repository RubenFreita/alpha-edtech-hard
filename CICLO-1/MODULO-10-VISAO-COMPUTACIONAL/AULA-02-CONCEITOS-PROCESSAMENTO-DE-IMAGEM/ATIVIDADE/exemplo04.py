import numpy as np
import cv2
from skimage import io
from PIL import Image
import requests
import matplotlib.pylab as plt


urls = [
    "https://pbs.twimg.com/media/EmyyymHW4AALiGR?format=png&name=small",
    "https://img.elo7.com.br/product/zoom/4BA6264/satoru-gojo-fundo-amarelo-ilustracao-digital-papelaria.jpg",
    "https://images.educamaisbrasil.com.br/content/noticias/8-licoes-do-anime-one-piece-para-a-sua-vida-profissional_g.jpg",
    "https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2024/01/03/frieren-e-a-jornada-para-o-alem-qhvlvd2l8mr5.jpg",
]


for url in urls:

    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Lê os dados binários da imagem
        image_array = np.frombuffer(response.content, dtype=np.uint8)

        # Decodifica os dados binários em uma imagem OpenCV
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        if image is not None:

            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            h, w = image_gray.shape

            image2 = image_gray[(h // 4) : (h // 4) * 3, (w // 4) : (w // 4) * 3]
            h, w = image2.shape
            limiar = 50
            image3 = image2 > limiar
            print(image3)

            image4 = image3.astype("int")  # typy int
            print(image4.dtype)
            print(image4)
            plt.figure(figsize=(5, 5))
            _ = plt.imshow(image3, "gray")
            plt.show()
