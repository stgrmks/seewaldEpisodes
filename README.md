# Seewald - Episodes
Downloads latest [Seewald Episode](https://www.egofm.de/musik/entdecken/sendung-seewald-zum-nachhoeren) and pushes it to slack.
## Install
$ python3 -m pip install -U git+git://github.com/stgrmks/seewaldEpisodes.git
## Usage
### Python
```python
from seewaldEpisodes import get_episode
from typing import Dict

custom_settings: Dict = {} # overwrites settings.py 
get_episode(**custom_settings)
```
### Docker
TODO

