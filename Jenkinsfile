node {
    def nombre_proyecto = 'deploy'
    def url_proyecto = 'https://github.com/sebsot/deploy'
    
    stage('Git Clone'){
        git credentialsId: 'github_key', url: url_proyecto
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
            

            sh(script: "ssh ${produccion} 'minikube start'")
            // sh(script: "ssh ${produccion} 'kubectl delete service deploy-proyecto-final'")
            // sh(script: "ssh ${produccion} 'kubectl delete deployment deploy-proyecto-final'")


            sh(script: "ssh ${produccion} 'kubectl create deployment deploy-proyecto-final --image=${USER_DOCKER}/${nombre_proyecto}'")
            sh(script: "ssh ${produccion} 'kubectl expose deployment deploy-proyecto-final --port=5000 --type=LoadBalancer'")
            

            // sleep(time:10, unit: "SECONDS")
            sh(script: "ssh ${produccion} 'minikube service deploy-proyecto-final --url'")


            def minikubeIp = sh(script:"ssh ${produccion} 'minikube ip'", returnStdout: true).trim()
            def puerto = sh(script:"ssh ${produccion} 'kubectl get service deploy-proyecto-final --output='jsonpath={.spec.ports[0].nodePort}' --namespace=default'", returnStdout: true).trim()

            // sh(script: "echo ssh -L 192.168.192.130:${puerto}:${minikubeIp}:${puerto}")

        }
    }
}
