from matplotlib import pyplot as plt

def f(lamda, x):
	return lamda*x*(1-x)

def run(lamda, x, length):
	for _ in range(length):
		x = f(lamda, x)
	return x

def map(value, start1, stop1, start2, stop2):
	return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

def rnd(seed):
	num = (run(seed, 0.5, 100 + int((seed*100)%32))*10000*seed)%1
	seed = map(num, 0, 1, 3.6, 3.99)
	return seed, num

plt.ion()
plt.style.use('dark_background')
y = []

seed = 3.54 # in [3.6, 4[
num = None

while True:
	
	# calc random
	seed, num = rnd(seed)

	# save random
	y.append(num)

	# plot
	if len(y)%10000 == 0:
		plt.clf()
		plt.hist(y, bins=100, color='cyan')
		plt.pause(0.001)

# finished
print('done')
plt.pause(10000000)