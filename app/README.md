# Webhook

* Step 1: Create and activate Virtualenv

```bash
virtualenv -p python3 venv
```

```bash
source venv/bin/activate
```

* Step 2: Install requirements
```bash
pip install flask
```

* Step 3: Run the app
```bash
python app.py
```

* Now pass the requests into `/listner` url

Format should be 
* For Error
```bash
{
        "type": 'error',
        "data": {
            "data": "hell event"
        }
    }
```

* For Success
```bash
{
        "type": 'success',
        "data": {
            "data": "hell event"
        }
    }
```