# hakaton

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Сборка Docker образа
> Перед сборкой небходимо выставить переменную VUE_APP_BASE указывающую на backend server
### windows
```
set VUE_APP_BASE=http://localhost:8000
docker build  -t vue-hakaton  --build-arg VUE_APP_BASE=%VUE_APP_BASE% .
```
### linux
```
export VUE_APP_BASE=http://localhost:8000
docker build  -t vue-hakaton  --build-arg VUE_APP_BASE=$VUE_APP_BASE .
```

## Запуск Docker
```
docker run -it -p 8080:80 --rm --name vue vue-hakaton
```

## Docker Compose
> Перед сборкой небходимо выставить переменную VUE_APP_BASE указывающую на backend server

### linux
```
export VUE_APP_BASE=http://localhost:8000
docker-compose build --no-cache
docker-compose up
```