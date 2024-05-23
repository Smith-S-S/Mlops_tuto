# Mlops_tuto
* 
* https://dagshub.com/Smith-S-S/Mlops_tuto.mlflow
* import dagshub
* dagshub.init(repo_owner='Smith-S-S', repo_name='Mlops_tuto', mlflow=True)
* 
* import mlflow
* with mlflow.start_run():
*   mlflow.log_param('parameter name', 'value')
*   mlflow.log_metric('metric name', 1)
* 
* export MLFLOW_TRACKING_URI=https://dagshub.com/Smith-S-S/Mlops_tuto.mlflow
* export MLFLOW_TRACKING_USERNAME=Smith-S-S
* -----------------------------------------------------------------------
* 
* sudo apt update
* sudo apt install python3-pip
* sudo pip3 install pipenv
* sudo pip3 install virtualenv
* mkdir mlflow
* 
* 
* python3 -m venv myenv
* source myenv/bin/activate
* pip install mlflow
* 
* pip install setuptools
* mlflow server -h 0.0.0.0 --default-artifact-root s3://mlflow-busket-smith-101


# see u