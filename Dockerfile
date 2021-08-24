# Test Stage
FROM alpine:3.13 AS test
LABEL application=motion_picture_db

RUN apk add --no-cache bash git

RUN apk add --no-cache gcc python3-dev py3-pip libffi-dev musl-dev linux-headers mariadb-dev
RUN pip3 install wheel

COPY /src/requirements* /build/
WORKDIR /build

RUN pip3 wheel -r requirements_test.txt --no-cache-dir --no-input
RUN pip3 install -r requirements_test.txt -f /build --no-index --no-cache-dir

COPY /src /app
WORKDIR /app

CMD ["python3", "manage.py", "test", "--noinput", "--settings=motion_picture_db.settings_test"]

# Release stage
FROM alpine:3.13
LABEL application=motion_picture_db

RUN apk add --no-cache python3 py3-pip mariadb-client bash

RUN addgroup -g 1000 app && adduser -u 1000 -G app -D app

COPY --from=test --chown=app:app /build /build
COPY --from=test --chown=app:app /app /app
RUN pip3 install -r /build/requirements.txt -f /build --no-index --no-cache-dir
RUN rm -rf /build

WORKDIR /app
USER app

