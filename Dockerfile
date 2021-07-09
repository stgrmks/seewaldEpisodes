FROM python:3.9-slim-buster
COPY ./ /app
WORKDIR /app
RUN pip install pip==21.1.2
RUN pip install -e .
CMD ["python", "-c", "from seewaldEpisodes import get_episode;get_episode()"]