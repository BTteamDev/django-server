### For installing libraries:

```bash
    pip install -r requirements.txt
```
# If will throw an error:

```bash
    pip install -r requirements.txt --user
```
 - or

```bash
    python -m pip install -r requirements.txt
```
### If 'db.sqlite3' file not found:

```bash
    python manage.py migrate
```

### Run

```bash
    python manage.py runserver
```
