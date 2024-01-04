km_ran = float(input("How many kilometers did you ran today?\n"))
data_type = str(type(km_ran)).replace("<class '", "").replace("'>", "")
if data_type == 'float':
    print(f'Your {km_ran} km run was {(km_ran*0.621371):.4f10} mi')
else:
    print("Wrong input added")