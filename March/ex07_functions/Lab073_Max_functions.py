# Toppings - chilli , paneer , corn , potato , onion , pineapple

def make_pizza(*toppings):
    print(toppings)

    # for i in topping
    # print(i)

    sai = make_pizza(*toppings, "tomato", "olives")
    vijay = make_pizza(*toppings, "pineapple", "olives", "corn", "paneer")
    suyash = make_pizza("tomato")

    r1 = max(1, 2, 3, 4, 6)
