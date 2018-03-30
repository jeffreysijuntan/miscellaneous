import numpy as np

class RandomNumberGenerator():
	def __init__(self, seed=1000, multiplier=7893, increment=3517, modulus=2**13):
		self.x = seed
		self.a = multiplier
		self.c = increment
		self.K = modulus

	def next(self):
		self.x = (self.a * self.x + self.c) % self.K
		u = self.x / self.K
		return u

class RandomVariableGenerator():
	def to_discrete_random_variable(u):
		if (0 < u <= 0.2):
			return 1
		if (0.2 < u <= 0.5):
			return 2
		if (0.5 < u <= 1):
			return 3

	def to_exponential_random_variable(u):
		x = -12 * np.log(1-u)
		return x

def main():
	generator = RandomNumberGenerator()
	W = []
	for i in range(500):
		w = 0
		discrete_var = RandomVariableGenerator.to_discrete_random_variable(generator.next())

		for i in range(4):
			if (discrete_var == 1): w += 10
			if (discrete_var == 2): w += 32
			if (discrete_var == 3):
				w += 7
				x =  RandomVariableGenerator.to_exponential_random_variable(generator.next())
				if (x > 25): w += 25
				if (x <= 25): 
					w += x
					break
		W.append(w)
	
	w5, w6, w7 = W[4:7]
	W = np.sort(W)
	mean = np.mean(W)
	median = np.median(W)

	print('First quartile: ' +  str(W[124]))
	print('Third quartile range: ' + str(W[374]))
	print('Median is: ' + str(median) )
	print('Mean is:' + str(mean))

	Wle15 = len(W[W <= 15]) / 500
	Wle20 = len(W[W <= 20]) / 500
	Wle30 = len(W[W <= 30]) / 500
	Wg40  = len(W[W > 40]) / 500
	Wgw5  = len(W[W > w5]) / 500
	Wgw6  = len(W[W > w6]) / 500
	Wgw7  = len(W[W > w7]) / 500

	print(Wle15)
	print(Wle20)
	print(Wle30)
	print(Wg40)
	print(Wgw5)
	print(Wgw6)
	print(Wgw7)

if __name__ == '__main__':
	main()	

#0.1146240234375, 0.15673828125, 0.5645751953125
