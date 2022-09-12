FROM python:3.8-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --use-deprecated=legacy-resolver -r requirements.txt

# Port for GRPC
EXPOSE 5000
# Port for REST
EXPOSE 9000

COPY . /app
RUN mkdir -p /app/.cache
ENV TRANSFORMERS_CACHE /app/.cache
# Define environment variable

ENV MODEL 'cardiffnlp/twitter-roberta-base-sentiment'
ENV TOKENIZER 'cardiffnlp/twitter-roberta-base-sentiment-latest'
ENV MODEL_NAME Sentiment
ENV SERVICE_TYPE MODEL

USER root
RUN chmod -R 777 /app

RUN python util.py
CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE
