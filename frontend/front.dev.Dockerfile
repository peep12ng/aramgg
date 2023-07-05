FROM node
WORKDIR /frontend/app
ADD . ./
CMD npm install && npm run serve
EXPOSE 8080