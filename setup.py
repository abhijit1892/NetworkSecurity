"""
For packaging and distributing python projects. 
it is used by setuptools to define the configuration
of project,such as metadata, dependencies and more
"""
from setuptools import find_packages,setup
from typing import List

def get_requirements() ->List[str]:
    """
    This function will return list of requiremets
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!="-e .":
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Abhijit Patil",
    author_email="abhijitpatil1892@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)