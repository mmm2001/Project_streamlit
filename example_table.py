import streamlit as st
import pandas as pd
import numpy as np
#import emoji

def generate_sample_data(rows=10):
    return pd.DataFrame({
        "ID": range(1, rows + 1),
        "Name": [f"Item {i}" for i in range(1, rows + 1)],
        "Category": np.random.choice(["A", "B", "C"], rows),
        "Price": np.random.randint(10, 500, rows),
        "Stock": np.random.randint(0, 100, rows)
    })

st.title("📊 Интерактивная Таблица в Streamlit")

if "df" not in st.session_state:
    st.session_state.df = generate_sample_data(10)

df = st.session_state.df.copy()

st.subheader("Редактируемая таблица")
edited_df = st.data_editor(df, num_rows="dynamic", key="table_editor")

# Фильтрация по категории
category_filter = st.selectbox("Фильтр по категории", ["Все"] + sorted(df["Category"].unique().tolist()))
if category_filter != "Все":
    edited_df = edited_df[edited_df["Category"] == category_filter]

# Кнопка для добавления случайной строки
if st.button("➕ Добавить строку"):
    new_row = {
        "ID": df["ID"].max() + 1 if not df.empty else 1,
        "Name": f"Item {df.shape[0] + 1}",
        "Category": np.random.choice(["A", "B", "C"]),
        "Price": np.random.randint(10, 500),
        "Stock": np.random.randint(0, 100)
    }
    st.session_state.df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    st.rerun()

# Кнопка для удаления выделенных строк
selected_rows = st.multiselect("Выберите ID строк для удаления", df["ID"].tolist())
if st.button("🗑 Удалить выбранные"):
    st.session_state.df = df[~df["ID"].isin(selected_rows)]
    st.rerun()

# Визуализация
st.subheader("📈 Анализ данных")
st.bar_chart(edited_df.set_index("Name")["Price"])
