list_input_inches = [i for i in list(map(int,input().split()))]
list_output_cm = [cm * 2.54 for cm in list_input_inches]
print(list_output_cm)
