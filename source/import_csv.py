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
        
    
def plot_historic_sales():
	plt.figure(1)
	x = np.arange(0, len(fish), 1)
	plt.plot(x, fish, color = 'b', label = 'Fishes')
	plt.plot(x, ducks, color = 'g', label = 'Ducks')
	plt.plot(x, total, color = 'r', label = 'Total')
	plt.xticks(x, time, rotation = 45)
	#plt.title('Fig 3: Historical data of sales')
	plt.ylabel('number of sales')
	#plt.xlabel('time')
	plt.subplots_adjust(bottom=0.2)
	plt.margins(x=0)
	plt.grid()
	plt.legend()
	plt.savefig('../paper/fig_historical_sales.pdf', format='pdf')
	#plt.show()
    
#plot the feasible region with the variables from the book
def plot_feasible_region():

	
	plt.figure(2)
	#plot time constraint
	plt.axhline(y=400, linestyle='--', color = 'b', label='time ducks')
	plt.axvline(x=300, linestyle='--', color = 'r', label='time fishes')
	plt.ylim(0, 500)
	plt.xlim(0, 500)
	
	#plot pallets constraint
	x_values = [400, 0]
	y_values = [0, 500]
	plt.plot(x_values, y_values, linestyle='--', color = 'g', label='rubber supply')
	
	#fill green color in the feasible region
	x = np.arange(0,300,1) 
	m = -500/400
	y1 = m*x + 500
	y = np.minimum(y1, 400)
	plt.fill_between(x, y, color='lime')
	
	plt.ylabel('ducks')
	plt.xlabel('fishes')
	plt.scatter(80, 400, marker='o', color='k', label='product mix')
	plt.legend(loc=5)
	plt.savefig('../paper/feasible_region.pdf', format='pdf')
    
dataImport()
plot_historic_sales()
plot_feasible_region()
