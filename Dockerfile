# Usar uma imagem Python
FROM python:3.10-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos para o container
COPY gera_log.py /app/gera_log.py
COPY requirements.txt /app/requirements.txt
COPY templates /app/templates  

# Instalar as dependências
RUN pip install -r requirements.txt

# Expor a porta 5000 (como definida na aplicação Flask)
EXPOSE 5000

# Comando para rodar o servidor Flask
CMD ["python", "gera_log.py"]
