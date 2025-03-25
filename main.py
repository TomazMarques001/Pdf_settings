import os
from PyPDF2 import PdfMerger

# Caminho da pasta onde estão os PDFs
pasta = 'C:/Users/tomaz/Downloads/NAED'

# Caminho do arquivo PDF final
arquivo_combinado = 'C:/Users/tomaz/Downloads/Conselho escolar NAED Leste.pdf'

# Cria uma instância do PdfMerger
merger = PdfMerger()

# Verifica se o arquivo combinado já existe
if os.path.exists(arquivo_combinado):
    # Se existir, abre o arquivo combinado para adicionar novos PDFs
    merger.append(arquivo_combinado)

# Lista todos os arquivos da pasta
arquivos = os.listdir(pasta)

# Filtra apenas os arquivos que terminam com .pdf
pdfs = [arq for arq in arquivos if arq.endswith('.pdf')]

# Adiciona os PDFs ao merge
for pdf in pdfs:
    caminho_pdf = os.path.join(pasta, pdf)
    merger.append(caminho_pdf)

# Cria ou atualiza o arquivo final combinado
merger.write(arquivo_combinado)
merger.close()

print("PDFs combinados com sucesso!")
