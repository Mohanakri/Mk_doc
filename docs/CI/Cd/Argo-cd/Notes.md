# Complete ArgoCD Guide - Architecture, EKS Installation & Operations

## Table of Contents
1. [ArgoCD Architecture Overview](#argocd-architecture-overview)
2. [Core Components](#core-components)
3. [EKS Installation](#eks-installation)
4. [Pod Architecture in EKS](#pod-architecture-in-eks)
5. [User Interface (UI)](#user-interface-ui)
6. [Command Line Interface (CLI)](#command-line-interface-cli)
7. [Configuration Management](#configuration-management)
8. [Troubleshooting](#troubleshooting)
9. [Best Practices](#best-practices)

---

## ArgoCD Architecture Overview

ArgoCD is a declarative, GitOps continuous delivery tool for Kubernetes. It follows the GitOps pattern of using Git repositories as the source of truth for defining the desired application state.

### High-Level Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Git Repository │    │    ArgoCD       │    │   Kubernetes    │
│                 │────│   Controller     │────│    Cluster      │
│  Application    │    │                 │    │                 │
│  Manifests      │    │  Sync & Monitor │    │  Target Apps    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Key Principles
- **Declarative**: Desired state defined in Git
- **Versioned & Immutable**: Git provides version control
- **Pulled not Pushed**: ArgoCD pulls changes from Git
- **Continuously Reconciled**: Automatic drift detection and correction

---

## Core Components

### 1. ArgoCD Server
- **Purpose**: API server and Web UI
- **Responsibilities**:
  - Serves the Web UI
  - Provides gRPC/REST API
  - Handles authentication
  - Manages application definitions

### 2. Application Controller
- **Purpose**: Core controller managing applications
- **Responsibilities**:
  - Monitors Git repositories
  - Compares desired vs actual state
  - Triggers synchronization
  - Reports application health

### 3. Repository Server
- **Purpose**: Internal service for Git operations
- **Responsibilities**:
  - Clones and updates Git repositories
  - Generates Kubernetes manifests
  - Caches repository contents
  - Handles Helm/Kustomize processing

### 4. Redis
- **Purpose**: Caching and session storage
- **Responsibilities**:
  - Caches application data
  - Stores user sessions
  - Temporary data storage

### 5. Dex (Optional)
- **Purpose**: OIDC identity provider
- **Responsibilities**:
  - External authentication
  - SSO integration
  - User identity management

---

## EKS Installation

### Prerequisites

```bash
# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Install AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Install eksctl
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
```

### Step 1: Create EKS Cluster

```bash
# Create cluster configuration
cat << EOF > cluster-config.yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: argocd-cluster
  region: us-west-2

nodeGroups:
  - name: worker-nodes
    instanceType: t3.medium
    desiredCapacity: 3
    minSize: 1
    maxSize: 5
    volumeSize: 20
    ssh:
      allow: true
EOF

# Create cluster
eksctl create cluster -f cluster-config.yaml
```

### Step 2: Install ArgoCD

```bash
# Create namespace
kubectl create namespace argocd

# Install ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Wait for pods to be ready
kubectl wait --for=condition=available --timeout=300s deployment/argocd-server -n argocd
```

### Step 3: Configure Load Balancer (AWS)

```yaml
# argocd-server-service.yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
    service.beta.kubernetes.io/aws-load-balancer-scheme: internet-facing
  labels:
    app.kubernetes.io/component: server
    app.kubernetes.io/name: argocd-server
    app.kubernetes.io/part-of: argocd
  name: argocd-server-lb
  namespace: argocd
spec:
  type: LoadBalancer
  ports:
  - name: https
    port: 443
    protocol: TCP
    targetPort: 8080
  - name: grpc
    port: 443
    protocol: TCP
    targetPort: 8080
  selector:
    app.kubernetes.io/name: argocd-server
```

```bash
# Apply load balancer service
kubectl apply -f argocd-server-service.yaml

# Get load balancer URL
kubectl get svc argocd-server-lb -n argocd
```

---

## Pod Architecture in EKS

### ArgoCD Pods Overview

```bash
# List all ArgoCD pods
kubectl get pods -n argocd

# Expected output:
# NAME                                  READY   STATUS    RESTARTS   AGE
# argocd-application-controller-0       1/1     Running   0          5m
# argocd-dex-server-xxx                 1/1     Running   0          5m
# argocd-redis-xxx                      1/1     Running   0          5m
# argocd-repo-server-xxx                1/1     Running   0          5m
# argocd-server-xxx                     1/1     Running   0          5m
```

### Detailed Pod Analysis

#### 1. ArgoCD Server Pod
```bash
# Describe server pod
kubectl describe pod -l app.kubernetes.io/name=argocd-server -n argocd

# Key specifications:
# - Image: quay.io/argoproj/argocd:latest
# - Port: 8080 (HTTP), 8083 (gRPC)
# - Resources: CPU/Memory requests and limits
# - Volume mounts: Config, TLS certificates
```

#### 2. Application Controller Pod
```bash
# Check controller pod
kubectl describe pod -l app.kubernetes.io/name=argocd-application-controller -n argocd

# Characteristics:
# - StatefulSet with 1 replica
# - Manages application lifecycle
# - High memory usage for large deployments
# - Persistent volume for data
```

#### 3. Repository Server Pod
```bash
# Examine repo server
kubectl describe pod -l app.kubernetes.io/name=argocd-repo-server -n argocd

# Features:
# - Handles Git operations
# - Processes Helm/Kustomize
# - Caches repository data
# - Multiple replicas for HA
```

#### 4. Redis Pod
```bash
# Check Redis pod
kubectl describe pod -l app.kubernetes.io/name=argocd-redis -n argocd

# Purpose:
# - Caching layer
# - Session storage
# - Application metadata
```

### Resource Requirements

```yaml
# Resource specifications for EKS
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 512Mi
```

### Persistent Volumes in EKS

```bash
# Check persistent volumes
kubectl get pv
kubectl get pvc -n argocd

# ArgoCD uses PVCs for:
# - Application controller data
# - Redis persistence (if enabled)
# - Repository cache
```

---

## User Interface (UI)

### Accessing the UI

```bash
# Get initial admin password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

# Port forward for local access
kubectl port-forward svc/argocd-server -n argocd 8080:443

# Access UI at: https://localhost:8080
# Username: admin
# Password: [decoded password from above]
```

### UI Components

#### 1. Applications Dashboard
- **Overview**: All applications at a glance
- **Status indicators**: Healthy, Progressing, Degraded, Missing
- **Sync status**: Synced, OutOfSync, Unknown
- **Filters**: By cluster, namespace, health, sync status

#### 2. Application Details
- **Resource Tree**: Visual representation of Kubernetes resources
- **Live Manifests**: Current state in cluster
- **Desired Manifests**: Target state from Git
- **Diff View**: Comparison between live and desired state
- **Events**: Application events and logs
- **Parameters**: Helm values, Kustomize parameters

#### 3. Repository Management
- **Git Repositories**: Configure source repositories
- **Credentials**: SSH keys, tokens, certificates
- **Webhook Configuration**: Automated sync triggers

#### 4. Cluster Management
- **Cluster List**: Connected Kubernetes clusters
- **Cluster Info**: Version, nodes, resources
- **Permissions**: RBAC configuration

#### 5. Settings
- **User Management**: Local users, SSO integration
- **Projects**: Application grouping and access control
- **Repositories**: Git repo configurations
- **Certificates**: TLS certificates for Git repositories

### UI Navigation Tips

```
Applications → Select App → App Details
                         → Live Manifests
                         → Desired Manifests
                         → Diff
                         → Events
                         → Parameters

Settings → Repositories → Add Repository
        → Clusters → Add Cluster
        → Projects → Create Project
        → Users → Manage Users
```

---

## Command Line Interface (CLI)

### Installation

```bash
# Download ArgoCD CLI
curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
chmod +x /usr/local/bin/argocd

# Verify installation
argocd version
```

### Authentication

```bash
# Login to ArgoCD server
argocd login argocd-server-lb-xxx.elb.amazonaws.com

# Login with port-forward
argocd login localhost:8080

# Login with token
argocd login argocd-server --auth-token <TOKEN>

# Context management
argocd context
argocd context argocd-server
```

### Essential CLI Commands

#### Application Management

```bash
# List applications
argocd app list

# Get application details
argocd app get <app-name>

# Create application
argocd app create guestbook \
  --repo https://github.com/argoproj/argocd-example-apps.git \
  --path guestbook \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default

# Sync application
argocd app sync <app-name>

# Delete application
argocd app delete <app-name>

# Set application parameters
argocd app set <app-name> --parameter key=value
```

#### Repository Management

```bash
# Add repository
argocd repo add https://github.com/username/repo.git

# List repositories
argocd repo list

# Remove repository
argocd repo rm https://github.com/username/repo.git
```

#### Cluster Management

```bash
# Add cluster
argocd cluster add <context-name>

# List clusters
argocd cluster list

# Remove cluster
argocd cluster rm <cluster-url>
```

#### Project Management

```bash
# Create project
argocd proj create myproject

# List projects
argocd proj list

# Add repository to project
argocd proj add-source myproject https://github.com/username/repo.git

# Add destination to project
argocd proj add-destination myproject <cluster-url> <namespace>
```

#### Synchronization Commands

```bash
# Sync with prune
argocd app sync <app-name> --prune

# Sync specific resource
argocd app sync <app-name> --resource <group>:<kind>:<name>

# Hard refresh
argocd app get <app-name> --hard-refresh

# Wait for sync
argocd app wait <app-name>
```

### CLI Configuration

```bash
# Show current configuration
argocd config

# Set configuration
argocd config set server.insecure true

# CLI autocompletion
source <(argocd completion bash)
```

---

## Configuration Management

### ArgoCD Configuration

#### Main Configuration (argocd-cm)

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-cm
  namespace: argocd
data:
  # Git repositories
  repositories: |
    - url: https://github.com/argoproj/argocd-example-apps.git
    - url: https://github.com/company/apps.git
      passwordSecret:
        name: private-repo
        key: password
      usernameSecret:
        name: private-repo
        key: username
  
  # OIDC configuration
  oidc.config: |
    name: SSO
    issuer: https://company.okta.com
    clientId: argocd
    clientSecret: $oidc.clientSecret
    requestedIDTokenClaims: {"groups": {"essential": true}}
  
  # URL configuration
  url: https://argocd.company.com
  
  # Application instance label key
  application.instanceLabelKey: argocd.argoproj.io/instance
```

#### RBAC Configuration (argocd-rbac-cm)

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-rbac-cm
  namespace: argocd
data:
  policy.default: role:readonly
  policy.csv: |
    # Admin policy
    p, role:admin, applications, *, */*, allow
    p, role:admin, clusters, *, *, allow
    p, role:admin, repositories, *, *, allow
    
    # Developer policy
    p, role:developer, applications, *, dev/*, allow
    p, role:developer, applications, get, */*, allow
    
    # Group mappings
    g, company:admin, role:admin
    g, company:developers, role:developer
```

#### Server Configuration (argocd-server-config)

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-cmd-params-cm
  namespace: argocd
data:
  # Server parameters
  server.insecure: "true"
  server.grpc.web: "true"
  
  # Application parameters
  application.instanceLabelKey: argocd.argoproj.io/instance
  
  # Repository parameters
  repo.server: "argocd-repo-server:8081"
```

### Application Configuration

#### Basic Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: guestbook
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/argoproj/argocd-example-apps.git
    targetRevision: HEAD
    path: guestbook
  destination:
    server: https://kubernetes.default.svc
    namespace: guestbook
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```

#### Helm Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: nginx-helm
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://charts.bitnami.com/bitnami
    targetRevision: 9.5.0
    chart: nginx
    helm:
      parameters:
      - name: service.type
        value: LoadBalancer
      - name: replicaCount
        value: "3"
      values: |
        image:
          tag: 1.21.0
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
  destination:
    server: https://kubernetes.default.svc
    namespace: nginx
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```

#### Kustomize Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: kustomize-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/company/kustomize-apps.git
    targetRevision: HEAD
    path: overlays/production
    kustomize:
      commonLabels:
        env: production
      images:
      - name: nginx
        newTag: 1.21.0
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Pod Not Starting

```bash
# Check pod status
kubectl get pods -n argocd
kubectl describe pod <pod-name> -n argocd

# Check logs
kubectl logs <pod-name> -n argocd

# Common causes:
# - Resource constraints
# - Image pull errors
# - Configuration issues
# - PVC mounting problems
```

#### 2. Application Sync Failures

```bash
# Check application status
argocd app get <app-name>

# View sync operation details
argocd app get <app-name> --show-operation

# Common solutions:
# - Check Git repository access
# - Verify Kubernetes permissions
# - Review manifest syntax
# - Check resource conflicts
```

#### 3. Repository Connection Issues

```bash
# Test repository connection
argocd repo get <repo-url>

# Add repository with credentials
kubectl create secret generic repo-secret \
  --from-literal=username=<username> \
  --from-literal=password=<password> \
  -n argocd

# Update repository configuration
argocd repo add <repo-url> --username <username> --password <password>
```

#### 4. High Memory Usage

```bash
# Check resource usage
kubectl top pods -n argocd

# Increase memory limits
kubectl patch deployment argocd-server -n argocd -p '{"spec":{"template":{"spec":{"containers":[{"name":"argocd-server","resources":{"limits":{"memory":"1Gi"}}}]}}}}'

# For application controller (StatefulSet)
kubectl patch statefulset argocd-application-controller -n argocd -p '{"spec":{"template":{"spec":{"containers":[{"name":"argocd-application-controller","resources":{"limits":{"memory":"2Gi"}}}]}}}}'
```

### Debugging Commands

```bash
# Get all ArgoCD resources
kubectl get all -n argocd

# Check ArgoCD server logs
kubectl logs -f deployment/argocd-server -n argocd

# Check application controller logs
kubectl logs -f statefulset/argocd-application-controller -n argocd

# Check repository server logs
kubectl logs -f deployment/argocd-repo-server -n argocd

# Describe problematic resources
kubectl describe application <app-name> -n argocd

# Check events
kubectl get events -n argocd --sort-by='.lastTimestamp'
```

### Health Checks

```bash
# ArgoCD server health
curl -k https://argocd-server/healthz

# Application health via CLI
argocd app get <app-name> -o json | jq '.status.health'

# Cluster connectivity
argocd cluster list
```

---

## Best Practices

### Security Best Practices

#### 1. Authentication and Authorization
- Enable SSO integration (OIDC/SAML)
- Use RBAC for fine-grained access control
- Regularly rotate passwords and tokens
- Implement least privilege principle

```yaml
# Example RBAC policy
policy.csv: |
  # Production access only for SRE team
  p, role:sre, applications, *, production/*, allow
  p, role:sre, clusters, get, *, allow
  
  # Development access for dev team
  p, role:developer, applications, *, development/*, allow
  g, sre-team, role:sre
  g, dev-team, role:developer
```

#### 2. Network Security
- Use TLS for all communications
- Implement network policies
- Restrict ingress access
- Use private Git repositories

```yaml
# Network policy example
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: argocd-network-policy
  namespace: argocd
spec:
  podSelector:
    matchLabels:
      app.kubernetes.io/part-of: argocd
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: argocd
    ports:
    - protocol: TCP
      port: 8080
```

### Operational Best Practices

#### 1. Resource Management
- Set appropriate resource requests and limits
- Monitor resource usage
- Use horizontal pod autoscaling for repo-server
- Implement proper backup strategies

```yaml
# Resource configuration
resources:
  requests:
    cpu: 250m
    memory: 256Mi
  limits:
    cpu: 500m
    memory: 512Mi
```

#### 2. High Availability
- Run multiple replicas of repo-server
- Use external Redis for persistence
- Implement proper monitoring and alerting
- Regular backup of ArgoCD configuration

```yaml
# HA Redis configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-cmd-params-cm
  namespace: argocd
data:
  redis: "redis-ha-haproxy:6379"
  redis-sentinel: "true"
```

#### 3. GitOps Best Practices
- Use separate repositories for application code and manifests
- Implement proper branching strategies
- Use signed commits for security
- Automate manifest generation with CI/CD

```
Repository Structure:
├── applications/
│   ├── production/
│   │   ├── app1/
│   │   └── app2/
│   ├── staging/
│   └── development/
├── clusters/
│   ├── prod-cluster/
│   └── staging-cluster/
└── projects/
    ├── team-a/
    └── team-b/
```

### Monitoring and Observability

#### 1. Metrics and Monitoring

```yaml
# ServiceMonitor for Prometheus
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: argocd-metrics
  namespace: argocd
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: argocd-metrics
  endpoints:
  - port: metrics
```

#### 2. Logging Configuration

```yaml
# Logging configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-cmd-params-cm
  namespace: argocd
data:
  server.log.level: "info"
  controller.log.level: "info"
  reposerver.log.level: "info"
```

#### 3. Health Checks and Alerts

```bash
# Create health check endpoint monitoring
kubectl create configmap argocd-health-check \
  --from-literal=health-check.sh='#!/bin/bash
  curl -f http://localhost:8082/healthz || exit 1' \
  -n argocd
```

This comprehensive guide covers all aspects of ArgoCD architecture, installation on EKS, pod management, UI navigation, CLI usage, and operational best practices. Use this as a reference for implementing and managing ArgoCD in your Kubernetes environment.