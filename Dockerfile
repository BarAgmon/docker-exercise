FROM python
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
CMD python app.py
