FROM docker.elastic.co/logstash/logstash-oss:6.5.3 
 
#RUN logstash-plugin install logstash-filter-jdbc_streaming \ 
#    && logstash-plugin install logstash-filter-aggregate \ 
#    && logstash-plugin install logstash-input-jdbc \ 
#    && logstash-plugin install logstash-filter-translate 
 
COPY ./logstash/config /usr/share/logstash/config 
COPY ./logstash/pipeline /usr/share/logstash/pipeline 
