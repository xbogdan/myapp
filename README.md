# Description
This repository contains test cases for different celery issues/bugs.

# Run
```pip install -r requirements.txt```

```./manage.py test_cmd```

# Run worker
```celery -A myapp worker -c 200 -P gevent -Q requests_queue --soft-time-limit=100 --time-limit=120 -l INFO```
