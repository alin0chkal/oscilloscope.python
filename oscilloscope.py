from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse


#ввод интервала и частоты функции
z,n,m = map(int, input().split())
#z - левая часть интервала;
#n - правая часть интервала;
#m - частота функции

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)


#функция, с которой происходит сравнение
def init():
    line.set_data([], [])
    return line,

#функция для анимации синусоидального сигнала
def animate_sin(i):
    x = np.linspace(z, n, m)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,


#функция для анимации прямоугольного сигнала
def animate_square(i):
    x = np.linspace(z, n, m)
    y = signal.square(2 * np.pi * 5 * (x - 0.01 * i))
    line.set_data(x, y)
    return line,


#функция для анимации треугольного сигнала
def animate_triangle(i):
    x = np.linspace(z, n, m)
    y = signal.sawtooth(2 * np.pi * 5 * (x - 0.01 * i), 0.5)
    line.set_data(x, y)
    return line,


#функция для анимации пилообразного сигнала
def animate_sawtooth(i):
    x = np.linspace(z, n, m)
    y = signal.sawtooth(2 * np.pi * 5 * (x - 0.01 * i))
    line.set_data(x, y)
    return line,


#функция, которая позволила разбить все сигналы на параметры, запускаемые по отдельности
def main():
    parser = argparse.ArgumentParser(description='Тут описание программы')
    parser.add_argument('--function_type',
                        choices=['square', 'sin','triangle','sawtooth'],
                        default='sin',
                        help='Signal type')
    parser.add_argument( # example
        '--my_optional',
        type=int,
        default=2,
    help='provide an integer (default: 2)'
    )
    
    my_namespace = parser.parse_args()
    print(my_namespace.function_type)

    
    if my_namespace.function_type == 'sin':
        anim = FuncAnimation(fig, animate_sin, init_func=init, frames=200, interval=20, blit=True)
# anim.save('sin.gif', writer='imagemagick', fps=60)
# надо установить imagemagic https://imagemagick.org/script/download.php#windows

    elif my_namespace.function_type == 'square':
        anim = FuncAnimation(fig, animate_square, init_func=init, frames=200, interval=20, blit=True)
    # anim.save('square.gif', writer='imagemagick',fps=60) # надо установить imagemagic https://imagemagick.org/script/download.php#windows
    
    elif my_namespace.function_type == 'triangle':
    anim = FuncAnimation(fig,animate_triangle, init_func=init, frames=200, interval=20, blit=True)
    # anim.save('sin.gif', writer='imagemagick', fps=60)
    
    elif my_namespace.function_type == 'sawtooth':
    anim = FuncAnimation(fig, animate_sawtooth, init_func=init, frames=200, interval=20, blit=True)
    # anim.save('sin.gif', writer='imagemagick', fps=60)
    plt.show()
    
if __name__ == '__main__':
    main()
