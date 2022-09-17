FROM python:3.8-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --use-deprecated=legacy-resolver -r requirements.txt

# Port for GRPC
EXPOSE 5000
# Port for REST
EXPOSE 9000

COPY . /app
# Define environment variable
ENV MODEL_NAME Combiner
ENV SERVICE_TYPE COMBINER

CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE
