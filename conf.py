# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mastodon'
copyright = '2022, Jean-Yves Tinevez'
author = 'Jean-Yves Tinevez'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'javasphinx']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'docs/index.md']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = ['attrs_image']

html_theme = 'groundwork'

# Show full TOC in the theme sidebar.
html_sidebars = {
   '**': ['globaltoc.html', 'searchbox.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html'],
} 
html_favicon = 'docs/img/favicon.ico'

# Customized the theme.
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]
