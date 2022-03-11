def func_counter(func):
	def wrapper(*args, **kwargs):
		wrapper.counter += 1
		return func(*args, **kwargs)

	wrapper.counter = 0
	return wrapper

@func_counter
def testfunc(x):
	print(f'Testing {x}')
	return 1

def main():
	testfunc(1)
	testfunc(2)
	print(testfunc.counter)

if __name__ == "__main__":
	main()
