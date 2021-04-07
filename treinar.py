import streamlit as st
import SessionState
import random
import parabens
import time


def app():
    ss = SessionState.get(x=1, multiplicando=4,
                          multiplicador=4, lista=[], tabuadas=[], pos=0, fim=False, tempo=time.time(), firstrun=True)

    if ss.firstrun:

        ss.tabuadas = st.multiselect('Selecione a tabuada', [
                                     2, 3, 4, 5, 6, 7, 8, 9])
        print(ss.tabuadas, len(ss.tabuadas), ss.firstrun)
        if len(ss.tabuadas) > 0:
            if st.button('Iniciar'):
                print('apertou e selecionou')
                ss.firstrun = False
    else:

        @st.cache(allow_output_mutation=True)
        def tabuada(estud):
            print('Dentro tabuada')
            print(estud)
            lista_estud = []
            tabuada = [[[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0]],
                       [[1, 0, 0], [1, 1, 1], [1, 2, 2], [1, 3, 3], [1, 4, 4], [1, 5, 5],
                        [1, 6, 6], [1, 7, 7], [1, 8, 8], [1, 9, 9], [1, 10, 10]],
                       [[2, 0, 0], [2, 1, 2], [2, 2, 4], [2, 3, 6], [2, 4, 8], [2, 5, 10],
                        [2, 6, 12], [2, 7, 14], [2, 8, 16], [2, 9, 18], [2, 10, 20]],
                       [[3, 0, 0], [3, 1, 3], [3, 2, 6], [3, 3, 9], [3, 4, 12], [3, 5, 15],
                        [3, 6, 18], [3, 7, 21], [3, 8, 24], [3, 9, 27], [3, 10, 30]],
                       [[4, 0, 0], [4, 1, 4], [4, 2, 8], [4, 3, 12], [4, 4, 16], [4, 5, 20],
                        [4, 6, 24], [4, 7, 28], [4, 8, 32], [4, 9, 36], [4, 10, 40]],
                       [[5, 0, 0], [5, 1, 5], [5, 2, 10], [5, 3, 15], [5, 4, 20], [5, 5, 25],
                        [5, 6, 30], [5, 7, 35], [5, 8, 40], [5, 9, 45], [5, 10, 50]],
                       [[6, 0, 0], [6, 1, 6], [6, 2, 12], [6, 3, 18], [6, 4, 24], [6, 5, 30],
                        [6, 6, 36], [6, 7, 42], [6, 8, 48], [6, 9, 54], [6, 10, 60]],
                       [[7, 0, 0], [7, 1, 7], [7, 2, 14], [7, 3, 21], [7, 4, 28], [7, 5, 35],
                        [7, 6, 42], [7, 7, 49], [7, 8, 56], [7, 9, 63], [7, 10, 70]],
                       [[8, 0, 0], [8, 1, 8], [8, 2, 16], [8, 3, 24], [8, 4, 32], [8, 5, 40],
                        [8, 6, 48], [8, 7, 56], [8, 8, 64], [8, 9, 72], [8, 10, 80]],
                       [[9, 0, 0], [9, 1, 9], [9, 2, 18], [9, 3, 27], [9, 4, 36], [9, 5, 45],
                        [9, 6, 54], [9, 7, 63], [9, 8, 72], [9, 9, 81], [9, 10, 90]],
                       [[10, 0, 0], [10, 1, 10], [10, 2, 20], [10, 3, 30], [10, 4, 40], [10, 5, 50], [10, 6, 60], [10, 7, 70], [10, 8, 80], [10, 9, 90], [10, 10, 100]]]

            if len(estud) > 0:
                print(len(estud))
                for i in estud:
                    print(i)
                    for j in tabuada[i]:
                        print(j)
                        lista_estud.append(j)
            random.shuffle(lista_estud)
            return lista_estud
        ss.lista = tabuada(ss.tabuadas)

        if ss.fim:
            parabens.congrats()
            st.balloons()
        else:
            st.title('Vamos estudar Cecilia?')
            st.subheader('Responda abaixo')
            pergunta = str(ss.lista[ss.pos][0]) + ' * ' + \
                str(ss.lista[ss.pos][1]) + ' = ?'
            a = st.text_input(pergunta)
            if a.isnumeric():
                if int(a) == int(ss.lista[ss.pos][2]):

                    if ss.pos < (len(ss.lista)-1):
                        ss.pos += 1
                        if st.button("Próximo"):
                            print(a)
                        st.info('😄 Acertou')
                    else:

                        print('Acabou o treino')
                        delay = round((time.time() - ss.tempo), 2)
                        print('Tempo total: ', delay)
                        st.title(
                            'Parabéns, acabamos o treino hoje, você demorou ' + str(delay) + ' segundos.')
                        ss.fim = True
                        if st.button("finalizar"):
                            print(a)

                else:
                    if st.button("Próximo"):
                        print('Errou: '+pergunta+' Respondeu: '+str(a))
                    st.error('Você errou 🥵')

                # st.text(ss.x)
                # st.write(ss.multiplicando)
                # st.write(ss.multiplicador)
