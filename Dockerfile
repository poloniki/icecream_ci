FROM python:3.8-slim
COPY icecream icecream/
COPY setup.py setup.py
COPY requirements.txt requirements.txt
RUN pip install .
CMD uvicorn icecream.api:app --host 0.0.0.0 --port $PORT
