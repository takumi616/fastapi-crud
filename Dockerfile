# ---------- Builder Stage ----------
FROM python:3.14-slim AS builder

RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*
        
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
        
WORKDIR /app
        
COPY pyproject.toml uv.lock ./
    
RUN uv venv && \
    uv sync --frozen --no-dev --no-editable
        
COPY ./app ./app


# ---------- Final Stage ----------
FROM python:3.14-slim AS final
        
RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*
        
RUN useradd -m appuser
        
WORKDIR /app
        
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/app ./app
        
ENV PATH="/app/.venv/bin:$PATH"
ENV VIRTUAL_ENV="/app/.venv"
        
RUN chown -R appuser:appuser /app
        
USER appuser
    
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]