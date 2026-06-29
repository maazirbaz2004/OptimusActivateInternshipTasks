import streamlit as st
from google import genai
client = genai.Client(api_key="API_KEY")
st.title("University FAQ Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
user_input = st.chat_input("Ask a question")
if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.write(user_input)
    prompt = """
    You are a university FAQ assistant.
    Answer questions about:
    - Admissions
    - Fees
    - Courses
    - Scholarships
    - Campus facilities
    Keep answers concise and helpful.
    Conversation:
    """
    for msg in st.session_state.messages:
        prompt += f"{msg['role']}: {msg['content']}\n"
    response = client.models.generate_content(model="gemini-2.5-flash",contents=prompt)
    bot_reply = response.text
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)