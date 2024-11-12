FROM python:3.10-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y poppler-utils

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY src ./src

EXPOSE 8501

CMD ["streamlit", "run", "src/app.py"]
