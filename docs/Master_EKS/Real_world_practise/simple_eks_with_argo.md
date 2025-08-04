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

