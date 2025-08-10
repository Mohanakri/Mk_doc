# User data for Ec2 to install awscli,kubectl,eksctl

Your bastion or working machine should has access to create aws eks , aws cli or Iam role 

```bash
#!/bin/bash

# Update system
apt update -y

# Install AWS CLI
snap install aws-cli --classic

# Download kubectl v1.30
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.11/2025-04-17/bin/linux/amd64/kubectl
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.11/2025-04-17/bin/linux/amd64/kubectl.sha256

# Verify SHA
sha256sum -c kubectl.sha256

# Make kubectl executable and move to bin
chmod +x ./kubectl
mkdir -p /usr/local/bin
mv ./kubectl /usr/local/bin/kubectl

# Persist PATH
echo 'export PATH=/usr/local/bin:$PATH' >> /etc/profile

# eksctl install
ARCH=amd64
PLATFORM=$(uname -s)_$ARCH

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"
curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz
install -m 0755 /tmp/eksctl /usr/local/bin && rm /tmp/eksctl

curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh

# === Run and log version checks ===
echo "===== TOOL VERSION CHECKS =====" > /var/log/tool-verify.log
{
  aws --version  
  kubectl version --client  
  eksctl version  
  helm version
} >> /var/log/tool-verify.log 2>&1

# Optional: tail the log for debugging in the background
# (remove if not needed)
tail -f /var/log/tool-verify.log &

```

-----------------------

## eks kubernetes provision

# aws eks cluster creation only master nodes 
```bash
eksctl create cluster --name=observability \
                      --region=us-east-1 \
                      --zones=us-east-1a,us-east-1b \
                      --without-nodegroup

```

# OIDC acts as an authentication mechanism
Intstead of workder node i am nodes this one give fine grined control.

```bash
eksctl utils associate-iam-oidc-provider \
    --region us-east-1 \
    --cluster observability \
    --approve

```
#workernode creation

```bash
eksctl create nodegroup --cluster=observability \
                        --region=us-east-1 \
                        --name=observability-ng-private \
                        --node-type=t3.medium \
                        --nodes-min=2 \
                        --nodes-max=3 \
                        --node-volume-size=20 \
                        --managed \
                        --asg-access \
                        --external-dns-access \
                        --full-ecr-access \
                        --appmesh-access \
                        --alb-ingress-access \
                        --node-private-networking

```


# Update ./kube/config file
aws eks update-kubeconfig --name observability


# Argocd installation

manual : https://argo-cd.readthedocs.io/en/stable/getting_started/

through helm:  https://argo-cd.readthedocs.io/en/stable/operator-manual/installation/#helm


# Argo cd Samples for play



# ingress for argocd 
install iam policy and service iam role before alb controller installation

--------------------
Perfect! Since it's now working, here's a **complete, clean guide** that walks you through **end-to-end setup of Ingress using AWS Load Balancer Controller (ALB)** in an EKS cluster — including Helm installation, IAM setup, Ingress creation, and optional HTTPS setup.

---

# ✅ Complete AWS EKS Ingress Setup via ALB Controller (Step-by-Step)

---

## 🔹 1. Prerequisites

Make sure you have:

* ✅ An **EKS cluster** running
* ✅ `kubectl`, `eksctl`, `helm` installed locally
* ✅ `aws` CLI configured with IAM admin or proper permissions
* ✅ IAM OIDC provider associated with the EKS cluster

---

## 🔹 2. Associate OIDC Provider (if not done yet)

```bash
eksctl utils associate-iam-oidc-provider \
  --region <region> \
  --cluster <cluster-name> \
  --approve
```

---

## 🔹 3. Create IAM Policy for Load Balancer Controller

Download and create the IAM policy:

```bash
curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json

aws iam create-policy \
  --policy-name AWSLoadBalancerControllerIAMPolicy \
  --policy-document file://iam-policy.json
```

---

## 🔹 4. Create IAM Role for Service Account (IRSA)

```bash
eksctl create iamserviceaccount \
  --cluster <cluster-name> \
  --namespace kube-system \
  --name aws-load-balancer-controller \
  --attach-policy-arn arn:aws:iam::<account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve
```

---

## 🔹 5. Install AWS Load Balancer Controller via Helm

Add the Helm repo:

```bash
helm repo add eks https://aws.github.io/eks-charts
helm repo update
```

Install the controller:

```bash
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --set clusterName=<cluster-name> \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  --set region=<region> \
  --set vpcId=<vpc-id>
```

---

## 🔹 6. Verify Controller Is Running

```bash
kubectl get pods -n kube-system | grep aws-load
```

Should show a running pod like:

```
aws-load-balancer-controller-xxxx   Running
```

---

## 🔹 7. Patch Argo CD Service

Argo CD's default service is `ClusterIP`, which ALB can use with `target-type: ip`.

```bash
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "ClusterIP"}}'
```

---

## 🔹 8. Create Ingress for Argo CD (HTTP)

