import streamlit as st
import random
import joblib



model= joblib.load("Chatbot_Model.pkl")
vector=joblib.load("tfidf.pkl")
response=joblib.load("responses.pkl")

st.title("Welcome Jitesh Chatbot 😊")
st.write("Ask me Something...→")

if "massage" not in st.session_state:
    st.session_state.massage=[]

for message in st.session_state.massage:
     with st.chat_message(message['role']):
          st.write(message['content'])

user_input = st.chat_input("You :")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
        st.session_state.massage.append({"role":"user","content":user_input
     })
        #st.warning("Plz Enter a Message")
    
        input_vector= vector.transform([user_input]).toarray()
        predict = model.predict(input_vector)[0]

    if predict in response:
        reply =random.choice(response[predict])
        st.success("Jitesh :" + reply)
    else:
        st.error("Sorry, I don't Understand")

    st.session_state.massage.append({"role":"Jitesh","content":reply
    })