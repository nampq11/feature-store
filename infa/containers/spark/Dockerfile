FROM deltaio/delta-docker:0.8.1_2.3.0
# https://github.com/delta-io/delta-docs/blob/main/static/quickstart_docker/0.8.1_2.3.0/Dockerfile

USER root

COPY ./infa/containers/spark/requirements.txt ./
COPY ./infa/containers/spark/.env ./
RUN pip install -r requirements.txt

COPY ./batch_processing/ ./batch_processing/
# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run cron
ENTRYPOINT ["tail", "-f", "/dev/null"]