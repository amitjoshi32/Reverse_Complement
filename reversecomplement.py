DNA=input("Enter your DNA sequence below:\n")
DNA_upper=DNA.upper()
DNA_upper_reversed=DNA_upper[::-1]

for i in DNA_upper_reversed:
  if(i=="A"):print("T", end='')
  elif(i=="T"):print('A',end='')
  elif(i=="C"):print('G',end='')
  elif(i=='G'):print("C",end='')