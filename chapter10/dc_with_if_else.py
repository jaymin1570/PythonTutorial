# odd_even ={}

# for i in range(1,11):
#     if i%2==0:
#         odd_even[i]='even'
#     else:
#         odd_even[i]='odd'
# print(odd_even)

odd_even = {i :'even' if i%2==0 else 'odd' for i in range(1,11)}
print(odd_even)
