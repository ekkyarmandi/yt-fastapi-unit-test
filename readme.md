# Cara Menulis Unit Test untuk Aplikasi FastAPI

# Requirements

```
coverage==7.6.1
fastapi==0.114.1
httpx==0.27.2
pytest==8.3.3
uvicorn==0.30.6
```

## Cara install requirements.txt

```bash
pip install -r requirements.txt
```

## Uvicorn command

```bash
uvicorn main:app --reload
uvicorn [file]:[var] --reload
```

## Pytest command

```bash
pytest dir/
pytest path/to/file.py
pytest path/to/file.py::test_unit_function
```

## Coverage command

```bash
coverage run -m pytest dir/
```
