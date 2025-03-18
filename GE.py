import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
import plotly.express as px
from io import BytesIO
import time 

menu = st.sidebar.radio('***',
    (
    "Элементы ввода",
    "Элементы вывода",
    "Медиа элементы",
    "Элементы прогресса и статуса",
    "Макеты",
    "Прочие элементы",
    )
)

if menu == "Элементы ввода":
    st.title("Элементы ввода Streamlit")
    st.markdown("---")

    # Кнопка
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Кнопка (Button)")
        st.code('''
clicked = st.button(
    label="Нажми меня",
    key="btn1",
    help="Это пример кнопки",
    disabled=False
)
''', language='python')

    with col2:
        st.subheader("Пример")
        clicked = st.button(
            label="Нажми меня",
            key="btn1",
            help="Это пример кнопки",
            disabled=False
        )
        st.write(f"Состояние кнопки: {clicked}")
        st.markdown("---")

    # Текстовый ввод
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("2. Текстовый ввод (Text Input)")
        st.code('''
text = st.text_input(
    label="Введите текст",
    value="Привет!",
    max_chars=50,
    placeholder="Введите что-нибудь...",
    help="Это текстовое поле",
    key="text_input1"
)
''', language='python')

    with col2:
        st.subheader("Пример")
        text = st.text_input(
            label="Введите текст",
            value="Привет!",
            max_chars=50,
            placeholder="Введите что-нибудь...",
            help="Это текстовое поле",
            key="text_input1"
        )
        st.write(f"Введённый текст: {text}")
        st.markdown("---")

    # Слайдер
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("3. Слайдер (Slider)")
        st.code('''
slider_val = st.slider(
    label="Выберите значение",
    min_value=0,
    max_value=100,
    value=50,
    step=5,
    format="%d%%",
    key="slider1"
)
''', language='python')

    with col2:
        st.subheader("Пример")
        slider_val = st.slider(
            label="Выберите значение",
            min_value=0,
            max_value=100,
            value=50,
            step=5,
            format="%d%%",
            key="slider1"
        )
        st.write(f"Выбрано: {slider_val}%")
        st.markdown("---")

    # Выпадающий список
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("4. Selectbox")
        st.code('''
option = st.selectbox(
    label="Выберите вариант",
    options=["Python", "JavaScript", "Java", "C++"],
    index=0,
    format_func=lambda x: x.upper(),
    help="Выберите язык программирования",
    key="selectbox1"
)
''', language='python')

    with col2:
        st.subheader("Пример")
        option = st.selectbox(
            label="Выберите вариант",
            options=["Python", "JavaScript", "Java", "C++"],
            index=0,
            format_func=lambda x: x.upper(),
            help="Выберите язык программирования",
            key="selectbox1"
        )
        st.write(f"Выбран: {option}")
        st.markdown("---")

    # Множественный выбор
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("5. Multiselect")
        st.code('''
selected = st.multiselect(
    label="Выберите технологии",
    options=["Python", "SQL", "Docker", "AWS", "PyTorch"],
    default=["Python"],
    help="Выберите нужные технологии",
    key="multiselect1"
)
''', language='python')

    with col2:
        st.subheader("Пример")
        selected = st.multiselect(
            label="Выберите технологии",
            options=["Python", "SQL", "Docker", "AWS", "PyTorch"],
            default=["Python"],
            help="Выберите нужные технологии",
            key="multiselect1"
        )
        st.write(f"Выбрано: {', '.join(selected)}")
        st.markdown("---")

    # Чекбокс
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("6. Checkbox")
        st.code('''
checked = st.checkbox(
    label="Принять лицензионное соглашение",
    value=False,
    help="Необходимо для продолжения",
    key="checkbox1"
                

option = st.radio(
    "Выбрать опцию",
    ["Опция 1", "Опция 2", "Опция 3"],
    index=None,
)

st.write("Вы выбрали:", option)
)
''', language='python')

    with col2:
        st.subheader("Пример")
        checked = st.checkbox(
            label="Принять лицензионное соглашение",
            value=False,
            help="Необходимо для продолжения",
            key="checkbox1"
        )
        st.write(f"Состояние чекбокса: {checked}")

        option = st.radio(
            "Выбрать опцию",
            ["Опция 1", "Опция 2", "Опция 3"],
            index=None,
        )
        st.write("Вы выбрали:", option)

        st.markdown("---")


    # Загрузка файла
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("7. File Uploader")
        st.code('''
uploaded_file = st.file_uploader(
    label="Загрузите документ",
    type=["txt", "pdf", "docx"],
    accept_multiple_files=False,
    help="Максимальный размер файла: 200MB",
    key="file_uploader1"
)
''', language='python')

    with col2:
        st.subheader("Пример")
        uploaded_file = st.file_uploader(
            label="Загрузите документ",
            type=["txt", "pdf", "docx"],
            accept_multiple_files=False,
            help="Максимальный размер файла: 200MB",
            key="file_uploader1"
        )
        if uploaded_file:
            st.write(f"Загружен файл: {uploaded_file.name}")
        st.markdown("---")

    # Цветовой пикер
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("8. Color Picker")
        st.code('''
color = st.color_picker(
    label="Выберите цвет фона",
    value="#FF0000",
    key="color_picker1"
)
''', language='python')

    with col2:
        st.subheader("Пример")
        color = st.color_picker(
            label="Выберите цвет фона",
            value="#FF0000",
            key="color_picker1"
        )
        st.write(f"Выбранный цвет: {color}")
        st.markdown(f'<div style="height:50px; background:{color}"></div>', unsafe_allow_html=True)
        st.markdown("---")

    # Дата и время
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("9. Date/Time Input")
        st.code('''
date = st.date_input(
    label="Выберите дату",
    value=datetime.now(),
    min_value=datetime(2000, 1, 1),
    max_value=datetime(2030, 12, 31),
    format="DD.MM.YYYY",
    key="date_input1"
)

time_ = st.time_input(
    label="Выберите время",
    key="time_input1"
)
''', language='python')

    with col2:
        st.subheader("Пример")
        date = st.date_input(
            label="Выберите дату",
            value=datetime.now(),
            min_value=datetime(2000, 1, 1),
            max_value=datetime(2030, 12, 31),
            format="DD.MM.YYYY",
            key="date_input1"
        )
        time_ = st.time_input(
            label="Выберите время",
            key="time_input1"
        )
        st.write(f"Выбрано: {date} {time_}")
        st.markdown("---")

