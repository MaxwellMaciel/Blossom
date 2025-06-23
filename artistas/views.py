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
    
    # Parâmetros de filtro vindos da URL
    filtro_tipo = request.GET.get('tipo', '').lower()
    filtro_busca = request.GET.get('busca', '').lower()

    # Verifica se a pasta existe
    if os.path.exists(galeria_dir):
        # Lista todos os arquivos na pasta
        for nome_arquivo in os.listdir(galeria_dir):
            extensao = nome_arquivo.lower()
            if (extensao.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.tiff')) or 
                extensao.endswith(('.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv', '.m4v'))):
                
                caminho_completo = os.path.join(galeria_dir, nome_arquivo)
                try:
                    tamanho = os.path.getsize(caminho_completo)
                    if tamanho < 1024 * 1024:
                        tamanho_formatado = f"{tamanho / 1024:.1f} KB"
                    else:
                        tamanho_formatado = f"{tamanho / (1024 * 1024):.1f} MB"
                except:
                    tamanho_formatado = "N/A"
                
                nome_sem_extensao = os.path.splitext(nome_arquivo)[0]
                tipo_arquivo = os.path.splitext(nome_arquivo)[1].lower().replace('.', '')
                
                # Determina se é imagem ou vídeo
                if extensao.endswith(('.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv', '.m4v')):
                    tipo_midia = 'video'
                else:
                    tipo_midia = 'image'
                
                imagens.append({
                    'nome': nome_arquivo,
                    'nome_sem_extensao': nome_sem_extensao,
                    'caminho': f'artistas/images/galeria/{nome_arquivo}',
                    'tamanho': tamanho_formatado,
                    'tipo': tipo_arquivo,
                    'alt': nome_sem_extensao,
                    'tipo_midia': tipo_midia
                })
        # Ordena as imagens por nome
        imagens.sort(key=lambda x: x['nome'].lower())

    # Aplica os filtros
    if filtro_tipo:
        if filtro_tipo in ['image', 'video']:
            imagens = [img for img in imagens if img['tipo_midia'] == filtro_tipo]
        else:
            imagens = [img for img in imagens if img['tipo'] == filtro_tipo]
    if filtro_busca:
        imagens = [img for img in imagens if filtro_busca in img['nome_sem_extensao'].lower()]

    return render(request, 'artistas/galeria.html', {
        'imagens': imagens,
        'total_imagens': len(imagens),
        'filtro_tipo': filtro_tipo,
        'filtro_busca': filtro_busca
    })

def urias_album(request):
    return render(request, 'artistas/albuns/urias.html')

def furia_album(request):
    return render(request, 'artistas/albuns/furia.html')

def hermind_album(request):
    return render(request, 'artistas/albuns/hermind.html')
