FROM python:3.8-alpine as runtime

RUN apk add --no-cache -u ffmpeg flac
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY test_audio.ogg .
COPY transcribe.py .
COPY app.py .

ENTRYPOINT ["gunicorn"]
CMD ["-b", "0.0.0.0", "app:app"]
