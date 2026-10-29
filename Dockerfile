FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN --mount=type=secret,id=proxy_ca,required=false \
    if [ -f /run/secrets/proxy_ca ]; then export PIP_CERT=/run/secrets/proxy_ca SSL_CERT_FILE=/run/secrets/proxy_ca; fi; \
    pip install --no-cache-dir uv==0.12.23 && uv sync --frozen --no-dev
COPY services ./services
RUN chmod -R a+rX /app/services
ENV PATH="/app/.venv/bin:$PATH" PYTHONPATH="/app/services/api/src"
USER 10001:10001
CMD ["uvicorn", "engineerquest_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