if menu == "Элементы вывода":
    st.title("Элементы вывода Streamlit")
    st.markdown("---")

    # Генерация тестовых данных
    data = pd.DataFrame({
        'Город': ['Москва', 'Санкт-Петербург', 'Казань', 'Екатеринбург'],
        'Население (млн)': [12.6, 5.4, 1.3, 1.5],
        'Рейтинг': [4.7, 4.5, 4.3, 4.2]
    })

    # Текстовые элементы
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Текст")
        st.code('''
    st.subheader("Пример")
    st.text("Обычный текст без форматирования")
    st.markdown("**Жирный текст** и *курсив*")
    st.latex(r"\sum_{i=1}^n x_i^2")
    st.code("print('Hello World!')", language='python')
    st.title("Главный заголовок")
    st.header("Заголовок раздела")
    st.subheader("Подзаголовок")
    st.markdown("---")
    ''', language='python')

    with col2:
        st.subheader("Пример")
        st.text("Обычный текст без форматирования")
        st.markdown("**Жирный текст** и *курсив*")
        st.latex(r"\sum_{i=1}^n x_i^2")
        st.code("print('Hello World!')", language='python')
        st.title("Главный заголовок")
        st.header("Заголовок раздела")
        st.subheader("Подзаголовок")
        st.markdown("---")

    # Таблицы
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("2. Таблицы")
        st.code('''
st.subheader("Пример")
    
st.markdown("**Статическая таблица**")
st.table(data.head(2))

st.markdown("**Интерактивная таблица**")
st.dataframe(
    data,
    height=150,
    use_container_width=True,
    hide_index=True,
    column_order=["Город", "Население (млн)"]
)

st.markdown("**Метрики**")
col_metric1, col_metric2 = st.columns(2)
with col_metric1:
    st.metric("Влажность", "65%", "-3%")
with col_metric2:
    st.metric("Продажи", "$12,500", "+15%", delta_color="off")
)
    ''', language='python')

    with col2:
        st.subheader("Пример")
        
        st.markdown("**Статическая таблица**")
        st.table(data.head(2))
        
        st.markdown("**Интерактивная таблица**")
        st.dataframe(
            data,
            height=150,
            use_container_width=True,
            hide_index=True,
            column_order=["Город", "Население (млн)"]
        )
        
        st.markdown("**Метрики**")
        col_metric1, col_metric2 = st.columns(2)
        with col_metric1:
            st.metric("Влажность", "65%", "-3%")
        with col_metric2:
            st.metric("Продажи", "$12,500", "+15%", delta_color="off")
        st.markdown("---")

    # Графики
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("3. Графики")
        st.code('''
    st.markdown("**Линейный график**")
    st.line_chart(data.set_index('Город')['Рейтинг'])
    
    st.markdown("**Столбчатая диаграмма**")
    st.bar_chart(data.set_index('Город')['Население (млн)'])
    
    st.markdown("**Area chart**")
    st.area_chart(data.set_index('Город'))
    
    st.markdown("**Plotly график**")
    fig = px.scatter(
        data,
        x='Население (млн)',
        y='Рейтинг',
        size='Население (млн)',
        color='Город',
        title="Соотношение населения и рейтинга"
    )
    st.plotly_chart(fig)
    ''', language='python')

    with col2:
        st.subheader("Пример")
        
        st.markdown("**Линейный график**")
        st.line_chart(data.set_index('Город')['Рейтинг'])
        
        st.markdown("**Столбчатая диаграмма**")
        st.bar_chart(data.set_index('Город')['Население (млн)'])
        
        st.markdown("**Area chart**")
        st.area_chart(data.set_index('Город'))
        
        st.markdown("**Plotly график**")
        fig = px.scatter(
            data,
            x='Население (млн)',
            y='Рейтинг',
            size='Население (млн)',
            color='Город',
            title="Соотношение населения и рейтинга"
        )
        st.plotly_chart(fig)
        st.markdown("---")

    # JSON
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("4. JSON")
        st.code('''
    st.json({
        "система": "Streamlit Demo",
        "версия": 2.1,
        "статус": "активный",
        "настройки": {
            "тема": "темная",
            "язык": "русский"
        }
    })
    ''', language='python')

    with col2:
        st.subheader("Пример")
        st.json({
            "система": "Streamlit Demo",
            "версия": 2.1,
            "статус": "активный",
            "настройки": {
                "тема": "темная",
                "язык": "русский"
            }
        })
        st.markdown("---")

