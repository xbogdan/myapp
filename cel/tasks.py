from celery.task import Task


class AddTask(Task):
	def run(self, a, b, *args, **kwargs):
		return a + b