# AWS DevOps Interview Questions & Troubleshooting Scenarios
## For Mohana Krishna - 3.6 Years Experience

---

## TECHNICAL INTERVIEW QUESTIONS

### AWS & Cloud Infrastructure (20-25 minutes)

**1. EKS & Kubernetes (Based on Microservice Cluster Management Project)**
- Walk me through your EKS cluster upgrade process. How do you ensure zero downtime?
- Explain IRSA (IAM Roles for Service Accounts) and why it's important for security
- How do you handle EKS node group migrations during upgrades?
- What's your approach to EKS cluster autoscaling configuration?

**2. Terraform & Infrastructure as Code**
- Describe your Terraform module structure for multi-environment deployments
- How do you handle Terraform state management in a team environment?
- Explain how you implement environment-specific configurations in Terraform
- What's your strategy for Terraform state locking and remote backends?

**3. AWS Organizations & Multi-Account Strategy**
- How did you implement Service Control Policies (SCPs) at Axway?
- Explain your approach to consolidated billing and cost optimization
- Describe the networking setup for multi-account architecture with Transit Gateways

**4. CI/CD & GitOps**
- Compare Jenkins vs GitHub Actions vs ArgoCD - when would you use each?
- How do you implement GitOps with ArgoCD for microservices?
- Describe your CI/CD security scanning integration (SonarQube, Trivy, OWASP ZAP)
- How do you handle rollbacks in ArgoCD?

**5. Monitoring & Observability**
- Explain your OpenTelemetry implementation for distributed tracing
- How do you configure Prometheus for EKS workloads?
- Describe your ELK stack setup for centralized logging
- What alerting strategies do you use for 99.9% uptime?

---

## TROUBLESHOOTING SCENARIOS

### SMALL COMPLEXITY ISSUES (5-10 minutes each)

#### Scenario 1: Pod CrashLoopBackOff
**Problem**: A microservice pod keeps restarting with CrashLoopBackOff status in EKS

**Expected Troubleshooting Steps**:
```bash
# Check pod status and events
kubectl get pods -n <namespace>
kubectl describe pod <pod-name> -n <namespace>

# Check logs
kubectl logs <pod-name> -n <namespace> --previous

# Common causes to check:
# 1. Resource limits (CPU/Memory)
# 2. Missing environment variables
# 3. Health check failures
# 4. Application startup issues
```

**Answer**: 
- Check pod events for specific error messages
- Review resource requests/limits in deployment spec
- Verify environment variables and ConfigMaps/Secrets
- Check application health check endpoints
- Review container image and startup commands
- Examine node resources and scheduling issues

#### Scenario 2: Jenkins Pipeline Failure
**Problem**: Jenkins pipeline fails during Docker build stage with "disk space" error

**Expected Solution**:
```bash
# Check Jenkins node disk usage
df -h

# Clean Docker resources on Jenkins agents
docker system prune -f
docker image prune -a -f

# Configure Jenkins to cleanup workspace
# Add post-build cleanup step
```

**Answer**:
- Implement automated cleanup in Jenkins pipeline
- Configure Docker daemon with storage limits
- Set up log rotation for Jenkins logs
- Use multi-stage Docker builds to reduce image size
- Implement regular cleanup jobs for Jenkins agents

#### Scenario 3: Terraform State Lock
**Problem**: Terraform operations fail with "state is locked" error

**Expected Solution**:
```bash
# Check current state lock
terraform force-unlock <lock-id>

# Identify who has the lock (in DynamoDB for S3 backend)
aws dynamodb scan --table-name <terraform-state-locks-table>
```

**Answer**:
- Verify if another team member is running Terraform
- Check CI/CD pipeline for running Terraform jobs
- Use `terraform force-unlock` cautiously
- Implement proper state locking strategy with timeouts
- Set up monitoring for long-running Terraform operations

---

### MEDIUM COMPLEXITY ISSUES (10-15 minutes each)

#### Scenario 4: EKS Networking Issues
**Problem**: Pods in EKS cluster cannot communicate with RDS database, but can reach internet

**Troubleshooting Approach**:
```bash
# Check security groups
aws ec2 describe-security-groups --group-ids <sg-id>

# Test network connectivity from pod
kubectl exec -it <pod-name> -- nc -zv <rds-endpoint> 5432

# Check route tables and NACLs
aws ec2 describe-route-tables
aws ec2 describe-network-acls
```

