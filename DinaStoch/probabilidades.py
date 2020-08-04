import random 
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
output_notebook()

def tirar_dado(num_tiros):
    secuencia_tiros = []
    for _ in range(num_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_tiros.append(tiro)

    return secuencia_tiros

def main(num_tiros, num_intentos):
    tiros = []
    for _ in range(num_intentos):
        secuencia_tiros = tirar_dado(num_tiros)
        tiros.append(secuencia_tiros)
    
    tiros_con_1 = 0
    for tiro in tiros:
        if 1 not in tiro:
            tiros_con_1 += 1

    probabilidad_tiros_1 = tiros_con_1 / num_intentos
    print(f'Probabilidad de no obtener por lo menos un 1 en {num_tiros} tiros = {probabilidad_tiros_1}')
    ploter(tiros, probabilidad_tiros)

def ploter(sim, prob):
    plot = figure(title='Probability get 1 with 1 shot',
                  x_axis_label='Attempts',
                  y_axis_label='Probability')
    
    plot.line(sim,prob)
    show(plot)

if __name__ == '__main__':
    num_tiros = int(input('Cuantos tiros del dado: '))
    num_intentos = int(input('Cuantas veces correra la simulacion: '))

    main(num_tiros, num_intentos)
