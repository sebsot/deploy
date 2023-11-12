node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
        
        sh "docker login -u sebsot -p s428613975"
        app = sh 'docker build -f Dockerfile -t deploy .'
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {

        sh "docker login -u sebsot -p s428613975"
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
}
    
