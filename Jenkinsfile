node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
  
       app = sh 'docker build -f Dockerfile -t deploy .'
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        withCredentials([string(CredentialsId: 'DOCKER_HUB_CREDENTIALS', VARIABLE: 'DOCKER_HUB_CREDENTIALS')]) {
            sh "docker login -u sebsot -p ${DOCKER_HUB_CREDENTIALS}"
        }                
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
}
    
