from setuptools import setup, find_packages

setup(
    name='FR3-Vicon-Visualizer',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your project's dependencies here.
        # For example:
        # 'numpy>=1.18.0',
        # 'matplotlib>=3.2.1',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python package for visualizing Vicon data in the FR3 format.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/FR3-Vicon-Visualizer',  # Replace with your project's URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Replace with your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
