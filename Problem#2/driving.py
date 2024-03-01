#Name: Xander Konell
#Hour: 3
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   return dollars_per_gallon/miles_per_gallon*miles_driven
   #write your code here

if __name__ == '__main__':
   miles_per_gallon = float(input())
   dollars_per_gallon = float(input())
    #print your costs here like example below
   miles_driven=[10, 50, 400]
    #print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
   for miles in miles_driven:
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles):.2f}')