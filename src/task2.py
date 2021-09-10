import contextlib
import inspect
import io


def decorator_2(f):
	def wrapper(*args, **kwargs):
		print('Name:\t', f.__name__)
		print('Type:\t', type(f))
		print('Sign:\t', inspect.signature(f))
		print('Args:\tPositional: ', f.__defaults__)
		print('\t\tkey-worded: ', f.__kwdefaults__)
		print('\nDoc: ', f.__doc__)
		print('\nSource:', inspect.getsource(f))
		print('\nOutput:\t')
		with contextlib.redirect_stdout(io.StringIO()) as fun:
			f(*args, **kwargs)
		res = fun.getvalue()
		print(res)

	return wrapper