FROM python:3.13-slim

ARG UID=1000
ARG GID=1000

RUN groupadd -g ${GID} eli && \
    useradd -u ${UID} -g ${GID} -m eli

WORKDIR /workspace

USER eli

CMD ["bash"]