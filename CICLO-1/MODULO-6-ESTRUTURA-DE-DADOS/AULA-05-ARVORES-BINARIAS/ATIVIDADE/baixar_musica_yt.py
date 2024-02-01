from pytube import YouTube

# Definindo o URL do vídeo
video_url = "https://www.youtube.com/watch?v=rPjQchWHlL0"  # Substitua URL_DO_VIDEO_AQUI pela URL do vídeo do YouTube

# Criando um objeto YouTube
yt = YouTube(video_url)

# Acessando a stream de maior qualidade
audio_stream = yt.streams.get_audio_only()

# Baixando o arquivo de áudio
audio_stream.download(output_path=".", filename="minha_musica.mp3")

print("Download completo!")
