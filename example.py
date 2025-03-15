# presentation.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Настройка страницы
st.set_page_config(page_title="Презентация Streamlit", layout="wide")
st.sidebar.title("Разделы")

sections = {
    "Общая характеристика ПО":"1",
    "Установка":"2",
    "Работа с текстом":"3",
    "Таблицы":"4",
    "Научная графика":"5",
    "Элементы графического интерфейса":"6",
    "Составные области":"7",
    "Расчетная программа с параметрическим вводом":"8",
    "Кмопоновка страницы":"9",
    "Многостраничный документ":"10",
}

choice = st.sidebar.radio("Выберите раздел", list(sections.keys()))

st.title(choice)
st.write(sections[choice])

# Заголовок презентации
st.title("Презентация Streamlit")

# Раздел 1: Общая характеристика ПО
if choice == "Общая характеристика ПО":
    st.header("1. Общая характеристика ПО")
    st.write("""
    Streamlit — это библиотека для создания интерактивных веб-приложений на Python.
    Она позволяет быстро создавать прототипы и презентации.
    """)
    st.code("""
    import streamlit as st
    st.write('Привет, Streamlit!')
    """, language="python")

# Раздел 2: Установка
elif choice == "Установка":
    st.header("2. Установка")
    st.write("Установите Streamlit с помощью pip:")
    st.code("""
    pip install streamlit
    """, language="bash")
    st.write("Запустите приложение:")
    st.code("""
    streamlit run ваш_скрипт.py
    """, language="bash")

# Раздел 3: Работа с текстом (markdown, LaTeX)
elif choice == "Работа с текстом":
    st.header("3. Работа с текстом (markdown, LaTeX)")
    st.write("Пример Markdown:")
    st.code("""
    st.markdown('''
    ### Заголовок
    - **Жирный текст**
    - *Курсив*
    - [Ссылка](https://streamlit.io)
    ''')
    """, language="python")
    st.markdown('''
    ### Заголовок
    - **Жирный текст**
    - *Курсив*
    - [Ссылка](https://streamlit.io)
    ''')

    st.write("Пример LaTeX:")
    st.code("""
    st.latex(r'E = mc^2')
    """, language="python")
    st.latex(r'E = mc^2')

# Раздел 4: Таблицы
elif choice == "Таблицы":
    st.header("4. Таблицы")
    st.write("Пример создания таблицы:")
    st.code("""
    data = pd.DataFrame({
        'Колонка 1': [1, 2, 3, 4],
        'Колонка 2': [10, 20, 30, 40]
    })
    st.table(data)  # Статическая таблица
    st.dataframe(data)  # Интерактивная таблица
    """, language="python")
    data = pd.DataFrame({
        'Колонка 1': [1, 2, 3, 4],
        'Колонка 2': [10, 20, 30, 40]
    })
    st.table(data)
    st.dataframe(data)

# Раздел 5: Научная графика
elif choice == "Научная графика":
    st.header("5. Научная графика")
    st.write("Пример графика с Matplotlib:")
    st.code("""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('График функции sin(x)')
    st.pyplot(fig)
    """, language="python")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('График функции sin(x)')
    st.pyplot(fig)

# Раздел 6: Элементы графического интерфейса
elif choice == "Элементы графического интерфейса":
    st.header("6. Элементы графического интерфейса")
    st.write("Пример слайдера и чекбокса:")
    st.code("""
    slider_value = st.slider('Выберите значение', 0, 100, 50)
    st.write(f'Вы выбрали: {slider_value}')

    checkbox_value = st.checkbox('Показать текст')
    if checkbox_value:
        st.write('Этот текст виден только если галочка поставлена.')
    """, language="python")
    slider_value = st.slider('Выберите значение', 0, 100, 50)
    st.write(f'Вы выбрали: {slider_value}')

    checkbox_value = st.checkbox('Показать текст')
    if checkbox_value:
        st.write('Этот текст виден только если галочка поставлена.')

# Раздел 7: Расчетная программа с параметрическим вводом
elif choice == "Расчетная программа с параметрическим вводом":
    st.header("7. Расчетная программа с параметрическим вводом")
    st.write("Пример расчета площади круга:")
    st.code("""
    radius = st.number_input('Введите радиус круга', min_value=0.0, value=1.0)
    area = np.pi * radius ** 2
    st.write(f'Площадь круга с радиусом {radius} равна {area:.2f}')
    """, language="python")
    radius = st.number_input('Введите радиус круга', min_value=0.0, value=1.0)
    area = np.pi * radius ** 2
    st.write(f'Площадь круга с радиусом {radius} равна {area:.2f}')

# Раздел 8: Компоновка страницы
elif choice == "Компоновка страницы":
    st.header("8. Компоновка страницы")
    st.write("Пример использования колонок:")
    st.code("""
    col1, col2 = st.columns(2)
    with col1:
        st.write('Это левая колонка')
        st.button('Кнопка 1')
    with col2:
        st.write('Это правая колонка')
        st.button('Кнопка 2')
    """, language="python")
    col1, col2 = st.columns(2)
    with col1:
        st.write('Это левая колонка')
        st.button('Кнопка 1')
    with col2:
        st.write('Это правая колонка')
        st.button('Кнопка 2')

# Раздел 9: Многостраничный документ
elif choice == "Многостраничный документ":
    st.header("9. Многостраничный документ")
    st.write("""
    Streamlit поддерживает многостраничные приложения. Создайте папку `pages` и добавьте туда файлы `.py`.
    """)
    st.code("""
    your_app/
    ├── main.py
    └── pages/
        ├── page1.py
        └── page2.py
    """, language="plaintext")
