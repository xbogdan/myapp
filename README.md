# run
```pip install -r requirements.txt```

```./manage.py test_cmd```

# run worker
```celery -A myapp worker -c 200 -P gevent -Q requests_queue --soft-time-limit=100 --time-limit=120 -l INFO```
