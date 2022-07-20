# Copyright 2022 Wingify Software Pvt. Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# flake8: noqa

import os

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools import Command

# import subprocess

# current_directory = os.path.join(os.path.dirname(__file__))

# with open(os.path.join(current_directory, "requirements.txt")) as f:
#     REQUIREMENTS = f.read().splitlines()

with open("README.md", "r") as f:
    long_description = f.read()



class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    def run(self):
        print("\nRUNNING POST INSTALL DEVELOP SCRIPT \n")

        develop.run(self)


setup(
    name="vwo-sdk-log-messages",
    version="0.10.0",
    description="Log messages for VWO server-side SDKs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="VWO",
    author_email="dev@wingify.com",
    url="https://github.com/wingify/vwo-sdk-log-messages",
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    cmdclass={
        "develop": PostDevelopCommand
    },
    packages=find_packages(exclude=["tests"]),
    install_requires=[]
)
