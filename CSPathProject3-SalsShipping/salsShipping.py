
premiumGroundShipping = 125.00

#calculates the ground shipping cost based on the weight of the package
def groundShippingPriceCalculator (weight):
    cost = 20
    if weight <= 2:
        cost += (1.50*weight)
    elif weight <=6:
        cost += (3.00*weight)
    elif weight <=10:
        cost += (4.00*weight)
    else:
        cost += (4.75*weight)
    return cost


def droneShippingPriceCalculator (weight):
    cost = 0
    if weight <= 2:
        cost += (4.50*weight)
    elif weight <=6:
        cost += (9.00*weight)
    elif weight <=10:
        cost += (12.00*weight)
    else:
        cost += (14.25*weight)
    return cost

#This function will compare the values of the calculator functions
def calculateLowestCost(weight):
    costOfGroundShipping = groundShippingPriceCalculator(weight)
    costOfDroneShipping = droneShippingPriceCalculator(weight)
    print("Ground shipping: " + str(costOfGroundShipping))
    print("Drone shipping: " + str(costOfDroneShipping))

    print("For a package that weighs " + str(weight) + "...")
    if premiumGroundShipping < costOfDroneShipping and premiumGroundShipping < costOfGroundShipping:
        print("Premium ground shipping is the cheapest option and costs 125 dollars.")
    elif costOfGroundShipping < costOfDroneShipping:
        print("Ground shipping is the cheapest option and will cost " + str(costOfGroundShipping) + " dollars.")
    else:
        print("Drone shipping is the cheapest option and will cost " + str(costOfDroneShipping) + " dollars.")

#Test values for the function
        
calculateLowestCost(2)
print
calculateLowestCost(100)
print
calculateLowestCost(4.8)
print
