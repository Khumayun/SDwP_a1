import contextlib
import io
import time


class decorator_3:
	"""
	Decorator class which calculates execution time of arbitrary number of functions and saves data to a global varaible "rank".
	:param func: arbitrary number of functions
	:return: None
	"""

	def __init__(self, f):
		self.f = f
		self.rank = f.__globals__['rank']

	def __call__(self, *args, **kwargs):
		with contextlib.redirect_stdout(io.StringIO()) as fun:
			start = time.perf_counter()
			self.f(*args, **kwargs)
			end = time.perf_counter()
			self.rank.append({'name': self.f.__name__, 'rank': 0, 'elapsed': str(end-start)})
		res = fun.getvalue()
		with open('text.txt', 'a') as file:
			file.write('function name: ' + self.f.__name__)
			file.write('\n' + res)
		print(res)
		return res
