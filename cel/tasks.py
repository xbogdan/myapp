import requests
from celery.task import Task
from myapp.celery import app


class AddTask(Task):
    def run(self, a, b, *args, **kwargs):
        print(a, b)
        print(args)
        print(kwargs)
        return a + b


@app.task(ignore_result=True, queue='request_queue')
def request_task(url, *args, **kwargs):
    # make the request
    req = requests.get(url)

    request = {
        'status_code': req.status_code,
        'content': req.text,
        'headers': dict(req.headers),
        'encoding': req.encoding
    }

    process_task.apply_async(kwargs={'url': url, 'request': request})


@app.task(ignore_result=True, queue='process_queue')
def process_task(url, request, *args, **kwargs):
    # do something
    pass
