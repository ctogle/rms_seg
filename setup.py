import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rms_seg",
    version="0.0.1",
    author="Curtis Ogle",
    author_email="curtis.t.ogle@gmail.com",
    description="RMS level-based audio segmentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ctogle/rms_seg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
    ],
    python_requires='>=3.6',
)
