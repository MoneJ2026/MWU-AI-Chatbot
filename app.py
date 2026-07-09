import streamlit as st
from chatbot import get_response


# Page configuration
st.set_page_config(
    page_title="MWU AI Chatbot",
    page_icon="🎓"
)


st.title("🎓 MWU AI Chatbot")
st.write("Ask me anything about Madda Walabu University")


# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# User input
user_message = st.chat_input("Write your question...")


if user_message:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message("user"):
        st.write(user_message)


    # Get chatbot response
    response = get_response(user_message)


    # Show chatbot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.write(response)