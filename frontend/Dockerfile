FROM node:lts-alpine
WORKDIR /usr/src/app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build
WORKDIR /usr/src/app/dist
EXPOSE 8080
CMD ["npm", "run", "start"]