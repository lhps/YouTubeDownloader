from pytube import YouTube
from sys import argv

# link = argv[1]
link = input("Digite o link do vídeo que deseja baixar: ")
yt = YouTube(link)
downloadsPath = input("Digite o caminho onde quer salvar seu vídeo: ")
print(f"O vídeo {yt.title} será salvo em {downloadsPath}")


youTubeDownloader = yt.streams.get_highest_resolution()

youTubeDownloader.download(downloadsPath)
print(f"Download concluído com sucesso! Seu vídeo foi salvo em {downloadsPath}")

