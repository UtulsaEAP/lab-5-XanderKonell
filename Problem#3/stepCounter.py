#Name: Xander Konell
#Hour: 3
def feet_to_steps(user_feet):
   #write your code here
   steps = user_feet / 2.5
   return round(steps)
if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
    user_feet = float(input())
    steps_walked = feet_to_steps(user_feet)
    #print your steps here
    print(steps_walked)