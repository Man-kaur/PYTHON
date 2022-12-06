import random
def axes(n):
    if (n>0):
        print("{} is a positive number.".format(n))
    elif (n==0):
        print("The number is {} .".format(n))
    else:
        print("{} is a negative number.".format(n))
def odd(n):
    if (n%2==0):
        print("{} is an even number.".format(n))
    else:
        print("{} is an odd number.".format(n))
def prime(n):
    if (n>=2):
        i=1
        count=0
        while (i<=n):
            if (n%i==0):
                count+=1
            i+=1
        if (count==2):
            print("{} is a prime number.".format(n))
        else:
            print("{} is a composite number.".format(n))
    elif (n==0) or (n==1):
        print("{} is neither prime nor composite.".format(n))
    else:
        print("For negative numbers, the property of prime numbers doesn't exist.")
while (True):
    print("Press '1' to enter the program. \nPress '2' to print the location of integer on axes. \nPress '3' to print the odd/even property. \nPress '4' to print the prime composite/property.\nPress '5' to Exit the current range. \nEnter 'Yes' to continue. \nEnter any random charcter to exit the program.")
    enter=input("Enter your choice: ")
    if enter=='1':
        a=int(input("Enter the starting number for the range: "))
        b=int(input("Enter the ending number for the range: "))
        print("The range is ({0},{1})".format(a,b))
        n=random.randint(a,b)
        print("The randomly picked number is {}.".format(n))
        while True:
            choice=input("Which property do you want: ")
            if choice=='2':
                axes(n)
            elif choice=='3':
                odd(n)
            elif choice=='4':
                prime(n)
            continued='Yes'
            continued1=input("Do you want to continue?: ")
            if continued1==continued:
                continue
            else:
                break
    elif choice=="5":
        print("Exit")