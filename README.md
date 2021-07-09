Seewald - Episodes
==================
[![Current Version](https://img.shields.io/badge/version-0.1.0-green.svg)](https://github.com/stgrmks/seewaldEpisodes) [![Python 3.8](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

Downloads the latest [Seewald Episode](https://www.egofm.de/musik/entdecken/sendung-seewald-zum-nachhoeren) and pushes it to slack or writes it to disk.

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
Create a .env file containing `SLACK_TOKEN` and `SLACK_CHANNEL` in case you want to use the slack pipeline.

In case you want to use the FilePipeline adjust the settings.py:
```python
ITEM_PIPELINES = {
    "seewaldEpisodes.seewaldEpisodes.pipelines.FilePipeline": 300,
}
```

Start docker:

    $ docker-compose up -d

Stop docker:
    
    $ docker-compose down

## ToDos
- Add env flag to docker-compose for FilePipeline usage
- Tests

## Code Formatter & Style Guide Enforcer
- [Black - The Uncompromising Code Formatter](https://github.com/psf/black)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[APACHE 2.0](https://choosealicense.com/licenses/apache-2.0/)