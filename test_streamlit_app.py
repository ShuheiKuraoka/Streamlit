import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit 入門")

st.write("DateFrame")

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

#st.write(df)
#→表示のみの機能
#st.dataframe(df, width=200, height=200)
#st.dataframe(df.style.highlight_max(axis=0),width=200, height=200)
#style.highlight_max()最大値をハイライト※pandasの機能
#axis=0が行の最大、1が列の最大
st.table(df)