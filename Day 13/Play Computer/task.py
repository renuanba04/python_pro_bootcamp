year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
else:
    first_born = input("Are you the first born? Type 'y' or 'n'").lower()
    if first_born:
        print("You are a GEN Z")
    else:
        print("You are a millennial")