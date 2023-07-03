"""Invoke tasks for packaging the project as a Lambda Layer"""
import os
import sys
import shutil
import subprocess
import zipfile
from invoke import task


@task
def package_lambda(ctx):
    """Package the project as a Lambda Layer"""
    # Create the layer directory
    layer_dir = "layer"
    os.makedirs(layer_dir, exist_ok=True)

    # Copy the source files to the layer directory
    source_files = [
        "articles_to_s3.py",
        "news_article_pipeline.py",
        "text_extractor.py",
        "url_fetcher.py",
    ]
    for file in source_files:
        shutil.copy(file, layer_dir)

    # Install project dependencies into the layer directory
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            "requirements.txt",
            "-t",
            layer_dir,
        ],
        check=True,
    )

    # Zip the layer directory
    package_name = "lambda_package.zip"
    with zipfile.ZipFile(package_name, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(layer_dir):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, layer_dir)
                zf.write(abs_path, arcname=rel_path)

    # Clean up
    shutil.rmtree(layer_dir)
