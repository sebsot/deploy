node {

    stage('Git Clone'){
        git credentialsId: 'github_key', url: 'https://github.com/sebsot/deploy'
    }

    stage('Build Docker Image'){
        sh "docker build -t sebsot/deploy ."
    }
}
    