if menu == "Медиа элементы":    
    st.title("Медиа элементы Streamlit")
    st.markdown("---")

    # Изображение
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Изображение (Image)")
        st.code('''
    # Пример с URL
    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
        caption="Логотип Streamlit",
        width=300
    )
    
    # Пример с локальным файлом (для демонстрации)
    st.image(
        "XPpic.jpg",
        caption="XPpic.jpg",
        use_container_width=True
    )
    ''', language='python')

    with col2:
        st.subheader("Пример")
        
        # Пример с URL
        st.image(
            "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
            caption="Логотип Streamlit",
            width=300
        )
        
        # Пример с локальным файлом (для демонстрации)
        st.image(
            "XPpic.jpg",
            caption="XPpic.jpg",
            use_container_width=True
        )
        st.markdown("---")

    # Аудио
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("2. Аудио (Audio)")
        st.code('''
    st.audio(
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        format="audio/mp3",
        start_time=10
    )
    st.write("Пример аудиофайла (начало с 10 секунды)")    start_time=0               # Начало воспроизведения в секундах
    )
    ''', language='python')

    with col2:
        st.subheader("Пример")
        st.audio(
            "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
            format="audio/mp3",
            start_time=10
        )
        st.write("Пример аудиофайла (начало с 10 секунды)")
        st.markdown("---")

    # Видео
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("3. Видео (Video)")
        st.code('''
    st.video(
        "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4",
        format="video/mp4",
        start_time=5
    )
    st.write("Пример видео (начало с 5 секунды)")
    ''', language='python')

    with col2:
        st.subheader("Пример")
        st.video(
            "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4",
            format="video/mp4",
            start_time=5
        )
        st.write("Пример видео (начало с 5 секунды)")
        st.markdown("---")

    # Дополнительная информация
    st.markdown("### Поддерживаемые форматы:")
    st.markdown("""
    - **Изображения:** PNG, JPG/JPEG, GIF, BMP, WEBP
    - **Аудио:** WAV, MP3, OGG, FLAC
    - **Видео:** MP4, WEBM, OGG

    **Советы:**
    1. Для больших файлов используйте прогресс-бар загрузки
    2. Локальные файлы можно загружать через `st.file_uploader`
    3. Для YouTube видео используйте специальные компоненты
    """)

