from PyPDF2 import PdfReader
import openai

def read_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PdfReader(f)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def send_to_chatgpt(text, prompt):
    openai.api_key = "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"
    model_engine = "gpt-4"  # Use "gpt-3.5-turbo" instead of "text-davinci-002"
    max_tokens = 100

    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "Você é o coordenador do curso de engenharia de controle e automação, um aluno está buscando validar uma disciplina já cursada em outra universidade."},
            {"role": "user", "content": prompt},
            {"role": "user", "content": text}
        ],
        max_tokens=max_tokens
    )

    return response['choices'][0]['message']['content'].strip()


if __name__ == "__main__":
    pdf1_content = read_pdf("Alunos Teste\BLU3702_ProjetoIntegrador_Turma_7754.pdf")
    pdf2_content = read_pdf("Alunos Teste\CAC3900_ProjetoEspecializado_Turma_9754.pdf")
    
    combined_content = f"Ementa 1:\n{pdf1_content}\n\nEmenta 2:\n{pdf2_content}"
    
    prompt = "O aluno apresentou as ementas das disciplinas e você precisa validar se a disciplina é equivalente ou não. responda apenas com 'sim' ou 'não' e o percentual de equivalência."
    
    summary = send_to_chatgpt(combined_content, prompt)
    print("Arquivos: " + "BLU3702_ProjetoIntegrador_Turma_7754.pdf" + " e " + "CAC3900_ProjetoEspecializado_Turma_9754.pdf")
    print(f"Summary: {summary}")
