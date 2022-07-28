FROM python:alpine

RUN apk update && \
    apk add git

RUN git clone https://github.com/sandy-sunday/qabot

# WORKDIR /chatbotapp
# WORKDIR .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
ADD start.sh /
RUN chmod +x /start.sh
EXPOSE 8080
CMD ["/start.sh"]
# CMD ["python", "server.py"]