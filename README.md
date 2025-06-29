# FastAPI CRUD App

A simple FastAPI application demonstrating CRUD operations on users, with a CI/CD pipeline using GitHub Actions and Docker.

---

## 🚀 Features

- ✅ RESTful CRUD API for user management (`/users`)
- ✅ Built with FastAPI + Pydantic for data validation
- ✅ Fully Dockerized for environment consistency
- ✅ GitHub Actions CI/CD pipeline using a self-hosted runner
- ✅ Automatically deployed on AWS EC2 instance
- ✅ Swagger UI available at `/docs`

---

## 📦 Technologies Used

- **FastAPI**
- **Pydantic**
- **Docker**
- **GitHub Actions**
- **AWS EC2 (Ubuntu)**
- **Self-hosted GitHub runner**

---

## 🖥️ How It Works

1. Code is pushed to the `main` branch.
2. GitHub Actions (on self-hosted runner in EC2) builds and deploys the app via Docker.
3. Docker container exposes the FastAPI app on **port 80**.
4. App is accessible via:  
   `http://<your-ec2-public-ip>`

---

## 🔧 API Endpoints

| Method | Endpoint         | Description       |
|--------|------------------|-------------------|
| GET    | `/users`         | Get all users     |
| GET    | `/users/{id}`    | Get user by ID    |
| POST   | `/users`         | Create new user   |
| PUT    | `/users/{id}`    | Update user       |
| DELETE | `/users/{id}`    | Delete user       |

Try them on Swagger UI:  
➡️ `http://<your-ec2-ip>/docs`

---

## 👨‍💻 Developer

**Vipun Sanjana**  
Former Intern - Software Engineer, WSO2  
Cloud Security Operations Center  
[GitHub](https://github.com/vipunsanjana) | [LinkedIn](https://linkedin.com/in/vipunsanjana)

---

## 📥 Deployment

Hosted on an **Ubuntu EC2 instance** (AWS), running:
- Docker
- Self-hosted GitHub Actions runner

Deployment is fully automated on push to `main`.

---
