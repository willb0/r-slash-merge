import streamlit as st
import streamlit_pydantic as sp
import requests
from models import LinkRequest

data = sp.pydantic_form(key='dat way',model = LinkRequest)
if data:
    st.json(data.json())
    print(data)
    print(type(data))
    res = requests.post('http://pipeline:82/compilation',data=data.json())
    with open('video.mp4','wb+') as f:
        f.write(res.content)
    st.video('video.mp4')


