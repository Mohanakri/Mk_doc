# Mohana Krishna - Project Details & Day-to-Day Activities

## PROJECT 1: AXWAY - AWS AUTOMATION ADMIN
**Duration:** Feb 2022 – Aug 2023 (1.5 years)  
**Role:** AWS Automation Admin  
**Technologies:** AWS, Terraform, Python

---

### 🏗️ INFRASTRUCTURE OVERVIEW

#### Multi-Account AWS Architecture
```
AWS Organization Structure:
├── Master Account (Billing & Management)
├── Security Account (Logging & Compliance)
├── Shared Services Account (DNS, Monitoring)
├── Development Accounts (Multiple)
├── Staging Accounts (Multiple)  
└── Production Accounts (Multiple)

Total Managed: 50+ environments across multiple AWS accounts
```

#### Account Management Details
- **AWS Organizations:** Centralized management with consolidated billing
- **Service Control Policies (SCPs):** Organizational-level security guardrails
- **Cross-account access:** IAM roles for secure account switching
- **Cost management:** Resource tagging and cost allocation per environment

#### Infrastructure Scale
```yaml
Environment Distribution:
  Development: ~20 environments
  Staging: ~15 environments
  Production: ~15 environments
  
Account Types:
  - Application-specific accounts
  - Environment-specific isolation
  - Shared services account
  - Security and compliance account
```

---

### 🚀 DAY-TO-DAY ACTIVITIES (AXWAY PROJECT)

#### Morning Activities (9:00 AM - 11:00 AM)
- **Infrastructure Health Checks:**
  - Review CloudWatch dashboards for all accounts
  - Check overnight Terraform runs and deployments
  - Monitor AWS costs and resource utilization
  - Validate backup statuses across environments

#### Core Development (11:00 AM - 4:00 PM)
- **Terraform Development:**
  ```hcl
  # Daily Terraform tasks
  - Module development for reusable components
  - Environment-specific configuration updates
  - State file management and cleanup
  - Resource drift detection and remediation
  ```

- **Python Automation:**
  ```python
  # CloudWatch Events & EventBridge integration
  - Resource utilization monitoring scripts
  - Unused resource identification automation
  - Cost optimization reporting
  - Compliance checking automation
  ```

#### Afternoon Activities (4:00 PM - 6:00 PM)
- **Team Collaboration:**
  - Code reviews for Terraform modules
  - Sprint planning and stand-up meetings
  - Documentation updates
  - Knowledge sharing sessions

#### Infrastructure Management Tasks
- **AWS EKS Clusters:**
  - Cluster provisioning using Terraform
  - Node group management and scaling
  - IRSA (IAM Roles for Service Accounts) configuration
  - Cluster upgrades and maintenance

- **Networking Architecture:**
  - VPC design and implementation
  - Transit Gateway configurations
  - VPC peering setup
  - Route table management

---

### 📊 TECHNICAL SPECIFICATIONS (AXWAY)

#### Storage & Data Management
```yaml
S3 Implementation:
  - Cross-region replication setup
  - Versioning and lifecycle policies
  - KMS encryption implementation
  - Intelligent tiering configuration
  - Glacier and Deep Archive transitions

Storage Scale:
  - Multiple TB of data across environments
  - Automated lifecycle management
  - Cost-optimized storage classes
```

#### Networking Details
```yaml
Network Architecture:
  VPCs per Environment: 1-2 VPCs
  Subnets: Public, Private, Database tiers
  NAT Gateways: Multi-AZ deployment
  Transit Gateways: Inter-VPC connectivity
  Route Tables: Environment-specific routing
```

---

## PROJECT 2: ACCOR - MICROSERVICE CLUSTER MANAGEMENT
**Duration:** Sep 2023 – Present  
**Role:** Kubernetes Developer  
**Technologies:** EKS, Jenkins, ArgoCD, Helm, Terraform, Prometheus, Grafana, EFK, Jaeger

---

### 🎯 CURRENT PROJECT INFRASTRUCTURE

#### EKS Cluster Configuration
```yaml
Cluster Details:
  Total Clusters: 3-5 EKS clusters
  Environments: Development, Staging, Production
  
  Per Cluster Configuration:
    Node Groups: 2-3 managed node groups
    Instance Types: 
      - t3.medium (development)
      - m5.large (staging)  
      - m5.xlarge, m5.2xlarge (production)
    
    Scaling Configuration:
      Min Nodes: 2
      Max Nodes: 10-20 (environment dependent)
      Desired: 3-5 nodes per environment
```

#### Multi-Environment Setup
```yaml
Development Environment:
  Nodes: 2-4 nodes
  Instance Type: t3.medium, t3.large
  Workloads: 5 microservices
  Resource Allocation: Minimal for testing

Staging Environment:
  Nodes: 3-6 nodes  
  Instance Type: m5.large
  Workloads: Full application stack
  Resource Allocation: Production-like

Production Environment:
  Nodes: 5-15 nodes
  Instance Type: m5.xlarge, m5.2xlarge
  Workloads: 5 production microservices
  Resource Allocation: Optimized for performance
  High Availability: Multi-AZ deployment
```

---

### 🔄 CURRENT DAY-TO-DAY ACTIVITIES (ACCOR)