if menu == "Элементы прогресса и статуса":
    st.title("Элементы прогресса и статуса Streamlit")
    st.markdown("---")

    # Прогресс-бар
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Прогресс-бар (Progress)")
        st.code('''
    # Создание прогресс-бара
    if st.button("Запустить прогресс"):
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
    ''', language='python')

    with col2:
        st.subheader("Пример")
        
        # Пример с анимацией
        if st.button("Запустить прогресс"):
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()

        st.markdown("---")

    # Спиннер
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("2. Спиннер (Spinner)")
        st.code('''
if st.button("Запустить обработку"):
    with st.spinner("Подождите 3 секунды...", show_time=True):
        time.sleep(3)
    st.success("Операция успешно завершена!")
    ''', language='python')

    with col2:
        st.subheader("Пример")
        if st.button("Запустить обработку"):
            with st.spinner("Подождите 3 секунды...", show_time=True):
                time.sleep(3)
            st.success("Операция успешно завершена!")
        st.markdown("---")

    # Сообщения
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("3. Сообщения (Messages)")
        st.code('''
if st.button("Показать сообщения"):
    st.success("Данные сохранены успешно!", icon="💾")
    st.error("Ошибка подключения к базе", icon="🔌")
    st.warning("Недостаточно памяти", icon="💽")
    st.info("Обновление доступно", icon="🔄")
    
if st.button("Показать исключение"):
    try:
        # Генерируем ошибку
        raise ValueError("Пример кастомной ошибки")
    except Exception as e:
        st.exception(e)
    ''', language='python')

    with col2:
        st.subheader("Пример")
        
        if st.button("Показать сообщения"):
            st.success("Данные сохранены успешно!", icon="💾")
            st.error("Ошибка подключения к базе", icon="🔌")
            st.warning("Недостаточно памяти", icon="💽")
            st.info("Обновление доступно", icon="🔄")
            
        if st.button("Показать исключение"):
            try:
                # Генерируем ошибку
                raise ValueError("Пример кастомной ошибки")
            except Exception as e:
                st.exception(e)
        
        st.markdown("---")

    # Дополнительные возможности
    st.markdown("### Дополнительные параметры:")
    st.markdown("""
    1. **Иконки:** Можно использовать любые эмодзи (https://emojipedia.org/)
    2. **Время отображения:** Сообщения остаются до перезагрузки страницы
    3. **Кастомизация:** 
        - Используйте `st.markdown()` для стилизации
        - Комбинируйте с `st.container()` для сложных сообщений
    4. **Очистка:** Используйте `.empty()` для удаления элементов
    """)

