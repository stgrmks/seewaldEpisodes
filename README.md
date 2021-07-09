# Seewald - Episodes
Downloads the latest [Seewald Episode](https://www.egofm.de/musik/entdecken/sendung-seewald-zum-nachhoeren) and pushes it to slack.
## Install
    $ python3 -m pip install -U git+git://github.com/stgrmks/seewaldEpisodes.git
## Usage
### Python
```python
from seewaldEpisodes import get_episode
from typing import Dict

custom_settings: Dict = {} # overwrites settings.py 
custom_settings["DOWNLOAD_DELAY"] = 10 # configure a delay for requests
get_episode(**custom_settings)
```
### Docker
Start docker:

    $ docker-compose up -d

Stop docker:
    
    $ docker-compose down