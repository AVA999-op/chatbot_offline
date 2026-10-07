import utils
import streamlit as st

st.title('CHATBOT PROJECT')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role':'ai', 'content':'how can i help you'}]

for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

prompt = st.chat_input()
model = 'qwen2.5-coder:7b'

if prompt:

    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role':'user','content':prompt}) 

    with st.spinner('Generating Response ....'):
        new_prompt = 'describe your answer using emojies and examples and description' + prompt
        response = utils.call_ollama_model(model,new_prompt)

    st.chat_message('ai').write(response)
    st.session_state['messages'].append({'role':'ai','content':response})
