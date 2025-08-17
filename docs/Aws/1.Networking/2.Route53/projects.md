Got it ✅
Here’s your **AWS Route 53 Projects – Complete Hands-on Collection** converted into the **MkDocs Material** style with `??? question` dropdowns, grouped as **Basic / Intermediate / Advanced** — exactly like the VPC example.

---

# AWS Route 53 Projects – Complete Hands-on Collection

## 📚 Table of Contents

### Basic Route 53 Projects

### Intermediate Route 53 Projects

### Advanced Route 53 Projects

---

## 🟢 Basic Route 53 Projects

??? question "Q1: Domain Registration & Basic A Record"

````
```
**Goal:** Register a domain, create a public hosted zone, and point it to an EC2 instance.
**Steps:**
1. Register a domain in Route 53 (or use an existing one from another registrar).
2. Create a Public Hosted Zone for the domain.
3. Add an A record pointing to your EC2 public IP.
4. Test the domain in a browser.

**Teaches:** Hosted zones, DNS record basics.
```
````

??? question "Q2: Subdomain Delegation"

````
```
**Goal:** Create and delegate a subdomain to a separate hosted zone.
**Steps:**
1. In your main hosted zone, create a subdomain (e.g., dev.example.com).
2. Create a hosted zone for that subdomain.
3. Copy the NS records from the subdomain zone into the parent zone.
4. Verify subdomain DNS resolution.

**Teaches:** Subdomain delegation, DNS hierarchy.
```
````

??? question "Q3: CNAME to External Service"

````
```
**Goal:** Point a subdomain to an external service using a CNAME.
**Steps:**
1. Create a CNAME record for app.example.com.
2. Point it to the external service’s hostname (e.g., GitHub Pages, Netlify).
3. Test access via the new domain.

**Teaches:** CNAME usage, alias record differences.
```
````

??? question "Q4: Simple MX Records for Email"

````
```
**Goal:** Set up MX records for custom email hosting.
**Steps:**
1. Sign up for an email service (Amazon WorkMail, Google Workspace, etc.).
2. Obtain the MX record values.
3. Add MX records in Route 53 hosted zone.
4. Verify by sending/receiving email.

**Teaches:** Email routing via MX records.
```
````

---

## 🟡 Intermediate Route 53 Projects

??? question "Q1: Simple Failover Routing"

````
```
**Goal:** Configure failover DNS between two EC2 instances in different regions.
**Steps:**
1. Launch EC2 instances in two different regions.
2. Create a health check for the primary instance.
3. Create a failover routing policy — primary (active), secondary (passive).
4. Test failover by stopping the primary instance.

**Teaches:** Health checks, failover routing policy.
```
````

??? question "Q2: Weighted Routing for Blue/Green Deployment"

````
```
**Goal:** Distribute traffic between two app versions.
**Steps:**
1. Deploy "blue" and "green" app versions on separate endpoints.
2. Create weighted routing records: blue (80%), green (20%).
3. Test traffic distribution using multiple requests.

**Teaches:** Weighted routing, gradual rollout strategy.
```
````

??? question "Q3: Latency-Based Routing"

````
```
**Goal:** Serve users from the lowest-latency AWS region.
**Steps:**
1. Launch EC2 instances in two or more regions.
2. Create latency-based routing records.
3. Test using clients from different geographic locations.

**Teaches:** Geographically optimized DNS responses.
```
````

??? question "Q4: Private Hosted Zone + VPC Linking"

````
```
**Goal:** Resolve internal DNS names only within a VPC.
**Steps:**
1. Create a private hosted zone for internal.example.com.
2. Associate it with your VPC.
3. Add A records for internal services.
4. Test resolution from inside the VPC (not from public internet).

**Teaches:** Private hosted zones, VPC DNS association.
```
````

---

## 🔴 Advanced Route 53 Projects

??? question "Q1: Multi-Region Active-Active with Health Checks"

````
```
**Goal:** Deploy an active-active DNS setup for high availability.
**Steps:**
1. Deploy apps in two AWS regions.
2. Create health checks for both endpoints.
3. Use latency-based routing for best performance.
4. Test failover by stopping one region’s endpoint.

**Teaches:** Multi-region HA, latency + health check integration.
```
````

??? question "Q2: Route 53 Resolver for Hybrid Cloud"

````
```
**Goal:** Enable DNS resolution between AWS and on-premises.
**Steps:**
1. Connect on-prem to AWS via VPN or Direct Connect.
2. Set up Route 53 Resolver inbound/outbound endpoints.
3. Configure DNS rules for bidirectional name resolution.

**Teaches:** Hybrid DNS, Route 53 Resolver.
```
````

??? question "Q3: Geolocation Routing for Regional Services"

````
```
**Goal:** Serve region-specific content using geolocation routing.
**Steps:**
1. Deploy EC2 instances for different countries/regions.
2. Create geolocation routing policies (e.g., India → Mumbai EC2, US → Virginia EC2).
3. Test from different IP locations.

**Teaches:** Geolocation-based routing for compliance & localization.
```
````

??? question "Q4: Disaster Recovery DNS Switch"

````
```
**Goal:** Automate DNS failover with CloudWatch + Lambda.
**Steps:**
1. Set primary workload in one region, backup in another.
2. Create CloudWatch alarm to detect primary failure.
3. Use Lambda to call Route 53 API and update DNS records.

**Teaches:** Programmatic DNS updates via API, disaster recovery.
```
````

??? question "Q5: Multi-Account Private DNS Setup"

````
```
**Goal:** Share a private hosted zone across AWS accounts.
**Steps:**
1. Create a private hosted zone in Account A.
2. Share it via AWS Resource Access Manager (RAM) with Account B.
3. Associate both accounts’ VPCs with the hosted zone.

**Teaches:** Cross-account private DNS design.
```
````

---

If you want, I can now prepare a **full step-by-step with AWS Console screenshots** for **Basic Route 53 Projects** so you can follow and record them like a lab manual.
That would make it ready for **MkDocs site deployment**.
