from setuptools import setup, find_packages


with open('README.md') as readme_file:
    long_description = readme_file.read()

requirements = [
    "numpy",
    "iminuit",
    "scipy"
]

test_requirements = ['pytest>=3', ]

setup(
    author="Massimiliano Galli",
    author_email='massimiliano.galli.95@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    name="magastats",
    version="0.0.1",
    description="Collection of useful statistics tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=['magastats', 'magastats.*']),
    package_dir={"": "src"},
    install_requires=requirements,
    extras_require={
        "dev": test_requirements
    }
)