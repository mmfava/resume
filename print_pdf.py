
# Biblioteca weasyprint contém função HTML
# responsável por "printar" o html e transforma-lo
# em PDF.
from weasyprint import HTML

# HTML('path/to/doc.html').write_pdf('path/to/output.pdf')
HTML('CV.html').write_pdf('CV.pdf')
