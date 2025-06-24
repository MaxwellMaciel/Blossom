# Galeria++

Uma aplicação Django para gerenciamento de galeria de artistas.

## Instalação Local

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário (opcional):
   ```bash
   python manage.py createsuperuser
   ```

6. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

## Deploy no Railway

O projeto está configurado para deploy no Railway com os seguintes arquivos:

- `requirements.txt` - Dependências Python
- `Procfile` - Configuração do processo web
- `runtime.txt` - Versão do Python
- Configurações de produção no `settings.py`

### Variáveis de Ambiente no Railway

Configure as seguintes variáveis de ambiente no Railway:

- `SECRET_KEY` - Chave secreta do Django
- `DEBUG` - Defina como 'False' para produção

## Estrutura do Projeto

- `artistas/` - App principal com modelos e views
- `galeria/` - Configurações do projeto Django
- `static/` - Arquivos estáticos (CSS, JS, imagens)
- `templates/` - Templates HTML 