import time


def decorator_1(f):
	"""
	Function decorator which calculates execution time of function and number of calls of function
	:param f: function
	:return: modified function
	"""
	def executer(*args):
		start = time.perf_counter()
		result = f(*args)
		end = time.perf_counter()
		print(f.__name__ + ' call ' + str(executer.counter) + ' elapsed time: ' + str(end-start))
		executer.counter += 1
		return result
	executer.counter = 1
	return executer
