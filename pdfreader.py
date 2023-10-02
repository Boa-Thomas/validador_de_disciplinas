
from PyPDF2 import PdfReader
import openai
import os
import re

def read_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PdfReader(f)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Extract the file name from the file path
    file_name = file_path.split("\\")[-1]  # Replace "/" with "\\" if you are on Windows

    # Use regular expression to check the filename pattern
    if re.match(r"^[a-zA-Z]{3}\d{4}", file_name):
        return extract_course_info(text)  # If the filename starts with 3 letters followed by 4 numbers, send the text to funcb
    else:
        return text  # Otherwise, return the text as is

def extract_course_info(text):
    course_info = {}
    
    # Extracting Nome da Disciplina using the specific code format
    nome_match = re.search(r'(\w{3}\d{4})\s+([\w\s-]+)\s+\d+\s+\d+\s+-?\d*\s+\d+', text)
    if nome_match:
        course_info['Nome da Disciplina'] = nome_match.group(2).strip()
    
    # Extracting Ementa
    ementa_match = re.search(r'Ementa:\s*(.*?)(Objetivos:|$)', text, re.S)
    if ementa_match:
        course_info['Ementa'] = ementa_match.group(1).strip().replace("\n", " ")
    
    # Extracting Objetivos
    objetivos_match = re.search(r'Objetivos:\s*(.*?)(Conteúdo programático:|$)', text, re.S)
    if objetivos_match:
        course_info['Objetivos'] = objetivos_match.group(1).strip().replace("\n", " ")

    # Extracting Conteúdo programático
    conteudo_match = re.search(r'Conteúdo programático:\s*(.*?)(Metodologia de ensino:|$)', text, re.S)
    if conteudo_match:
        course_info['Conteúdo programático'] = conteudo_match.group(1).strip().replace("\n", " ")
        
    return course_info


#print(read_pdf("Alunos\Aluno Teste 1\BLU3702_ProjetoIntegrador_Turma_7754.pdf"))
# Using the function
#course_info = extract_course_info(textoo)
#Printing the result
#for key, value in course_info.items():
#    print(f"{key}: {value}")
