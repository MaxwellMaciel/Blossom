from django.core.management.base import BaseCommand
from artistas.models import MidiaGaleria

class Command(BaseCommand):
    help = 'Lista os primeiros caminhos de arquivos de mídia no banco de dados.'

    def handle(self, *args, **options):
        midias = MidiaGaleria.objects.all()[:20]
        for midia in midias:
            self.stdout.write(midia.arquivo.name) 