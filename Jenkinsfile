node {

    stage('Git Clone'){
        git credentialsId: 'github_key', url: 'https://github.com/sebsot/deploy'
    }

    stage('Build Docker Image'){
        sh "docker build -t sebsot/deploy ."
    }

    stage('run'){
        sh 'docker login -u sebsot -p s428613975'
        sh 'docker run --rm -p 5000:5000 deploy'
    }
}
    
