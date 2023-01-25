from os import system
from random import choice
from colorama import Fore

class TTT:
	def __init__(self):
		print('Modes:\nEasy - 1\nMedium - 2\nHard - 3')
		self.mode = input('Choose: ')
		self.sign = input('X or O:')
		self.sign = 'X' if self.sign.lower()=='x' else 'O'
		self.laptop = 'O' if self.sign == 'X' else 'X'
		self.spaces = list(range(9))
		self.desk = [str(i) for i in range(1,10)]
		self.step = 0
		if self.mode == '1':
			self.start(self.put)
	def start(self,f):
		qadam = 1
		self.step = 1 if self.sign == 'X' else 0
		while qadam<=9:
			system("clear")
			self.show()
			if self.step:
				if f(int(input('Choose a number: '))-1):
					qadam+= 1
					self.step = not self.step
			else:
				f(choice(self.spaces))
				qadam += 1
				self.step = not self.step
			res = self.finished()
			if res[0]:
				system('clear')
				self.show()
				print('You win!' if self.sign in res[1] else 'AI win!')
				break
		if not self.finished()[0]:
			system("clear")
			self.show()
			print('Draw!')
	def finished(self):
		for i in range(0,7,3):
			if len(s:=set(self.desk[i:i+3])) == 1:
				return [True,s]
		for i in range(3):
			if len(s:=set(self.desk[i::3])) == 1:
				return [True,s]
		s = set(self.desk[::4])
		if len(s) == 1:
			return [True,s]
		s = set(self.desk[2:7:2])
		if len(s) == 1:
			return [True,s]
		return [False,{''}]
	def put(self,i):
		if self.desk[i] not in 'OX':
			self.desk[i] = self.sign if self.step%2 else self.laptop
			self.spaces.remove(i)
			return True
		return False
	def show(self):
		line = '+---'*3+'+'
		print(Fore.WHITE+line)
		for i in range(9):
			l = len(self.desk[i])
			print(Fore.WHITE+f"|{' '*(2-l)}",end='')
			if self.desk[i] == 'X':
				print(Fore.RED+'X ',end='')
			elif self.desk[i] == 'O':
				print(Fore.BLUE+'O ',end='')
			else:
				print(Fore.YELLOW+f'{self.desk[i]} ',end='')
			if i%3 == 2:
				print(Fore.WHITE+f"|\n{line}")
class TTTMedium(TTT):
	def __init__(self):
		super().__init__()
		if self.mode == '2':
			self.start(self.put2)
	def put2(self,i):
		if self.step%2 and self.desk[i] not in 'XO':
			self.desk[i] = self.sign
			self.spaces.remove(i)
			return True
		elif self.step%2==0:
			for j in self.spaces:
				self.desk[j] = self.sign
				if self.finished()[0]:
					self.desk[j] = self.laptop
					self.spaces.remove(j)
					return True
				else:
					self.desk[j] = str(j+1)
			self.desk[i] = self.laptop
			self.spaces.remove(i)
		else:
			return False
class TTTHard(TTTMedium):
	def __init__(self):
		super().__init__()
		if self.mode == '3':
			self.start(self.put3)
	def put3(self,i):
		if self.step%2 and self.desk[i] not in 'XO':
			self.desk[i] = self.sign
			self.spaces.remove(i)
			return True
		elif self.step%2==0:
			if self.desk[4] == '5':
				self.desk[4] = self.laptop
				self.spaces.remove(4)
				return True
			elif self.desk[4] == self.sign and self.desk[0] == '1':
				self.desk[0] = self.laptop
				self.spaces.remove(0)
				return True
			for j in self.spaces:
				self.desk[j] = self.laptop
				if self.finished()[0]:
					return True
				else:
					self.desk[j] = str(j+1)
			for j in self.spaces:
				self.desk[j] = self.sign
				if self.finished()[0]:
					self.desk[j] = self.laptop
					self.spaces.remove(j)
					return True
				else:
					self.desk[j] = str(j+1)
			if self.step == 4:
				while (i == 2 or i == 6) and self.desk[0]==self.sign and self.desk[8] == self.sign:
					i = choice(self.spaces)
				self.desk[i] = self.laptop
				self.spaces.remove(i)
				return True
			self.desk[i] = self.laptop
			self.spaces.remove(i)
		else:
			return False
if __name__ == "__main__":
	TTTHard()

