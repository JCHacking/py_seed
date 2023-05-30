import sys
import os

from sphinx_pyproject import SphinxConfig

# Path Setup
sys.path.insert(0, os.path.abspath('../../src'))

# PyProject.toml config
config = SphinxConfig("../../pyproject.toml", globalns=globals())
