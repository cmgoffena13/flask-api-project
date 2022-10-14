#docker run -dp 5000:5000 flask-smorest-api # For Deployment
docker run -dp 5000:5000 --name flask-smorest-api -w /app -v "$(Get-Location):/app" flask-smorest-api # For Testing