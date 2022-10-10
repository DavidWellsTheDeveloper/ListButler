FROM node:lts-alpine
RUN mkdir -p /usr/src/frontend
WORKDIR /usr/src/frontend

RUN apk update && apk upgrade
RUN apk add git

COPY frontend ./

RUN npm install
RUN npm run build
RUN npm run generate

WORKDIR /usr/src/frontend/dist

EXPOSE 3000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

CMD ["npm", "start"]