FROM node:16-alpine as build

WORKDIR /code/
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:stable-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/default.conf /etc/nginx/conf.d
COPY --from=build /code/build /build/
EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]