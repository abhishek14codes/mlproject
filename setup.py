from setuptools import find_packages , setup
from typing import List

hyp_e = "-e ."
def get_requirements(file_path:str) -> List[str] :
    requirements=[]
    with open(file_path, encoding="utf-8") as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.strip() for req in requirements]
        if hyp_e in requirements :
            requirements.remove(hyp_e)
        return requirements        




setup(
    name="mlproject",
    version="0.0.1",
    author="Abhishek Dhingra" ,
    author_email="dhingraabhishek514@gmail.com" ,
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)