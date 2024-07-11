import subprocess
import os
from weasyprint import HTML

# Cria o diretório "results" se não existir
if not os.path.exists('results'):
    os.makedirs('results')

def render_quarto_document(archive):
    command = ["quarto", "render", archive]
    
    try:
        # Executa o comando
        subprocess.run(command, check=True)
        print(f"Documento Quarto {archive} renderizado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao renderizar o documento Quarto: {e}")

# Chama a função para renderizar o documento Quarto
for l in ['cv_pt.qmd', 'cv_en.qmd', 'cv_es.qmd']:
    render_quarto_document(l)
    print(f"done for '{l}'")

# Transformar em PDF ---------------------------------
# Lista de arquivos HTML gerados
html_files = ['cv_en.html', 'cv_es.html', 'cv_pt.html']

# Converte cada arquivo HTML para PDF e salva na pasta "results"
for html_file in html_files:
    pdf_file = os.path.join('results', html_file.replace('.html', '.pdf'))
    HTML(html_file).write_pdf(pdf_file)
    print(f"{html_file} convertido para {pdf_file}")

# Move os arquivos HTML para o diretório "results"
for html_file in html_files:
    os.rename(html_file, os.path.join('results', html_file))
    print(f"{html_file} movido para a pasta 'results'")
