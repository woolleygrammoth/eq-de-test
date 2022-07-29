FROM python:3
WORKDIR /usr/eq-de-test
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD /bin/bash