#########   PRODUCTS   ##########

# strat de date ( data layer )
p_1_name  = " iphone IX"
p_1_price = 1000
p_1_q     = 3
p_1_ava   = True

p_2_name  = " iphone XI"
p_2_price = 2000
p_2_q     = 0
p_2_ava   = False

p_3_name  = " samsung note10"
p_3_price = 1500
p_3_q     = 4
p_3_ava   = True

######  Logic layer

p_total_q = p_1_q + p_2_q + p_3_q
p_total_cost = p_1_q * p_1_price + p_2_q * p_2_price + p_3_q * p_3_price

#######    Presentation Layer
print()
print("#" * 15, "GRAND TOTAL", "#" * 15)
print("TOTAL PHONE: " + str(p_total_q))
print("TOTAL WORTH: " + str(p_total_cost))
print("Is" + p_1_name + " Avalaible?  " + str(p_1_ava))
print("Is" + p_2_name + " Avalaible?  " + str(p_2_ava))
print("Is" + p_3_name + " Avalaible?  " + str(p_3_ava))