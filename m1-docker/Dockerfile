FROM python:3.12.7-slim@sha256:ab12cd34ab12cd34ab12cd34ab12cd34ab12cd34ab12cd34ab12cd34ab12cd34
WORKDIR /app
COPY src/ ./src/
RUN useradd --system --uid 10001 app
USER app
CMD ["python", "-m", "src.main"]
