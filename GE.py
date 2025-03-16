import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
import plotly.express as px
from io import BytesIO
import time 

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
    time_ = st.time_input(
        label="Выберите время",
        value=datetime.now().time(),
        key="time_input1"
    )
    st.write(f"Выбрано: {date} {time_}")
    st.markdown("---")

#
# ЭЛЕМЕНТЫ ВЫВОДА
# 


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
# Простой текст
st.text("Обычный текст без форматирования")

# Markdown
st.markdown("**Жирный текст** и *курсив*")

# LaTeX
st.latex(r"\sum_{i=1}^n x_i^2")

# Код
st.code("print('Hello World!')", language='python')

# Заголовки
st.title("Главный заголовок")
st.header("Заголовок раздела")
st.subheader("Подзаголовок")
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
# Статическая таблица
st.table(data)

# Интерактивная таблица
st.dataframe(
    data,
    height=300,              # Высота области
    use_container_width=True,# На всю ширину
    hide_index=True,         # Скрыть индексы
    column_order=["Город", "Рейтинг"] # Порядок колонок
)

# Метрики
st.metric(
    label="Температура",    # Название
    value="+23°C",          # Значение
    delta="+2°C",           # Изменение
    delta_color="normal"    # Цвет: normal/off/inverse
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
# Линейный график
st.line_chart(data.set_index('Город')['Рейтинг'])

# Столбчатая диаграмма
st.bar_chart(data.set_index('Город')['Население (млн)'])

# Area chart
st.area_chart(data.set_index('Город'))

# Plotly график
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

    st.title("Медиа элементы Streamlit")
st.markdown("---")

# Изображение
col1, col2 = st.columns(2)
with col1:
    st.subheader("1. Изображение (Image)")
    st.code('''
st.image(
    image="https://example.com/image.jpg",  # URL или путь к файлу
    caption="Описание изображения",        # Подпись
    width=400,                             # Ширина в пикселях
    use_column_width=False,                # Растянуть на всю колонку
    clamp=False,                           # Ограничить цветовой диапазон
    channels="RGB",                        # Цветовые каналы (RGB/BGR)
    output_format="auto"                   # Формат (JPEG/PNG)
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
        use_column_width=True
    )
    st.markdown("---")

# Аудио
col1, col2 = st.columns(2)
with col1:
    st.subheader("2. Аудио (Audio)")
    st.code('''
st.audio(
    data="audio.mp3",          # Путь к файлу, URL или bytes
    format="audio/mp3",        # Формат (автоопределение)
    start_time=0               # Начало воспроизведения в секундах
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
    data="video.mp4",          # Путь к файлу, URL или bytes
    format="video/mp4",        # Формат (автоопределение)
    start_time=0               # Начало воспроизведения в секундах
)
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

st.title("Элементы прогресса и статуса Streamlit")
st.markdown("---")

# Прогресс-бар
col1, col2 = st.columns(2)
with col1:
    st.subheader("1. Прогресс-бар (Progress)")
    st.code('''
# Создание прогресс-бара
progress_bar = st.progress(
    value=0,        # Начальное значение (0-100)
    text="Загрузка" # Текст над прогресс-баром
)

# Обновление значения
progress_bar.progress(
    value=75,       # Новое значение (0-100)
    text="75% завершено" # Обновлённый текст
)
''', language='python')

with col2:
    st.subheader("Пример")
    
    # Пример с анимацией
    if st.button("Запустить прогресс"):
        progress = st.progress(0, text="Начало обработки...")
        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1, text=f"Обработка: {i+1}%")
        progress.empty()
    
    # Статичный пример
    static_progress = st.progress(45)
    static_progress.progress(45, "Постоянный прогресс (45%)")
    st.markdown("---")

# Спиннер
col1, col2 = st.columns(2)
with col1:
    st.subheader("2. Спиннер (Spinner)")
    st.code('''
with st.spinner(
    text="Идёт загрузка..."  # Текст спиннера
):
    # Долгая операция
    time.sleep(2)
    
st.success("Готово!")  # Сообщение после завершения
''', language='python')

with col2:
    st.subheader("Пример")
    if st.button("Запустить обработку"):
        with st.spinner("Подождите 3 секунды..."):
            time.sleep(3)
        st.success("Операция успешно завершена!")
    st.markdown("---")

# Сообщения
col1, col2 = st.columns(2)
with col1:
    st.subheader("3. Сообщения (Messages)")
    st.code('''
# Успех
st.success(
    "Успешное выполнение!", 
    icon="✅"  # Можно менять иконку
)

# Ошибка
st.error(
    "Произошла ошибка",
    icon="🚨"
)

# Предупреждение
st.warning(
    "Внимание! Это важно",
    icon="⚠️"
)

# Информационное
st.info(
    "Полезная информация",
    icon="ℹ️"
)

# Исключение
try:
    1 / 0
except Exception as e:
    st.exception(e)  # Показывает трейсбэк
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