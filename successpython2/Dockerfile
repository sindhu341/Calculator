# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py /

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD [ "python", "./main.py" ]
