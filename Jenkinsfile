pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "tmt-monitor:${env.BUILD_NUMBER}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
        stage('K8s Health Check') {
            steps {
                sh "kubectl diff -f k8s-deployment.yaml || true"
            }
        }
        stage('Deploy to Prod') {
            steps {
                echo "Deploying to MTA Cloud Infrastructure..."
                // sh "kubectl apply -f k8s-deployment.yaml"
            }
        }
    }
}