FROM ubuntu

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y python3 python3-pip \
    pip install streamlit

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]

LABEL maintainer="Taha Taha"
LABEL version="1.0"
LABEL description="Recipe app built with Streamlit"
