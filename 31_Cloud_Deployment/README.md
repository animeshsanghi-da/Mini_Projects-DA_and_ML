# Project 31: ML Model Cloud Deployment (GCP)

This project demonstrates the MLOps pipeline for deploying containerized Machine Learning applications to production environments using Google Cloud Platform (GCP).

## Overview
Moving a model from a local notebook to a production cloud environment is a critical skill for any Data Scientist or Data Analyst. This project uses **Cloud Build** and **Cloud Run** to automate the containerization and deployment lifecycle.

## Key Files
* **cloud_config.yaml**: Defines the automated CI/CD pipeline steps (Build -> Push -> Deploy) using Artifact Registry.
* **deployment_guide.txt**: A step-by-step technical manual for configuring your local environment and executing the cloud deployment.

## Technical Workflow
1.  **Dockerization**: The application is wrapped into a lightweight container using a `Dockerfile`.
2.  **Continuous Integration (CI)**: `cloud_config.yaml` automates the image creation process in the cloud.
3.  **Continuous Deployment (CD)**: The resulting image is pushed to the Google Artifact Registry and deployed to a scalable, serverless Cloud Run instance.
4.  **Secrets Management**: Sensitive data (API Keys, Database URLs) are injected via Secrets Manager, ensuring no hardcoded values are committed.

## Prerequisites
* Active Google Cloud Platform (GCP) Account.
* Google Cloud SDK (gcloud) installed and configured.
* Docker installed locally for testing.
* Secrets Manager configured for secure environment variable injection.

## How to Deploy
1. Ensure you have your `Dockerfile` and `requirements.txt` ready in your project root.
2. Authenticate with your GCP account:
```bash
gcloud auth login
gcloud config set project [YOUR_PROJECT_ID]
```
3. Trigger the automated deployment:
```bash
gcloud builds submit --config cloud_config.yaml .
```

## Future Enhancements
* Integrate with GitHub Actions for automated triggers on git push.
* Add Terraform files for Infrastructure as Code (IaC) management.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License
This project is open-source and free to use.