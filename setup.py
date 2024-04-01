from setuptools import setup, find_packages

setup(
    name="Covers to Colors",
    version="0.1",
    packages=find_packages(),
    # author="Your Name",
    # author_email="your.email@example.com",
    # description="A brief description of your package",
    # long_description=open('README.md').read(),
    # long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/mypackage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "urllib",
        "matplotlib",
        "mpl_toolkits",
        "numpy",
        "kneed",
        "PIL",
        "sklearn",
        "scipy",
        "fuzzywuzzy",
        "discogs_client",
        "musicbrainzngs",
        "pylast",
        "requests"
    ],
)