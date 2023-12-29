from setuptools import setup, find_packages

setup(
    name="spawn-grabber",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "cryptography"
    ],
    entry_points={
        'console_scripts': [
            'spawn-grabber=spawn_grabber.ardrive_downloader:main',
        ],
    },
    # Spawn
)
