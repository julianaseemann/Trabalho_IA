# iMPORTAR AS BIBLIOTECAS
import streamlit as st
import fitz
from groq import Groq

# Cofigufigurar chave da Groq
# GROQ_API_KEY = "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"
cliente = Groq(api_key = GROQ_API_KEY)

# função para extrair os arquivos     
def extract_files(uploader):
    text = ""
    for pdf in uploader:
        with fitz.open(stream=pdf.read(), filetype="pdf") as doc: 
            for page in doc:
                text += page.get_text("text") 
    return text
    
def chat_with_groq(prompt, context):
    response = client.chat.completions.create(
        model-"1lama-3.3-70b-versatile", 
        messages= [
            {"role": "system","content": "Você é um assistente que responde com b.
            {"role": "user","content": f"{context) \n\Pergunta: (prompt) "}

# CRIAR A INTERFACE
def main():
    st.title("O nome do meu sistema inteligente")
    # Incluir uma imagem de acordo ao sistema escolhido
    with st.sidebar:
        st.header("UPLoader Files")
        uploader = st.file_uploader("Adicione arquivos", type="pdf", accept_multiple_files=True)
    if uploader:
        text = extract_files(uploader)
        st.session_state["document-text"] = text
    user_input = st.text_input("Digite a sua pergunta")



if __name__ == "__main__":
    main()