from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requiremnets=[]
    with open(file_path) as file_obj:
        requiremnets=file_obj.readlines()
        requiremnets = [req.replace("\n","") for req in requiremnets ]
        
        if HYPEN_E_DOT in requiremnets:
            requiremnets.remove(HYPEN_E_DOT)
        return requiremnets
    

setup(
    name='Thyroid_Disease_Detection',
    version='0.0.1',
    author='Amrendra Kumar',
    authoe_email = 'amrendra001122@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages = find_packages()
)   