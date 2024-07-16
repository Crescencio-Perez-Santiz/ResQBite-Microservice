FROM node:20

WORKDIR /app

COPY package*.json ./
COPY .env ./

RUN npm install
RUN npm install -g ts-node-dev

COPY src ./src

EXPOSE 3001

CMD ["npm", "run", "dev"]
