import os
import sys
import shutil
from invoke import task


@task
def package_lambda(ctx):
    """Package the project as a Lambda Layer"""
    # Create a temporary directory for the virtual environment
    venv_dir = "layer_venv"
    ctx.run(f"python -m venv {venv_dir}")

    # Activate the virtual environment and install project dependencies
    with ctx.prefix(f"source {venv_dir}/bin/activate"):
        ctx.run("pip install -r requirements.txt")

    # Copy the virtual environment contents to the layer directory
    layer_dir = "layer"
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    site_packages_dir = os.path.join(
        venv_dir, "lib", f"python{python_version}", "site-packages"
    )
    shutil.copytree(site_packages_dir, layer_dir)

    # Create a ZIP archive of the layer directory
    ctx.run(f"zip -r layer.zip {layer_dir}")

    # Clean up the temporary directory
    shutil.rmtree(venv_dir)
    shutil.rmtree(layer_dir)
