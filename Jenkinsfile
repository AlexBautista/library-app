pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/main']],
                    extensions: [], userRemoteConfigs: [[credentialsId: 'github-jenkins', url: 'https://github.com/AlexBautista/library-app']]
                )
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
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying Kubernetes Cluster"
                /*kubernetesDeploy configs: 'deployment.yaml', kubeconfigId: 'kubeconfig-id'*/
                withKubeConfig(caCertificate: '', clusterName: 'minikube', contextName: 'minikube', credentialsId: 'my_kubernetes', namespace: '', restrictKubeConfigAccess: false, serverUrl: 'https://192.168.49.2:8443') {
                    sh "kubectl get ns"
                }
            }
        }
    }
