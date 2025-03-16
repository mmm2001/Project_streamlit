import streamlit as st
from datetime import datetime

st.title("Элементы ввода Streamlit")
st.markdown("---")

# Кнопка
col1, col2 = st.columns(2)
with col1:
    st.subheader("1. Кнопка (Button)")
    st.code('''
st.button(
    label="Нажми меня",  # Текст на кнопке
    key="my_button",     # Уникальный идентификатор
    help="Подсказка",    # Текст при наведении
    disabled=False       # Блокировка кнопки
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
st.text_input(
    label="Введите текст",    # Заголовок
    value="По умолчанию",     # Стартовое значение
    max_chars=50,            # Макс. символов
    placeholder="Введите...",# Подсказка
    help="Подсказка",        # Всплывающая помощь
    key="text_input1"        # Уникальный ключ
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
st.slider(
    label="Выберите значение",  # Заголовок
    min_value=0,               # Минимальное значение
    max_value=100,             # Максимальное значение
    value=50,                  # Стартовое значение
    step=5,                    # Шаг изменения
    format="%d%%",             # Формат отображения
    key="slider1"              # Уникальный ключ
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
st.selectbox(
    label="Выберите вариант",  # Заголовок
    options=["A", "B", "C"],  # Список вариантов
    index=0,                   # Стартовый индекс
    format_func=lambda x: x*2,# Форматирование
    help="Подсказка",          # Всплывающая помощь
    key="selectbox1"           # Уникальный ключ
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
st.multiselect(
    label="Выберите варианты",  # Заголовок
    options=["A", "B", "C"],    # Список вариантов
    default=["A"],              # Выбрано по умолчанию
    help="Подсказка",           # Всплывающая помощь
    key="multiselect1"          # Уникальный ключ
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
st.checkbox(
    label="Согласен с условиями",  # Текст чекбокса
    value=False,                   # Стартовое состояние
    help="Подсказка",             # Всплывающая помощь
    key="checkbox1"               # Уникальный ключ
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
    st.markdown("---")

# Загрузка файла
col1, col2 = st.columns(2)
with col1:
    st.subheader("7. File Uploader")
    st.code('''
st.file_uploader(
    label="Загрузите файл",    # Заголовок
    type=["jpg", "png", "pdf"],# Разрешённые типы
    accept_multiple_files=True,# Множественная загрузка
    help="Подсказка",          # Всплывающая помощь
    key="file_uploader1"       # Уникальный ключ
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
st.color_picker(
    label="Выберите цвет",  # Заголовок
    value="#00FF00",        # Стартовый цвет
    key="color_picker1"     # Уникальный ключ
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
    st.markdown(f'<div style="height:50px; background:{color}"></div>', 
                unsafe_allow_html=True)
    st.markdown("---")

# Дата и время
col1, col2 = st.columns(2)
with col1:
    st.subheader("9. Date/Time Input")
    st.code('''
# Дата
st.date_input(
    label="Выберите дату",
    value=datetime.now(),    # Стартовая дата
    min_value=datetime(2000, 1, 1), # Минимальная дата
    max_value=datetime(2030, 12, 31),# Максимальная дата
    format="DD.MM.YYYY",     # Формат
    key="date_input1"
)

# Время
st.time_input(
    label="Выберите время",
    value=datetime.now().time(), # Стартовое время
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
    time = st.time_input(
        label="Выберите время",
        value=datetime.now().time(),
        key="time_input1"
    )
    st.write(f"Выбрано: {date} {time}")
    st.markdown("---")