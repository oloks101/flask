pipeline {
  agent any
  stages {
    stage('Git') {
      steps {
        git(url: 'https://github.com/oloks101/flask.git', branch: 'main')
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t oloks101/flask_app .'
      }
    }

    stage('Docker Login') {
      steps {
        sh 'docker login -u oloks101 -p dckr_pat_vM9bUZtMTTRuLQ572KCAMw3mpWo'
      }
    }

    stage('Docker push') {
      steps {
        sh 'docker push oloks101/flask_app'
      }
    }

  }
}