**Expected Answer**:
- Verify RDS security group allows inbound from EKS node security groups
- Check subnet routing to RDS subnets
- Verify RDS is in same VPC or proper VPC peering is configured
- Check Network ACLs for blocking rules
- Verify DNS resolution for RDS endpoint
- Check if RDS is in private subnets and NAT gateway configuration

#### Scenario 5: ArgoCD Sync Failures
**Problem**: ArgoCD applications show "OutOfSync" status but manual kubectl apply works

**Troubleshooting Steps**:
```bash
# Check ArgoCD application status
argocd app get <app-name>

# Compare desired vs live state
argocd app diff <app-name>

# Check ArgoCD server logs
kubectl logs -n argocd argocd-server-xxx
```

**Expected Answer**:
- Check for resource quotas and RBAC permissions
- Verify ArgoCD service account has proper cluster permissions
- Check for webhook configurations interfering with sync
- Review Helm chart templating issues
- Check for custom resource definitions (CRDs) not being applied
- Verify Git repository access and branch configurations

#### Scenario 6: High Memory Usage in EKS Nodes
**Problem**: EKS nodes showing high memory utilization, pods getting evicted

**Analysis Approach**:
```bash
# Check node resource usage
kubectl top nodes

# Check pod resource consumption
kubectl top pods --all-namespaces

# Check resource requests vs limits
kubectl describe nodes
```

**Expected Solution**:
- Analyze pod resource requests vs actual usage
- Implement resource quotas per namespace
- Configure pod disruption budgets
- Set up cluster autoscaler for horizontal scaling
- Implement vertical pod autoscaler for right-sizing
- Review memory leaks in applications

---

### COMPLEX SCENARIOS (15-20 minutes)

#### Scenario 7: Multi-Environment Terraform Deployment Issues
**Problem**: Terraform works in dev but fails in production with dependency cycle errors

**Complex Troubleshooting**:
```hcl
# Example dependency issue
resource "aws_security_group" "app" {
  # References ALB security group
  ingress {
    from_port       = 80
    to_port         = 80
    security_groups = [aws_security_group.alb.id]
  }
}

resource "aws_security_group" "alb" {
  # References app security group - CYCLE!
  egress {
    from_port       = 80
    to_port         = 80
    security_groups = [aws_security_group.app.id]
  }
}
```

**Expected Resolution**:
- Refactor security groups to break circular dependencies
- Use separate security group rules resources
- Implement proper module dependencies
- Use data sources for existing resources
- Create dependency graph visualization

#### Scenario 8: Production Incident - Complete Service Outage
**Problem**: All microservices in production EKS cluster are down after routine deployment

**War Room Approach**:
1. **Immediate Assessment** (2-3 minutes)
   - Check overall cluster health
   - Identify scope of impact
   - Activate incident response team

2. **Root Cause Investigation** (5-10 minutes)
   ```bash
   # Check recent deployments
   kubectl rollout history deployment/<app-name>
   
   # Check cluster events
   kubectl get events --sort-by=.metadata.creationTimestamp
   
   # Check node status
   kubectl get nodes
   ```

3. **Mitigation Strategy**
   - Rollback recent deployments
   - Scale up healthy replicas
   - Implement circuit breakers

**Expected Answer Components**:
- Systematic approach to incident response
- Communication with stakeholders
- Documentation of timeline and actions
- Post-incident review and lessons learned
- Implementation of preventive measures

---

## NORMAL INTERVIEW QUESTIONS BASED ON RESUME

### Background & Introduction (5-10 minutes)

**1. Tell me about yourself and your journey in DevOps**
- Expected: Brief overview of 3.6 years experience, transition from college to TCS, focus on AWS and containerization

**2. What attracted you to DevOps and cloud technologies?**
- Looking for: Genuine interest, learning mindset, problem-solving nature

**3. Why are you looking for a new opportunity now?**
- Professional growth, new challenges, technology expansion

### Education & Early Career (5 minutes)

**4. You graduated from Reva University in 2020 but started at TCS in Feb 2022. What did you do during that gap?**
- COVID impact, preparation, certifications, personal projects

**5. How did your B.Tech background prepare you for DevOps?**
- Technical foundation, problem-solving skills, learning approach

### Current Role & Responsibilities (10-15 minutes)

**6. Walk me through your current role at TCS**
- Daily responsibilities, team structure, client interactions

**7. You've worked on two major projects. Which one taught you the most and why?**
- Learning experience, challenges faced, growth

