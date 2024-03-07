pipeline {
    // use Docker as agent
    agent {
        docker {
            // Docker file attached below. Image pushed to dockerhub
            image 'efimovaleksey/mlops:stable'
            args '-u root:sudo '
        }
    }

    stages {
        stage('prepare_repo') {
            steps {
                //sh "rm -rf MLOps_UrFU"
                //sh "git clone https://github.com/AAEfimov/MLOps_UrFU.git"
                sh "pwd"
                sh "python3 -m venv venv"
                sh ". venv/bin/activate"
                dir('MLOps_UrFU') {
                    sh "pip3 install -rrequirements.txt"
                }

                // Copy secret file to builddir
                withCredentials([file(credentialsId: 'kaggle_id', variable: 'kaggle_id')]) {
                    sh "cp \$kaggle_id $WORKSPACE/MLOps_UrFU"
                }
                
                dir('MLOps_UrFU') {
                    sh "ls -la"
                }
            }
        }
        
        stage('model_preprocession') {
             steps {
                dir('MLOps_UrFU') {
                    sh "pwd"
                    sh "./pipeline.sh model_preprocession"
                }
            }
        }
        
        stage('data_creation') {
             steps {
                dir('MLOps_UrFU') {
                    sh "pwd"
                    sh "./pipeline.sh data_creation"
                }
            }
        }
        
        stage('model_preparation') {
             steps {
                dir('MLOps_UrFU') {
                    sh "pwd"
                    sh "./pipeline.sh model_preparation"
                }
            }
        }
        
        stage('model_testing') {
             steps {
                dir('MLOps_UrFU') {
                    sh "pwd"
                    sh "./pipeline.sh model_testing"
                }
            }
        }
        
    }
}
