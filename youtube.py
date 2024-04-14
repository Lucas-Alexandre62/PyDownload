from pytube import YouTube
import os

opcao = int(input("Digite o formato no qual voce quer baixar\n[1] Audio\n[2] Video\n"))
url = input("Digite a url do video: ")
yt = YouTube(url)

if(opcao == 1):
    destino = "audio"
    audio = yt.streams.filter(only_audio=True).first()

    arquivo_de_saida = audio.download(output_path=destino) 
    base, ext = os.path.splitext(arquivo_de_saida) 
    novo_nome = base + '.mp3'
    os.rename(arquivo_de_saida, novo_nome) 

    print(yt.title + "foi baixado com sucesso.")

elif(opcao == 2):
    destino = "video"
    video = yt.streams.get_highest_resolution()
    out_file = video.download(output_path=destino)

    print(yt.title + "foi baixado com sucesso.")