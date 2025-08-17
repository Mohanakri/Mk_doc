Got it ✅
Here’s the **AWS Organizations** beginner, intermediate, and advanced projects in the same dropdown + fenced code block style you requested.

---

# AWS Organizations Projects – Beginner, Intermediate, Advanced

## 📚 Table of Contents

* Beginner Level Projects
* Intermediate Level Projects
* Advanced Level Projects

---

## 🟢 Beginner Level Projects

??? question "Q1: Create an AWS Organization and Add an Account"

```
1. Open AWS Organizations in the Management account.
2. Click **Create Organization** and choose "All Features".
3. From the console, select **Add account** → Create a new AWS account.
4. Provide email and account name, then create.
5. Verify new account creation from the Organizations dashboard.
```

??? question "Q2: Invite an Existing AWS Account to Your Organization"

```
1. In the AWS Organizations console, go to **Accounts**.
2. Click **Add account** → Invite an existing account.
3. Enter the AWS account ID or email.
4. The invited account owner must accept from their console.
5. Once accepted, verify the account appears under your organization.
```

??? question "Q3: Enable Consolidated Billing for All Accounts"

```
1. Ensure the organization is set to "All Features".
2. In the Management account, go to **Billing → Payment Methods**.
3. Set up a single payment method for all accounts.
4. Enable **Consolidated Billing** in AWS Organizations.
5. Verify from member accounts that billing is centralized.
```

---

## 🟡 Intermediate Level Projects

??? question "Q4: Create and Apply a Service Control Policy (SCP) to Restrict Regions"

```
1. Go to AWS Organizations → **Policies**.
2. Enable Service Control Policies if not already enabled.
3. Create a new SCP that denies actions in specific AWS regions.
4. Attach the SCP to a specific OU (Organizational Unit).
5. Test by trying to launch resources in the restricted region from a member account.
```

??? question "Q5: Organize Accounts into Multiple OUs"

```
1. In the Organizations console, go to **Organize accounts**.
2. Create OUs like "Prod", "Dev", "Sandbox".
3. Move accounts into the respective OUs.
4. Apply different SCPs for each OU (e.g., deny EC2 in Sandbox).
5. Verify policy enforcement in each account.
```

??? question "Q6: Enable AWS Single Sign-On (SSO) for Organization Accounts"

```
1. In AWS SSO, choose **Enable AWS SSO**.
2. Connect AWS SSO with your AWS Organization.
3. Create user groups like Admins, Developers, Auditors.
4. Assign SSO users/groups to member accounts with specific roles.
5. Test login for each role to confirm access control.
```

---

## 🔴 Advanced Level Projects

??? question "Q7: Automate AWS Account Creation with AWS CLI"

```
1. Install AWS CLI and configure with the Management account credentials.
2. Run:
   aws organizations create-account --email "newaccount@example.com" --account-name "NewAccountName"
3. Capture the `CreateAccountStatusId` and check creation status.
4. Assign the new account to an OU via CLI:
   aws organizations move-account --account-id <id> --source-parent-id <id> --destination-parent-id <id>
5. Apply default SCPs using CLI.
```

??? question "Q8: Cross-Account Role Setup Across Organization"

```
1. In the Management account, create an IAM role with trust policy for member accounts.
2. In each member account, create an IAM role allowing access from the Management account.
3. Use AWS CLI or SDK to assume roles:
   aws sts assume-role --role-arn arn:aws:iam::<member-account-id>:role/RoleName --role-session-name session
4. Automate role switching for operational tasks.
```

??? question "Q9: Automate OU and SCP Management with Terraform"

```
1. Define AWS Organizations resources in Terraform (aws_organizations_organization, aws_organizations_organizational_unit, aws_organizations_policy).
2. Create OUs, attach SCPs in code.
3. Run `terraform apply` to provision changes.
4. Modify policies or OU structure by updating code.
5. Use GitHub Actions to auto-apply Terraform changes on push.
```

---

If you want, I can also prepare **step-by-step AWS Control Tower projects** in the **same dropdown format** since it extends AWS Organizations for account governance. That would make the learning flow more real-world.
