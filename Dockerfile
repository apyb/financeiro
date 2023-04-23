FROM python:3.11

ENV PATH="/app/.venv/bin:$PATH"

RUN mkdir -p /app
WORKDIR /app

COPY pyproject.toml /app
COPY poetry.lock /app
COPY poetry.toml /app

RUN pip install poetry
RUN poetry install --no-root --without dev

COPY . /app

# ---
# Force read-only mode
# Only needed until Fava v1.25 is released
RUN chmod a=r financeiro/main.beancount
RUN groupadd -r apyb && useradd --no-log-init -r -g apyb apyb
USER apyb
# ---

CMD ["fava", "financeiro/main.beancount", "--host", "0.0.0.0", "--port", "5000"]
