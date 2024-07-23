# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요.') #두번째 인자로 예시가 제공될 수 있음.

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = chat_model.predict(content + "에 대한 시를 써줘") #invoke는 줄바꿈이 안됨
        # result = llm.predict("write a poem about " + content + ": ")
        st.write(result) #문자 그 자체 또는 결과값이 출력됨.

# llm = CTransformers(
#     model="llama-2-7b-chat.ggmlv3.q2_K.bin",
#     model_type="llama"
# )