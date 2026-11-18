# Question 11 – Palindrome Program with Kubernetes

## Build image
```bash
docker build -t palindrome-app:latest .
```
The local Kubernetes cluster must be able to access this image. With Docker Desktop Kubernetes, build the image using the same Docker engine used by the cluster. With Minikube, you can run `minikube image build -t palindrome-app:latest .`.

## Deploy
```bash
kubectl apply -f deployment.yaml
kubectl get deployments
kubectl get pods
kubectl get services
```
For a local NodePort setup, access `http://localhost:30080` for the operational web form, or `http://localhost:30080/check?word=MADAM` for the JSON endpoint. If using Minikube, run `minikube service palindrome-service --url` and use the returned address instead.

## Selenium
Install Selenium and configure Chrome/ChromeDriver, then run:
```bash
pip install selenium
python -m unittest test_palindrome_selenium.py
```
Keep the Kubernetes deployment running while tests execute.

## GitHub
```bash
git init
git add .
git commit -m "Add palindrome application and Kubernetes deployment"
git branch -M main
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```
