# Diamond Price Prediction Project

## Overview

Welcome to the Diamond Price Prediction project! This project leverages advanced machine learning techniques to predict diamond prices based on various features. The pipeline is built using Data Version Control (DVC), MLflow, and Dagshub for efficient version control, experiment tracking, and collaboration. Deployment is automated using GitHub Actions, AWS ECR, and AWS AppRunner for a seamless end-to-end solution.

## Key Components

1. **Linear Regression Model:**
   - A sophisticated linear regression model is developed to accurately predict diamond prices.

2. **DVC (Data Version Control):**
   - DVC is used to manage the dataset, providing versioning and change tracking capabilities.

3. **MLflow:**
   - MLflow is employed for experiment tracking, model packaging, and reproducibility.

4. **Dagshub:**
   - Dagshub facilitates collaboration by providing a platform for managing machine learning projects.

5. **GitHub Actions:**
   - CI/CD is achieved through GitHub Actions, automating testing, building, and deployment processes.

6. **AWS ECR (Elastic Container Registry):**
   - Docker containers are stored in AWS ECR, ensuring a centralized and scalable repository.

7. **AWS AppRunner:**
   - The model is deployed on AWS AppRunner, offering a fully managed and scalable serverless solution.

## Benefits

- **Scalability:** AWS AppRunner ensures the project can handle varying workloads with ease.
- **Collaboration:** Tools like DVC and Dagshub enhance collaboration among data scientists and developers.
- **Reproducibility:** Version control with DVC and experiment tracking with MLflow ensure the reproducibility of the entire machine learning workflow.
- **Automation:** GitHub Actions automate the testing and deployment process, reducing manual intervention.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository: `git clone [repository_url]`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the src/GemstonePricePrediction/pipelines/training_pipeline.py for training.
4. Run the src/GemstonePricePrediction/pipelines/prediction_pipeline.py for prediction.
## Contributing

We welcome contributions! If you'd like to contribute, please follow our [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to the open-source communities of DVC, MLflow, and Dagshub.
- Inspiration from the advancements in machine learning and cloud technologies.

Feel free to explore the project, contribute, and enjoy predicting diamond prices with our advanced model!
