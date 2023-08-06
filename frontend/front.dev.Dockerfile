FROM node:16-alpine
WORKDIR /frontend
EXPOSE 8080

COPY package-lock.json /frontend
COPY package.json /frontend
RUN npm ci

COPY . /frontend
CMD ["npm", "run", "serve"]