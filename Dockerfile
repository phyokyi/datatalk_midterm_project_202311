FROM python:3.10.12-slim
RUN pip install pipenv
WORKDIR /app
COPY ["Pipfile","Pipfile.lock","./"]
RUN pipenv install --deploy --system
COPY ["app.py","complain_forecast.pkl", "./"]
EXPOSE 2001
ENTRYPOINT  ["gunicorn","--bind","0.0.0.0:2001","app:app"]