# How to Run this project?

Do a git clone or a git fork of this repo.

With docker running, open git bash or your favorite terminal inside the project folder, and type:

```
docker build -t validador-im
```

And when build finish, type:

```
docker run -d -p 80:8501 --name validador validador-im
```

In your browser, access "localhost" URL.
