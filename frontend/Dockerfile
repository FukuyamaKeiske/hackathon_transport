FROM node:latest

WORKDIR /gorodbezprobok

COPY package.json ./
RUN npm install
COPY . .

CMD ["npm", "start"]
