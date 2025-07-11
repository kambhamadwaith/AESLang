from setuptools import setup, find_packages

setup(
    name="aeslang",
    version="1.1.0",
    author="Kambham Adwaith",
    author_email="kambhamadwaith@algorithmeduspace.com",  # 🔁 Replace with your actual email
    description="A programming language made entirely of the word AES",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kambhamadwaith/AESLang",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Interpreters",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "aeslang=aeslang.main:main"
        ]
    },
    include_package_data=True,
)