Save this as `argocd-ingress.yaml`:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: argocd-ingress
  namespace: argocd
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/group.name: argocd
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}]'
spec:
  ingressClassName: alb
  rules:
    - host: argocd.example.com  # Optional. Can also omit and use ALB DNS.
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: argocd-server
                port:
                  number: 443
```

Apply the Ingress:

```bash
kubectl apply -f argocd-ingress.yaml
```

---

## 🔹 9. Get the Load Balancer URL

```bash
kubectl get ingress argocd-ingress -n argocd
```

Sample output:

```
NAME             CLASS   HOSTS                  ADDRESS                                              PORTS   AGE
argocd-ingress   alb     argocd.example.com     k8s-argocd-xxxxx.us-east-1.elb.amazonaws.com         80      2m
```

Now access:

```
http://<alb-dns-name>
```

Or map your domain (`argocd.example.com`) in Route 53.

---

## 🔹 10. (Optional) Enable HTTPS with ACM

Steps:

1. Request an ACM certificate for your domain
2. Use the ARN in your Ingress annotations:

```yaml
alb.ingress.kubernetes.io/listen-ports: '[{"HTTPS":443}]'
alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:<region>:<account>:certificate/xxxxxxxx
```

Also update the `service.port.number` to 443.

---

## 🔐 11. Login to Argo CD UI

Get the Argo CD admin password:

```bash
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d && echo
```

Open browser:

```
http://<alb-dns> or https://<your-domain>
```

Login with:

* Username: `admin`
* Password: (from secret above)

---

## ✅ Final Architecture

```plaintext
User Browser
     │
     ▼
AWS Application Load Balancer (ALB)
     │
     ▼
Ingress Controller (aws-load-balancer-controller)
     │
     ▼
Argo CD Service (argocd-server - ClusterIP)
     │
     ▼
Argo CD Pod
```

---

Would you like:

* HTTPS + Route 53 domain setup?
* Example Ingress + Service for another app like NGINX or your microservice?
* Full Terraform setup for all of the above?

Let me know!
-----------------------------

If you're unable to access the Argo CD UI via the AWS ALB (Ingress), here’s a structured **troubleshooting checklist** to help you debug the issue:

---

# 🛠️ Ingress/ALB Access Troubleshooting for EKS

---

## ✅ 1. **Check ALB DNS Works**

From your browser (or via `curl`):

```bash
curl -I http://<alb-dns-name>
```

If you get a response (even 403/404), ALB is reachable.

If you get **timeout / unreachable**, go through the next steps.

---

## ✅ 2. **Check ArgoCD Service Type + Port**

Make sure `argocd-server` is **type: ClusterIP** (or NodePort) and exposes **port 443** internally:

```bash
kubectl get svc argocd-server -n argocd
```

Should show something like:

```
NAME            TYPE        CLUSTER-IP     PORT(S)
argocd-server   ClusterIP   10.0.32.143    443/TCP
```

If not:

```bash
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "ClusterIP"}}'
```

---

## ✅ 3. **Check Ingress Resource**

Check if the Ingress is attached to an ALB:

```bash
kubectl describe ingress argocd-ingress -n argocd
```

You should see:

* IngressClassName: `alb`
* Events showing ALB provisioning succeeded
* Annotations like `alb.ingress.kubernetes.io/...`

If you see errors like **“failed to create target group”** or **“no endpoints”**, move to step 5.

---

## ✅ 4. **Check Target Group Health (AWS Console)**

1. Go to **EC2 → Load Balancers → Select ALB**
2. Check **Target Groups**
3. Select the **Target Group** created for Argo CD
4. Check **Health checks**

You may see:

* ❌ Unhealthy (because of wrong port or path)
* ✅ Healthy if backend is responding correctly

🔁 If **Unhealthy**, do this:

```bash
kubectl get endpoints argocd-server -n argocd
```

If it’s empty — it means **no pods** are ready or service port mismatch.

---

## ✅ 5. **Check Pod Readiness**

```bash
kubectl get pods -n argocd
```

Ensure:

* `argocd-server` pod is running
* It has a readiness probe configured correctly
* No crash loops

---

## ✅ 6. **Port Confusion: Use HTTP on 443**

ALB is sending HTTP to port 443 (not HTTPS).

Argo CD by default listens for **HTTPS on 443**, so the Ingress sends plain HTTP to HTTPS port → it fails.

---

### 🔄 Solution 1: Change Argo CD Service to Port 80

Expose **port 80** instead of 443, or use HTTPS correctly in Ingress.

```bash
kubectl edit svc argocd-server -n argocd
```

Change:

```yaml
ports:
  - name: https
    port: 443
    targetPort: 8080  # or whatever ArgoCD uses internally
