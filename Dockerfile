FROM python:3.9-slim

EXPOSE 8501

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    python3-pip git && \
    git clone https://github.com/tahataha005/recipe-app . &&\
    pip3 install -r requirements.txt

CMD ["streamlit", "run", "app.py"]

LABEL maintainer="Taha Taha"
LABEL version="1.0"
LABEL description="Recipe app built with Streamlit"
