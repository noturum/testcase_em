FROM python:3.12-slim
LABEL authors="noturum"
WORKDIR /test
ENV PYTHONPATH=/test
COPY . .
RUN pip install -r requirements.txt
CMD ["pytest", "test_api.py"]