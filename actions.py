# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.koanda.com"  # Give your site a name

def welcome():
	print()
	print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!\n" % site_name)

def print_stores():
	"""
	prints the list of stores in a nice readable format.
	"""
	# your code goes here!
	for store in stores:
		print ("\n- %s" % store.name)
	print()

def get_store(store_name):
	"""
	receives a name for a store, and returns the store object with that name.
	"""
	# your code goes here!
	for store in stores:
		if store_name.lower() == store.name.lower():
			
			return store
		
			
	#return False

def pick_store():
	"""
	prints list of stores and prompts user to pick a store.
	"""
	# your code goes here!
	print_stores()
	print("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.\n")
	user_input = ""
	while user_input != "checkout":
		user_input = input()
		store_object = get_store(user_input)
		if store_object:
			return store_object

	return "checkout"

	 
		# if user_input == "checkout":
		# 	return checkout()
		# elif user_input == get_store(user_input):
		# 	return get_store(user_input)
		# else:
		# print("No store with that name.")

def pick_products(cart, picked_store):
	"""
	prints list of products and prompts user to add products to card.
	"""
	# your code goes here!

	# print(cart)
	# print(pick_store)
	# print("---")
	
	#picked_store.print_products()
	#user_input = ""
	print("type the name of the product exactly as it is shown above, or type \"back\" to return to your previous window.")
	user_input = input()
	while user_input != "back":  
		for product in picked_store.products:
			if user_input.lower() == product.name.lower():
				cart.add_to_cart(product)
				print("\"%s\" has been added to your order!" % (user_input.upper()))
				print()
			
		user_input = input()
	
	return user_input   
			  


def shop():
	"""
	The main shopping functionality
	"""
	cart = Cart()
	# your code goes here!
	xyz = ""
	
	while xyz != "checkout":
		xyz = ""
		variable_name_store = pick_store()
		if variable_name_store == "checkout":
			break

		variable_name_store.print_products()

		xyz = pick_products(cart,variable_name_store)



	cart.checkout()


def thank_you():
	print("Thank you for shopping with us at %s" % site_name)