**8. Describe your team structure and how you collaborate with developers**
- Team dynamics, communication, stakeholder management

**9. How do you typically spend your day as a DevOps engineer?**
- Time management, priorities, reactive vs proactive work

### Project Deep Dive - Accor Project (15-20 minutes)

**10. You mentioned managing 5 microservices. Can you walk me through the architecture?**
- System design understanding, component interaction

**11. Tell me about the EKS cluster upgrades you performed. What was your process?**
- Planning, risk mitigation, communication, execution

**12. You achieved 99.9% uptime. How did you measure and maintain this?**
- Monitoring strategy, incident response, preventive measures

**13. What was the most critical incident you handled in this project?**
- Problem-solving under pressure, communication, resolution

**14. How did you handle the migration of 5 legacy applications to EKS?**
- Migration strategy, challenges, lessons learned

### Project Deep Dive - Axway Project (10-15 minutes)

**15. You managed 50+ environments with Terraform. How did you structure this?**
- Organization, scalability, maintainability

**16. Explain your AWS Organizations setup and why you chose that architecture**
- Multi-account strategy, governance, security

**17. What was the biggest challenge in implementing Infrastructure as Code at scale?**
- Team adoption, technical challenges, process changes

**18. How did you handle state management for multiple environments?**
- Technical implementation, team coordination

### Technical Skills Assessment (15-20 minutes)

**19. You list both AWS and Azure. Compare your experience with both platforms**
- Depth of knowledge, preferences, transferable skills

**20. Which CI/CD tool do you prefer - Jenkins, GitHub Actions, or ArgoCD - and why?**
- Tool selection criteria, use case understanding

**21. How do you approach security in your DevOps pipelines?**
- Security mindset, tools, best practices

**22. Explain your monitoring strategy. Why did you choose Prometheus + Grafana?**
- Tool selection, implementation, value delivered

**23. You have HashiCorp Terraform Associate certification. How has this helped you?**
- Certification value, knowledge application, continuous learning

### Problem-Solving & Soft Skills (10-15 minutes)

**24. Describe a time when you had to learn a new technology quickly for a project**
- Learning agility, resourcefulness, application

**25. Tell me about a time you disagreed with a team member about a technical approach**
- Communication, collaboration, conflict resolution

**26. How do you stay updated with the rapidly changing DevOps landscape?**
- Continuous learning, resources, community engagement

**27. Describe a time when you had to explain a technical concept to a non-technical stakeholder**
- Communication skills, audience awareness

**28. What's been your biggest failure or mistake, and what did you learn from it?**
- Self-awareness, learning from mistakes, growth mindset

### Career Aspirations & Goals (5-10 minutes)

**29. Where do you see yourself in the next 2-3 years?**
- Career progression, skill development, leadership aspirations

**30. What aspects of DevOps interest you the most for future learning?**
- Continuous learning, emerging technologies, specialization

**31. Are you interested in moving toward a more specialized role (like Site Reliability Engineering) or staying generalist?**
- Career direction, interests, growth path

**32. What kind of company culture and work environment do you thrive in?**
- Cultural fit, work style, team dynamics

### Company-Specific Questions (5 minutes)

**33. What do you know about our company and why do you want to work here?**
- Research, genuine interest, alignment

**34. What questions do you have about the role or our team?**
- Engagement, thoughtfulness, genuine interest

### Scenario-Based Behavioral Questions (10-15 minutes)

**35. Tell me about a time you had to work under tight deadlines**
- Time management, pressure handling, prioritization

**36. Describe a situation where you had to convince someone to adopt a new tool or process**
- Influence, communication, change management

**37. How do you handle competing priorities from different stakeholders?**
- Stakeholder management, communication, prioritization

**38. Tell me about a time you mentored or helped a junior team member**
- Leadership potential, knowledge sharing, team building

**39. Describe a time when you had to troubleshoot an issue you'd never seen before**
- Problem-solving, resourcefulness, persistence

**40. How do you handle situations where you don't know the answer to a technical question?**
- Honesty, learning approach, resourcefulness

### Technical Preference & Opinion Questions (5-10 minutes)

**41. What's your opinion on the future of container orchestration? Will Kubernetes remain dominant?**
- Industry awareness, technical opinions, forward thinking

**42. How do you see the role of AI/ML in DevOps evolving?**
- Technology trends, adaptation, innovation

**43. What's your take on serverless vs containerized applications?**
- Technical judgment, use case understanding

