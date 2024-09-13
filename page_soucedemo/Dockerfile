FROM python:3.11-slim
LABEL authors="noturum"
WORKDIR /page_soucedemo
ENV PYTHONPATH=/page_soucedemo
COPY . .
RUN pip install -r requirements.txt
CMD ["pytest", "Tests"]