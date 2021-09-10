import time


def decorator_1(f):
	def executer(*args):
		start = time.perf_counter()
		result = f(*args)
		end = time.perf_counter()
		print(f.__name__ + ' call ' + str(executer.counter) + ' elapsed time: ' + str(end-start))
		executer.counter += 1
		return result
	executer.counter = 1
	return executer