**44. Infrastructure as Code vs ClickOps - when might you choose one over the other?**
- Practical judgment, context awareness

### Location & Logistics (2-3 minutes)

**45. You're currently in Bangalore. Are you open to relocating?**
- Flexibility, personal constraints

**46. How do you feel about remote work vs office work?**
- Work style preferences, productivity

**47. What's your notice period at TCS?**
- Availability, transition planning

### BEHAVIORAL & SCENARIO-BASED QUESTIONS

### Project-Specific Questions

**1. Accor Microservice Project**
- "You mentioned achieving 99.9% uptime. Walk me through a specific incident where you had to maintain this SLA"
- "Describe the most challenging EKS cluster upgrade you performed"

**2. Axway AWS Infrastructure Project**
- "How did you approach migrating 50+ environments to Terraform?"
- "Tell me about a time when you had to troubleshoot a complex multi-account AWS issue"

### Problem-Solving Scenarios

**3. Capacity Planning**
- "How would you design auto-scaling for a microservice that has predictable traffic spikes every day at 9 AM?"

**4. Cost Optimization**
- "A client complains about high AWS bills. How would you approach cost optimization for their EKS workloads?"

**5. Security Implementation**
- "Describe how you would implement security best practices for a new EKS cluster from scratch"

---

## HANDS-ON CODING/CONFIGURATION

### Terraform Challenge
Write a Terraform module for an EKS cluster with:
- Managed node groups
- IRSA configuration
- Security groups
- IAM roles

### Kubernetes YAML
Create a Deployment with:
- Resource limits
- Health checks
- ConfigMap integration
- Service account

### Jenkins Pipeline
Write a Jenkinsfile for:
- Multi-stage Docker build
- Security scanning integration
- Deployment to multiple environments

---

## ADVANCED TOPICS FOR SENIOR DISCUSSION

1. **GitOps Strategy**: Compare different GitOps tools and implementation patterns
2. **Observability**: Discuss OpenTelemetry implementation and distributed tracing strategies
3. **Security**: Deep dive into container security, image scanning, and runtime protection
4. **Performance**: EKS performance tuning and optimization techniques
5. **Disaster Recovery**: Multi-region EKS setup and backup strategies

---

## EVALUATION CRITERIA

### Technical Competency (40%)
- Depth of AWS and Kubernetes knowledge
- Understanding of DevOps principles
- Problem-solving approach

### Practical Experience (30%)
- Real-world scenario handling
- Troubleshooting methodology
- Tool expertise

### Communication (20%)
- Clarity in explanations
- Ability to break down complex topics
- Incident communication skills

### Growth Mindset (10%)
- Learning from failures
- Staying updated with technology
- Continuous improvement approach


I'll break down these DevOps and cloud concepts for you:

## AWS vs Azure Pipelines

**AWS CodePipeline** is Amazon's CI/CD service that integrates with other AWS services like CodeBuild, CodeDeploy, and CodeCommit. It's designed for AWS-centric workflows and provides good integration with the broader AWS ecosystem.

**Azure Pipelines** (part of Azure DevOps) is Microsoft's CI/CD platform that supports multiple cloud providers, on-premises deployments, and various programming languages. It offers both YAML and classic editor approaches for defining pipelines.

Key differences:
- Azure Pipelines has better multi-cloud support
- AWS CodePipeline integrates more seamlessly with AWS services
- Azure Pipelines offers more flexible pricing with free tiers for open source
- AWS CodePipeline pricing is pay-per-pipeline execution

## Why Jenkins Remains Popular

Jenkins stays relevant because it's:
- **Open source and free** - no licensing costs
- **Highly customizable** - thousands of plugins available
- **Platform agnostic** - runs anywhere Java runs
- **Self-hosted** - complete control over your CI/CD environment
- **Mature ecosystem** - extensive community support and documentation
- **Flexible** - can integrate with virtually any tool or service

While cloud-native solutions are convenient, Jenkins offers unmatched flexibility for complex, hybrid, or highly customized workflows.

## Git vs ArgoCD

**Git** is a distributed version control system for tracking code changes and collaboration.

**ArgoCD** is a GitOps continuous delivery tool specifically for Kubernetes that uses Git repositories as the source of truth for defining desired application state.

They work together - Git stores your Kubernetes manifests, and ArgoCD monitors the Git repo and automatically syncs changes to your Kubernetes clusters. ArgoCD essentially bridges the gap between your Git repository and your Kubernetes deployment.

