from os import getenv
from typing import Dict

from requests import get, post
from tqdm import tqdm
from seewaldEpisodes.seewaldEpisodes.items import SeewaldepisodesItem


class SlackPipeline:
    def process_item(self, item: SeewaldepisodesItem, _):
        content: bytes = b""
        with get(url=item.get("url"), stream=True) as r:
            r.raise_for_status()
            data_chunk: bytes
            for data_chunk in tqdm(r.iter_content(chunk_size=4096)):
                content += data_chunk
        file_name: str = item.get("url").split("/")[-1]
        data: Dict = {
            "token": getenv("TOKEN"),
            "channels": [getenv("CHANNEL")],
            "content": content,
            "filename": file_name,
            "filetype": "mp3",
        }
        response = post(
            url="https://slack.com/api/files.upload",
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        if response.status_code != 200:
            raise ValueError(
                f"Request error! Status-Code: {response.status_code} Response:{response.text}"
            )
        return item

class FilePipeline:
    def process_item(self, item: SeewaldepisodesItem, _):
        with get(url=item.get("url"), stream=True) as r:
            r.raise_for_status()
            with open(item.get("url").split("/")[-1],"wb") as f:
                data_chunk: bytes
                for data_chunk in tqdm(r.iter_content(chunk_size=4096)):
                    f.write(data_chunk)
        return item
