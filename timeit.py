import os
import time

def calculate_time(func):
	def wrapper(*args, **kwargs):
		start_time = time.time()
		res = func(*args, **kwargs)
		end_time = time.time()
		print(f'Total time {end_time - start_time}')
		return res
	return wrapper

def main():
	def testfunc():
		print("Test wait for 5s")
		time.sleep(5)

	newfunc = calculate_time(testfunc)
	newfunc()

if __name__ == "__main__":
	main()
