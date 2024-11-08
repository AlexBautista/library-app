pipeline {
    agent any
stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/AlexBautista/library-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("balat2020/library-app:latest")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying Kubernetes Cluster"
		/*kubernetesDeploy configs: 'deployment.yaml', kubeconfigId: 'kubeconfig-id'*/
            }
        }
    }
}
