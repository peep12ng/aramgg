FROM node
WORKDIR /frontend
COPY package.json .
ADD . .
RUN npm install
EXPOSE 8080
CMD ["npm", "run", "serve"]