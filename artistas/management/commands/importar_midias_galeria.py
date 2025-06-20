from django.core.management.base import BaseCommand
from artistas.models import MidiaGaleria
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Importa imagens e vídeos já existentes na pasta galeria para o banco de dados.'

    def handle(self, *args, **options):
        pasta_galeria = os.path.join(settings.BASE_DIR, 'media', 'galeria', 'midias')
        arquivos = os.listdir(pasta_galeria)
        count = 0
        for arquivo in arquivos:
            caminho_arquivo = os.path.join('galeria/midias', arquivo)
            nome, ext = os.path.splitext(arquivo)
            ext = ext.lower().replace('.', '')
            if ext in ['jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp', 'tiff']:
                tipo = ext
            elif ext in ['mp4', 'mov', 'avi', 'mkv', 'wmv', 'flv', 'webm', 'm4v']:
                tipo = ext
            else:
                continue
            peso = os.path.getsize(os.path.join(pasta_galeria, arquivo))
            if not MidiaGaleria.objects.filter(arquivo=caminho_arquivo).exists():
                MidiaGaleria.objects.create(
                    titulo=nome,
                    arquivo=caminho_arquivo,
                    tipo=tipo,
                    peso=peso
                )
                count += 1
        self.stdout.write(self.style.SUCCESS(f'{count} mídias importadas com sucesso!')) 