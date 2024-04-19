FROM natandias1/spark-base:1.0.8

ARG spark_uid=185

RUN apt-get install -y tini libnss3 && \
    mkdir -p /opt/spark/work-dir && \
    rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*

RUN mv /opt/spark/kubernetes/dockerfiles/spark/entrypoint.sh /opt/ && \
    mv /opt/spark/kubernetes/dockerfiles/spark/decom.sh /opt/ 

RUN echo "auth required pam_wheel.so use_uid" >> /etc/pam.d/su && \
    chgrp root /etc/passwd && chmod ug+rw /etc/passwd

WORKDIR /opt/spark/work-dir

RUN chmod g+w /opt/spark/work-dir
RUN chmod a+x /opt/decom.sh

ENTRYPOINT [ "/opt/entrypoint.sh" ]

USER ${spark_uid}