if menu == "Макеты":
    st.title("Макеты в Streamlit")
    st.markdown("---")

    # Столбцы
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Столбцы (Columns)")
        st.code('''
    # Создание колонок
    col1, col2, col3 = st.columns(
        spec=3,                  # Количество колонок (или список весов)
        gap="medium",            # Расстояние между колонками: "small", "medium", "large"
        # vertical_align="center" # Выравнивание (только с custom CSS)
    )

    # Использование контекстного менеджера
    with col1:
        st.button("Кнопка в 1 колонке")
        
    col2.write("Текст во 2 колонке")

    # Пример с разными ширинами
    wide_col, narrow_col = st.columns([3, 1])
    ''', language='python')

    with col2:
        st.subheader("Пример")
        
        # Простые колонки
        demo_col1, demo_col2, demo_col3 = st.columns(3, gap="small")
        with demo_col1:
            st.button("Пример 1")
        with demo_col2:
            st.button("Пример 2")
        with demo_col3:
            st.button("Пример 3")
        
        # Колонки с разной шириной
        wide_col, narrow_col = st.columns([3, 1])
        with wide_col:
            st.write("Широкая колонка")
        with narrow_col:
            st.metric("Метрика", "42")
        
        st.markdown("---")

    # Вкладки
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("2. Вкладки (Tabs)")
        st.code('''
    tab1, tab2 = st.tabs(
        ["Первая вкладка", "Вторая вкладка"], # Названия вкладок
        # gap="small"                        # Расстояние между вкладками
    )

    with tab1:
        st.write("Контент первой вкладки")

    tab2.markdown("**Маркдаун** во второй вкладке")
    ''', language='python')

    with col2:
        st.subheader("Пример")
        
        tab1, tab2, tab3 = st.tabs(["📊 График", "📝 Текст", "⚙️ Настройки"])
        
        with tab1:
            st.line_chart([1, 3, 2, 4])
            st.caption("Пример графика")
        
        with tab2:
            st.write("Пример текстового контента")
            st.code("print('Hello World!')")
        
        with tab3:
            st.slider("Пример настройки", 0, 100)
        
        st.markdown("---")

    # Сайдбар
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("3. Сайдбар (Sidebar)")
        st.code('''
    # Вариант 1: Контекстный менеджер
    with st.sidebar:
        st.header("Меню")
        selected = st.selectbox("Выберите", ["Главная", "О нас"])
        
    # Вариант 2: Прямой доступ
    st.sidebar.button("Специальная кнопка")
    ''', language='python')

    with col2:
        st.subheader("Пример")
        
        # Имитация сайдбара в основном интерфейсе для демонстрации
        with st.expander("Показать пример сайдбара", expanded=True):
            with st.sidebar.container():  # Временный контейнер для демонстрации
                st.header("Пример меню")
                page = st.selectbox("Навигация", ["Главная", "Настройки", "Помощь"])
                st.slider("Яркость", 0, 100, 50)
                if st.button("Обновить"):
                    st.toast("Настройки сохранены!")
        
        st.write("**Примечание:** Настоящий сайдбар отображается слева за пределами основного контейнера")
        st.markdown("---")

    # Дополнительные возможности
    st.markdown("### Дополнительные параметры:")
    st.markdown("""
    1. **Вложенные макеты:** Колонки внутри вкладок и наоборот
    2. **CSS-кастомизация:** Используйте `st.markdown` с `unsafe_allow_html=True`
    3. **Контейнеры:** `st.container()` для сложных макетов
    4. **Пустые элементы:** `placeholder = st.empty()` для динамического контента
    """)

    # Пример сложного макета
    st.markdown("---")
    st.subheader("Комбинированный пример")

    main_col, side_col = st.columns([4, 1])
    with main_col:
        analytics_tab, logs_tab = st.tabs(["Аналитика", "Логи"])
        
        with analytics_tab:
            st.scatter_chart([(x, x**2) for x in range(10)])
        
        with logs_tab:
            st.json({"event": "click", "time": "12:34:56"})

    with side_col:
        with st.container(border=True):
            st.metric("Пользователи", "1423", "+5.2%")
            st.progress(75)

