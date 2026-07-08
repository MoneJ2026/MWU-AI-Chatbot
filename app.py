import streamlit as st
from chatbot import get_answer

st.set_page_config(
    page_title="MWU AI Chatbot",
    page_icon="🎓"
   )

st.title("🎓 MWU AI Chatbot perfect ")
st.write("Gaaffii :")

question = st.text_input("enter your question please  ")

if st.button("Ergi"):
    if question.strip() == "":
        st.warning("Maaloo .")
    else:
        answer = get_answer(question)
        st.success(answer)
      