address = ("Kadi", "Gujarat", "India", 382715)

# ACCESS
print(address)
print(address[3])
print(address[1:3])
print(address[::-1])


# UNPACKING
city, state, country, pin = address
print(city)


# METHODS
print(address.index("Gujarat"))
print(address.count(382715))

# SWAP VARIABLES using tuple
a,b = 10, 20
a, b = b,a
print(a, b)