##### AGE ESTIMATOR#######

print("Introduceti numele: ")
name        = str(input())
print("Introduceti anul nasterii:")
year_birth  = int(input())
age         = 2020 - int(year_birth)
print(name, " are: ", age, "ani!")
if year_birth < 1990 or year_birth > 2020:
    print("EROARE: anul nasterii nu corespunde.")
else:
    if age <= 3 :
        print("1-3 ani - 'baby'")
    elif age  <= 9:
        print("4-9 ani - 'kid'")
    elif age <= 15:
        print("10-15 ani - 'teen'")
    elif age <= 18:
        print("16-18 ani - 'young'")
    elif age <= 50:
        print("19-50 ani - 'adult'")
    else:
        print("51+ ani -'old'")
