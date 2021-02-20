import math
import sys
import os
"""
-----------------------------Riddle Solver------------------------------
Based on riddles from:
Problem solving and algorithmic thinking course | College of Management 
------------------------------------------------------------------------
"""

sys.setrecursionlimit(1000)

#https://imgur.com/1M2MzU5
def snake_skin(BirthSize,DeadSize,MultBy):
	if BirthSize==DeadSize:
		return 0 
	if DeadSize % MultBy == 0  and DeadSize / MultBy >= BirthSize:
		return snake_skin(BirthSize, DeadSize / MultBy, MultBy)+1
	return snake_skin(BirthSize, DeadSize-1, MultBy)+1

#https://imgur.com/P26d852
def ladder(n):
	if n<=2:
		return n
	return ladder(n-1) +ladder(n-2)

def xor(x,y):
	return x^y

#https://imgur.com/DeUU1ma
def hanoi(n):
	return (pow(2,n) - 1)

#https://imgur.com/dLWrn9S
def josephus(n , k):
    if n==1:
        return 1
    else:
        return (josephus(n-1 , k) + k-1) % n +1

#https://imgur.com/a/NJqSwOd
def light_bulbs(x):
	list =[]
	for i in range(1,x):
		if math.sqrt(i) == int(math.sqrt(i)):
			list.append(i)
	return list

#https://imgur.com/c1vqdXy
def yarkan(x):
	if x ==1:
		return 1
	return yarkan(x-1)*3 + 1

#https://imgur.com/1g35S90
def coins_chain(x):
	even = 0
	odd = 0
	for i in range(0,len(x)):
		if i % 2 == 0:
			even += x[i]
		else :
			odd+=x[i]
	return max(even,odd)

ascii_header = """
  _____     _ _      ___ _    _    _ _       ___      _             
 |_   _|_ _| ( )___ | _ (_)__| |__| | |___  / __| ___| |_ _____ _ _ 
   | |/ _` | |/(_-< |   / / _` / _` | / -_) \__ \/ _ \ \ V / -_) '_|
   |_|\__,_|_| /__/ |_|_\_\__,_\__,_|_\___| |___/\___/_|\_/\___|_|  
                                                                    """
intro = ascii_header + '\n' + "© https://github.com/TAL4real" + '\n' + "╭─────────────────────────╮" + '\n' + "│ 1 - Snake Skin          │\n│ 2 - FireFighters Ladder │\n│ 3 - XOR                 │\n│ 4 - HanoiTowers         │\n│ 5 - Josephus Problem    │\n│ 6 - Light Bulbs         │\n│ 7 - Yarkan's Problem    │\n│ 8 - Coins Chain         │\n│-------------------------│\n│ C - Clear Screen        │\n│ exit - Exits the program│" + '\n' + "╰─────────────────────────╯"
print(intro)
if __name__ == "__main__":
	while True:
		
		num = input("Choose a number: ")
		try:
			num = int(num)
		except:
			if num.lower() == 'c' or num.lower() == 'clear':
				os.system('cls')
				print(intro)
			elif num.lower() == 'exit' or num.lower() == 'e':
			    quit()
			else:
				print('Invalid input')

		if num == 1:
			try:
				x = int(input("  Birth length: "))
				y = int(input("  Die length: "))
				z = int(input("  Growing option 1 - multiple by?: "))
				ans = snake_skin(x,y,z)
				print(f"• It will take him {ans} sheddings\n")
			except:
				print('ERROR: Numbers only\n')

		if num == 2:
			try:
				x = int(input(" Ladder length: "))
				ans = ladder(x)
				print(f'• There are {ans} climbing options\n')
			except:
				print('ERROR: Numbers only\n')

		if num == 3:
			try:
				x = int(input(" Number 1: "))
				y = int(input(" Number 2: "))
				ans = xor(x,y)
				print(f'• {x} ⊕ {y} = {ans}\n')
			except:
				print('ERROR: Numbers only\n')

		if num == 4:
			try:
				x = int(input("  Number of rings: "))
				ans = hanoi(x)
				print(f'• It will take {ans} moves\n')
			except:
				print('ERROR: Numbers only\n')

		if num == 5:
			try:
				x = int(input("  Number of people: "))
				y = int(input("  Jump: "))	
				ans = josephus(x,y)
				print(f'• The survivor is seat {ans}\n')
			except:
				print('ERROR: Numbers only\n')

		if num == 6:
			try:
				x = int(input("  Number of light bulbs: "))
				ans = light_bulbs(x)
				print("• The active light bulbs are:",ans)
			except:
				print('ERROR: Numbers only\n')

		if num == 7:
			try:
				x = int(input("  Number of weights: "))
				ans = yarkan(x)
				print(f'There are {ans} options\n')
			except:
				print('ERROR: Numbers only\n')

		if num == 8:
			try:
				x = list(map(int,input("  Enter the coins(With spaces between every coin) : ").strip().split()))
				ans = coins_chain(x)
				print(f'• The biggest win option is {ans}\n')
			except:
				print("Invalid input, Exmaple: 10 8 5 1 5 7 2 6 4\n")