## AWS vs Azure Networking

**AWS Networking:**
- **VPC** (Virtual Private Cloud) as the foundational networking service
- **Subnets** for network segmentation
- **Internet Gateway** for internet access
- **NAT Gateway/Instance** for outbound internet from private subnets
- **Route Tables** for traffic routing
- **Security Groups** (stateful) and NACLs (stateless) for security
- **VPC Peering** and **Transit Gateway** for connecting VPCs

**Azure Networking:**
- **Virtual Network** (VNet) as the core networking service
- **Subnets** for segmentation within VNets
- **Network Security Groups** (NSGs) for security rules
- **Application Security Groups** for logical grouping
- **VNet Peering** and **Virtual WAN** for connectivity
- **Azure Load Balancer** and **Application Gateway** for load balancing
- **ExpressRoute** for dedicated connections

Azure tends to have more integrated security features and simpler routing concepts, while AWS offers more granular control and service options.

## Ansible Overview

**Ansible** is an open-source automation platform that uses simple, human-readable YAML playbooks to automate configuration management, application deployment, and orchestration tasks.

Key characteristics:
- **Agentless** - uses SSH for Linux/Unix and WinRM for Windows
- **Idempotent** - running the same playbook multiple times produces the same result
- **Declarative** - you describe the desired state, not the steps to get there
- **Inventory-based** - manages groups of hosts through inventory files
- **Module-based** - extensive library of modules for different tasks

Ansible excels at configuration management, server provisioning, and orchestrating complex multi-tier deployments across diverse infrastructure environments.



I'll walk you through each of these areas based on best practices and real-world implementation strategies:

## 1. EKS & Kubernetes

**EKS Cluster Upgrade Process for Zero Downtime:**
- **Blue-Green cluster strategy**: Maintain two clusters, upgrade the secondary, then gradually migrate workloads
- **Rolling upgrades**: Use managed node groups with proper pod disruption budgets (PDBs)
- **Pre-upgrade validation**: Run `kubectl drain` on nodes systematically, ensure applications have multiple replicas
- **Upgrade sequence**: Control plane first (AWS manages this), then node groups, finally add-ons
- **Health checks**: Implement comprehensive readiness/liveness probes and use rolling update strategies

**IRSA (IAM Roles for Service Accounts):**
```yaml
# Service Account with IRSA annotation
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-service-account
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::ACCOUNT:role/MyServiceRole
```
- **Security benefit**: Eliminates need for AWS credentials in pods
- **Principle of least privilege**: Each service gets only required permissions
- **Token rotation**: Automatic credential rotation via OIDC provider
- **Audit trail**: CloudTrail logs show which pod assumed which role

**Node Group Migrations:**
- **Gradual replacement**: Create new node groups with updated AMI/instance types
- **Taint and drain**: Systematically cordon old nodes, drain workloads
- **Pod disruption budgets**: Ensure minimum replicas during migration
- **Monitoring**: Watch pod scheduling and cluster resource utilization

**EKS Cluster Autoscaling:**
```yaml
# Cluster Autoscaler deployment configuration
spec:
  containers:
  - image: k8s.gcr.io/autoscaling/cluster-autoscaler:v1.21.0
    command:
    - ./cluster-autoscaler
    - --v=4
    - --stderrthreshold=info
    - --cloud-provider=aws
    - --skip-nodes-with-local-storage=false
    - --expander=least-waste
    - --node-group-auto-discovery=asg:tag=k8s.io/cluster-autoscaler/enabled,k8s.io/cluster-autoscaler/eks-cluster-name
```

## 2. Terraform & Infrastructure as Code

**Module Structure for Multi-Environment:**
```hcl
# Directory structure
terraform/
├── modules/
│   ├── vpc/
│   ├── eks/
│   ├── rds/
│   └── security-groups/
├── environments/
│   ├── dev/
│   ├── staging/
│   └── prod/
└── shared/
    ├── backend.tf
    └── providers.tf

# Environment-specific main.tf
module "vpc" {
  source = "../../modules/vpc"
  
  environment = var.environment
  vpc_cidr    = var.vpc_cidr
  azs         = var.availability_zones
}
```

