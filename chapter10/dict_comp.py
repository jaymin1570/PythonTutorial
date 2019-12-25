# dictionary comprehension 
# new = dict()
# for i in range(1,4):
#     new[i]= i**2
# print(new)
# print(type(new))

# new2 = {f"square of {i} ": i**2 for i in range(1,4)}
# for k,v in new2.items():
#     print(f"{k}:{v}")

# jaymin
name ="jaym ina"
# counter = dict()
# for ch in name:
#     counter[ch]=name.count(ch)
# print(counter)

counter = {ch : name.count(ch) for ch in name}
print(counter)

j1 = "jayminmakwana "
print("#".join(j1))