echo [$(date)]: " START ";

echo [$(date)]: "Creating Python Environments ";

conda create --prefix ./env python=3.8 -y 

echo [$(date)]: "Activating Python Environment ";

source activate ./env  

echo [$(date)]: "Installing Necessary Requiremnets ";

pip install -r requirements.txt

echo [$(date)]: "Environment Setup and Installation is Done ";