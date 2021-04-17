pipeline {
    agent any
    environment {
        db_path = '127.0.0.1'
        POSTGRES_DB='mydb'
        POSTGRES_USER='rishabh'
        POSTGRES_PASSWORD='rishabh'
        redis_path='redis://127.0.0.1:6379/'
        CORS_ORIGIN_WHITELIST='http://localhost:3000'
        PATH_TODO_PLATEFORM='/var/lib/jenkins/workspace/TodoPlatformDeploy'
    }
    stages {
        stage('Build') {
            steps {
                git credentialsId: 'cff5313b-2c9f-4d48-9be4-5b51400e4338', url: 'git@code.jtg.tools:rishabh.bansal/todo-platform.git'
            }
        }
        stage('test') {
            steps {
                dir('backend'){
                    sh """#!/bin/bash
                        export  SENDGRID_PASSWORD=$SENDGRID_PASSWORD
                        python3 manage.py test
                    """
                }
            }
        }
        stage('Deploy') {
            steps {
                dir(''){
                    sh """#/bin/bash
                        rm -rf backend.zip 
                        zip -r backend.zip backend/
                    """
                }
                dir('ansible'){
                    sh """#/bin/bash
                        ansible-playbook deploy.yml --key-file "/home/ubuntu1820/terraform/us_key/main-key.pem" --extra-vars "PATH_TODO_PLATEFORM=$PATH_TODO_PLATEFORM" 
                        ansible-playbook todo-automation.yml --key-file "/home/ubuntu1820/terraform/us_key/main-key.pem" --extra-vars "OLD=$OLD NEW=$NEW"
                    """
                }
                
            }
        }
    }
    post {
       success {
          slackSend message: 'demo_react success'
       }
       failure {
           slackSend message: 'demo_react failure failure'
       }
    }
}
