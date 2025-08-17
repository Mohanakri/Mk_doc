Got it — here’s your **AWS CloudFront Projects – Complete Hands-on Collection** in **MkDocs Material** Markdown format with `??? question` dropdowns, grouped by **Beginner / Intermediate / Advanced** just like the Direct Connect one you gave me earlier.

---

# AWS CloudFront Projects – Complete Hands-on Collection

## 📚 Table of Contents

### Beginner CloudFront Projects

### Intermediate CloudFront Projects

### Advanced CloudFront Projects

---

## 🟢 Beginner CloudFront Projects

??? question "Q1: Simple S3 Static Website Distribution"

    ```markdown
    **Goal:** Serve a static website from an S3 bucket using CloudFront.  
    **Steps:**  
    1. Create an S3 bucket and upload static website files.  
    2. Enable static website hosting on the bucket.  
    3. Create a CloudFront distribution with the S3 bucket as the origin.  
    4. Test website access via the CloudFront domain.  

    **Teaches:** Basic CloudFront setup, S3 origin integration.
    ```

??? question "Q2: CloudFront with Custom Domain & SSL"

    ```markdown
    **Goal:** Serve content securely over HTTPS with a custom domain.  
    **Steps:**  
    1. Request an SSL/TLS certificate in AWS Certificate Manager (ACM).  
    2. Create a CloudFront distribution with the S3 origin.  
    3. Attach the custom domain and ACM certificate.  
    4. Update Route 53 to point the domain to CloudFront.  

    **Teaches:** HTTPS with CloudFront, custom domain setup.
    ```

??? question "Q3: Restrict S3 Access via Origin Access Control (OAC)"

    ```markdown
    **Goal:** Secure S3 bucket so it's only accessible through CloudFront.  
    **Steps:**  
    1. Create an S3 bucket and disable public access.  
    2. Create a CloudFront distribution with OAC enabled.  
    3. Update S3 bucket policy to allow access only from CloudFront.  
    4. Test that direct S3 URL access is blocked.  

    **Teaches:** S3 security with CloudFront, OAC usage.
    ```

??? question "Q4: Cache Behavior for File Types"

    ```markdown
    **Goal:** Set custom caching rules for different file types.  
    **Steps:**  
    1. Create CloudFront distribution for your S3 site.  
    2. Add separate cache behaviors for images, CSS, and HTML.  
    3. Configure TTLs (e.g., images → 30 days, HTML → 1 hour).  
    4. Test cache behavior changes.  

    **Teaches:** Cache behavior customization, TTL management.
    ```

---

## 🟡 Intermediate CloudFront Projects

??? question "Q1: CloudFront with EC2 as Origin"

    ```markdown
    **Goal:** Distribute content served from an EC2-hosted application.  
    **Steps:**  
    1. Launch EC2 with a web server (NGINX/Apache).  
    2. Create a CloudFront distribution with EC2 public DNS as the origin.  
    3. Configure caching and compression.  
    4. Test access through CloudFront.  

    **Teaches:** EC2 as CloudFront origin, caching dynamic content.
    ```

??? question "Q2: CloudFront Signed URLs for Private Content"

    ```markdown
    **Goal:** Restrict file downloads to authorized users only.  
    **Steps:**  
    1. Store files in S3.  
    2. Create CloudFront distribution with OAC enabled.  
    3. Enable signed URLs and generate them via AWS SDK or CLI.  
    4. Test access with valid/invalid signed URLs.  

    **Teaches:** Secure content delivery with signed URLs.
    ```

??? question "Q3: CloudFront Functions for URL Rewrites"

    ```markdown
    **Goal:** Rewrite incoming request paths at the edge.  
    **Steps:**  
    1. Create a CloudFront distribution.  
    2. Write a CloudFront Function to modify request paths.  
    3. Associate the function with the viewer request event.  
    4. Test rewriting behavior.  

    **Teaches:** Edge request manipulation using CloudFront Functions.
    ```

??? question "Q4: Multiple Origins + Path-Based Routing"

    ```markdown
    **Goal:** Serve different content paths from different origins.  
    **Steps:**  
    1. Create an S3 bucket (static assets) and an EC2 app (API).  
    2. Create a CloudFront distribution with both origins.  
    3. Configure path-based routing: `/api/*` → EC2, `/assets/*` → S3.  
    4. Test requests for both paths.  

    **Teaches:** Multi-origin CloudFront distribution, path-based rules.
    ```

---

## 🔴 Advanced CloudFront Projects

??? question "Q1: Live Video Streaming via CloudFront"

    ```markdown
    **Goal:** Deliver live video using CloudFront with Media Services.  
    **Steps:**  
    1. Set up AWS MediaLive or MediaPackage for video streaming.  
    2. Create a CloudFront distribution with MediaPackage as origin.  
    3. Enable caching and configure TTL for streaming chunks.  
    4. Test live stream playback.  

    **Teaches:** Streaming content delivery, low-latency CloudFront setup.
    ```

??? question "Q2: Lambda\@Edge for Advanced Authentication"

    ```markdown
    **Goal:** Add custom authentication logic at the edge.  
    **Steps:**  
    1. Create a CloudFront distribution for your app.  
    2. Write a Lambda@Edge function for viewer request authentication.  
    3. Deploy to US East (N. Virginia) region.  
    4. Test with valid and invalid tokens.  

    **Teaches:** Serverless edge authentication with Lambda@Edge.
    ```

??? question "Q3: Global Failover with Multiple Origins"

    ```markdown
    **Goal:** Serve content from the closest healthy origin.  
    **Steps:**  
    1. Deploy apps in two AWS regions.  
    2. Create a CloudFront distribution with both origins.  
    3. Enable origin failover.  
    4. Test failover by stopping one origin.  

    **Teaches:** Origin failover for high availability.
    ```

??? question "Q4: Real-Time CloudFront Metrics and Alarms"

    ```markdown
    **Goal:** Monitor CloudFront usage and performance.  
    **Steps:**  
    1. Enable real-time logs for the distribution.  
    2. Stream logs to Kinesis Data Stream.  
    3. Process logs with Lambda for analytics.  
    4. Create CloudWatch alarms for latency/errors.  

    **Teaches:** CloudFront observability and monitoring.
    ```

??? question "Q5: WAF Integration for Global Security"

    ```markdown
    **Goal:** Protect content with AWS WAF at the CloudFront edge.  
    **Steps:**  
    1. Create a WAF WebACL with rules (IP block, SQLi, XSS).  
    2. Associate WAF with CloudFront distribution.  
    3. Test blocked and allowed requests.  

    **Teaches:** Edge security, WAF + CloudFront integration.
    ```

---

If you want, I can also put your **Direct Connect** and **CloudFront** markdown into a **single MkDocs-ready project structure** so they’re instantly usable in your docs site with working dropdowns.
Would you like me to merge them like that?
