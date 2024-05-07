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

        # image = io.imread(url)
        if image is not None:

            image_2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            final_frame = cv2.hconcat((image, image_2))
            cv2.imshow(f"imagem {urls.index(url)+1}", final_frame)
            cv2.waitKey(0)
            # Fechar todas as janelas
            cv2.destroyAllWindows()
            print("\n")
