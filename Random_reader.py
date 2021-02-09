#Reads a textfile with random numbers and plots it

#imports packages
import matplotlib.pyplot as plt


#open the random numbers file
file = open("random_numbers.txt")


#reads the lines
line = file.readlines()

#makes an array of all the numbers to plot them
i=0
x=[]
for i in range(0,len(line)):
    x.append(float(line[i]))
# an array of random numbers using our Random class
file.close()
print(x)

#plots the histogram
plt.hist(x,bins= 25)    
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Uniform random number')
plt.grid(True)
plt.show()




