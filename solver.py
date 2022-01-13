import numpy as np


#profits of duck and fish
profit_per_duck = 5
profit_per_fish = 4

#decision variables
#count_duck = 300
#count_fish = 250

#constraint time
max_duck = 400
max_fish = 300

#constraint rubber
total_pallets = 50000
pallets_per_duck = 100
pallets_per_fish = 125


def solver():
	product_mix = []
	max_profit = 0
	for count_duck in range(0, max_duck+1):
		for count_fish in range(0, max_fish+1):
			if(((count_duck * pallets_per_duck) + (count_fish * pallets_per_fish)) <= total_pallets):
				current_profit = profit_per_duck * count_duck + profit_per_fish * count_fish
				if(current_profit > max_profit):
					max_profit = current_profit
					product_mix = [current_profit, count_duck, count_fish]
	
	return product_mix

	
	
print(solver())