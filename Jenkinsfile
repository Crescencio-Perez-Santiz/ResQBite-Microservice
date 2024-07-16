pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'api-payment'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker run -d -p 4242:4242 ${DOCKER_IMAGE}:latest'
                }
            }
        }
    }
}
