#!/bin/bash
# Script de build para Railway

echo "Iniciando build..."

# Instalar dependências
pip install -r requirements.txt

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Executar migrações
python manage.py migrate

echo "Build concluído!" 