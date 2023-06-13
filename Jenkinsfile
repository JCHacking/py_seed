pipeline {
    agent {
        label "python"
    }

    environment {
        venv = "${pwd()}/venv"
        venv_bin = "${venv}/bin"
    }

    stages {
        stage("DEPLOY"){
            steps{
                sh "python -m venv venv"
                withPythonEnv(venv_bin){
                    sh "pip install poetry"
                    sh "poetry install --with dev,tests,docs"
                    sh "poetry update --with dev,tests,docs"
                }
            }
        }

        stage("LINTER"){
            steps{
                parallel(
                    typing: {
                        withPythonEnv(venv_bin){
                            sh "poe test-typing"
                            archiveArtifacts artifacts: "reports/typing/**"
                            junit "reports/typing/junit.xml"
                        }
                    },
                    linter: {
                        withPythonEnv(venv_bin){
                            sh "poe test-linter"
                            archiveArtifacts artifacts: "reports/linter/**"
                            junit "reports/linter/junit.xml"
                        }
                    },
                    changelog: {
                        withPythonEnv(venv_bin){
                            sh "poe test-changelog"
                        }
                    }
                )
            }
        }

        stage("TESTS"){
            steps{
                withPythonEnv(venv_bin){
                    sh "poe test-tests"

                    archiveArtifacts artifacts: "reports/coverage/**"
                    cobertura coberturaReportFile: 'reports/coverage/coverage.xml'

                    archiveArtifacts artifacts: "reports/tests/**"
                    junit "reports/tests/junit.xml"
                }
            }
        }

        stage("DEPENDENCIES"){
            steps{
                parallel(
                    dependencies_bom: {
                        withPythonEnv(venv_bin){
                            sh "poe export-dependencies"
                            archiveArtifacts artifacts: "dependencies_bom.xml"
                        }

                    },
                    dependencies_outdated: {
                        withPythonEnv(venv_bin){
                            sh "poe outdated-dependencies"
                            archiveArtifacts artifacts: "dependencies_outdated.txt"
                        }
                    }
                )
            }
        }

        stage("DOC"){
            steps{
                withPythonEnv(venv_bin){
                    sh "poe doc"
                    archiveArtifacts artifacts: "docs/dist/**", onlyIfSuccessful: true
                }
            }
        }

        stage("BUILD"){
            steps{
                withPythonEnv(venv_bin){
                    sh "poe build"
                    archiveArtifacts artifacts: "dist/*", onlyIfSuccessful: true
                }
            }
        }
    }
}
