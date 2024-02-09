from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(filename: str) -> List[str]:
    """Read and parse a requirements file to be used in install_requires.
    
    Parameters:
    - filename (str): The path to the requirements file.
    
    Returns:
    - List[str]: A list of requirement strings.
    
    Raises:
    - FileNotFoundError: If the specified requirements file does not exist.
    - IOError: If there's an issue reading the file.
    """
    try:
        with open(filename, 'r') as file:
            requirements = []
            for line in file:
                # Strip leading/trailing whitespace
                line = line.strip()
                # Skip blank lines and lines starting with '#' (comments)
                if line and not line.startswith('#'):
                    # Handle requirement specifiers with inline comments
                    line = line.split('#', 1)[0].strip()
                    requirements.append(line)

            # handle .e -
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
            
            return requirements
    except FileNotFoundError:
        raise FileNotFoundError(f"Requirements file '{filename}' not found.")
    except IOError as e:
        raise IOError(f"Error reading '{filename}': {e.strerror}")

setup(
    name='test_app',  
    version='0.1.0',  
    author='Oleksandr Balabanov',  
    author_email='balabanovsasha@gmail.com',  
    description='test end to end app', 
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/oleksandr-balabanov/TestProject',
    packages=find_packages(exclude=['tests*']),
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3.8',
    ],
    keywords='test app',  
    license='MIT',  
)

