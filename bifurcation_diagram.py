from matplotlib import pyplot as plt

def f(lamda, x):
	return lamda*x*(1-x)

r = 0

x = []
y = []

while r < 4:

	pop = 0.5

	for _ in range(1000):
		pop = f(r, pop)
	for _ in range(64):
		x.append(r)
		y.append(pop)
		pop = f(r, pop)

	r += 0.0001

plt.style.use('dark_background')
plt.scatter(x, y, s=0.1, color='cyan')
plt.show()