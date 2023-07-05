FROM node
WORKDIR /frontend
ADD . ./
CMD npm install && npm run serve
EXPOSE 8080