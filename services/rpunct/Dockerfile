FROM python:3.8-slim

RUN pip install \
  torch==1.9.0+cpu \
  torchvision==0.10.0+cpu \
  torchaudio==0.9.0 \
  -f https://download.pytorch.org/whl/torch_stable.html \
  && rm -rf /root/.cache/pip

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --use-deprecated=legacy-resolver -r requirements.txt

# Port for GRPC
EXPOSE 5000
# Port for REST
EXPOSE 9000

COPY . /app

ENV TRANSFORMERS_CACHE /app/.cache
USER root
RUN chmod -R 777 /app

RUN python /app/fetch_model.py
# Define environment variable
ENV MODEL_NAME RPunct
ENV SERVICE_TYPE MODEL

CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE
