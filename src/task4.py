from time import strftime


def decorator_4(f):
	def wrapper(*args, **kwargs):
		try:
			res = f(*args, **kwargs)
		except Exception as e:
			res = '\nException name: \t| ' + str(e) + '\nFunction name: ' + f.__name__ + ' | ' + str(strftime('%d.%m.%Y %H:%M:%S'))
			with open('log.txt', 'a') as file:
				file.write(res)
		return res
	return wrapper


class decorator_4_classed:

	def __init__(self, f):
		self.f = f

	def __call__(self, *args, **kwargs):
		try:
			res = self.f(*args, **kwargs)
		except Exception as e:
			res = '\nException name: \t| ' + str(e) + '\nFunction name: ' + self.f.__name__ + ' | ' + str(strftime('%d.%m.%Y %H:%M:%S'))
			with open('log.txt', 'a') as file:
				file.write(res)
		return res
