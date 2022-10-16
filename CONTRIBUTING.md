# How to run docker locally
## Located in docker_run.ps1

docker run -dp 5000:5000 --name flask-smorest-api -w /app -v "$(Get-Location):/app" flask-smorest-api sh -c "flask run"