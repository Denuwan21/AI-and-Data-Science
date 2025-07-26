import streamlit as st
from llm_model import model_function
st.set_page_config(page_title="Chat with HR Database", layout="wide")

st.header("LLM Model Streamlit App Chat with HR Database")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#st.set_page_config(page_title="Chat with HR Database", layout="wide")
st.sidebar.title("History")

for i, chat in enumerate(st.session_state.chat_history):
    if st.sidebar.button(f"{chat['question'][:30]}...", key=f"chat_{i}"):
        st.session_state.selected_chat = i

if 'selected_chat' in st.session_state:
    sel = st.session_state.selected_chat
    st.subheader("📌 Selected Previous Chat")
    st.write("**Question:**", st.session_state.chat_history[sel]['question'])
    st.write("**Answer:**", st.session_state.chat_history[sel]['answer'])

Question = st.text_area("Ake me...")

if Question:
    llm_model = model_function()
    answer = llm_model.run(Question)

    st.session_state.chat_history.append({
        'question': Question,
        'answer': answer
    })

    st.header("Answer")
    st.write(answer)