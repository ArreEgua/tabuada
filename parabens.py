import streamlit as st


def congrats():
    st.title('Parabéns')
    st.subheader('Aos pouquinhos vamos aprendendo.')
    st.text('🤗 Aqui está um prêmio para você 🤗')
    with open('./images/charlie.mp4', 'rb') as video_file:
        video_bytes = video_file.read()
    st.video(video_bytes)
