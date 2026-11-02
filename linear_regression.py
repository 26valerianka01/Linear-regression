import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Загружаем данные из Excel (используем openpyxl для .xlsx)
data = pd.read_excel('TATN.xlsx', engine='openpyxl')
# Преобразуем столбец 'Дата' в порядковые номера (t)
data['t'] = np.arange(len(data))
# Извлекаем столбцы t и y (котировки)
t = data['t'].values  # t_i — моменты времени
y = data['Цена'].apply(lambda x: float(str(x).replace(',', '.'))).values  # y_i — значения котировок
# Рассчитываем средние значения по формулам:
t_mean = np.mean(t)  # <t_i>
y_mean = np.mean(y)  # <y_i>
t_squared_mean = np.mean(t ** 2)  # <t_i^2>
t_y_mean = np.mean(t * y)  # <y_i * t_i>
# Рассчитываем коэффициенты A и B по формулам:
# A = (<y_i * t_i> - <y_i> * <t_i>) / (<t_i^2> - <t_i>^2)
A = (t_y_mean - y_mean * t_mean) / (t_squared_mean - t_mean ** 2)
# B = <y_i> - A * <t_i>
B = y_mean - A * t_mean
# Формируем линейный тренд: y_trend = A * t + B
y_trend = A * t + B
# Визуализация
plt.figure(figsize=(14, 7))
plt.scatter(t, y, label='Исходные данные', color='blue', alpha=0.5)
plt.plot(t, y_trend, label=f'Линейный тренд: y = {A:.4f}t + {B:.4f}', color='red', linewidth=2)
plt.xlabel('Время (порядковый номер)')
plt.ylabel('Цена акции (руб.)')
plt.title('Линейная регрессия котировок акций Татнефть (TATN)')
plt.legend()
plt.grid(True)
plt.show()
# Анализ адекватности: рассчитываем среднеквадратичную ошибку (MSE)
mse = np.mean((y - y_trend) ** 2)
print(f"Среднеквадратичная ошибка (MSE): {mse:.4f}")
print(f"Коэффициенты: A = {A:.4f}, B = {B:.4f}")
