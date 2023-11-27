pipeline {
    
    agent any
    
    environment{
        NOMBRE_IMG = "py-flask-mysql"
    }
    
    stages {
        stage('Git Clone'){
            steps {
                git credentialsId: 'GIT_CREDENTIALS', url: 'https://github.com/GerLechner/deploy-final'
            }
        }
    
        stage('test de la imagen') {
            steps {
                
                sh "docker-compose up -d --build"
                sleep(time:15, unit: "SECONDS")
            
                sh "docker exec flask-app-container python tests.py"
                
                sh "docker stop flask-app-container"
                sh "docker stop flask-app-db-container"
                
                sh "docker rm flask-app-container"
                sh "docker rm flask-app-db-container"

            }
        }
        
        stage('SonarQube Analysis') {
            steps{
                script{
                sh "docker start sonarqube"
                sleep(time:60, unit: "SECONDS")
                withCredentials([string(credentialsId: 'USER_SONARQUBE', variable: 'USER_SONARQUBE'), string(credentialsId: 'PASS_SONARQUBE', variable: 'PASS_SONARQUBE')]){
                        def scannerHome = tool name: 'sonarscanner'
                        withSonarQubeEnv('SonarQube') {
                                sh "${scannerHome}/bin/sonar-scanner -Dsonar.login=${USER_SONARQUBE} -Dsonar.password=${PASS_SONARQUBE}"
                                        }
                                }
                        }
                }
        }
        stage('Build Docker Image'){
            steps {
                sh "docker-compose build"
            }
        }
    
    
    
       stage('Push Docker Image') {
           steps {
                withCredentials([string(credentialsId: 'USER_DOCKER', variable: 'USER_DOCKER'), string(credentialsId: 'PASS_DOCKER', variable: 'PASS_DOCKER')]) {
                    sh "docker login -u ${USER_DOCKER} -p ${PASS_DOCKER}"
                    sh "docker push ${USER_DOCKER}/flask-app"
                }
            }
       }

        
        stage('Deploy Kubernetes'){
            steps {
                script {
                    withCredentials([string(credentialsId: 'IP_PRODUCCION', variable: 'IP_PRODU'), string(credentialsId: 'USER_PRODUCCION', variable: 'USER_PRODU')]) 
                    {
            
                        def produccion = "${USER_PRODU}@${IP_PRODU}"
                        def infra =
                        sh "mkdir -p /$HOME/deploy-final"
                        sh "scp -r Kubernetes ${produccion}:/$HOME/deploy-final"
                        sh "ssh ${produccion} 'kubectl apply -f \$(printf \"%s,\" $HOME/deploy-final/*.yaml | sed \"s/,\$//\")'"
                        sleep(time:4, unit: "SECONDS")
                        sh "ssh ${produccion} 'minikube service app --url'"
            
                        
                        def minikubeIp = sh(script:"ssh ${produccion} 'minikube ip'", returnStdout: true).trim()
                        def puerto = sh(script:"ssh ${produccion} 'kubectl get service app --output='jsonpath={.spec.ports[0].nodePort}' --namespace=default'", returnStdout: true).trim()
                        
                        sh(script: "echo ssh -L 192.168.229.134:${puerto}:${minikubeIp}:${puerto}")
                        
                        //sh "ssh ${produccion} 'kubectl delete deployments,services app db'" 
                        
                        sh "ssh ${produccion} 'rm /$HOME/deploy-final/*.yaml'"
                        sh "ssh ${produccion} 'rmdir /$HOME/deploy-final'"
                    }
                }
            }
        }
    }
}














/*
 node {
    def nombre_proyecto = 'deploy'
    def url_proyecto = 'https://github.com/sebsot/deploy'
    
    stage('Git Clone'){
        git credentialsId: 'github_key', url: url_proyecto
    }

    
    stage('SonarQube Analysis') {
        sh "docker start sonarqube"
        sleep(time:60, unit: "SECONDS")
        withCredentials([string(credentialsId: 'USER_SONARQUBE', variable: 'USER_SONARQUBE'), string(credentialsId: 'PASS_SONARQUBE', variable: 'PASS_SONARQUBE')]){
            def scannerHome = tool name: 'sonarscanner'
            withSonarQubeEnv('SonarQube') {
                    sh "${scannerHome}/bin/sonar-scanner -Dsonar.login=${USER_SONARQUBE} -Dsonar.password=${PASS_SONARQUBE}"
            }
        }
    }
    
    
    stage('Build Docker Image'){
        withCredentials([string(credentialsId: 'USER_DOCKER', variable: 'USER_DOCKER')]){
            sh "docker build -t ${USER_DOCKER}/${nombre_proyecto} ."
        }
    }

    
    stage('Push Docker Image') {
        withCredentials([string(credentialsId: 'USER_DOCKER', variable: 'USER_DOCKER'), string(credentialsId: 'PASS_DOCKER', variable: 'PASS_DOCKER')]) {
            sh "docker login -u ${USER_DOCKER} -p ${PASS_DOCKER}"
            sh "docker push ${USER_DOCKER}/${nombre_proyecto}"
        }

    }

  
    stage('Deploy WebApp en Kubernetes'){
        withCredentials([string(credentialsId: 'IP_PRODUCCION', variable: 'IP_PRODU'), string(credentialsId: 'USER_PRODUCCION', variable: 'USER_PRODU'),string(credentialsId: 'USER_DOCKER', variable: 'USER_DOCKER')]) {

            def produccion = "${USER_PRODU}@${IP_PRODU}"
            

            // sh(script: "ssh ${produccion} 'minikube start'")
            // sh(script: "ssh ${produccion} 'kubectl delete service app db'")
            // sh(script: "ssh ${produccion} 'kubectl delete deployment app db'")


            // sh(script: "ssh ${produccion} 'kubectl create deployment deploy-proyecto-final --image=${USER_DOCKER}/${nombre_proyecto}'")
            // sh(script: "ssh ${produccion} 'kubectl expose deployment deploy-proyecto-final --port=5000 --type=LoadBalancer'")
            
             sh(script: "scp -r Kubernetes ${produccion}:/$HOME/prueba/deploy-final")
             // def archivos = "$(echo $HOME/prueba/deploy-final/Kubernetes/* | tr ' ' ',')"
            
            // sh(script: "ssh ${produccion} 'kubectl apply -f \$(echo $HOME/prueba/deploy-final/Kubernetes/* | tr ' ' ',')'") 
            sh(script: "ssh ${produccion} 'kubectl apply -f $HOME/prueba/deploy-final/Kubernetes/app-deployment.yaml,$HOME/prueba/deploy-final/Kubernetes/app-service.yaml,$HOME/prueba/deploy-final/Kubernetes/db-claim0-persistentvolumeclaim.yaml,$HOME/prueba/deploy-final/Kubernetes/db-claim1-persistentvolumeclaim.yaml,$HOME/prueba/deploy-final/Kubernetes/db-deployment.yaml,$HOME/prueba/deploy-final/Kubernetes/db-service.yaml'") 
            sleep(time:10, unit: "SECONDS")
            sh(script: "ssh ${produccion} 'minikube service app --url'")
        

            def minikubeIp = sh(script:"ssh ${produccion} 'minikube ip'", returnStdout: true).trim()
            def puerto = sh(script:"ssh ${produccion} 'kubectl get service app --output='jsonpath={.spec.ports[0].nodePort}' --namespace=default'", returnStdout: true).trim()

             sh(script: "echo ssh -L 192.168.192.134:${puerto}:${minikubeIp}:${puerto}")

        }
    }
}
*/
