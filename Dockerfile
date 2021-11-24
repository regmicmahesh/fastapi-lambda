FROM public.ecr.aws/lambda/python:3.9

WORKDIR /usr/src/app

COPY ./setup.py .

RUN python3 -m ensurepip
RUN pip install .

COPY . ${LAMBDA_TASK_ROOT}

CMD ["app.main.handler"]

