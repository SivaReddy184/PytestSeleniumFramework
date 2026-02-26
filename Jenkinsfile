pipeline {
    agent any
    parameters {
        choice(name: 'BROWSER', choices: ['chrome', 'firefox', 'edge'], description: 'Select the browser for execution')
        // choice(name: 'ENVIRONMENT', choices: ['QA', 'UAT', 'PROD'], description: 'Select the Test Environment')
        // string(name: 'THREADS', defaultValue: '3', description: 'Number of parallel workers (xdist)')
    }

    // environment {
    //     // Define path to your virtual environment if needed
    //     //PATH = "C:\Users\ASUS\Desktop\Projects\PythonSeleniumFramework\.venv"
    // }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SivaReddy184/PytestSeleniumFramework.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Execute Tests') {
            steps {
                // Running in headless mode is mandatory for Jenkins
                bat "pytest -v -s -n 3 --browser ${params.BROWSER} --headless true --alluredir=reports/allure-results"
            }
        }
    }

    post {
        always {
            // This publishes the report even if tests fail
            allure includeProperties: false, jdk: '', results: [[path: 'reports/allure-results']]
        }
    }
}