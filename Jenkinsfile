node {

    stage('Git Clone'){
        git credentialsId: 'github_key', url: 'https://github.com/sebsot/deploy'
    }
/*
    stage('Build Docker Image'){
        sh "docker build -t sebsot/deploy ."
    }

    stage('Push Docker Image') {
        withCredentials([string(credentialsId: 'DOCKER_HUB_CREDENTIALS', variable: 'DOCKER_HUB_CREDENTIALS')]) {
            sh "docker login -u sebsot -p ${DOCKER_HUB_CREDENTIALS}"
        }
        sh "docker push sebsot/deploy"
    }
    */
    stage('Deploy App in K8S'){

                script {
                    // Configurar la conexión SSH
                    
                        def remote = [:]
                        remote.name = 'test'
                        remote.host = '192.168.229.129'
                        remote.user = 'sebsot'
                        remote.password = 'sebsot'
                        remote.allowAnyHosts = true

                        def palabraBuscar = 'primerdeploy'
                        def resultadoRemoto = sshCommand remote: remote, returnStatus: false, command: """kubectl get services | awk '\$1 == "${palabraBuscar}" {split(\$5, array, ":"); split(array[2], subarray, "/"); print subarray[1]}'"""
                    
                    //"kubectl get services | awk '{split(\$5, array, \":\"); split(array[2], subarray, \"/\"); print subarray[1]}'"
                    
                    

                    // Imprimir el resultado
                    echo "Resultado remoto:"
                    echo "${resultadoRemoto}"
            }

        /*
        sh "ssh sebsot@192.168.229.129 'kubectl get services | awk '{split(\$3, array, ":"); split(array[2], subarray, "/"); print subarray[1]}''"
        
        environment{
            env.PUERTO = sh "ssh sebsot@192.168.229.129 'kubectl get services | awk '{split($campo, array, ":"); split(array[2], subarray, "/"); print subarray[1]}''"
        }
        echo "El valor actual de PUERTO es: ${env.PUERTO}"
    */
    }
}
    
