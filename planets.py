def weight_on_planets():
   # write your code here
   
   earthWeight = input() # getting earth weight 
   earthWeight2 = float(earthWeight)
   marsWeight, jupiterWeight = (earthWeight2 * 0.38), (earthWeight2 * 2.34)     # converting weights
   
   print("What do you weigh on earth? \nOn Mars you would weigh", marsWeight, "pounds.\nOn Jupiter you would weigh", jupiterWeight, "pounds.") #final statement
   
   
if __name__ == '__main__':
   weight_on_planets()