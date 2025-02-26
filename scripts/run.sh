docker build --no-cache -t francoischastel/opencustomsgpt:latest .
docker run -p 8501:8501 -p 4000:4000 -e DB_URI=$DB_URI -e OPENAI_API_KEY=$OPENAI_API_KEY francoischastel/opencustomsgpt:latest
