from celery.task import Task


class AddTask(Task):
	def run(self, a, b, *args, **kwargs):
		print(a, b)
		print(args)
		print(kwargs)
		return a + b