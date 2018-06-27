# Installation
## Step 1: Create virtualenv
```bash
virtualenv -p python3 <VIRTUALENV_PATH>
```

## Step 2:  Activate virtualenv

```bash
source <VIRTUALENV_PATH>/bin/activate
``` 

## Step 3:  Install requirements

```bash
pip install -r requirements.txt
```

## Step 4: Run migrations

```bash
python manage.py migrate
```

## Step 5: Run watson installation

```bash
python manage.py installwatson
```

## Config enviroiment variables

```bash
cp .env-example .env
```
Access the ``.env`` file and config the need variables