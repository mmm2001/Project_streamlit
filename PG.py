import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Визуализация суперформулы')
st.markdown("### Изменяйте параметры для создания различных форм")

# Отображение исходного кода
with st.expander("Показать исходный код"):
    with open(__file__, 'r') as f:
        st.code(f.read(), language='python')

# Параметры управления
col1, col2, col3, col4 = st.columns(4)
with col1:
    m = st.slider('Количество лепестков (m)', 1, 20, 5)
with col2:
    n1 = st.slider('Форма 1 (n1)', 0.1, 10.0, 2.0)
with col3:
    n2 = st.slider('Форма 2 (n2)', 0.1, 10.0, 2.0)
with col4:
    n3 = st.slider('Форма 3 (n3)', 0.1, 10.0, 2.0)

# Блок с формулой
st.markdown(r"""
**Математическая формула:**
$$
r(\phi) = \left( \left| \frac{1}{a} \cos\left( \frac{m\phi}{4} \right) \right|^{n_2} + 
           \left| \frac{1}{b} \sin\left( \frac{m\phi}{4} \right) \right|^{n_3} \right)^{-1/n_1}
$$
*где a = b = 1.0 в данной реализации*
""")

# Функция суперформулы
def superformula(phi, m, n1, n2, n3):
    a = 1.0
    b = 1.0
    t1 = np.abs((1/a) * np.cos(m * phi / 4))
    t2 = np.abs((1/b) * np.sin(m * phi / 4))
    return (t1**n2 + t2**n3)**(-1/n1)

# Генерация и отрисовка графика
theta = np.linspace(-np.pi, np.pi, 1000)
r = superformula(theta, m, n1, n2, n3)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')
ax.plot(theta, r, color='purple', lw=2)
ax.set_rmax(2)
ax.grid(True)
ax.set_title("Визуализация суперформулы", va='bottom')

st.pyplot(fig)

# Пояснение параметров
st.markdown("""
**Как работают параметры:**
- `m` - определяет количество лепестков/выступов
- `n1` - контролирует общий размер формы
- `n2` и `n3` - влияют на форму лепестков и впадин
""")