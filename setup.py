import setuptools
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements from requirements.txt
def read_requirements():
    """Read requirements from requirements.txt file"""
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            # Filter out comments and empty lines
            requirements = [
                line.strip() 
                for line in f 
                if line.strip() and not line.startswith('#')
            ]
            return requirements
    return []

setuptools.setup(
    name="rosbag_to_pandas", 
    version="0.0.1",
    author="Floris van Breugel, Claude, Strawlab",
    author_email="fvanbreugel@unr.edu",
    description="Helper functions to extract data from rosbag files and organize into pandas compatible structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/RosBagToPandas",  # Add your repo URL
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=read_requirements(),
    # Optional: specify extra dependencies for development
    extras_require={
        'dev': [
            'pytest>=7.0',
            'pytest-cov>=3.0',
            'black>=22.0',
            'flake8>=4.0',
        ],
    },
    # If you want to include the scripts as console commands
    entry_points={
        'console_scripts': [
            'bag2hdf5=rosbag_to_pandas.bag2hdf5:main',  # Adjust module path as needed
        ],
    },
)
