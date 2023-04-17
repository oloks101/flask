pipeline {
  environment {
    registry = 'oloks101/flask_app'
    registryCredentials = 'docker'
    cluster_name = 'skillstorm'
  }
  agent any
  stages {
    stage('Git') {
      steps {
        git(url: 'https://github.com/oloks101/flask.git', branch: 'main')
      }
    }

stage('Build Stage') {
    steps {
        script {
            dockerImage = docker.build(registry)
        }
      }
    }

stage('Deploy Stage') {
    steps {
        script {
          docker.withRegistry('', registryCredentials) {
                dockerImage.push()  
          }
        }
    }
}