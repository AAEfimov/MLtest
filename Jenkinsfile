pipeline {
    agent { 
        dockerfile true
    }
    stages {
        stage('prepare_repo') {
                sh "python3 -m venv venv"
                sh ". venv/bin/activate"
                sh "pip3 install -r MLOps_UrFU/requirements.txt"
            }
        }
    post {
        success {
            setBuildStatus("Build succeeded", "SUCCESS");
        }
        failure {
            setBuildStatus("Build failed", "FAILURE");
        }
  }
}
