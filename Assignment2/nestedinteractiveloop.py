list_input_inches = list(map(int,input().split()))
list_output_cm = []
for element in list_input_inches:
    list_output_cm.append(element * 2.54)
print(list_output_cm)
