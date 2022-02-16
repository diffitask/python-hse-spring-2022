import setuptools

setuptools.setup(
    name="ast-graph-fibonacci-generator",
    version="1.0",
    author="Evgenia Fedotova",
    description="Generator of ast_graph of fibonacci func",
    url="https://github.com/diffitask/python-hse-spring-2022",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)