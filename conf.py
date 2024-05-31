# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os, sys
import sphinx_material

# For extensions.
sys.path.append(os.path.abspath('exts'))

project = 'Mastodon'
copyright = '2022 - 2024, Jean-Yves Tinevez'
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

myst_enable_extensions = ['attrs_inline']

html_theme = 'sphinx_material'

# Show full TOC in the theme sidebar.

html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()

html_favicon = 'docs/img/favicon.ico'
html_logo = 'docs/img/android-chrome-192x192.png'

# Customized the theme.
# html_static_path = ['_static']
# html_css_files = [
#     'css/custom.css',
# ]

html_theme_options = {
    'base_url': 'http://bashtage.github.io/sphinx-material/',
    'repo_url': 'https://github.com/mastodon-sc/',
    'repo_name': 'Mastodon',
    # 'html_minify': True,
    # 'css_minify': True,
    'logo_icon': '&#xe88a',
    'nav_title': 'Mastodon',
    'globaltoc_depth': 3
}


