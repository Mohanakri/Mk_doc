Got it — you want the **AWS VPC projects** in a **MkDocs Material format** with dropdowns (`??? question`) for each project, grouped under **Basic / Intermediate / Advanced**, and each dropdown containing the step-by-step outline.

Here’s how it would look:

---

# AWS VPC Projects – Complete Hands-on Collection

## 📚 Table of Contents

### Basic VPC Projects

### Intermediate VPC Projects

### Advanced VPC Projects

---

## 🟢 Basic VPC Projects

??? question "Q1: Single Public Subnet + EC2 Web Server"


    ```
    **Goal:** Create a VPC with 1 public subnet and host a simple NGINX web server.
    **Steps:**
    1. Create a VPC (CIDR: `10.0.0.0/16`).
    2. Add 1 Public Subnet (`10.0.1.0/24`).
    3. Create an Internet Gateway & attach to the VPC.
    4. Update Route Table: `0.0.0.0/0` → IGW.
    5. Launch EC2 with public IP in the public subnet.
    6. Install NGINX and verify via browser.

    **Teaches:** VPC creation, IGW, route tables, security groups.
    ```

??? question "Q2: Two Public Subnets Across AZs (HA Ready)"
**Goal:** Build a highly available setup with 2 public subnets in different AZs.

    ```
    **Goal:** Build a highly available setup with 2 public subnets in different AZs.
    **Steps:**
    1. Create VPC (`10.0.0.0/16`).
    2. Add two public subnets in different AZs.
    3. Attach IGW & update route table.
    4. Launch EC2 instances in both subnets.
    5. Create an ELB to balance traffic.

    **Teaches:** Multi-AZ networking, ELB setup.
    ```

??? question "Q3: Private Subnet + Bastion Host"


    ```
    **Goal:** Access private EC2 only through a bastion host.
    **Steps:**
    1. Create a public subnet + private subnet.
    2. Launch Bastion EC2 in public subnet.
    3. Launch Private EC2 in private subnet.
    4. Configure SG to allow SSH only from Bastion.
    5. Test SSH hop through Bastion.

    **Teaches:** Private subnet isolation, bastion host pattern.
    ```

??? question "Q4: Static Website Hosting via S3 + VPC Gateway Endpoint"


    ```
    **Goal:** Access S3 privately from inside the VPC.
    **Steps:**
    1. Create VPC with public subnet & EC2.
    2. Create S3 bucket with static website hosting.
    3. Add VPC Gateway Endpoint for S3.
    4. Test EC2 → S3 access without internet.

    **Teaches:** Gateway endpoints, private AWS service access.
    ```

---

## 🟡 Intermediate VPC Projects

??? question "Q1: Public + Private Subnets with NAT Gateway"


    ```
    **Goal:** Enable private EC2 instances to reach internet via NAT Gateway.
    **Steps:**
    1. Create two public + two private subnets (multi-AZ).
    2. Deploy NAT GW in each AZ.
    3. Configure private route table: `0.0.0.0/0` → NAT GW.
    4. Test internet access from private EC2.

    **Teaches:** NAT GW, private egress routing.
    ```

??? question "Q2: Three-Tier Architecture (Web, App, DB)"


    ```
    **Goal:** Deploy a secure 3-layer VPC design.
    **Steps:**
    1. Public subnets → Web servers.
    2. Private subnets → App servers.
    3. Isolated subnets → RDS DB.
    4. SG rules to allow only layer-to-layer communication.

    **Teaches:** Layered security, subnet segregation.
    ```

??? question "Q3: Private Subnets with Interface Endpoints"


    ```
    **Goal:** Access AWS services from private subnets without internet.
    **Steps:**
    1. Create VPC with private subnets.
    2. Create Interface Endpoints for SSM, DynamoDB.
    3. Remove internet route from private subnets.
    4. Test access from private EC2.

    **Teaches:** Interface & Gateway endpoints.
    ```

??? question "Q4: Hybrid Connectivity via Site-to-Site VPN"


    ```
    **Goal:** Connect AWS VPC to on-prem (simulated with another AWS VPC).
    **Steps:**
    1. Create VPC A (AWS) and VPC B (simulated on-prem).
    2. Deploy Virtual Private Gateway in VPC A.
    3. Deploy Customer Gateway in VPC B.
    4. Establish Site-to-Site VPN.

    **Teaches:** VPN, VGW, CGW.
    ```

---

## 🔴 Advanced VPC Projects

??? question "Q1: Multi-VPC Peering Setup"


    ```
    **Goal:** Connect 3 VPCs (prod, dev, shared services) using peering.
    **Steps:**
    1. Create 3 VPCs.
    2. Peer shared services VPC with prod & dev.
    3. Update route tables accordingly.
    4. Test DNS resolution.

    **Teaches:** Peering, routing, DNS.
    ```

??? question "Q2: Transit Gateway Hub-and-Spoke"


    ```
    **Goal:** Centralize routing for multiple VPCs.
    **Steps:**
    1. Create TGW in central account.
    2. Attach multiple VPCs to TGW.
    3. Apply TGW route table segmentation.

    **Teaches:** Scalable inter-VPC networking.
    ```

??? question "Q3: PrivateLink Service Publishing"


    ```
    **Goal:** Share a private service across accounts.
    **Steps:**
    1. Provider VPC hosts NLB & API.
    2. Publish via PrivateLink endpoint service.
    3. Consumer creates Interface Endpoint to connect.

    **Teaches:** Private service sharing.
    ```

??? question "Q4: Centralized Logging & Flow Logs"

    ```
    **Goal:** Aggregate VPC Flow Logs from multiple accounts.
    **Steps:**
    1. Create central S3 bucket.
    2. Enable Flow Logs in all VPCs.
    3. Grant cross-account S3 permissions.
    4. Query logs with Athena.

    **Teaches:** Flow logs, log analysis.
    ```

??? question "Q5: Inspection VPC with AWS Network Firewall"
**Goal:** Filter all VPC traffic through a firewall.

    ```
    **Goal:** Filter all VPC traffic through a firewall.
    **Steps:**
    1. Create dedicated firewall VPC.
    2. Deploy AWS Network Firewall.
    3. Route all egress/ingress traffic via firewall VPC.

    **Teaches:** L3/L4/L7 inspection, advanced routing.
    ```

---

If you want, I can now **add code blocks inside each dropdown for Terraform & AWS CLI commands** so you can run them directly while following the guide. That way it’s a ready-to-use **MkDocs lab manual**.
