# media-report by zbduid12
Print tracks of a video/audio file, and retrieves info on those tracks.

Tested On:
Macbook Pro (Retina, 15-inch, Mid 2015) | macOS Mojave Version 10.14.5

Made for:
Was originally made for mac, cross platform with some minor tweaks

# Dependencies:
* python3
* pymediainfo
* IMDbPy
* teletype
* colorama

# Optional Dependencies:
* VLC
* Handbrake

# How to install
`pip3 install -r requirements.txt`

# Usage
`python3 media_report.py -h`

# Coming Soon:
* Retrieving box office information
* A full blown tv guide
* Better information for subtitles tracks

# Features:

NOTE: Information on TV-Series/Movies is limtied to what IMDB has to offer. If its not on IMDB
than whatever your searching for is not here.

* Print video file properties liked encoding library, bit depth, etc..
    `python3 media_report -e [FILE]` Will show all information in regards to the file

    Output:
    ==> General Track
    [i] Title: Dragon Ball Super - 01 - The Peace Prize. Who'll Get the 100 Million Zeny!
    [i] File Name: **FILENAME HERE**
    [i] File Size: 237 MiB
    [i] Date Encoded: UTC 2019-03-05 11:39:25
    [i] Unique ID: **UID HERE**
    [i] Writing Application: mkvmerge v19.0.0 ('Brave Captain') 64-bit
    [i] Writing Library: libebml v1.3.5 + libmatroska v1.4.8
    [i] Format: Matroska
    [i] Duration: 23 min 7 s 226 ms
    [i] Container: None

    ==> Video Track
    [i] Resolution: 1920x1080
    [i] Pixel Aspect Ratio: 1.000
    [i] Frame Count: 33260
    [i] Frame Rate (FPS): 23.976
    [i] Bit Rate: 1183863
    [i] Bit Depth: 10
    [i] Format: HEVC
    [i] Encoded Library: x265
    [i] Other Encoded Library: video/H265
    [i] Codec ID: V_MPEGH/ISO/HEVC

    ==> Audio Track
    [i] Language: English
    [i] Codec ID: A_OPUS
    [i] Delay: 0
    [i] Format Info: Opus
    [i] Channel #: None

    ==> Audio Track
    [i] Language: Japanese
    [i] Codec ID: A_OPUS
    [i] Delay: 0
    [i] Format Info: Opus
    [i] Channel #: None

    ==> Subtitles Track
    [i] Hard Coded: No

    ==> Subtitles Track
    [i] Hard Coded: No

* Finding shasum's for files
    `python3 media_report.py --hash [FILE]` will show
    md5, sha1, sha256, and sha512 hashes for the contents
    of the file. If the file is an .mkv file than the unique ID
    will also be listed

    NOTE: This can take a moment, depending on the speed of your computer

* Search for movies, and tv-shows (powered by IMDbPy)
    `python3 media_report.py -s` Will show an interactive search, that prints general info when you pick a movie/show
    `python3 media_report.py -ss` Similar to `-s`. Just non interactive, also doesnt show general info, just ID's

    Output:

    Search for media: my hero academia
    My Hero Academia [ID: 5626028]
    My Hero Academia: Two Heroes [ID: 7745068]
    My Hero Academia (in development) [ID: 9198442]
    My Hero Academia: Heroes Rising [ID: 11107074]
    My Hero Academia: All Might Rising [ID: 11589858]
    Boku no hîrô akademia: Training of the Dead [ID: 6848466]
    My Hero Academia Abridged [ID: 7836396]
    Boku no hîrô akademia: One's Justice [ID: 8858118]
    My Hero Academia [ID: 8938088]
    My Hero Academia: Smash Tap [ID: 6807166]
    My Hero Academio [ID: 9419886]
    Blind Wave: My Hero Academia Reaction [ID: 11281064]
    My Hero Academia: Battle of All [ID: 5534302]
    My Hero Academia: Heroes Rising [ID: 11908800]
    Top 10 My Hero Academia Villains [ID: 11595686]
    My Hero Academia Heroes: Rising Review [ID: 11962426]
    MY HERO ACADEMIA - LORE in a Minute! [ID: 10422254]
    Teens React to My Hero Academia [ID: 8265866]
    My Hero Academia (S2) en 7 minutes [ID: 9448024]
    My Hero Academia: My Student Debt [ID: 11230206]

