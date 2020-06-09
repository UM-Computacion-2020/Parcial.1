FROM python:3

WORKDIR /app/src/

RUN git clone https://github.com/juarez-gonza/Computacion.Parcial.1.git && \
pip install parameterized

ENTRYPOINT ["/bin/bash", "-c", "/app/src/Computacion.Parcial.1/run_tests"]
