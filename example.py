import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Настройка страницы
st.set_page_config(page_title="Презентация Streamlit", layout="wide")
st.sidebar.title("Разделы")

# Словарь разделов
sections = {
    "Общая характеристика ПО": "1",
    "Установка": "2",
    "Работа с текстом": "3",
    "Таблицы": "4",
    "Научная графика": "5",
    "Элементы графического интерфейса": "6",
    "Составные области": "7",
    "Расчетная программа с параметрическим вводом": "8",
    "Компоновка страницы": "9",
    "Многостраничный документ": "10",
}

# Выбор раздела
choice = st.sidebar.radio("Выберите раздел", list(sections.keys()))

# Раздел 1: Общая характеристика ПО
if choice == "Общая характеристика ПО":
    st.write("""
    Streamlit — это фреймворк с открытым исходным кодом для языка программирования Python, который позволяет быстро создавать интерактивные веб-приложения для анализа данных и машинного обучения. 
    
    ##### Особенности:
    + **Виджеты и визуализация.** В Streamlit есть встроенные стандартные виджеты для частых действий, например ползунки или поля для ввода текста. Можно отрисовать график или картинку, вывести результат работы программы в виде схемы или таблицы.
    + **Интерактивность.** Каждый раз, когда пользователь взаимодействует с веб-интерфейсом или разработчик меняет что-то в коде, Streamlit сам обновляет и перерисовывает нужные части страницы.
    + **Быстрое развертывание.** Достаточно нескольких десятков строк кода, и веб-приложение готово, отрисовано и работает.
    + **Открытый исходный код.** Любой разработчик может посмотреть, как устроен фреймворк.
    + **Поддержка различных соединений с базами данных.** Streamlit работает с такими базами, как AWS S3, MS SQL Server, Oracle DB и другие.
    """)
    st.write("")
    col1, col2, col3 = st.columns(3)
    with col1:
        file = st.file_uploader("Выберите файл")
    with col2:
        number = st.slider("Выберите номер", 0, 100)
    with col3:
        color = st.color_picker("Выберите цвет")
        st.code("""
        import streamlit as st
        st.write('Привет, Streamlit!')
        """, language="python")

# Раздел 2: Установка
elif choice == "Установка":
    st.header("2. Установка")
    st.write("""
    ### Установка

    ##### Необходимые компоненты
    
    Для установки Streamlit сначала нужно убедиться, что компьютер правильно настроен. В частности, понадобится:
    
    + Python: версия от 3.9 до 3.13;
    + Менеджер среды Python (рекомендуется);
    + Менеджер пакетов Python;
    + Редактор кода.
    
    ##### Установка с помощью командной строки
    
    1. Создайте виртуальную среду в своей директории:
    """)
    st.code("python -m venv myvenv")
    st.write("2. Активируйте среду с помощью одной из следующих команд в зависимости от операционной системы:")
    txt = """
         myvenv\Scripts\activate  #Windows
         source myvenv/bin/activate  #Linux
         """
    st.code(txt)
    st.write("3. Установите Streamlit в среде:")
    st.code("pip install streamlit")
    st.write("4. Проверьте, что установка прошла успешно, запустив пример приложения Streamlit Hello:")
    st.code("streamlit hello")
    st.write("   Если это не помогло, используйте длинную форму команды:")
    st.code("python -m streamlit hello")
    st.write("5. Когда вы закончите использовать эту среду, вернитесь в обычную оболочку, введя:")
    st.code("deactivate")
    st.write("")
    st.markdown("[Справочная информация о установке Streamlit](https://docs.streamlit.io/get-started/installation)")

# Раздел 3: Работа с текстом (markdown, LaTeX)
elif choice == "Работа с текстом":
    st.header("3. Работа с текстом (markdown, LaTeX)")
    st.write("**Пример Markdown:**")
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

    st.write("**Пример LaTeX:**")
    st.code("""
    st.latex(r'E = mc^2')
    """, language="python")
    st.latex(r'E = mc^2')

# Раздел 4: Таблицы
elif choice == "Таблицы":
    st.header("4. Таблицы")
    st.write("**Пример создания таблицы:**")
    st.code("""
    data = pd.DataFrame({
        'Колонка 1': [1, 2, 3, 4],
        'Колонка 2': [10, 20, 30, 40]
    })
    st.table(data)  # Статическая таблица
    st.dataframe(data)  # Интерактивная таблица
    """, language="python")
    # Функция для генерации данных
    def generate_sample_data(rows=10):
        return pd.DataFrame({
            "ID": range(1, rows + 1),
            "Name": [f"Item {i}" for i in range(1, rows + 1)],
            "Category": np.random.choice(["A", "B", "C"], rows),
            "Price": np.random.randint(10, 500, rows),
            "Stock": np.random.randint(0, 100, rows)
        })

    st.title("📊 Интерактивная Таблица в Streamlit")

    # Инициализация данных в session_state
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

# Раздел 5: Научная графика
elif choice == "Научная графика":
    st.header("5. Научная графика")
    st.write("**Пример графика с Matplotlib:**")
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
    st.write("**Пример слайдера и чекбокса:**")
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

# Раздел 7: Составные области
elif choice == "Составные области":
    st.header("7. Составные области")
    st.write("**Пример использования вкладок:**")
    st.code("""
    tab1, tab2 = st.tabs(["Вкладка 1", "Вкладка 2"])
    with tab1:
        st.write("Контент вкладки 1")
    with tab2:
        st.write("Контент вкладки 2")
    """, language="python")
    tab1, tab2 = st.tabs(["Вкладка 1", "Вкладка 2"])
    with tab1:
        st.write("Контент вкладки 1")
    with tab2:
        st.write("Контент вкладки 2")

# Раздел 8: Расчетная программа с параметрическим вводом
elif choice == "Расчетная программа с параметрическим вводом":
    st.header("8. Расчетная программа с параметрическим вводом")
    st.write("**Пример расчета площади круга:**")
    st.code("""
    radius = st.number_input('Введите радиус круга', min_value=0.0, value=1.0)
    area = np.pi * radius ** 2
    st.write(f'Площадь круга с радиусом {radius} равна {area:.2f}')
    """, language="python")
    radius = st.number_input('Введите радиус круга', min_value=0.0, value=1.0)
    area = np.pi * radius ** 2
    st.write(f'Площадь круга с радиусом {radius} равна {area:.2f}')

# Раздел 9: Компоновка страницы
elif choice == "Компоновка страницы":
    st.header("9. Компоновка страницы")
    st.write("**Пример использования колонок:**")
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

# Раздел 10: Многостраничный документ
elif choice == "Многостраничный документ":
    st.header("10. Многостраничный документ")
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
    st.write("**Пример структуры:**")
    st.write("- `main.py`: Главная страница.")
    st.write("- `pages/page1.py`: Первая дополнительная страница.")
    st.write("- `pages/page2.py`: Вторая дополнительная страница.")
