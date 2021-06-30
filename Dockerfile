FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY ./ /app
WORKDIR /app
RUN pip install pip==21.1.2
RUN pip install -e .
CMD ["python", "-c", "from seewaldEpisodes import get_episode;get_episode()"]