FROM python:3.8-alpine
WORKDIR ./

ENV TOKEN_BOT=2028729815:AAFkaNtIxd4NRxhFIf8FqBaKeqB2f3A1YZk
ENV APP_PORT=8443

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "app.py"]