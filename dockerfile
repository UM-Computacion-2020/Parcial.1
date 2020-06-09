FROM python:3
RUN https://github.com/IvanCsir/parcial-1.git
WORKDIR /parcial-1
CMD ["python3", "test_member.py"]&&["python3", "test_book.py"]