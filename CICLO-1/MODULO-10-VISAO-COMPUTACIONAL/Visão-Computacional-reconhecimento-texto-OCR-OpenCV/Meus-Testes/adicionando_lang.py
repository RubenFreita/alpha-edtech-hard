import urllib.request


# Baixar arquivos de idioma e movê-los para a pasta do Google Drive
languages = [
    # "eng",
    # "por",
    "osd",
]  # Exemplo com inglês e português. Você pode adicionar outros idiomas conforme necessário.

for lang in languages:
    # Baixar arquivo de idioma
    urllib.request.urlretrieve(
        f"https://github.com/tesseract-ocr/tessdata/raw/main/{lang}.traineddata",
        f"tessdata/{lang}.traineddata",
    )
