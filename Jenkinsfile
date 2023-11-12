node {

    stage('Git Clone'){
        git credentialsId: 'github_key', url: 'https://github.com/sebsot/deploy'
    }

    stage('Build Docker Image'){
        sh "docker build -t sebsot/deploy ."
    }

    stage('Push Docker Image') {
        withCredentials([string(credentialsId: 'DOCKER_HUB_CREDENTIALS', variable: 'DOCKER_HUB_CREDENTIALS')]) {
            sh "docker login -u sebsot -p ${DOCKER_HUB_CREDENTIALS}"
        }
        sh "docker push sebsot/deploy"
    }
    stage('Run Image'){
        withCredentials([string(credentialsId: 'DOCKER_HUB_CREDENTIALS', variable: 'DOCKER_HUB_CREDENTIALS')]) {
            sh "docker login -u sebsot -p ${DOCKER_HUB_CREDENTIALS}"
        }
        sh "docker run --rm -p 5000:5000 sebsot/deploy"
    }
}
    
