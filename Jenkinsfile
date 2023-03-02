pipeline {
    agent any
    
    stages {

        stage('Create directory') {
            steps {
                sh 'mkdir repo'
            }
        }
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Ajghumaliya/static-web-host-s3.git', dir: 'repo'
            }
        }
        
        stage('Build and package website') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }
        
        stage('Upload to S3 bucket') {
            steps {
                withAWS(region: 'ap-south-1', credentialsId: 'staticwebkey') {
                    s3Upload(bucket: 'advance-jenkins-pipeline-project-1', pathStyleAccess: true, workingDir: 'repo', fileSet: '**/*')
                }
            }
        }
    }
}
