from PyPDF2 import PdfReader
import openai
import os
import re
from pdfreader import extract_course_info

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


def send_to_chatgpt(text, prompt):
    openai.api_key = "PLACEHOLDER"
    model_engine = "gpt-4"
    max_tokens = 100

    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "Você é o coordenador do curso de engenharia de controle e automação, um aluno está buscando validar uma disciplina já cursada em outra universidade."},
            {"role": "user", "content": text},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )

    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    results = []
    root_folder = "Alunos"

    for subdir, _, files in os.walk(root_folder):
        if files:  # Check if folder contains files
            pdf_contents = []
            for file in files:
                if file.endswith('.pdf'):
                    pdf_path = os.path.join(subdir, file)
                    pdf_content = read_pdf(pdf_path)
                    pdf_contents.append(pdf_content)

            combined_content = f"\n\n".join([f"Ementa {idx+1}:\n{content}" for idx, content in enumerate(pdf_contents)])

            prompt = "Um aluno apresentou as ementas das disciplinas e você precisa verificar se a disciplina é equivalente ou não, leve em consideração o conteudo os objetivos e a carga horaria das disciplinas. Responda APENAS com 'sim' ou 'não' e um percentual de similaridade (Ex: Sim 90%).\n\n"

            summary = send_to_chatgpt(combined_content, prompt)
            results.append(f"Pasta: {subdir}\nResposta: {summary}\n")

    print("Results:")
    for result in results:
        print(result)
