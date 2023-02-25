apple_three = int(input())
apple_two = int(input())
apple_one = int(input())
banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

total_apple = 3*apple_three + 2*apple_two + 1*apple_one
total_banana = 3*banana_three + 2*banana_two + 1*banana_one

if (total_apple > total_banana) :
	print("A")
elif (total_apple == total_banana) :
	print("T")
else :
	print("B")