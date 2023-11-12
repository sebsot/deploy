node {

    stage('Git Clone'){
        git credentialsId: 'github_key', url: 'https://github.com/sebsot/deploy'
    }

    stage('Build Docker Image'){
        sh "docker build -t sebsot/deploy ."
    }

    stage('Push Docker Image') {
        withCredentials([string(credentialsId: 'DOCKER_CREDENTIALS', variable: 'DOCKER_CREDENTIALS')]) {
            sh "docker login -u sebsot -p ${DOCKER_CREDENTIALS}"
        }
        sh "docker push sebsot/deploy"
    }
}
}
    
