import csv
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

#path to the repro dir
path = Path(__file__).absolute()
repro_dir = str(path.parent.parent)

#arrays for ploting the historical data
filename = repro_dir + '/data/historical_sales_data.csv'
time = []
fish = []
ducks = []
total = []
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
x_lable_offset = 4 # not every month needs a lable. it is enogth to print every 4th lable

#read the csv-file at 'filename' and load the date in separatly lists
def dataImport():
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        header_row = next(reader)
        i = 0
        for row in reader: # run through the rows of the dataset
            if ((i%x_lable_offset) == 0):
                time.append(month[i] + row[1][2:4]) # generate a list with month and year of the data for the x-lable 
            else :
                time.append('');
            i = ((i+1) % 12)
            
            #load the sales date in the lists
            fish.append(int(row[2]))
            ducks.append(int(row[3]))
            total.append(int(row[4]))
        
    
def plot_historic_sales():
	plt.figure(1) # create a new figure
	x = np.arange(0, len(fish), 1)
    # plot datesets
	plt.plot(x, fish, color = 'b', label = 'Fishes')
	plt.plot(x, ducks, color = 'g', label = 'Ducks')
	plt.plot(x, total, color = 'r', label = 'Total')
	# plot x- and y-lable
	plt.xticks(x, time)
	plt.ylabel('number of sales')
	# align the plot
	plt.subplots_adjust(bottom=0.2)
	plt.margins(x=0)
    # plot a grid in the figure
	plt.grid()
    # plot the legend 
	plt.legend()
    #safing the plot as pdf-file
	plt.savefig(repro_dir + '/paper/fig_historical_sales.pdf', format='pdf')
    
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
	plt.text(80, 400 + 2, '(80, 400, 2350$)')
	plt.savefig(repro_dir + '/paper/feasible_region.pdf', format='pdf')
    
dataImport()
plot_historic_sales()
plot_feasible_region()
