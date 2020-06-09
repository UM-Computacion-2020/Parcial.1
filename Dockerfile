FROM python:3
RUN git clone https://github.com/militomba/59128.Tomba.Milagros.git
WORKDIR /59128.Tomba.Milagros
CMD ["python3", "test_book.py"] && ["python3", "test_member.py"]