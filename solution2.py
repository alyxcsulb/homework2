# Solution 1

num0 = 0
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
sq0 = num0**2
sq1 = num1**2
sq2 = num2**2
sq3 = num3**2
sq4 = num4**2
sq5 = num5**2
cub0 = num0**3
cub1 = num1**3
cub2 = num2**3
cub3 = num3**3
cub4 = num4**3
cub5 = num5**3
head1 = 'Number'
head2 = 'Square'
head3 = 'Cube'

print (f'{head1: >20} {head2: >20} {head3: >20} \n {num0: >20} {sq0: >20} {cub0: >20} \n {num1: >20} {sq1: >20} {cub1: >20} \n {num2: >20} {sq2: > 20} {cub2: >20} \n {num3: >20} {sq3: >20} {cub3: >20} \n {num4: >20} {sq4: >20} {cub4: >20} \n {num5: >20} {sq5: >20} {cub5: >20} \n')



# Solution 2

# F = 9 / 5 * C  + 32

cel1 = -40
cel2 = 0
cel3 = 40
cel4 = 100
far1 = int((9/5 * cel1) + 32)
far2 = int((9/5 * cel2) + 32)
far3 = int((9/5 * cel3) + 32)
far4 = int((9/5 * cel4) + 32)

print(cel1, " degrees in Celcius is ", far1, " degrees in Farenheit \n")
print(cel2, " degrees in Celcius is ", far2, " degrees in Farenheit \n")
print(cel3, " degrees in Celcius is ", far3, " degrees in Farenheit \n")
print(cel4, " degrees in Celcius is ", far4, " degrees in Farenheit \n")



# Solution 3


x,y,z = [int(x) for x in (input("Enter three integers separated by a comma: ").split(','))]
sum = (x + y + z)
average = sum/ 3
print(f' \n The average of the integers is: {average: ,.2f}. \n')
print(f'The sum of the integers is: {sum: ,d}.')