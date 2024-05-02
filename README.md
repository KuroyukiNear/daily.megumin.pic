# Daily Megumin Pic

## Overview
Daily pictures of Megumin posted on Instagram from the `Waifu.pics` API.

The original images are located in the [`img`](/img/) folder.

## Code Explanation

### `download.py`

[`download.py`](/download.py/) is used to fetch the image from the API and download it. The number for the image will be recorded in [`image_data.json`](/image_data.json/). The script will check if the image exists in the JSON file. The script will fetch another image from the API if the same image that exists is fetched.

### `randomNumber.py`

[`randomNumber.py`](/randomNumber.py/) is used to choose a random number for the image that hasn't been chosen since 30 images to avoid the same image to be posted in a short period of time when the API runs out of images. The list of numbers will be stored in [`numbers.json`](/numbers.json/).

## API

### [Website](https://waifu.pics/)
### [GitHub](https://github.com/Waifu-pics/waifu-api)

<br><br><br>

###### Kuroyuki Near <br> 03 April 2024
