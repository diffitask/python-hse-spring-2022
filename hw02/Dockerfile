FROM python:3.9

# to copy a data from files to the container
COPY fibonacci_func.py fibonacci_func.py
COPY latex_generator.py latex_generator.py
COPY artifacts artifacts
COPY __main__.py __main__.py

# to download library and start a program
RUN apt-get update
RUN apt-get install -y texlive graphviz graphviz-dev python3-pygraphviz
RUN pip install networkx
RUN pip install matplotlib
RUN pip install pygraphviz
RUN pip install -i https://test.pypi.org/simple/ ast-graph-fibonacci-generator==2.0

RUN python3.9 __main__.py
WORKDIR ./artifacts
RUN pdflatex output.tex