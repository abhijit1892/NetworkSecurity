"""
Docstring for setup
id essential for packaging and distribution of projects. it is
use by setuptools to define the configuration of your project
"""
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return the list of requirements
    """
    requirements_lst:list[str]=[]
                    
    try:
        with open("requirements.txt","r") as file:
            #read lines from the file
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                ##ogonre empty lines and -e .
                if requirement and requirement!="-e .":
                    requirements_lst.append(requirement)
                    
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirements_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Abhi",
    author_email="abhijitpatil1892@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)




