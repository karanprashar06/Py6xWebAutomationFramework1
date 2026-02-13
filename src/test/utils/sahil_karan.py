def scooter(rs=None, year=None):
    if rs and year:
        print("ola scooty")
    elif year:
        print("bajaj scooter")
    else:
        print("default scooter")

scooter(rs=211, year=2000)
scooter(year=2000)
scooter()