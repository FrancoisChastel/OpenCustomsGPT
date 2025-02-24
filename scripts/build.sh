docker build -t francoischastel/open-customs-gpt:latest .
docker run -p 8501:8501 -e DB_URI=$DB_URI -e OPENAI_API_KEY=$OPENAI_API_KEY francoischastel/open-customs-gpt:latest
