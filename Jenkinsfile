pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-hexagonal-api'
    }

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE, '-f Dockerfile .')
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.run()
                }
            }
        }
    }
}
