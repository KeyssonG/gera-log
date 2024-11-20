from flask import Flask, render_template, request, redirect, url_for
import logging
from datetime import datetime
import os

app = Flask(__name__)

# Configuração do arquivo de log
log_dir = '/logs'
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'application.log')

# Configurar o logging
logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(module)s %(threadName)s %(message)s')

@app.route('/')
def home():
    return render_template('index.html')  # Rendeiza o front-end (index.html)

@app.route('/generate_log', methods=['POST'])
def generate_log():
    log_type = request.form['log_type']
    message = request.form['message']
    
    if log_type == 'DEBUG':
        logging.debug(message)
    elif log_type == 'INFO':
        logging.info(message)
    elif log_type == 'WARNING':
        logging.warning(message)
    elif log_type == 'ERROR':
        logging.error(message)

    return redirect(url_for('home'))  # Redireciona de volta para o front-end após a geração do log

@app.route('/generate_batch', methods=['POST'])
def generate_batch():
    batch_size = int(request.form['batch_size'])
    for _ in range(batch_size):
        logging.info(f"Batch log entry at {datetime.now()}")
    return redirect(url_for('home'))  # Redireciona de volta para o front-end

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082, debug=True)
