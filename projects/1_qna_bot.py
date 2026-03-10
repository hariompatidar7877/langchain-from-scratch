from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.title("AskBuddy AI QnA Bot")

st.markdown("MyQnA Bot with langchain and google Gemini !")

# while True:
#     que = input("user : ")
#     if que.lower() in["quit", "bye", "exit"]:
#         print("GoodBye")

#     result = llm.invoke(que)

#     print("AI :", result.content), "\n"

if "messages" not in st.session_state :
    st.session_state.messages = []   #messages ye hamne ek variable banaya hai 


for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown("content")



query = st.chat_input("Ask anythink ? ")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role":"user", "content":"query"})
    result = llm.invoke(query)
    st.chat_message("ai").markdown(result.content)
    st.session_state.messages.append({"role":"ai", "content":"result.content"})
