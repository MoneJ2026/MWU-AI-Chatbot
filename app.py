import streamlit as st
from chatbot import get_answer

st.set_page_config(
    page_title="MWU AI Chatbot",
    page_icon="🎓"
)

st.title("🎓 MWU AI Chatbot")
st.write("Gaaffii kee barreessi:")

question = st.text_input("Gaaffii:")

if st.button("Ergi"):
    if question.strip() == "":
        st.warning("Maaloo gaaffii barreessi.")
    else:
        answer = get_answer(question)
        st.success(answer)