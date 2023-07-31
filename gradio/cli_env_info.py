""" This file is the part of 'gradio/cli.py' for printing the environment info 
for the cli command 'gradio environment'
"""
import platform
from importlib import metadata


def print_environment_info():
    print("Gradio Environment Information:")
    print("Operating System: ", platform.system())
    print("\n")

    for package_name in ["gradio", "gradio_client"]:
        try:
            package_version = metadata.version(package_name)
            print(f"{package_name} version: ", package_version)

            print(f"\n{package_name} Dependencies:")
            dist = metadata.distribution(package_name)
            for req in dist.requires:
                try:
                    print(f"  {req}: {metadata.version(req)}")
                except metadata.PackageNotFoundError:
                    print(f"{req} is not installed.")
            print("\n")
        except metadata.PackageNotFoundError:
            print(f"{package_name} package is not installed.")
