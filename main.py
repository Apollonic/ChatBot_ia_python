# título
# input do chat (campo de mensagem)
# a cada mensagem que o usuário enviar:
# mostrar a mensagem que o usuário enviou no chat
# pegar a pergunta e enviar para uma IA responder
# exibir a resposta da IA na tela

# StreamLit -> apenas python para front e backend
# a ia que vamos usar: OpenIA

import streamlit as st
from openai import OpenAI

# aqui eu uso uma versão grátis!
modelo_ia = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

st.write("# BombIA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] =  [
        {"role": "system", "content": "Você é um assistente útil e deve responder sempre em português do Brasil."}
    ]


for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]

    if role != "system": 
        st.chat_message(role).write(content)

texto_user = st.chat_input("Gostaria de saber....")

# se texto_user existe, executa:
if texto_user:
    st.chat_message("user").write(texto_user)
    mensagem_user = {"role":"user","content":texto_user}
    st.session_state["lista_mensagens"].append(mensagem_user)

    # ia respondeu
    
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="llama-3.3-70b-versatile"        
    )
    
    texto_resposta_ia = resposta_ia.choices[0].message.content
    
    

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role":"assistant","content":texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
    