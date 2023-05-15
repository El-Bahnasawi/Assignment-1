FROM python:3.10

ADD test.py .

CMD ["pytest" , "./test.py"]