# Gerador de Currículos Multilíngues

Este repositório contém scripts para gerar currículos em HTML e PDF em três idiomas diferentes (Português, Inglês e Espanhol) utilizando Quarto e WeasyPrint. Os currículos são personalizados e formatados com base em um arquivo `.qmd` e dados de uma planilha Google.

## Funcionalidades

- Geração de currículos em HTML e PDF.
- Suporte a três idiomas: Português, Inglês e Espanhol.
- Personalização do conteúdo com base em dados de uma planilha Google.
- Estilização personalizada com CSS.

## Pré-requisitos

- [Quarto](https://quarto.org/)
- [WeasyPrint](https://weasyprint.org/)
- Python 3.x
- Bibliotecas Python:
  - pandas
  - weasyprint

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/mmfava/resume.git
cd resume
```

2. Instale as bibliotecas necessárias:

```bash
pip install pandas weasyprint
```

3. Certifique-se de ter o Quarto instalado e configurado no seu PATH.

## Como Usar

### Passo 1: Configurar a Planilha Google

A planilha Google deve conter as seguintes colunas:

- `lenguage`: Idioma do currículo (PT, EN, ES).
- `order`: Ordem de exibição das seções no currículo.
- `type`: Tipo da seção (Educação, Experiência, etc.).
- `what`: Título ou descrição da experiência/educação.
- `start`: Ano de início.
- `end`: Ano de término.
- `where_1`: Instituição ou empresa.
- `where_2`: Local específico (campus, departamento, etc.).
- `region`: Região (cidade, estado).
- `country`: País.
- `details_1`: Detalhes adicionais (cursos relevantes, atividades, etc.).
- `details_2`: Mais detalhes adicionais.
- `details_3`: Ainda mais detalhes adicionais.
- `worktools`: Ferramentas de trabalho usadas.

### Passo 2: Atualizar o Link da Planilha

No script Python, atualize o link da planilha Google para o seu próprio link exportável:

```python
csv_url = 'https://docs.google.com/spreadsheets/d/1h-kFMxdNLBDoanj2kMOimbAMGKqmacwB8Kc_rAcP9Xo/export?format=csv'
```

### Passo 3: Executar o Script Python

Execute o script Python para renderizar os currículos em HTML e convertê-los para PDF:

```python
import subprocess

def render_quarto_document(archive):
    command = ["quarto", "render", archive]
    
    try:
        subprocess.run(command, check=True)
        print("Documento Quarto renderizado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao renderizar o documento Quarto: {e}")

# Chama a função para renderizar o documento Quarto
for l in ['cv_pt.qmd', 'cv_en.qmd', 'cv_es.qmd']:
    render_quarto_document(l)
    print(f"done for '{l}'")

# Transformar em PDF
from weasyprint import HTML

HTML('cv_en.html').write_pdf('cv_en.pdf')
HTML('cv_es.html').write_pdf('cv_es.pdf')
HTML('cv_pt.html').write_pdf('cv_pt.pdf')
```

### Passo 4: Gerar os PDFs

O script acima renderiza os currículos em HTML e depois os converte para PDF utilizando WeasyPrint.Os arquivos serão salvos em "results".

## Estrutura do Repositório

```plaintext
resume/
├── cv_en.qmd
├── cv_es.qmd
├── cv_pt.qmd
├── custom.css
├── generate_cvs.py
├── results
└── README.md
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request. Futuramente, pretendo transformar a configuração da planilha em uma função para facilitar o processo de geração dos currículos.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Marília Melo Favalesso  
[LinkedIn](https://www.linkedin.com/in/mariliafavalesso/) | [GitHub](https://github.com/mmfava)