**State Management Strategy:**
- **Remote backend**: S3 with DynamoDB for locking
- **State isolation**: Separate state files per environment
- **Workspace strategy**: Use Terraform workspaces for environment separation
- **Backend configuration**:
```hcl
terraform {
  backend "s3" {
    bucket         = "company-terraform-state"
    key            = "environments/${var.environment}/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

**Environment-Specific Configurations:**
```hcl
# terraform.tfvars files per environment
# environments/prod/terraform.tfvars
environment = "prod"
instance_type = "c5.2xlarge"
min_size = 3
max_size = 20

# environments/dev/terraform.tfvars
environment = "dev"
instance_type = "t3.medium"
min_size = 1
max_size = 5
```

## 3. AWS Organizations & Multi-Account Strategy

**Service Control Policies (SCPs) Implementation:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "ec2:TerminateInstances",
        "rds:DeleteDBInstance"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalTag/Environment": ["prod"]
        }
      }
    }
  ]
}
```

**Cost Optimization Strategy:**
- **RI and Savings Plans**: Centralized purchasing through master account
- **Cost allocation tags**: Enforce consistent tagging across all accounts
- **Budget alerts**: Account-level and service-level budget monitoring
- **Resource scheduling**: Automated start/stop for non-prod environments

**Transit Gateway Network Architecture:**
```hcl
# Hub-and-spoke model
resource "aws_ec2_transit_gateway" "main" {
  description                     = "Main TGW"
  default_route_table_association = "disable"
  default_route_table_propagation = "disable"
}

# Separate route tables for different environments
resource "aws_ec2_transit_gateway_route_table" "prod" {
  transit_gateway_id = aws_ec2_transit_gateway.main.id
}
```

## 4. CI/CD & GitOps

**Tool Selection Strategy:**
- **Jenkins**: Complex enterprise workflows, existing infrastructure, custom plugins
- **GitHub Actions**: Git-native workflows, simple setup, integrated security scanning
- **ArgoCD**: Kubernetes-native GitOps, declarative deployments, drift detection

**ArgoCD GitOps Implementation:**
```yaml
# Application manifest
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: microservice-app
spec:
  project: default
  source:
    repoURL: https://github.com/company/k8s-manifests
    targetRevision: HEAD
    path: apps/microservice
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
```

**Security Scanning Integration:**
```yaml
# GitHub Actions pipeline
- name: SonarQube Scan
  uses: sonarqube-quality-gate-action@master
  
- name: Trivy Container Scan
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
    
- name: OWASP ZAP Scan
  uses: zaproxy/action-full-scan@v0.4.0
  with:
    target: 'https://staging.example.com'
```

**ArgoCD Rollback Strategy:**
- **Git-based rollbacks**: Revert commits to trigger automatic rollback
- **Application history**: Use ArgoCD UI to rollback to previous sync
- **Blue-green deployments**: Maintain multiple versions, switch traffic gradually
- **Canary releases**: Progressive traffic splitting with monitoring

## 5. Monitoring & Observability

**OpenTelemetry Implementation:**
```yaml
# OpenTelemetry Collector configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
data:
  config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
    processors:
      batch:
    exporters:
      jaeger:
        endpoint: jaeger-collector:14250
      prometheus:
        endpoint: "0.0.0.0:8889"
    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: [batch]
          exporters: [jaeger]
        metrics:
          receivers: [otlp]
          processors: [batch]
          exporters: [prometheus]
```

**Prometheus for EKS:**
```yaml
# ServiceMonitor for application metrics
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: app-metrics
spec:
  selector:
    matchLabels:
      app: my-microservice
  endpoints:
  - port: metrics
    path: /metrics
    interval: 30s
```

**ELK Stack Setup:**
- **Elasticsearch**: Clustered setup with data/master node separation
- **Logstash**: Multiple pipelines for different log types
- **Filebeat**: DaemonSet deployment for log collection
- **Kibana**: Centralized dashboards with RBAC

**Alerting Strategy for 99.9% Uptime:**
```yaml
# Prometheus alerting rules
groups:
- name: sla-alerts
  rules:
  - alert: HighErrorRate
    expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
    for: 2m
    annotations:
      summary: "High error rate detected"
      
  - alert: PodCrashLooping
    expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
    for: 5m
```

**Key SLA Metrics:**
- **Availability**: 99.9% = 8.76 hours downtime/year
- **Response time**: P95 < 500ms, P99 < 1s
- **Error budget**: 0.1% error rate allowance
- **MTTR**: Mean time to recovery < 30 minutes

This approach ensures robust, scalable, and maintainable cloud infrastructure with proper observability and security controls throughout the deployment pipeline.
