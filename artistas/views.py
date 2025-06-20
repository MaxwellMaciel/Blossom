from django.shortcuts import render
import os
from django.conf import settings
import mimetypes

# Create your views here.

def home(request):
    return render(request, 'artistas/home.html')

def visao(request):
    return render(request, 'artistas/visao.html')

def carreira(request):
    return render(request, 'artistas/carreira.html')

def albuns(request):
    return render(request, 'artistas/albuns.html')

def galeria(request):
    # Caminho para a pasta galeria
    galeria_dir = os.path.join(settings.BASE_DIR, 'artistas', 'static', 'artistas', 'images', 'galeria')
    
    imagens = []
    
    # Verifica se a pasta existe
    if os.path.exists(galeria_dir):
        # Lista todos os arquivos na pasta
        for nome_arquivo in os.listdir(galeria_dir):
            # Verifica se é uma imagem ou vídeo
            extensao = nome_arquivo.lower()
            if (extensao.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.tiff')) or 
                extensao.endswith(('.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv', '.m4v'))):
                
                caminho_completo = os.path.join(galeria_dir, nome_arquivo)
                
                # Obtém informações do arquivo
                try:
                    tamanho = os.path.getsize(caminho_completo)
                    # Converte para KB ou MB
                    if tamanho < 1024 * 1024:
                        tamanho_formatado = f"{tamanho / 1024:.1f} KB"
                    else:
                        tamanho_formatado = f"{tamanho / (1024 * 1024):.1f} MB"
                except:
                    tamanho_formatado = "N/A"
                
                # Extrai o nome sem extensão
                nome_sem_extensao = os.path.splitext(nome_arquivo)[0]
                
                # Determina o tipo de arquivo
                tipo_arquivo = os.path.splitext(nome_arquivo)[1].upper().replace('.', '')
                
                # Determina se é imagem ou vídeo
                if extensao.endswith(('.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv', '.m4v')):
                    tipo_midia = 'video'
                    numero_imagem = len([x for x in imagens if x['tipo_midia'] == 'image']) + 1
                    nome_amigavel = f"Vídeo {numero_imagem}"
                else:
                    tipo_midia = 'image'
                    numero_imagem = len([x for x in imagens if x['tipo_midia'] == 'image']) + 1
                    nome_amigavel = f"Imagem {numero_imagem}"
                
                # Cria um nome amigável baseado no número da imagem
                numero_imagem = len(imagens) + 1
                nome_amigavel = f"Arquivo {numero_imagem}"
                
                imagens.append({
                    'nome': nome_arquivo,
                    'nome_sem_extensao': nome_sem_extensao,
                    'caminho': f'artistas/images/galeria/{nome_arquivo}',
                    'tamanho': tamanho_formatado,
                    'tipo': tipo_arquivo,
                    'alt': nome_amigavel,
                    'numero': numero_imagem,
                    'tipo_midia': tipo_midia
                })
        
        # Ordena as imagens por nome
        imagens.sort(key=lambda x: x['nome'].lower())
    
    return render(request, 'artistas/galeria.html', {
        'imagens': imagens,
        'total_imagens': len(imagens)
    })

def urias_album(request):
    return render(request, 'artistas/albuns/urias.html')

def furia_album(request):
    return render(request, 'artistas/albuns/furia.html')

def hermind_album(request):
    return render(request, 'artistas/albuns/hermind.html')
