def make_sandwiches(*toppings):
    """Print a summary of sandwich being ordered"""
    print("\n Making sandwitch with below items")
    for topping in toppings:
        print(f'~ {topping}')