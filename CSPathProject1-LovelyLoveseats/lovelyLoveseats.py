

#sales tax that will likely be applied to all of the items. 
SALES_TAX = 0.088


#description and price for the loveseat
lovelyLoveseatDescription = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovelyLoveseatPrice = 254.00

#description and price for the settee
stylishSetteeDescription = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylishSetteePrice = 180.50

#description and price for the lamp
luxuriousLampDescription = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxuriousLampPrice = 52.15

#We have yet to learn Python data structures, so each customer is stored here in a variable.
customerOneTotal = 0;
customerTwoTotal = 0;

#This will hold the items that they are buying I think?
customerOneItemization = ""
customerTwoItemization = ""

########################
#Customer One Purchases#
########################

#customer one purchases the loveseat and lamp. Add the descriptions to the string
customerOneTotal += (lovelyLoveseatPrice + luxuriousLampPrice)
customerOneItemization = lovelyLoveseatDescription + "\n" + luxuriousLampDescription + "\n"

customerOneTax = customerOneTotal * SALES_TAX #calculate tax
customerOneTotal += customerOneTax #add tax to total

print ("Customer One Items: \n" + customerOneItemization)
print ("Customer One Total: \n" + str(customerOneTotal) + "\n\n")

########################
#Customer Two Purchases#
########################

#customer two purchases the settee and the lamp Add the descriptions to the string
customerTwoTotal += (luxuriousLampPrice + stylishSetteePrice)
customerTwoItemization = luxuriousLampDescription + "\n" + stylishSetteeDescription + "\n"

customerTwoTax = customerTwoTotal * SALES_TAX #calculate tax
customerTwoTotal += customerTwoTax #add tax total

print ("Customer Two Items: \n" + customerTwoItemization)
print ("Customer Two Total: \n" + str(customerTwoTotal) + "\n\n")