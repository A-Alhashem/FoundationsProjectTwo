# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.koanda.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
    	print ("- %s" % store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in store.name:
    	if store_name == store.name:
    		return store
    	else:
    		return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print(print_stores())
    print("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.")
    user_input = input()
    if user_input == "checkout":
    	return checkout()
    elif user_input == get_store(store_name):
    	return get_store(store_name)
    else:
    	print("No store with that name.")

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    picked_store.print_products()
    user_input = input()
    print("type the name of the product exactly as it is shown above, or type \"back\" to return to your previous window.")
    print(user_input())
    for product in picked_store:
    	if user_input == product.name:
    		cart.add_to_cart(product)
    	elif user_input == "back":
    		return pick_store()


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    user_input = input()
    print("Please pick a store, or type 'checkout'")
    if user_input == "checkout":
    	return checkout()
    else:
    	pick_products(cart, pick_store())


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
