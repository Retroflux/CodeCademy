
premiumGroundShipping = 125.00

#calculates the ground shipping cost based on the weight given.
def groundShippingPriceCalculator (weight):
    cost = 20 #base cost
    #test increasing weights to reduce comparisons to one per statement instead of boundary checks
    if weight <= 2:
        cost += (1.50*weight)
    elif weight <=6:
        cost += (3.00*weight)
    elif weight <=10:
        cost += (4.00*weight)
    else:
        cost += (4.75*weight)
    return cost

#calculates the drone shipping costs based on the weight given.
def droneShippingPriceCalculator (weight):
    cost = 0
    #test increasing weights to reduce comparisons to one per statement instead of boundary checks
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
    
    #call the above functions to get the numbers to compare
    costOfGroundShipping = groundShippingPriceCalculator(weight)
    costOfDroneShipping = droneShippingPriceCalculator(weight)

    #output to ensure correctness
    print("Ground shipping: " + str(costOfGroundShipping))
    print("Drone shipping: " + str(costOfDroneShipping))

    #final output based on a conditional branch
    print("For a package that weighs " + str(weight) + "...")
    if premiumGroundShipping < costOfDroneShipping and premiumGroundShipping < costOfGroundShipping:
        print("Premium ground shipping is the cheapest option and costs 125 dollars.")
    elif costOfGroundShipping < costOfDroneShipping:
        print("Ground shipping is the cheapest option and will cost " + str(costOfGroundShipping) + " dollars.")
    else:
        print("Drone shipping is the cheapest option and will cost " + str(costOfDroneShipping) + " dollars.")

#Main#
#Test values for the function  
calculateLowestCost(2)
print
calculateLowestCost(100)
print
calculateLowestCost(41.5)
print
calculateLowestCost(4.8)
print
