FROM docker.elastic.co/beats/filebeat:7.0.1

COPY ./filebeat/config /usr/share/filebeat

USER root

RUN chown root:filebeat /usr/share/filebeat/filebeat.yml

USER filebeat