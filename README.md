# spawn-grabber

## Introduction
`spawn-grabber` is a Python package that facilitates the downloading and processing of audio files from the Spawn catalog on ArDrive. It parses M3U files to identify necessary files on ArDrive, then downloads and decrypts them, concatenating the results into complete audio files.

## Installation

### Prerequisites
Before installing `spawn-grabber`, ensure you have the following dependencies installed:
- Python 3
- [Homebrew](https://brew.sh/)
- Git: `brew install git`
- Node.js: `brew install node`
- nvm: Install using the script from [nvm GitHub](https://github.com/nvm-sh/nvm)
- ArDrive CLI: `npm install -g ardrive-cli` and `npm update -g ardrive-cli`

### Installing spawn-grabber
To install `spawn-grabber`, clone the repository from GitHub and install it using pip:

git clone https://github.com/yourgithubusername/spawn-grabber.git
cd spawn-grabber
pip install .


## Usage
After installation, you can use `spawn-grabber` as follows:

spawn-grabber m3u_path ardrive_wallet_path [--music-path MUSIC_PATH]

- `m3u_path`: Path to your M3U file.
- `ardrive_wallet_path`: Path to your ArDrive wallet file.
- `--music-path`: (Optional) Path where the folders will be downloaded and decrypted. Defaults to the current working directory.

## License
`spawn-grabber` is released under the GPL-3.0 license. See the LICENSE file for more details.

## Contributing
Contributions to `spawn-grabber` are welcome! Please refer to the contributing guidelines for more information.

## Support
If you encounter any issues or have questions about `spawn-grabber`, please file an issue on the GitHub repository.
