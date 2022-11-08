# Scripting functions documentation.

This document describes the functions that are available in the Mastodon scripting interface, to be used within Fiji.
Check the [scripting tutorial](../partA/scripting_mastodon.md) for more information on how to script Mastodon.

| Function                                     | Description                                                  |
| -------------------------------------------- | ------------------------------------------------------------ |
| ***Opening and creating a project***         |                                                              |
| `mamut = Mamut.newProject(bdvFile)`          | Creates a new Mastodon project from a BDV file. The `bdvFile` needs to point to the XML file of BDV file. A new `Context` object is created on the fly. |
| `mamut = Mamut.newProject(bdvFile, context)` | Does the same, but uses an existing `Context` object. In a Fiji script, the current context can be obtained by adding a shebang in the first line of the script: `#@ Context context` |
| `mamut = Mamut.open(mamutProject)`           | Opens an existing Mastodon project. A new `Context` object is created on the fly. |
| `mamut = Mamut.open(mamutProject, context)`  | Does the same, but uses an existing `Context` object.        |
| ***Saving a project***                       |                                                              |
| `ok = mamut.saveAs(newMastodonFile)`         | Saves the current project to a Mastodon file (the extension `.mastodon` is recommended). Returns `True` if the saving happened with no problem. Otherwise sends an error message to the logger. |
| `ok = mamut.save()`                          | Saves the current project to the Mastodon file specified when `saveAs()` was called and returns `True`. If `saveAs` was not called, return `False` and sends an error message to the logger. |
|                                              |                                                              |
|                                              |                                                              |
|                                              |                                                              |
|                                              |                                                              |
|                                              |                                                              |
|                                              |                                                              |
|                                              |                                                              |

