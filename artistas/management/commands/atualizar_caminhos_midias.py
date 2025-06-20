from django.core.management.base import BaseCommand
from artistas.models import MidiaGaleria

class Command(BaseCommand):
    help = 'Atualiza os caminhos dos arquivos de mídia no banco de dados.'

    def handle(self, *args, **options):
        midias = MidiaGaleria.objects.all()
        count = 0
        for midia in midias:
            if 'artistas/images/galeria' in midia.arquivo.name:
                novo_caminho = midia.arquivo.name.replace('artistas/images/galeria\\', 'galeria/midias/')
                novo_caminho = novo_caminho.replace('artistas/images/galeria/', 'galeria/midias/')
                midia.arquivo.name = novo_caminho
                midia.save()
                count += 1
        self.stdout.write(self.style.SUCCESS(f'Caminhos atualizados em {count} mídias.')) 