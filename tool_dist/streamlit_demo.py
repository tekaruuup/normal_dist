import streamlit as st
import plotly.express as px
import random
import pandas as pd
import numpy as np
from config_pass import login

def test_num(random_seed, avg, sig, size):
    np.random.seed(seed=random_seed)
    num = np.random.normal(avg, sig, size)
    return num

def plot(seed, avg, sig, size):
    data = pd.DataFrame(test_num(seed, avg, sig, size), columns=["success"])
    data.reset_index(inplace=True)
    data = data.rename(columns={'index':'try'})
    fig = px.histogram(
        data,
        x="success"
    )
    st.plotly_chart(fig, use_container_width=True)



def view():
    login()
    st.title('正規分布のシミュレーションをしてみよう！')

    c_top = st.container()
    c_button = st.empty()

    st.subheader('設定')
    optional_avg = st.number_input('平均を入力してください',0)
    optional_sigma = st.number_input('標準偏差を入力してください',0)
    optional_try = st.number_input('実験回数を入力してください', 1)
    optional_seed = st.number_input('乱数seedを入力してください', 0)

    if c_button.button('実行'):
        plot(optional_seed, optional_avg, optional_sigma, optional_try)
        c_top.info('All process is done!')

view()