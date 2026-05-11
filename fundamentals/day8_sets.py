
frontend = {"Python", "HTML", "CSS"}
backend = {"Python", "Django", "MySQL"}


# Methods
frontend.add("JS")
print(frontend)

frontend.remove("JS") # Shows error
frontend.discard("JS")
print(frontend)


# Operations
frontend = frontend.union(backend)
print(frontend)

frontend = frontend.intersection(backend)
print(frontend)

frontend = frontend.difference(backend)
print(frontend)

frontend = frontend.symmetric_difference(backend)
print(frontend)