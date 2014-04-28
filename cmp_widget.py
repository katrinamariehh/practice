# need to take in number of children
# number of adults
# and compare total cost of visit to equivalent
# membership level

def total_cost_oak(adults, children, seniors):
	adult_cost = adults * 17.95
	children_cost = children * 11.95
	senior_cost = seniors * 14.95
	return adult_cost + children_cost + senior_cost

def total_cost_awm(adults, children, seniors):
	adult_cost = adults * 20
	children_cost = children * 10
	senior_cost = seniors * 20
	return adult_cost + children_cost + senior_cost

def total_cost_csc(adults, children, seniors):
	adult_cost = adults * 18.95
	children_cost = children * 11.95
	senior_cost = seniors * 18.95
	return adult_cost + senior_cost + children_cost

def membership_level(adults, children, seniors):
