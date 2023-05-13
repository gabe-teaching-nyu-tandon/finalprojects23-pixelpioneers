# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

project = 'Pixel Pioneers'
copyright = '2023, Aman Mittal, Amey Kolhe, Ankur Aggarwal, Anupam Tiwari, Karan Vora, Yashika Khurana'
author = 'Aman Mittal, Amey Kolhe, Ankur Aggarwal, Anupam Tiwari, Karan Vora, Yashika Khurana'
release = '0.1.dev'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Sphinx extension module names, see https://www.sphinx-doc.org/en/master/usage/extensions
extensions = [
    'sphinx.ext.autodoc',      # auto-generate documentation from docstrings
    'sphinx.ext.viewcode',     # links to highlighted source code for documented code objects
    'sphinx.ext.napoleon',     # support for Google and NumPy docstrings
    'sphinx.ext.autosummary',  # function/method/attribute summary lists
    'sphinx.ext.intersphinx',  # link to objects in external documentation
    'sphinx.ext.githubpages',  # creates .nojekyll file on generated HTML directory
    'nbsphinx',                # execute Jupyter notebooks and include HTML output in docs
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}


sys.path.insert(0, os.path.abspath("../../src"))


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Sphinx configuration
# - http://www.sphinx-doc.org/en/master/usage/configuration.html
add_module_names = True
autodoc_typehints = "description"

# autodoc
# - http://www.sphinx-doc.org/en/stable/ext/autodoc.html#confval-autodoc_member_order
autodoc_member_order = 'bysource'

# autosummary
# - https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-ii-6/
autosummary_generate = True