#### Morning Routine (9:00 AM - 10:30 AM)
- **Cluster Health Monitoring:**
  ```bash
  # Daily cluster checks
  kubectl get nodes --all-namespaces
  kubectl get pods --all-namespaces | grep -v Running
  kubectl top nodes
  kubectl top pods --all-namespaces
  ```

- **Dashboard Reviews:**
  - Grafana dashboards for cluster metrics
  - Prometheus alerts review
  - ArgoCD application sync status
  - Jenkins pipeline status

#### Development & Maintenance (10:30 AM - 4:00 PM)
- **CI/CD Pipeline Management:**
  ```yaml
  Jenkins Activities:
    - Pipeline troubleshooting and optimization
    - Security scanning integration (SonarQube, Trivy, OWASP ZAP)
    - Build artifact management
    - Multi-environment deployment coordination
  
  ArgoCD Management:
    - Application deployment monitoring
    - Git repository synchronization
    - Rollback operations when needed
    - Configuration drift resolution
  ```

- **Kubernetes Operations:**
  ```bash
  # Regular Kubernetes tasks
  - Pod troubleshooting and restart
  - Resource quota management
  - ConfigMap and Secret updates
  - Service and ingress configuration
  ```

#### Infrastructure Management (4:00 PM - 6:00 PM)
- **Terraform Operations:**
  ```hcl
  # Infrastructure updates
  - EKS cluster configuration changes
  - Node group scaling adjustments
  - Security group rule updates
  - IAM policy modifications
  ```

- **Monitoring & Observability:**
  - Prometheus metrics configuration
  - Grafana dashboard updates
  - ELK stack log analysis
  - Jaeger tracing investigation

---

### 🛠️ MICROSERVICES ARCHITECTURE

#### Application Stack
```yaml
Microservices (5 total):
  1. User Service (Java/Spring Boot)
  2. Authentication Service (Python/FastAPI)
  3. Payment Service (Node.js/Express)
  4. Notification Service (Java/Spring Boot)
  5. API Gateway (Kong/Istio)

Resource Allocation per Service:
  Development:
    CPU: 100m-200m
    Memory: 256Mi-512Mi
  
  Production:
    CPU: 500m-1000m
    Memory: 1Gi-2Gi
```

#### Build Tools Configuration
```yaml
Build Environment:
  Java Applications: Maven 3.8+
  Python Applications: pip, requirements.txt
  Node.js Applications: npm/yarn
  
Container Images:
  Base Images: Alpine Linux for minimal size
  Multi-stage builds: Optimized for production
  Security scanning: Trivy integration
```

---

### 📈 OPERATIONAL METRICS & ACHIEVEMENTS

#### Performance Metrics
```yaml
Current Achievements:
  Uptime: 99.9% across production workloads
  EKS Upgrades: 5+ successful zero-downtime upgrades
  Application Migrations: 5 legacy to containerized
  
Operational Metrics:
  Deployment Frequency: Multiple deployments per day
  Lead Time: Reduced from hours to minutes
  MTTR: Average 15-30 minutes
  Change Failure Rate: < 5%
```

#### Infrastructure Optimization
```yaml
Cost Optimization:
  - Spot instances for non-critical workloads
  - Cluster autoscaler implementation
  - Resource right-sizing
  - Unused resource cleanup automation

Performance Optimization:
  - Pod resource optimization
  - HPA (Horizontal Pod Autoscaler) configuration
  - Node group optimization
  - Network performance tuning
```

---

### 🔧 TROUBLESHOOTING & INCIDENT RESPONSE

#### Common Daily Issues
```yaml
Frequent Troubleshooting:
  1. Pod CrashLoopBackOff scenarios
  2. Image pull failures and registry issues
  3. Volume mount problems
  4. Network connectivity issues
  5. Resource constraint problems

Resolution Approach:
  - Systematic log analysis
  - Metrics correlation
  - Root cause identification
  - Preventive measure implementation
```

#### War Room Participation
- **P1 Incident Response:** Immediate escalation and resolution
- **Cross-team Coordination:** Development, QA, and Business teams
- **Post-incident Reviews:** Blameless post-mortems
- **Process Improvement:** Documentation and runbook updates

---

### 🎯 WEEKLY & MONTHLY ACTIVITIES

#### Weekly Tasks
- EKS cluster health reviews
- Security patch management
- Performance optimization analysis
- Team knowledge sharing sessions
- Sprint retrospectives and planning

#### Monthly Tasks
- Infrastructure cost analysis and optimization
- Disaster recovery testing
- Backup and restore validation
- Compliance audit support
- Capacity planning reviews

---

### 📊 TOOLS & INTEGRATION ECOSYSTEM

#### Development Workflow
```yaml
Source Control: Git, GitHub, GitLab
CI/CD: Jenkins, GitHub Actions, ArgoCD
Container Registry: Amazon ECR, Nexus3
Artifact Management: Nexus Repository
Security: SonarQube, Trivy, OWASP ZAP

Monitoring Stack:
  Metrics: Prometheus, Grafana
  Logging: Elasticsearch, Kibana, Fluentd
  Tracing: Jaeger, OpenTelemetry
  Alerting: Prometheus Alertmanager
```

This comprehensive overview shows the scale and complexity of infrastructure you're managing, demonstrating significant hands-on experience with enterprise-level AWS and Kubernetes environments. Your experience spans from infrastructure automation to microservices orchestration, showing progressive responsibility growth from the Axway to Accor projects.