
# `from setuptools import find_packages, setup` is importing the necessary functions `find_packages`
# and `setup` from the `setuptools` module. These functions are commonly used in Python packaging to
# define the structure of a Python package and its dependencies. The `setup` function is used to
# configure the package metadata and dependencies, while `find_packages` is used to automatically
# discover and include all Python packages in the project.
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements.
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
    name='ml1project',
    version='0.0.1',
    author='ganesh',
    author_email='khisteg5@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

