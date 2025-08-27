# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If your documentation source is outside the root directory, add paths here
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate UHC Card'
copyright = '2025, UnitedHealthcare'
author = 'UHC Support Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Extensions to use (add more if needed, like 'sphinx_rtd_theme')
extensions = []

# Allow raw HTML blocks in .rst files
raw_enabled = True

# List of patterns to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Templates path (uncomment if using custom HTML templates)
templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------

# HTML theme (optional: you can install and enable 'sphinx_rtd_theme' or others)
# html_theme = 'sphinx_rtd_theme'

# Set basic page titles
html_title = "How to Activate Your UHC Card – Step-by-Step Guide"
html_short_title = "Activate UHC Card"
html_favicon = 'favicon.ico'  # Optional: add your favicon to _static or root

# Hide "View page source" link
html_show_sourcelink = False

# Allow inline HTML in reStructuredText
html_allow_unsafe = True

# Theme customization options (expand as needed)
html_theme_options = {
    'show_powered_by': False,
}

# Static files (uncomment if using custom styles or logos)
# html_static_path = ['_static']
