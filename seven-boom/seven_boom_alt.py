def divisible_by_seven(num):
	divisible = num % 7 == 0
	return divisible

def contains_seven(num):
	contains = '7' in str(num)
	return contains

def seven_boom():
    num = 1
    counter = 1
    while True:
        if counter == 7:
            print("BOOM")
            counter = 0
        elif contains_seven(num):
            print("BOOM")
        else:
            print(num)
        num += 1
        counter += 1

if __name__ == "__main__":
	seven_boom()
