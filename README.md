Flask Todo App 🚀

A simple Todo application built with Flask, containerized with Docker, and deployed on AWS EC2.

Features ✅

REST APIs for managing Todos (GET, POST)

Lightweight backend using Flask

Containerized using Docker

Deployment on AWS EC2 instance

Accessible over public IP

Tech Stack 🛠

Python (Flask) – Web framework

Docker – Containerization

AWS EC2 – Cloud deployment

GitHub – Version control

Setup & Run Locally 🖥
# Clone repo
git clone https://github.com/akanshaasus04-spec/docker-aws-flask-todo.git
cd docker-aws-flask-todo

# Build Docker image
docker build -t flask-todo .

# Run container
docker run -d -p 8000:8000 flask-todo


👉 Now visit: http://localhost:8000

API Endpoints 🌐
Health Check

GET /
Response:

{ "status": "ok" }

Create Todo

POST /todos
Body:

{ "title": "Learn Docker" }


Response:

{ "id": 1, "title": "Learn Docker", "done": false }

Get All Todos

GET /todos

Deployment on AWS ☁️

Created EC2 Ubuntu instance

Installed Docker & Git

Cloned this repository

Built and ran Docker container on port 8000

Configured Security Group inbound rules (8000, 80, 22)

Public URL example: http://<EC2-PUBLIC-IP>:8000/ (replace with your IP) 
