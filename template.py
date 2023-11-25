import os
from pathlib import Path

package_name = 'GemstonePricePrediction'

list_of_path = [
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    "notebooks/research.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    "init_setup.sh",
]

for file_path in list_of_path:
    
    File_path = Path(file_path)
    folder,file = os.path.split(File_path)
    
    if folder != "":
        os.makedirs(folder,exist_ok=True)
        
    if (not os.path.exists(File_path)) or (os.path.getsize(File_path)==0):
        with open(File_path,"w") as f:
            pass
        
    else:
        print("File already exists.")