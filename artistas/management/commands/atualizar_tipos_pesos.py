from django.core.management.base import BaseCommand
from artistas.models import MidiaGaleria
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Atualiza o campo tipo e peso de todas as mídias.'

    def handle(self, *args, **options):
        midias = MidiaGaleria.objects.all()
        count = 0
        for midia in midias:
            nome, ext = os.path.splitext(midia.arquivo.name)
            midia.tipo = ext.lower().replace('.', '')
            caminho_arquivo = os.path.join(settings.MEDIA_ROOT, 'galeria', 'midias', os.path.basename(midia.arquivo.name))
            try:
                midia.peso = os.path.getsize(caminho_arquivo)
            except Exception:
                midia.peso = 0
            midia.save()
            count += 1
        self.stdout.write(self.style.SUCCESS(f'Tipo e peso atualizados em {count} mídias.')) 