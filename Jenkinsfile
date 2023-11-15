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

                    def comandoRemoto = "cd $HOME && ls"

                    // Ejecutar el comando remoto con sshCommand
                    def resultadoRemoto = sshCommand remote: [
                        host: '192.168.229.129',
                        user: 'sebsot',
                        command: 'cd $HOME && ls'
                    ]
                    // kubectl get services | awk '{split(\$3, array, ":"); split(array[2], subarray, "/"); print subarray[1]}'

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
    
