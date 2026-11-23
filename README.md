[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

# Mastodon documentation

Source files for the mastodon documentation published on [readthedocs.io](https://mastodon.readthedocs.io/)

[Mastodon documentation](https://mastodon.readthedocs.io/) © 2022 by [Jean-Yves Tinevez & contributors](https://github.com/mastodon-sc/mastodon-documentation/graphs/contributors) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

# Building the documentation locally

```bash
pixi run html
```

This fetches the necessary requirements and builds the [`pixi`](https://pixi.prefix.dev/latest/)
environment (in `.pixi`). If the environment is already created, it is not re-created again.
The command primarily, however, runs the task `html`, which calls the Sphinx to build the
documentation to be found in `_build/html` folder.
