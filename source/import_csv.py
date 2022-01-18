import csv
import matplotlib.pyplot as plt
import numpy as np

filename = '../data/historical_sales_data.csv'
time = []
fish = []
ducks = []
total = []
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def dataImport():
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        header_row = next(reader)
        i = 0
        for row in reader:
            if ((i%4) == 0):
                time.append(month[i] + row[1][2:4])
            else :
                time.append('');
            i = ((i+1) % 12)
            fish.append(int(row[2]))
            ducks.append(int(row[3]))
            total.append(int(row[4]))
        
    
def dataVisualisation():
    x = np.arange(0, len(fish), 1)
    plt.plot(x, fish, color = 'b', label = 'Fishes')
    plt.plot(x, ducks, color = 'g', label = 'Ducks')
    plt.plot(x, total, color = 'r', label = 'Total')
    plt.xticks(x, time, rotation = 45)
    plt.title('Fig 3: Historical data of sales')
    plt.ylabel('number of sales')
    #plt.xlabel('time')
    plt.subplots_adjust(bottom=0.2)
    plt.margins(x=0)
    plt.grid()
    plt.legend()
    plt.savefig('../Paper/fig_historical_sales.pdf', format='pdf')
    #plt.show()
    
dataImport()
dataVisualisation()
