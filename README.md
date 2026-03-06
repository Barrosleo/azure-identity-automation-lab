# Azure Identity Automation Lab

This repository demonstrates how common Azure Entra ID (Azure AD) identity operations can be automated using Python and Microsoft Graph.

The lab treats identity as infrastructure — a foundational concept for Cloud, Platform, and Security Engineers working in hybrid and cloud‑native environments.

---

## Scope and Objectives

This lab focuses on automating core identity lifecycle tasks that are commonly performed manually in enterprise environments. The goal is to demonstrate how these operations can be executed programmatically in a controlled, auditable, and repeatable way.

The repository is intentionally minimal and readable, prioritising clarity over complexity.

---

## Repository structure

```
azure-identity-automation-lab/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── scripts/
│   ├── auth.py
│   ├── create_users.py
│   ├── create_groups.py
│   ├── assign_group_membership.py
│   └── audit_identity_state.py
└── docs/
    ├── architecture.md
    └── security-notes.md
```

---

## What This Lab Demonstrates

- Programmatic creation of Azure Entra ID users
- Creation of security groups
- Assignment of users to groups
- Auditing of identity objects (users and groups)
- Secure authentication to Microsoft Graph using a service principal

All scripts are designed to be simple, explicit, and easy to reason about.

---

## Technologies Used

- Python 3
- Microsoft Graph API
- Azure Entra ID
- OAuth 2.0 (Client Credentials flow)

---

## Prerequisites

- An Azure tenant
- An Azure App Registration with the following Microsoft Graph permissions:
  - User.ReadWrite.All
  - Group.ReadWrite.All
- Python 3.9 or later

---

## Setup

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Barrosleo/azure-identity-automation-lab.git
cd azure-identity-automation-lab
pip install -r requirements.txt
```
Create a `.env` file using the provided `.env.example` template and populate it with your tenant ID, client ID, and client secret.

---

## Usage

Create users in Azure Entra ID:

```bash
python scripts/create_users.py
```

Create security groups:

```bash
python scripts/create_groups.py
```

Assign users to groups:

```bash
python scripts/assign_group_membership.py
```

Audit the current identity state:

```bash
python scripts/audit_identity_state.py
```

---

## Why This Matters

Identity is the control plane of the cloud. Automating identity operations reduces human error, improves security posture, and enables scalable platform operations.

This lab provides a practical foundation for more advanced identity automation scenarios, including Conditional Access policies, Privileged Identity Management workflows, and identity governance pipelines.

---

## Related Work

- **DefenderHunt** — Threat Hunting & Incident Response Toolkit  
- **Cloud Platform Engineer Roadmap** — Structured learning and lab progression
