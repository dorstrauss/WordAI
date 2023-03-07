FROM python:3.11-windowsservercore-1809

WORKDIR /documentGPT

COPY . /documentGPT/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

ENV OPENAI_API_KEY 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