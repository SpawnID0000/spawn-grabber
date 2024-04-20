# spawn-grabber

## Introduction
`spawn-grabber` is a Python package that facilitates the downloading and processing of audio files from the Spawn catalog on ArDrive. It parses specially-formatted M3U files to identify necessary folderIDs on ArDrive, then downloads and decrypts them, concatenating the results into complete audio files.

## M3U formatting
Compatible M3U files are plain text files with extension .m3u and the following format:
```
#EXTM3U
#EXTINF:68,folderID1
../Music/filename1.extension
#EXTINF:150,folderID2
../Music/filename2.extension
```
Where #EXTM3U is listed at the top, followed by #EXTINF & relative path lines for each track to be downloaded & processed.  In each #EXTINF line, the numeric value refers to the track duration in seconds and folderID corresponds with the encrypted track package on Arweave.
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **For example:**
```
#EXTM3U
#EXTINF:68,3653307f-306f-4628-ae1d-e64efdd361bd
../Music/ba7be4d0-e73f-4ecc-94d9-6658b510c69b_7c0ecbde-84d4-48c7-8cf4-77cecce423af.mp3
#EXTINF:150,264d398e-9e8b-4484-877f-bfe592d51476
../Music/ba7be4d0-e73f-4ecc-94d9-6658b510c69b_19d368c3-63fc-4159-ab41-bfc5d0ab105f.mp3
```
With the M3U file saved in a local folder (e.g. Playlists) under the same parent directory as Music, the playlist can be opened directly in a media player (like [VLC](https://www.videolan.org/vlc/)) after `spawn-grabber` has recovered the audio files, as long as the filenames (with extensions) match for each corresponding entry.  Expected filename formatting is ArtistMBID_RecordingMBID, based on [MusicBrainz IDs](https://musicbrainz.org/doc/MusicBrainz_Identifier).  
  
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

git clone https://github.com/SpawnID0000/spawn-grabber.git  
cd spawn-grabber  
pip install .


## Usage
After installation, you can use `spawn-grabber` as follows:

spawn-grabber m3u_path ardrive_wallet_path [--music-path MUSIC_PATH]

- `m3u_path`: Path to your M3U file ([sample file](https://github.com/SpawnID0000/spawn-grabber/blob/main/spawn-ardrive_30Hz.m3u))
- `ardrive_wallet_path`: Path to your ArDrive wallet file.
- `--music-path`: (Optional) Path where the folders will be downloaded and decrypted. Defaults to the current working directory

## License
`spawn-grabber` is released under the GPL-3.0 license. See the LICENSE file for more details


## Support
If you encounter any issues, have questions, or would like to contribute to the Spawn project, please reach out!
