def doubler(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		func(*args, **kwargs)
		return result
	return wrapper

def main():
	def testfunc():
		print("Testing")
	newfunc = doubler(testfunc)
	newfunc()

if __name__ == "__main__":
	main()
