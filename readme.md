# Validação-de-PDF-com-ChatGPT

Este script Python lê automaticamente múltiplos arquivos PDF de várias subpastas dentro de uma pasta raiz, extrai o texto e usa o modelo GPT-4 para avaliar se uma disciplina é equivalente com base nos conteúdos desses PDFs. O script é destinado para coordenadores acadêmicos que precisam validar disciplinas com base em ementas ou programas de cursos.

## Requisitos

- Python 3.x
- Biblioteca PyPDF2
- Biblioteca openai
- Biblioteca os

## Instalação

1. Clone este repositório.
2. Instale os pacotes Python necessários usando o pip.
    ```bash
    pip install PyPDF2 openai
    ```

## Configuração

Substitua o texto de espaço reservado `"PLACEHOLDER"` pela sua chave API do OpenAI real.

```python
openai.api_key = "PLACEHOLDER"

##Como Usar
Coloque suas subpastas contendo os arquivos PDF que você deseja avaliar dentro da pasta raiz chamada Alunos. Certifique-se de que cada subpasta represente um pedido único de validação de disciplina.

Ative o ambiente virtual Python no Windows:

```bash
.\venv\Scripts\Activate

Execute o script:

```bash
python test.py

O script produzirá os resultados, indicando se a disciplina é equivalente e fornecendo uma porcentagem de similaridade.

##Funções
read_pdf(file_path: str) -> str
Lê um arquivo PDF e retorna o seu conteúdo textual.

send_to_chatgpt(text: str, prompt: str) -> str
Envia o texto extraído e um prompt personalizado para o modelo GPT-4 e retorna o texto gerado como resposta.
