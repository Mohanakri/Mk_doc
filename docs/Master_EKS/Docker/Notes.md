# Docker Zero to Hero - Complete DevOps Notes

> **Repository**: [Docker-Zero-to-Hero by Abhishek Veeramalla](https://github.com/iam-veeramalla/Docker-Zero-to-Hero)
> 
> **Video Playlist**: [YouTube Docker Tutorial](https://www.youtube.com/watch?v=7JZP345yVjw&list=PLdpzxOOAlwvLjb0vTD9BXLOwwLD_GWCmC)

---

## 📚 Table of Contents

1. [Container Fundamentals](#container-fundamentals)
2. [Docker Architecture](#docker-architecture)
3. [Installation & Setup](#installation--setup)
4. [Docker Commands](#docker-commands)
5. [Writing Dockerfiles](#writing-dockerfiles)
6. [Hands-on Examples](#hands-on-examples)
7. [Docker Compose](#docker-compose)
8. [Docker Networking](#docker-networking)
9. [Docker Volumes](#docker-volumes)
10. [Production Best Practices](#production-best-practices)
11. [DevOps Integration](#devops-integration)
12. [Troubleshooting Guide](#troubleshooting-guide)

---

## 🐳 Container Fundamentals

### What is a Container?

**Simple Definition**: A container is a bundle of:
- Your application
- Application libraries
- Minimum system dependencies

**Technical Definition**: A lightweight, standalone, executable package that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings.

### Containers vs Virtual Machines

| Feature | Containers | Virtual Machines |
|---------|------------|------------------|
| **Size** | Ubuntu container: ~22MB | Ubuntu VM: ~2.3GB |
| **Startup Time** | Seconds | Minutes |
| **Resource Usage** | Shares host OS kernel | Full OS per VM |
| **Isolation** | Process-level | Hardware-level |
| **Portability** | Highly portable | Less portable |

### Why Containers are Lightweight?

**Container shares from Host OS**:
- Kernel and system calls
- Networking stack
- File system (through bind mounts)
- Hardware resources (CPU, memory)

**Container has its own**:
- `/bin`, `/sbin` - Binary executables
- `/etc` - Configuration files
- `/lib` - Library files
- `/usr` - User applications and utilities
- `/var` - Variable data (logs, temp files)
- `/root` - Root user home directory

---

## 🏗️ Docker Architecture

### Core Components

```
┌─────────────────────────────────────────────────────────────┐
│                    Docker Architecture                      │
├─────────────────────────────────────────────────────────────┤
│  Docker Client (CLI)                                       │
│  ├── docker build                                          │
│  ├── docker run                                            │
│  └── docker push                                           │
├─────────────────────────────────────────────────────────────┤
│  Docker Daemon (dockerd)                                   │
│  ├── Manages Images                                        │
│  ├── Manages Containers                                    │
│  ├── Manages Networks                                      │
│  └── Manages Volumes                                       │
├─────────────────────────────────────────────────────────────┤
│  Docker Registry (Docker Hub)                              │
│  ├── Public Images                                         │
│  └── Private Repositories                                  │
└─────────────────────────────────────────────────────────────┘
```

### Docker Objects

1. **Dockerfile** → Instructions to build image
2. **Image** → Read-only template
3. **Container** → Running instance of image
4. **Volume** → Persistent data storage
5. **Network** → Container communication
6. **Registry** → Image storage (Docker Hub)

---

## ⚙️ Installation & Setup

### Ubuntu Installation (AWS EC2)

```bash
# Update system
sudo apt update

# Install Docker
sudo apt install docker.io -y

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Check status
sudo systemctl status docker
```

### Post-Installation Setup

```bash
# Add user to docker group (replace 'ubuntu' with your username)
sudo usermod -aG docker $USER

# Apply group changes (logout/login required)
newgrp docker

# OR restart session
exit
# Login again
```

### Verify Installation

```bash
docker --version
docker run hello-world
```

**Expected Output:**
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

### Common Installation Issues

**Problem**: Permission denied error
```bash
docker: Got permission denied while trying to connect to the Docker daemon socket
```

**Solutions**:
1. Check if Docker daemon is running: `sudo systemctl status docker`
2. Start Docker: `sudo systemctl start docker`
3. Add user to docker group: `sudo usermod -aG docker $USER`
4. Logout and login back

---

## 🔧 Docker Commands

### Image Management

```bash
# Build image from Dockerfile
docker build -t image-name:tag .
docker build -t myapp:v1.0 .

# List all images
docker images
docker image ls

# Remove image
docker rmi image-name:tag
docker rmi myapp:v1.0

# Pull image from registry
docker pull ubuntu:20.04
docker pull nginx:alpine

# Push image to registry
docker push username/image-name:tag

# Image history and details
docker history image-name
docker inspect image-name

# Remove unused images
docker image prune
docker image prune -a  # Remove all unused images
```

### Container Management

```bash
# Run container
docker run image-name
docker run -d nginx  # Run in background (detached)
docker run -it ubuntu:20.04 /bin/bash  # Interactive mode

# Run with port mapping
docker run -d -p 8080:80 nginx

# Run with volume mounting
docker run -d -v /host/path:/container/path nginx

# Run with environment variables
docker run -d -e ENV_VAR=value nginx

# List containers
docker ps           # Running containers only
docker ps -a        # All containers

# Container operations
docker start container-id
docker stop container-id
docker restart container-id
docker pause container-id
docker unpause container-id

# Remove containers
docker rm container-id
docker rm -f container-id  # Force remove running container

# Execute commands in running container
docker exec -it container-id /bin/bash
docker exec container-id ls -la

# View logs
docker logs container-id
docker logs -f container-id  # Follow logs

# Copy files between host and container
docker cp file.txt container-id:/path/
docker cp container-id:/path/file.txt ./
```

### System Commands

```bash
# System information
docker info
docker version
docker system df  # Show disk usage

# Clean up
docker system prune  # Remove stopped containers, unused networks, dangling images
docker system prune -a  # Remove all unused containers, networks, images
docker container prune  # Remove stopped containers
docker image prune     # Remove dangling images
docker volume prune    # Remove unused volumes
docker network prune   # Remove unused networks
```

---

## 📝 Writing Dockerfiles

### Dockerfile Basics

```dockerfile
# Use official base image
FROM ubuntu:20.04

# Set metadata
LABEL maintainer="your-email@example.com"
LABEL version="1.0"
LABEL description="My first Docker image"

# Set working directory
WORKDIR /app

# Copy files
COPY . /app
COPY requirements.txt .

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONPATH=/app
ENV ENV_NAME=production

# Expose port
EXPOSE 8080

# Create non-root user
RUN useradd -m -u 1000 appuser
USER appuser

# Define startup command
CMD ["python3", "app.py"]
```

### Dockerfile Instructions

| Instruction | Purpose | Example |
|-------------|---------|---------|
| `FROM` | Base image | `FROM python:3.9-alpine` |
| `WORKDIR` | Working directory | `WORKDIR /app` |
| `COPY` | Copy files | `COPY . /app` |
| `ADD` | Copy + extract | `ADD archive.tar.gz /app` |
| `RUN` | Execute commands | `RUN apt-get update` |
| `CMD` | Default command | `CMD ["python", "app.py"]` |
| `ENTRYPOINT` | Fixed command | `ENTRYPOINT ["python"]` |
| `ENV` | Environment variables | `ENV DEBUG=1` |
| `EXPOSE` | Port information | `EXPOSE 8080` |
| `VOLUME` | Mount point | `VOLUME ["/data"]` |
| `USER` | User context | `USER appuser` |
| `ARG` | Build arguments | `ARG VERSION=1.0` |

### Multi-Stage Dockerfile Example

```dockerfile
# Build stage
FROM node:16-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# Production stage
FROM node:16-alpine AS production
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

---

## 🛠️ Hands-on Examples

### Example 1: Python Web Application

**Directory Structure:**
```
python-web-app/
├── Dockerfile
├── app.py
├── requirements.txt
└── .dockerignore
```

**app.py:**
```python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = os.environ.get('NAME', 'World')
    return f'Hello {name} from Docker!'

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

**requirements.txt:**
```
Flask==2.3.2
```

**Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

CMD ["python", "app.py"]
```

**.dockerignore:**
```
__pycache__
*.pyc
.git
.gitignore
README.md
Dockerfile
.dockerignore
```

**Build and Run:**
```bash
# Build image
docker build -t python-web-app:v1.0 .

# Run container
docker run -d -p 5000:5000 --name my-web-app python-web-app:v1.0

# Test application
curl http://localhost:5000

# View logs
docker logs my-web-app

# Stop and remove
docker stop my-web-app
docker rm my-web-app
```

### Example 2: Nginx Static Website

**Directory Structure:**
```
nginx-website/
├── Dockerfile
├── nginx.conf
└── html/
    ├── index.html
    ├── style.css
    └── script.js
```

**Dockerfile:**
```dockerfile
FROM nginx:alpine

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy website files
COPY html/ /usr/share/nginx/html/

# Add labels
LABEL maintainer="devops@company.com"
LABEL version="1.0"

EXPOSE 80

# Nginx runs as daemon, so no CMD needed
```

**nginx.conf:**
```nginx
events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    
    server {
        listen 80;
        server_name localhost;
        
        location / {
            root   /usr/share/nginx/html;
            index  index.html;
        }
        
        location /health {
            access_log off;
            return 200 "healthy\n";
            add_header Content-Type text/plain;
        }
    }
}
```

---

## 🐙 Docker Compose

### What is Docker Compose?

Docker Compose is a tool for defining and running multi-container Docker applications using a YAML file.

### docker-compose.yml Example

```yaml
version: '3.8'

services:
  web:
    build: 
      context: .
      dockerfile: Dockerfile
    ports:
      - "8080:5000"
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://user:password@db:5432/myapp
    volumes:
      - .:/app
      - /app/node_modules
    depends_on:
      - db
      - redis
    networks:
      - app-network

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app-network

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    networks:
      - app-network

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web
    networks:
      - app-network

volumes:
  postgres_data:

networks:
  app-network:
    driver: bridge
```

### Docker Compose Commands

```bash
# Start services
docker-compose up
docker-compose up -d  # Background mode

# Build and start
docker-compose up --build

# Stop services
docker-compose down
docker-compose down -v  # Remove volumes too

# View running services
docker-compose ps

# View logs
docker-compose logs
docker-compose logs web  # Specific service

# Scale services
docker-compose up --scale web=3

# Execute commands
docker-compose exec web bash
docker-compose run web python manage.py migrate
```

---

## 🌐 Docker Networking

### Network Types

1. **Bridge** (default) - Containers on same host
2. **Host** - Container uses host network
3. **None** - No networking
4. **Custom** - User-defined networks

### Network Commands

```bash
# List networks
docker network ls

# Create custom network
docker network create mynetwork
docker network create --driver bridge --subnet=172.20.0.0/16 mynetwork

# Run container in specific network
docker run -d --network mynetwork --name web nginx

# Connect container to network
docker network connect mynetwork container-name

# Disconnect container from network
docker network disconnect mynetwork container-name

# Inspect network
docker network inspect mynetwork

# Remove network
docker network rm mynetwork
```

### Container Communication Example

```bash
# Create custom network
docker network create app-net

# Run database container
docker run -d --name db --network app-net postgres:13

# Run web container
docker run -d --name web --network app-net -p 8080:80 nginx

# Containers can communicate using container names as hostnames
# db container is accessible at hostname 'db' from web container
```

---

## 💾 Docker Volumes

### Volume Types

1. **Named Volumes** - Managed by Docker
2. **Bind Mounts** - Host directory mounted
3. **tmpfs Mounts** - Temporary memory storage

### Volume Commands

```bash
# Create volume
docker volume create myvolume

# List volumes
docker volume ls

# Inspect volume
docker volume inspect myvolume

# Remove volume
docker volume rm myvolume
docker volume prune  # Remove unused volumes

# Run container with volume
docker run -d -v myvolume:/data nginx  # Named volume
docker run -d -v /host/path:/container/path nginx  # Bind mount
docker run -d --tmpfs /tmp nginx  # tmpfs mount
```

### Volume Examples

```bash
# Database with persistent storage
docker run -d \
  --name postgres-db \
  -e POSTGRES_PASSWORD=secret \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:13

# Web app with source code mounting (development)
docker run -d \
  --name web-dev \
  -p 8080:5000 \
  -v $(pwd):/app \
  python-web-app

# Nginx with config and logs
docker run -d \
  --name nginx-server \
  -p 80:80 \
  -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
  -v nginx_logs:/var/log/nginx \
  nginx
```

---

## 🚀 Production Best Practices

### Security Best Practices

```dockerfile
# Use official base images
FROM python:3.9-slim

# Don't run as root
RUN useradd -m -u 1000 appuser
USER appuser

# Use specific versions
FROM python:3.9.16-slim

# Minimize attack surface
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Use secrets management
# Don't: ENV PASSWORD=secret123
# Do: Use Docker secrets or external secret management
```

### Performance Optimization

```dockerfile
# Multi-stage builds
FROM node:16 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:16-alpine
COPY --from=builder /app/node_modules ./node_modules
COPY . .

# Optimize layers
RUN apt-get update && \
    apt-get install -y package1 package2 && \
    rm -rf /var/lib/apt/lists/*

# Use .dockerignore
# .git/
# node_modules/
# *.log
```

### Resource Management

```bash
# Limit container resources
docker run -d \
  --memory="512m" \
  --cpus="1.0" \
  --restart=unless-stopped \
  nginx

# Health checks
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1
```

---

## 🔄 DevOps Integration

### CI/CD Pipeline Example (.gitlab-ci.yml)

```yaml
stages:
  - build
  - test
  - deploy

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  DOCKER_LATEST: $CI_REGISTRY_IMAGE:latest

build:
  stage: build
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker tag $DOCKER_IMAGE $DOCKER_LATEST
    - docker push $DOCKER_IMAGE
    - docker push $DOCKER_LATEST

test:
  stage: test
  script:
    - docker run --rm $DOCKER_IMAGE python -m pytest tests/

deploy:
  stage: deploy
  script:
    - docker-compose down
    - docker-compose pull
    - docker-compose up -d
  only:
    - main
```

### Kubernetes Integration

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-app
        image: myregistry/web-app:v1.0
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
```

### Monitoring with Docker

```yaml
# docker-compose.monitoring.yml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin

  node-exporter:
    image: prom/node-exporter
    ports:
      - "9100:9100"
```

---

## 🔧 Troubleshooting Guide

### Common Issues and Solutions

#### 1. Container Exits Immediately
```bash
# Check exit code and logs
docker ps -a
docker logs container-name

# Run interactively to debug
docker run -it image-name /bin/bash
```

#### 2. Port Already in Use
```bash
# Find process using port
sudo lsof -i :8080
sudo netstat -tulpn | grep 8080

# Kill process or use different port
docker run -p 8081:80 nginx
```

#### 3. Permission Denied
```bash
# Check file permissions
ls -la

# Fix permissions
sudo chown -R $USER:$USER .
chmod +x script.sh
```

#### 4. Out of Disk Space
```bash
# Check disk usage
docker system df

# Clean up
docker system prune -a
docker volume prune
```

#### 5. Network Issues
```bash
# Check network connectivity
docker exec container-name ping google.com

# Inspect networks
docker network ls
docker network inspect bridge
```

### Debugging Commands

```bash
# Container inspection
docker inspect container-name
docker stats container-name
docker top container-name

# Resource usage
docker system df
docker system events

# Process monitoring
docker exec container-name ps aux
docker exec container-name top
```

---

## 📖 DevOps Learning Path

### Phase 1: Fundamentals (Week 1-2)
- [ ] Understand containerization concepts
- [ ] Install Docker and Docker Compose
- [ ] Run first containers (nginx, ubuntu, hello-world)
- [ ] Learn basic commands (run, ps, images, logs)
- [ ] Write first Dockerfile

### Phase 2: Intermediate (Week 3-4)
- [ ] Master Dockerfile best practices
- [ ] Understand Docker networking
- [ ] Work with Docker volumes
- [ ] Use Docker Compose for multi-container apps
- [ ] Push/pull images from registries

### Phase 3: Advanced (Week 5-6)
- [ ] Multi-stage builds
- [ ] Security scanning and hardening
- [ ] Performance optimization
- [ ] Monitoring and logging
- [ ] Integration with CI/CD pipelines

### Phase 4: Production (Week 7-8)
- [ ] Container orchestration (Docker Swarm/Kubernetes)
- [ ] Production deployment strategies
- [ ] Backup and disaster recovery
- [ ] Scaling and load balancing
- [ ] Security compliance

---

## 🎯 Practice Exercises

### Exercise 1: Basic Web Application
Create a simple web application with database using Docker Compose:
- Frontend: React/Angular/Vue
- Backend: Node.js/Python/Go
- Database: PostgreSQL/MongoDB
- Reverse Proxy: Nginx

### Exercise 2: Microservices Architecture
Build a microservices application:
- API Gateway
- User Service
- Product Service
- Order Service
- Database per service
- Message queue (Redis/RabbitMQ)

### Exercise 3: CI/CD Pipeline
Create a complete CI/CD pipeline:
- Source code management (Git)
- Automated testing
- Docker image building
- Security scanning
- Deployment to staging/production

---

## 📚 Additional Resources

### Official Documentation
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)

### Best Practices Guides
- [Docker Security Best Practices](https://docs.docker.com/develop/security-best-practices/)
- [Production Best Practices](https://docs.docker.com/develop/dev-best-practices/)

### Tools and Extensions
- **Docker Desktop**: GUI for Docker management
- **Portainer**: Web-based Docker management
- **Watchtower**: Automatic container updates
- **Dive**: Explore Docker image layers

### Community Resources
- [Docker Hub](https://hub.docker.com/) - Official registry
- [Docker Community Forums](https://forums.docker.com/)
- [Awesome Docker](https://github.com/veggiemonk/awesome-docker) - Curated list

---

## 🎉 Conclusion

Docker is a fundamental technology in modern DevOps practices. This comprehensive guide covers everything from basic concepts to production deployment. Practice with real projects, follow best practices, and integrate Docker into your DevOps workflows.

**Next Steps:**
1. Complete all practice exercises
2. Build and deploy a real application
3. Learn container orchestration (Kubernetes)
4. Explore cloud container services (AWS ECS, Google Cloud Run, Azure Container Instances)

**Happy Dockerizing! 🐳**

---

*Remember: The best way to learn Docker is by doing. Start with simple examples and gradually build more complex applications.*