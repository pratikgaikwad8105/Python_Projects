# new_list = [n * 2 for n in range(1, 5)]
# print(new_list)

names = ["Pratik", "Gaikwad", "John", "Deb"]

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
