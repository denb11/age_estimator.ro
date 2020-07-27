
#####   DATA

unit_symbol = "℃"
unit_name   = "celsius"

# meteo data 4 times a day
locality_name = "CHISINAU"
date          = "24.07.2020"
temp_mo       = 10
temp_no       = 30
temp_ev       = 25
temp_ni       = 6

# calculations
temp_avg      = round((temp_mo + temp_no + temp_ev + temp_ni) / 4)
temp_min      = min(temp_mo, temp_no, temp_ev, temp_ni)
temp_max      = max(temp_mo, temp_no, temp_ev, temp_ni)

is_hot_day = temp_no >= 25
is_cold_night = temp_ni < 10
is_hot_24 = temp_no >= 25 and temp_ni > 10


###### presentation
print()
print("☆" * 23, "METEO", "☆" *23)
print()
print("locality: "  + locality_name)
print("date:     " + date )
print("avg temp: " + str(temp_avg) + unit_symbol)
print("temp min: " + str(temp_min) + unit_symbol)
print("temp max: " + str(temp_max) + unit_symbol)
print("Hot day? : " +str(is_hot_day))
print("Cold night? : " + str(is_cold_night))
print("Hot during 24 hours? : " + str(is_hot_24))
print()
print("☆" * 50)