if menu == "Прочие элементы":
    st.title("Прочие элементы Streamlit")
    st.markdown("---")

    # Формы
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Форма (Form)")
        st.code('''
    with st.form(
        key="my_form",              # Уникальный идентификатор
        border=True,                # Граница формы
        clear_on_submit=False       # Очищать поля после отправки
    ):
        # Элементы внутри формы
        name = st.text_input("Имя")
        email = st.text_input("Email")
        
        # Кнопка отправки
        submitted = st.form_submit_button("Отправить")
        
    if submitted:
        st.write(f"Данные: {name}, {email}")
    ''', language='python')

    with col2:
        st.subheader("Пример")
        
        with st.form(key="example_form", border=True):
            st.write("**Регистрация**")
            
            form_name = st.text_input("Ваше имя:")
            form_email = st.text_input("Ваш email:")
            form_newsletter = st.checkbox("Подписаться на рассылку")
            
            submitted = st.form_submit_button("Зарегистрироваться")
            
        if submitted:
            if form_name and form_email:
                st.success("Регистрация успешна!")
                st.write(f"""
                - Имя: {form_name}
                - Email: {form_email}
                - Рассылка: {'Да' if form_newsletter else 'Нет'}
                """)
            else:
                st.error("Заполните обязательные поля!")
        st.markdown("---")

    # Экспериментальные элементы
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("2. Экспериментальные элементы")
        st.code('''
    # Анимация шариков
    st.balloons(
        # Не имеет параметров
    )

    # Анимация снегопада
    st.snow(
        # Не имеет параметров
    )

    # Toast-уведомление (v1.29+)
    st.toast("Успешно сохранено!", icon="🎉")
    ''', language='python')

    with col2:
        st.subheader("Пример")
        
        col_anim1, col_anim2 = st.columns(2)
        with col_anim1:
            if st.button("🎈 Запустить шарики"):
                st.balloons()
                
        with col_anim2:
            if st.button("❄️ Включить снег"):
                st.snow()
        
        if st.button("Показать уведомление"):
            st.toast("Данные обновлены!", icon="✅")
        
        st.markdown("---")

    # Дополнительные возможности
    st.markdown("### Важные примечания:")
    st.markdown("""
    1. **Формы:**
    - Все элементы формы должны быть внутри контекстного менеджера `with form:`
    - Только одна кнопка отправки на форму
    - Для сброса используйте `clear_on_submit=True`

    2. **Экспериментальные функции:**
    - Могут измениться в будущих версиях
    - Не поддерживают параметры настройки
    - Работают только при взаимодействии пользователя

    3. **Toast-уведомления:**
    - Доступны в Streamlit v1.29+
    - Исчезают автоматически через 3 секунды
    """)

    # Пример сложной формы
    st.markdown("---")
    st.subheader("Пример расширенной формы")

    with st.form("advanced_form"):
        cols = st.columns(3)
        with cols[0]:
            age = st.slider("Возраст", 18, 99)
        with cols[1]:
            color = st.color_picker("Любимый цвет")
        with cols[2]:
            lang = st.selectbox("Язык", ["Python", "JavaScript", "Java"])
        
        bio = st.text_area("О себе", max_chars=200)
        resume = st.file_uploader("Резюме (PDF)", type=["pdf"])
        
        if st.form_submit_button("Сохранить профиль"):
            st.toast("Профиль обновлён!", icon="💾")
            st.rerun()