```

Or (better) expose **port 80** for HTTP.

---

### 🔄 Solution 2: Use HTTPS Listener with ACM

If Argo CD listens on HTTPS (443), your Ingress **must use HTTPS listener** with ACM:

```yaml
alb.ingress.kubernetes.io/listen-ports: '[{"HTTPS": 443}]'
alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:region:account-id:certificate/xxxxxx
```

Update service port and Ingress accordingly.

---

## ✅ 7. **Test Internal Access**

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Then visit: [https://localhost:8080](https://localhost:8080)

If this works, Argo CD is running fine internally — the problem is the Ingress setup.

---

## ✅ 8. **Check Logs of Load Balancer Controller**

```bash
kubectl logs -n kube-system deployment/aws-load-balancer-controller
```

Look for:

* Errors about Ingress provisioning
* Warnings about target groups or health checks

---

## ✅ 9. (Optional) Test with Dummy App

Try deploying NGINX to isolate the issue from ArgoCD:

```bash
kubectl create deployment nginx --image=nginx -n default
kubectl expose deployment nginx --port=80 --target-port=80 --name=nginx -n default
```

Then create this Ingress:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
  namespace: default
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}]'
spec:
  ingressClassName: alb
  rules:
    - http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: nginx
                port:
                  number: 80
```

Apply and test in browser.

---

## 🧼 Summary Checklist

| Check                         | Fix If Missing                        |
| ----------------------------- | ------------------------------------- |
| ALB created                   | Check `kubectl get ingress`           |
| Service type & port           | Should be `ClusterIP`, port 443 or 80 |
| ArgoCD pod running            | Use `kubectl get pods -n argocd`      |
| ALB target group health       | Check in AWS Console                  |
| ALB sending to correct port   | 80 or 443 based on ArgoCD setup       |
| Load Balancer Controller logs | Look for ingress provisioning errors  |

---

Would you like me to:

* Generate a **fully working Ingress YAML** for HTTPS?
* Help fix the service port configuration?
* Give a script to test endpoint readiness?

Let me know what exact issue you're hitting in the above checks.
-----------------------

Absolutely — let’s **break down all the port types in Kubernetes** across:

### ✅ Ingress

### ✅ Service (ClusterIP / NodePort)

### ✅ Pod (Container)

We’ll use your **Argo CD setup** as an example for better clarity.

---

## 🔁 FLOW OVERVIEW

```bash
Internet
  ↓
Ingress (ALB / NGINX) → listens on :80 or :443
  ↓
Service (ClusterIP)   → listens on :80, forwards to targetPort (e.g., :8080)
  ↓
Pod (Container)       → listens on :8080 (application port)
```

---

## ✅ 1. **Ingress**: Entry into your cluster

**Ingress resource** is how **external users (Internet)** reach your app.

| Port  | Purpose | Notes                           |
| ----- | ------- | ------------------------------- |
| `80`  | HTTP    | Used for plain web              |
| `443` | HTTPS   | TLS termination (if configured) |

Ingress doesn’t need to match **pod ports** — it talks to the **Service**.

✅ ALB uses annotations to define which port to listen on:

```yaml
alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}]'
```

---

## ✅ 2. **Service**: Cluster access routing

A **Service (ClusterIP)** connects the Ingress to the right **Pod**. It listens on `port` and forwards to `targetPort` (which should match pod container port).

### Example:

```yaml
spec:
  ports:
    - name: http
      port: 80          # Service listens here
      targetPort: 8080  # Forwards to Pod container port
```

| Field        | Meaning                                               |
| ------------ | ----------------------------------------------------- |
| `port`       | Port exposed **inside the cluster** (used by Ingress) |
| `targetPort` | Actual port where the container listens               |

If you use `NodePort`, there’s also:

| Field      | Meaning                                              |
| ---------- | ---------------------------------------------------- |
| `nodePort` | External port on EC2 nodes (not needed with Ingress) |

---

## ✅ 3. **Pod / Container**: App runs here

The container in your pod exposes the **actual port** the app listens on — e.g., Argo CD usually listens on `8080`.

### Example:

```yaml
containers:
  - name: argocd-server
    image: ...
    ports:
      - containerPort: 8080
```

| Port   | Used for                             |
| ------ | ------------------------------------ |
| `8080` | Application server (internal to pod) |

---

## 🔍 Real-World Example: ArgoCD

| Layer   | Port                | Description                 |
| ------- | ------------------- | --------------------------- |
| Ingress | 80                  | HTTP from browser           |
| Service | 80                  | Exposes service for Ingress |
| Service | targetPort: 8080    | Forwards to app             |
| Pod     | containerPort: 8080 | ArgoCD HTTP server          |

---

## 🔁 Optional: HTTPS (Port 443)

If you add HTTPS support (ACM cert), then:

* ALB will listen on port `443`
* Traffic goes over TLS
* Still terminates at port `80` or `8080` in the pod, unless you enable mTLS

---

## ✅ Summary Table

| Layer   | Field         | Port   | Purpose                            |
| ------- | ------------- | ------ | ---------------------------------- |
| Ingress | listen-port   | 80/443 | Receives traffic from the internet |
| Service | port          | 80     | Forwards request to targetPort     |
| Service | targetPort    | 8080   | Points to the container’s port     |
| Pod     | containerPort | 8080   | The app listens on this            |

---

Would you like a diagram of this flow? Or YAML examples for each level?
