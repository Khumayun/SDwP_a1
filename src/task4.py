from time import strftime


def decorator_4(f):
	def wrapper(*args, **kwargs):
		try:
			res = f(*args, **kwargs)
		except Exception as e:
			res = 'Exception name: \t| ' + str(e) + '\nFunction name: ' + f.__name__ + ' | ' + str(strftime('%d.%m.%Y %H:%M:%S'))
			with open('log.txt', 'w') as file:
				file.write(res)
		return res
	return wrapper
