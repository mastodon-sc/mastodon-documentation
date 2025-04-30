# Example scripts.

This page collects several script examples that show how to interact with Mastodon using the Fiji scriptin interface. 
Check the page [scripting_mastodon](../partA/scripting_mastodon) to see how to create Mastodon scripts.

## Setting all spots Z position to 0 and resaving.

```python
#@ Context context

from org.mastodon.mamut import Mamut
import os

# Load image
mastodon_file = os.path.join( os.path.expanduser('~'), 'path', 'to', 'your_mastodon_file.mastodon' )
mamut = Mamut.open( mastodon_file, context )
mamut.info()

# Iterate over all spots and edit Z positio
it = mamut.getModel().getGraph().vertices().iterator()
new_z = 0.
while it.hasNext():
	spot = it.next()
	spot.setPosition( new_z, 2 ) # position 2nd index is Z

print('Done')

# Resave
new_mastodon_file = os.path.join( os.path.expanduser('~'),  'path', 'to', 'your_EDITED_mastodon_file.mastodon' )
mamut.saveAs( new_mastodon_file )

```
