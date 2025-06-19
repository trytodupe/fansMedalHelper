FROM python:3.9-alpine as requirements_stage
ENV TZ="Asia/Shanghai"
COPY ./docker/pip.conf /root/.config/pip/pip.conf

WORKDIR /wheel

COPY ./requirements.txt /wheel/

RUN python -m pip wheel --wheel-dir=/wheel --no-cache-dir --requirement ./requirements.txt


FROM python:3.9-alpine
ENV TZ="Asia/Shanghai"
COPY ./docker/pip.conf /root/.config/pip/pip.conf

WORKDIR /app

COPY . /app/
COPY --from=requirements_stage /wheel /wheel

RUN python -m pip install --no-cache-dir --find-links=/wheel -r /app/requirements.txt

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]