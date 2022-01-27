
import argparse as arg

#define commandline arguments to parse constraints to the solver
cli = arg.ArgumentParser(description='Add the Constraints for the Solver')
cli.add_argument('--profs','-p', type=int, nargs=2, default=[5,4], help='profit per duck (D), profit per fish (F) (default: %(default)s)', metavar=('D', 'F'))
cli.add_argument('--times','-t', type=int, nargs=2, default=[400,300],help='available production time for duckies (D), fishes (F) (default: %(default)s)',  metavar=('D', 'F'))
cli.add_argument('--palls','-e', type=int, nargs=2, default=[100,125], help='required pallets per duck (D), fish (F) (default: %(default)s)', metavar=('D', 'F'))
cli.add_argument('--rubbs','-r', type=int, nargs=1, default=50000, help='total supplied rubber pallets (N) (default:%(default)s)', metavar=('N'))
cli.add_argument('--assum','-a', type=int, nargs=2, default=[400,300], help='assumption for future sales duckies (D), fishes(F) (default: %(default)s)', metavar=('D','F'))

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
duck_sales = args.assum[0] #default = 400
fish_sales = args.assum[1] #default = 300



#assign the min of time and sales constraint to the max count of duckies and fishes
max_duck = min(time_duck, duck_sales)
max_fish = min(time_fish, fish_sales)


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
print('optimal product mix for the given constraints:')
print('[total_profit, duckies, fishes]')
print(solver())
