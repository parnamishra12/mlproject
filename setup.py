## setup.py will be responsible in creating my Machine Learning project as a package, from here anyone can do the installation and anyone can use it
from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] ## this is list comprehension

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # -e . should not come while running setup file so we are removing it

    print("Requirements:", requirements)

    return requirements


setup(

    name='mlproject',
    version='0.0.1',
    author='Parna',
    author_email='mishraparna0@gmail.com',
    packages=find_packages(),
    install_requires =get_requirements('requirements.txt')
)