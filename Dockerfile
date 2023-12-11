FROM python:3.9-slim-bullseye

LABEL maintainer="Brico Bc" 
WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt && pip install jupyter


EXPOSE 8888

CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
