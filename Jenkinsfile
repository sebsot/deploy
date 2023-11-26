node {
    def nombre_proyecto = 'deploy'
    def url_proyecto = 'https://github.com/sebsot/deploy'
    
    stage('Git Clone'){
        git credentialsId: 'github_key', url: url_proyecto
    }
/*
    
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

*/    
    stage('Deploy WebApp en Kubernetes'){
        withCredentials([string(credentialsId: 'IP_PRODUCCION', variable: 'IP_PRODU'), string(credentialsId: 'USER_PRODUCCION', variable: 'USER_PRODU'),string(credentialsId: 'USER_DOCKER', variable: 'USER_DOCKER')]) {

            def produccion = "${USER_PRODU}@${IP_PRODU}"
            

            // sh(script: "ssh ${produccion} 'minikube start'")
            // sh(script: "ssh ${produccion} 'kubectl delete service app db'")
            // sh(script: "ssh ${produccion} 'kubectl delete deployment app db'")


            // sh(script: "ssh ${produccion} 'kubectl create deployment deploy-proyecto-final --image=${USER_DOCKER}/${nombre_proyecto}'")
            // sh(script: "ssh ${produccion} 'kubectl expose deployment deploy-proyecto-final --port=5000 --type=LoadBalancer'")
            
             sh(script: "scp -r Kubernetes ${produccion}:/$HOME/prueba/deploy-final")
            def archivos = $(echo $HOME/prueba/deploy-final/Kubernetes/* | tr ' ' ',')
            
            sh(script: "ssh ${produccion} 'kubectl apply -f ${archivos}'") 
            
            // sleep(time:10, unit: "SECONDS")
            // sh(script: "ssh ${produccion} 'minikube service app --url'")
        

            def minikubeIp = sh(script:"ssh ${produccion} 'minikube ip'", returnStdout: true).trim()
            def puerto = sh(script:"ssh ${produccion} 'kubectl get service deploy-proyecto-final --output='jsonpath={.spec.ports[0].nodePort}' --namespace=default'", returnStdout: true).trim()

            // sh(script: "echo ssh -L 192.168.192.130:${puerto}:${minikubeIp}:${puerto}")

        }
    }
}
