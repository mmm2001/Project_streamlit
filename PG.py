import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from numba import jit

st.title('Фрактальный генератор Мандельброта 🌀')
st.markdown("### Параметры фрактала")

# Отображение исходного кода
with st.expander("Показать исходный код программы"):
    with open(__file__, 'r') as f:
        code = f.read()
    st.code(code, language='python')

# Параметры ввода в сайдбаре
with st.sidebar:
    st.header("Настройки генерации")
    width = st.slider("Ширина изображения", 100, 1000, 600)
    height = st.slider("Высота изображения", 100, 1000, 400)
    max_iter = st.slider("Макс. итераций", 20, 500, 100)
    zoom = st.slider("Масштаб", 0.1, 4.0, 1.0)

# Функция для расчета множества Мандельброта (ускоренная с помощью Numba)
@jit(nopython=True)
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return 0

# Генерация фрактала
def generate_fractal(width, height, zoom, max_iter):
    x = np.linspace(-2.0/zoom, 0.5/zoom, width)
    y = np.linspace(-1.1/zoom, 1.1/zoom, height)
    fractal = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            fractal[i,j] = mandelbrot(x[j] + 1j*y[i], max_iter)
    
    return fractal

# Основная логика приложения
if st.button('Сгенерировать фрактал'):
    with st.spinner('Генерация фрактала...'):
        fractal = generate_fractal(width, height, zoom, max_iter)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.imshow(fractal.T, cmap='hot', interpolation='bilinear')
        ax.axis('off')
        plt.tight_layout()
        
        st.pyplot(fig)
        st.success('Фрактал успешно сгенерирован!')
        st.markdown("**Интересный факт:** Каждая точка фрактала представляет собой комплексное число, "
                    "а цвет показывает скорость расходимости итерационной последовательности.")