docker build --no-cache -t francoischastel/opencustomsgpt:latest .
docker run -p 8501:8501 -p 4000:4000 ---env-file .env francoischastel/opencustomsgpt:latest