* Show information on movies
    Using `-s` will show general information, when you select a piece of media
    `python3 media_report.py -i [ID]` Will show more detailed information, but you need to know the ID
    which you can get with either `-g`, `-s`, or `-ss`

    NOTE: Box office support coming soon

    Output:
    ==> Media Description
    [i] Title: Paranormal Activity
    [i] ID: 1179904
    [i] Year: 2007
    [i] Media Type: movie
    [i] Avg. Runtime: 86 mins
    [i] Genres:  Horror,  Mystery,  Thriller,
    [i] Countries: ['United States']
    [i] Languages: ['English']
    [i] Rating: 6.3/10
    [i] Plot: After moving into a suburban home, a couple becomes increasingly disturbed by a nightly demonic presence.::Anonymous
    ==> Movie Information
    [M] Original Air Date:  16 Oct 2009 (USA)
    [M] Writer:  Oren Peli
    [M] Director:  Oren Peli

* Show an episode map of a tv-series
    `python3 media_report.py --episode-map [ID]` Will show a complete season-by-season, episode-by-episode
    guide (based on availabillity) of the series

    Format is as follow for priting data: "- Epsiode EP_NUMBER: EPISODE_TITLE - (YEAR_RELEASED) - [RATING OUT OF TEN]

    NOTE: For episodes that dont have a rating logged in IMDB, none will be shown

    Output:
    ==> Episode Map
    [i] Title: Cowboy Bebop
    [TV] Season Count: 1
    [TV] Epsiode Count:  26
    ==> Season 1
    - Episode 1: Asteroid Blues - (2001) - [8/10]
    - Episode 2: Stray Dog Strut - (2001) - [8/10]
    - Episode 3: Honky Tonk Women - (2001) - [8/10]
    - Episode 4: Gateway Shuffle - (2001) - [8/10]
    - Episode 5: Ballad of Fallen Angels - (2001) - [9/10]
    - Episode 6: Sympathy for the Devil - (2001) - [8/10]
    - Episode 7: Heavy Metal Queen - (2001) - [8/10]
    - Episode 8: Waltz for Venus - (2001) - [9/10]
    - Episode 9: Jamming with Edward - (2001) - [8/10]
    - Episode 10: Ganymede Elegy - (2001) - [8/10]
    - Episode 11: Toys in the Attic - (2001) - [8/10]
    - Episode 12: Jupiter Jazz: Part 1 - (2001) - [9/10]
    - Episode 13: Jupiter Jazz: Part 2 - (2001) - [9/10]
    - Episode 14: Bohemian Rhapsody - (2001) - [8/10]
    - Episode 15: My Funny Valentine - (2001) - [8/10]
    - Episode 16: Black Dog Serenade - (2001) - [8/10]
    - Episode 17: Mushroom Samba - (2001) - [8/10]
    - Episode 18: Speak Like a Child - (2001) - [8/10]
    - Episode 19: Wild Horses - (2001) - [7/10]
    - Episode 20: Pierrot le Fou - (2001) - [9/10]
    - Episode 21: Boogie Woogie Feng Shui - (2001) - [7/10]
    - Episode 22: Cowboy Funk - (2002) - [8/10]
    - Episode 23: Brain Scratch - (2001) - [8/10]
    - Episode 24: Hard Luck Woman - (2001) - [9/10]
    - Episode 25: The Real Folk Blues: Part 1 - (2001) - [9/10]
    - Episode 26: The Real Folk Blues: Part 2 - (2001) - [9/10]
    
