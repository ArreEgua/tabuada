from PIL import Image
import streamlit as st


# Carregando Imagens em memória
list_images = [list]
for i in range(1, 11):
    list_images.append(Image.open('./images/tab_{}.png'.format(i)))


def app():

    # Carregar imagens
    placeholder = st.empty()

    with placeholder.beta_container():
        # option = st.selectbox('Escolha o multiplicador?',
        #                       ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        option = st.number_input('Selecione Multiplicador:',
                                 min_value=1, max_value=10)
        st.image(list_images[int(option)],
                 caption='Tabuada de {}'.format(option))
