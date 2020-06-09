FROM python:3

RUN git clone https://github.com/MatiasTomasRobbio/Parcial1-Matias-Robbio.git

RUN pip3 install parameterized

WORKDIR /Parcial1-Matias-Robbio

CMD ["python3", "test_book.py"] && ["python3", "test_member.py"]
