import argparse as arg
import matplotlib.pyplot as plt
import numpy as np


#define commandline arguments to parse constraints to the solver
cli = arg.ArgumentParser(description='Add the Constraints for the Solver')
cli.add_argument('--profs','-p', type=int, nargs=2, default=[5,4], help='profit per duck (D), profit per fish (F) (default: %(default)s)', metavar=('D', 'F'))
cli.add_argument('--times','-t', type=int, nargs=2, default=[400,300],help='available production time for duckies (D), fishes (F) (default: %(default)s)',  metavar=('D', 'F'))
cli.add_argument('--palls','-e', type=int, nargs=2, default=[100,125], help='required pallets per duck (D), fish (F) (default: %(default)s)', metavar=('D', 'F'))
cli.add_argument('--rubbs','-r', type=int, nargs=1, default=50000, help='total supplied rubber pallets (N) (default:%(default)s)', metavar=('N'))
cli.add_argument('--assum','-a', type=int, nargs=2, help='assumption for future sales duckies (D), fishes(F) (default: %(default)s)', metavar=('D','F'))

args=cli.parse_args()


#constraint profits per duck and fish
profit_per_duck = args.profs[0] #default = 5
profit_per_fish = args.profs[1] #default = 4

#constraint max time for duckies and fishes available
time_duck = args.times[0] #default = 400
time_fish = args.times[1] #default = 300

#constraint rubber 
total_pallets = args.rubbs #default = 50000
pallets_per_duck = args.palls[0] #default = 100
pallets_per_fish = args.palls[1] #default = 125

#constraint assumtion for future sales
duck_sales = time_duck
fish_sales = time_fish
if(args.assum):
	duck_sales = args.assum[0] 
	fish_sales = args.assum[1] 



#assign the min of time and sales constraint to the max count of duckies and fishes
max_duck = min(time_duck, duck_sales)
max_fish = min(time_fish, fish_sales)


#plot the feasible region
def plot_feasible_region():
	
	#plot time constraint
	plt.axhline(y=time_duck, linestyle='--', color = 'b', label='time ducks')
	plt.axvline(x=time_fish, linestyle='--', color = 'r', label='time fishes')
	plt.ylim(0, time_duck+100)
	plt.xlim(0, time_fish+100)
	
	#plot pallets constraint
	x_values = [total_pallets/pallets_per_fish, 0]
	y_values = [0, total_pallets/pallets_per_duck]
	plt.plot(x_values, y_values, linestyle='--', color = 'g', label='rubber supply')
	
	#fill green color in the feasible region
	x_range = np.arange(0,time_fish,1) #from 0 to max_fish
	
	#points on the pallets constraint line
	m = (0-total_pallets/pallets_per_duck)/(total_pallets/pallets_per_fish-0)
	y1 = m*x_range + total_pallets/pallets_per_duck
	y = np.minimum(y1, time_duck)
	plt.fill_between(x_range, y, color='lime')
	
	plt.ylabel('duckies')
	plt.xlabel('fishes')
	#plt.title('feasible region')


#the solver to calculate the optimal produkt mix
#checks every possible mix within the given constraints
def solver():
	product_mix = [] #result [total_profit, duckies, fishes]

	max_profit = 0
	for count_duck in range(0, max_duck+1):
		for count_fish in range(0, max_fish+1):
			if(((count_duck * pallets_per_duck) + (count_fish * pallets_per_fish)) <= total_pallets):
				#objective function
				current_profit = profit_per_duck * count_duck + profit_per_fish * count_fish
				
				if(current_profit > max_profit):
					max_profit = current_profit
					product_mix = [current_profit, count_duck, count_fish]
	
	return product_mix
	
plot_feasible_region()

print('optimal product mix for the given constraints:')
print('[total_profit, duckies, fishes]')
p_mix = solver()
print(p_mix)

plt.scatter(p_mix[2], p_mix[1], marker='o', color='k', label='product mix')
plt.legend()
plt.savefig('../paper/feasible_region.pdf', format='pdf')
