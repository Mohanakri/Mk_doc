Got it — here’s your content reformatted fully in **Markdown** with MkDocs Material–style `??? question` dropdowns, no stray formatting issues:

```markdown
# AWS Direct Connect Projects – Complete Hands-on Collection

## 📚 Table of Contents

### Beginner Direct Connect Projects
### Intermediate Direct Connect Projects
### Advanced Direct Connect Projects

---

## 🟢 Beginner Direct Connect Projects

??? question "Q1: Simulated Direct Connect with VPN (Lab Environment)"
    **Goal:** Understand Direct Connect concepts by simulating it using AWS Site-to-Site VPN.  
    **Steps:**  
    1. Create two VPCs (one as AWS cloud, one as simulated on-prem).  
    2. Use a Site-to-Site VPN connection between them.  
    3. Configure routing to allow traffic between the networks.  
    4. Test connectivity with ping and SSH.  

    **Teaches:** Direct Connect fundamentals, routing concepts, lab simulation.  

---

??? question "Q2: Create a Direct Connect Virtual Interface (VIF) – Console Walkthrough"
    **Goal:** Learn the process of creating a Virtual Interface in AWS.  
    **Steps:**  
    1. Go to AWS Direct Connect console.  
    2. Choose “Create Virtual Interface”.  
    3. Select public or private VIF type.  
    4. Review VLAN, BGP ASN, and connection details.  

    **Teaches:** Direct Connect terminology, VIF creation process.  

---

??? question "Q3: Public VIF to Access AWS Services"
    **Goal:** Access AWS public endpoints via a Public Virtual Interface.  
    **Steps:**  
    1. Request a Direct Connect connection from AWS (or partner).  
    2. Create a Public VIF and link it to your AWS account.  
    3. Configure router BGP sessions to advertise AWS public prefixes.  
    4. Test access to AWS public services without internet.  

    **Teaches:** Public VIF, BGP routing basics.  

---

??? question "Q4: Private VIF to Access a Single VPC"
    **Goal:** Establish a private link to your VPC using Direct Connect.  
    **Steps:**  
    1. Request Direct Connect link from AWS.  
    2. Create a Private VIF mapped to your VPC.  
    3. Configure router settings (VLAN, BGP ASN).  
    4. Test private IP access from on-prem.  

    **Teaches:** Private VIF setup, VLAN/BGP configuration.  

---

## 🟡 Intermediate Direct Connect Projects

??? question "Q1: Direct Connect with AWS Transit Gateway"
    **Goal:** Connect multiple VPCs through a single Direct Connect link using Transit Gateway.  
    **Steps:**  
    1. Create a Transit Gateway and attach multiple VPCs.  
    2. Create a Direct Connect Gateway.  
    3. Associate the Direct Connect Gateway with Transit Gateway.  
    4. Test routing between on-prem and all VPCs.  

    **Teaches:** TGW + Direct Connect integration, hub-and-spoke design.  

---

??? question "Q2: High Availability with Redundant Direct Connect Links"
    **Goal:** Build a fault-tolerant Direct Connect setup.  
    **Steps:**  
    1. Request two physical Direct Connect connections in different locations.  
    2. Configure BGP on both links with failover settings.  
    3. Test failover by disabling one connection.  

    **Teaches:** Redundancy, failover routing.  

---

??? question "Q3: Direct Connect + VPN Backup (Hybrid Failover)"
    **Goal:** Use VPN as a backup for Direct Connect link.  
    **Steps:**  
    1. Create a Direct Connect link with a Private VIF.  
    2. Create a Site-to-Site VPN connection to the same VPC.  
    3. Configure routing so Direct Connect is primary, VPN is secondary.  
    4. Test failover.  

    **Teaches:** Hybrid redundancy, route priority.  

---

??? question "Q4: Public + Private VIF on Same Connection"
    **Goal:** Use one Direct Connect link to access AWS public services and private VPC resources.  
    **Steps:**  
    1. Create a Direct Connect connection.  
    2. Configure a Public VIF for AWS services.  
    3. Configure a Private VIF for VPC access.  
    4. Test both paths separately.  

    **Teaches:** Multi-VIF setup, shared physical link.  

---

## 🔴 Advanced Direct Connect Projects

??? question "Q1: Multi-Account Direct Connect with AWS RAM"
    **Goal:** Share a Direct Connect connection across multiple AWS accounts.  
    **Steps:**  
    1. Create a Direct Connect Gateway in Account A.  
    2. Share it via AWS Resource Access Manager (RAM) with other accounts.  
    3. Associate other accounts’ VPCs or TGWs to the shared gateway.  
    4. Test connectivity from all accounts.  

    **Teaches:** Cross-account Direct Connect sharing.  

---

??? question "Q2: Direct Connect with MPLS Integration"
    **Goal:** Integrate Direct Connect with existing MPLS WAN.  
    **Steps:**  
    1. Work with network provider to extend MPLS to AWS Direct Connect location.  
    2. Configure BGP between MPLS edge router and AWS.  
    3. Advertise AWS and on-prem routes.  
    4. Test routing across MPLS + AWS.  

    **Teaches:** Enterprise network integration, hybrid routing.  

---

??? question "Q3: Direct Connect for Multi-Region VPC Connectivity"
    **Goal:** Connect on-prem to multiple AWS regions via Direct Connect Gateway.  
    **Steps:**  
    1. Create a Direct Connect Gateway.  
    2. Associate VPCs from multiple regions.  
    3. Configure BGP to advertise all regional prefixes.  
    4. Test latency and connectivity.  

    **Teaches:** Multi-region private connectivity.  

---

??? question "Q4: Direct Connect Monitoring and Alarming"
    **Goal:** Monitor Direct Connect link health and set up alerts.  
    **Steps:**  
    1. Enable CloudWatch metrics for Direct Connect.  
    2. Create dashboards for BGP status, throughput, errors.  
    3. Set CloudWatch alarms for link down events.  
    4. Test by simulating link failure.  

    **Teaches:** Monitoring, alerting for Direct Connect.  

---

??? question "Q5: Programmatic Direct Connect Configuration via AWS CLI"
   ```
    **Goal:** Automate Direct Connect setup using AWS CLI.  
    **Steps:**  
    1. Use `aws directconnect create-connection` to request a connection.  
    2. Use CLI to create VIFs and gateways.  
    3. Store configuration scripts in Git for re-use.  

    **Teaches:** Infrastructure automation for Direct Connect.  
    ```

---

This version will work directly in **MkDocs Material** and produce collapsible Q\&A-style sections.
If you want, I can also make a **Beginner “Simulated Lab” MkDocs page** so you can test all beginner DX projects without an actual Direct Connect link. That would make your docs fully runnable in a training environment.

Do you want me to prepare that simulation-friendly version next?
