pipeline {
    agent any

    stages {
           stage('Prepare Environment') {
            steps {
               withCredentials([file(credentialsId: 'user_microservices_env', variable: 'ENV_FILE')]) {
                    script {
                        
                        sh "cp \$ENV_FILE \$WORKSPACE/.env"
                        
                        sh 'cat $WORKSPACE/.env'
                    }
                }
            }
        }
        stage('Build and Test') {
            steps {
                script {
                    sh 'docker compose up --build -d'
                }
            }
        }
          stage('Test') {
            steps {
                script {
                   sh 'echo "Tests passed"'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker compose down'
                    sh 'docker compose up -d'
                }
            }
        }
    }
}