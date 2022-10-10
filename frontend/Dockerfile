FROM node:lts-alpine
WORKDIR /usr/src/app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build
RUN npm run generate

WORKDIR /usr/src/app/dist

EXPOSE 3000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000
CMD ["npm", "start"]