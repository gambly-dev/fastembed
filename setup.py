from setuptools import setup, find_packages

setup(
    name="fastembed",
    version="0.3.4",
    description="Fast, light, accurate library built for retrieval embedding generation",
    author="Qdrant Team",
    author_email="info@qdrant.tech",
    license="Apache License",
    packages=find_packages(include=["fastembed"]),
    install_requires=[
        "onnx==1.15.0",
        "onnxruntime==1.17.0",
        "tqdm==4.66",
        "requests==2.31",
        "tokenizers>=0.15,<1.0",
        "huggingface-hub>=0.20,<1.0",
        "loguru==0.7.2",
        "numpy>=1.21,<2; python_version<'3.12'",
        "numpy>=1.26,<2; python_version>='3.12'",
        "pillow==10.3.0",
        "mmh3==4.0",
    ],
)
