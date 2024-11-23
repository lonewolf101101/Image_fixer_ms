import setuptools
from pathlib import Path

# Gather all the package files
package_files = Path("iopaint/web_app").glob("**/*")
package_files = [str(it).replace("iopaint/", "") for it in package_files]
package_files += [
    "model/anytext/ocr_recog/ppocr_keys_v1.txt",
    "model/anytext/anytext_sd15.yaml",
    "model/original_sd_configs/sd_xl_base.yaml",
    "model/original_sd_configs/sd_xl_refiner.yaml",
    "model/original_sd_configs/v1-inference.yaml",
    "model/original_sd_configs/v2-inference-v.yaml"
]

# Read the long description from the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Function to load requirements from the requirements.txt file
def load_requirements():
    requirements_file_name = "requirements.txt"
    requires = []
    with open(requirements_file_name, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():  # Avoid adding empty lines
                requires.append(line.strip())
    return requires

# Setup the package with setuptools
setuptools.setup(
    name="Image_fixer_ms",
    version="1.5.2",
    author="PanicByte",
    author_email="cwq1913@gmail.com",
    description="Image inpainting, outpainting tool powered by SOTA AI Model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lonewolf101101/Image_fixer_ms",
    packages=setuptools.find_packages("."),
    package_data={
        "iopaint": [
            "web_app/**/*",  # Include everything inside web_app
            "model/anytext/ocr_recog/ppocr_keys_v1.txt",
            "model/anytext/anytext_sd15.yaml",
            "model/original_sd_configs/sd_xl_base.yaml",
            "model/original_sd_configs/sd_xl_refiner.yaml",
            "model/original_sd_configs/v1-inference.yaml",
            "model/original_sd_configs/v2-inference-v.yaml",
        ],
    },
    install_requires=load_requirements(),
    python_requires=">=3.7",
    entry_points={"console_scripts": ["iopaint=iopaint:entry_point"]},
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
