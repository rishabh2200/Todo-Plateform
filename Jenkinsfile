pipeline {
    agent any
    environment {
        db_path='127.0.0.1'

        POSTGRES_DB='mydb'

        POSTGRES_USER='rishabh'

        POSTGRES_PASSWORD='rishabh'

        redis_path='redis://127.0.0.1:6379/'
        
        CORS_ORIGIN_WHITELIST='http://localhost:3000'
        
        PATH_TODO_PLATEFORM='/var/lib/jenkins/workspace/TodoWebAppDeploy'

    }
    stages {
        stage('test') {
            steps {
                git credentialsId: 'cff5313b-2c9f-4d48-9be4-5b51400e4338', url: 'git@code.jtg.tools:rishabh.bansal/todo_backend.git'
                sh '''#!/bin/bash
                export  SENDGRID_PASSWORD=$SENDGRID_PASSWORD
                cd $PATH_TODO_PLATEFORM/backend
                python3 manage.py test
                '''
            }
        }
        stage('Build') {
            steps {
                sh '''#!/bin/bash
                echo $SENDGRID_PASSWORD
                cd $PATH_TODO_PLATEFORM
                rm -rf backend.zip 
                pwd
                zip -r backend.zip backend/
                cd $PATH_TODO_PLATEFORM/ansible
                pwd
                ansible-playbook deploy.yml --key-file "/home/ubuntu1820/terraform/us_key/main-key.pem" --extra-vars "PATH_TODO_PLATEFORM=$PATH_TODO_PLATEFORM" 
                ansible-playbook docker.yml --key-file "/home/ubuntu1820/terraform/us_key/main-key.pem"
                '''
            }
        }
    }
    post {
       // only triggered when blue or green sign
       success {
          slackSend message: 'demo_react success'
       }
       // triggered when red sign
       failure {
           slackSend message: 'demo_react failure failure'
       }
    }
}
