FROM node:18-slim
ARG AXIOS_BASEURL
ARG AXIOS_BROWSER_BASEURL
ENV TZ Asia/Tokyo
RUN apt-get update
ENV APP_ROOT /code
WORKDIR ${APP_ROOT}
COPY . ${APP_ROOT}
RUN npm install
RUN npm run build
