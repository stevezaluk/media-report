#!/usr/bin/env python3
import sys, os, subprocess, hashlib
from pymediainfo import MediaInfo
import text
import imdb
from teletype.components import SelectOne, ChoiceHelper

"""
    TODO: Write tv-guide
    TODO: Implement box office information
"""

def usage():
    print("mediafileinfo [ARGS] [file] - Displays media info and descriptions")
    print("Powered by python3, pymediainfo, and IMDbPy")
    print('## File Arugments ##')
    print("-h : Displays this page")
    print("-k : Print MediaInfo keys")
    print("-v : Print video track info only")
    print("-a : Print audio track info only")
    print("-e : Print all file information")
    print("-c : Print only codec information")
    print("-b : Opens the file in handbrake")
    print("-l : Opens the file in VLC")
    print("--hash : Print hash information - sha1, sha256, sha512, md5")    

#hashes
def return_sha1_hash(file):
    with open(file, mode='rb') as _file:
        data = _file.read()
        sha1 = hashlib.sha1(data).hexdigest()
        return sha1

def return_sha256_hash(file):
    with open(file, mode='rb') as _file:
        data = _file.read()
        sha256 = hashlib.sha256(data).hexdigest()
        return sha256

def return_sha512_hash(file):
    with open(file, mode='rb') as _file:
        data = _file.read()
        sha512 = hashlib.sha512(data).hexdigest()
        return sha512

def return_md5_hash(file):
    with open(file, mode='rb') as _file:
        data = _file.read()
        md5 = hashlib.md5(data).hexdigest()
        return md5

# utilties
def verify_file_existance(file):
    if os.path.exists(file):
        pass
    else:
        text.print_error('Failed to open file')


def open_in_handbrake(file):
    verify_file_existance(file)
    execute = subprocess.Popen("open {f} -a /Applications/HandBrake.app".format(f=file), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
    if execute:
        print("Opening file in handbrake")
    else:
        text.print_error('Failed to open file')

def open_in_vlc(file):
    verify_file_existance(file)
    execute = subprocess.Popen("open {f} -a /Applications/VLC.app".format(f=file), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
    if execute:
        print("Opening file in vlc")
    else:
        text.print_error('Failed to open file')

# print information
def print_keys(file):
    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == "Video":
            text.print_info("Video Keys: {}".format(track.to_data().keys()))
            print("")
        elif track.track_type == "Audio":
            text.print_info("Audio Keys: {}".format(track.to_data().keys()))
            print("")
        elif track.track_type == "Text":
            text.print_info("Text Keys: {}".format(track.to_data().keys()))
            print("")
        elif track.track_type == "General":
            text.print_info("General Keys: {}".format(track.to_data().keys()))
        elif track.track_type == "Menu":
            text.print_info("Menu Keys: {}".format(track.to_data().keys()))


def print_everything(file, verbose=False):
    verify_file_existance(file)
    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == 'General':
            text.print_header("General Track")
            text.print_info("Title: {}".format(track.title))
            text.print_info("File Name: {}".format(track.complete_name))
            text.print_info("File Size: {}".format(track.other_file_size[0]))
            text.print_info("Date Encoded: {}".format(track.encoded_date))
            text.print_info("Unique ID: {}".format(track.unique_id))
            text.print_info("Writing Application: {}".format(track.writing_application))
            text.print_info("Writing Library: {}".format(track.writing_library))
            text.print_info("Format: {}".format(track.format))
            text.print_info("Duration: {}".format(track.other_duration[1]))
            text.print_info("Container: {}".format(track.container))
            print("")
        elif track.track_type == 'Video':
            text.print_header("Video Track")
            text.print_info("Resolution: {w}x{h}".format(w=track.width, h=track.height))
            text.print_info("Pixel Aspect Ratio: {}".format(track.pixel_aspect_ratio))
            text.print_info("Frame Count: {}".format(track.frame_count))
            text.print_info("Frame Rate (FPS): {}".format(track.frame_rate))
            text.print_info("Bit Rate: {}".format(track.bit_rate))
            text.print_info("Bit Depth: {}".format(track.bit_depth))
            text.print_info("Format: {}".format(track.other_format[0]))
            text.print_info("Encoded Library: {}".format(track.encoded_library_name))
            text.print_info("Other Encoded Library: {}".format(track.internet_media_type))
            text.print_info("Codec ID: {}".format(track.codec_id))
            if verbose:
                text.print_info("Encoded Settings: {}".format(track.encoding_settings))
            print("")
        elif track.track_type == 'Audio':
            text.print_header("Audio Track")
            text.print_info("Language: {}".format(track.other_language[1]))
            text.print_info("Codec ID: {}".format(track.codec_id))
            text.print_info("Delay: {}".format(track.delay))
            text.print_info("Format Info: {}".format(track.format))
            text.print_info("Channel #: {}".format(track.channel))
            print("")
        elif track.track_type == 'Text':
            text.print_header("Subtitles Track")
            text.print_info("Hard Coded: {}".format(track.forced))
            print("")


def print_video_only(file):
    verify_file_existance(file)
    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            text.print_header("Video Track")
            text.print_info("File Name: {}".format(track.complete_name))
            text.print_info("File Size: {}".format(track.other_file_size[0]))
            text.print_info("Date Encoded: {}".format(track.encoded_date))
            text.print_info("Duration: {}".format(track.other_duration[1]))
            text.print_info("Resolution: {w}x{h}".format(w=track.width, h=track.height))
            text.print_info("Pixel Aspect Ratio: {}".format(track.pixel_aspect_ratio))
            text.print_info("Frame Count: {}".format(track.frame_count))
            text.print_info("Frame Rate (FPS): {}".format(track.frame_rate))
            text.print_info("Bit Rate: {}".format(track.bit_rate))
            text.print_info("Bit Depth: {}".format(track.bit_depth))
            text.print_info("Format: {}".format(track.other_format[0]))
            text.print_info("Encoded Library: {}".format(track.encoded_library_name))
            text.print_info("Other Encoded Library: {}".format(track.internet_media_type))
            text.print_info("Codec ID: {}".format(track.codec_id))
            text.print_info("Encoded Settings: {}".format(track.encoding_settings))
            print("")

def print_audio_only(file):
    verify_file_existance(file)
    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == 'Audio':
            text.print_header("Audio Track")
            text.print_info("Language: {}".format(track.other_language[1]))
            text.print_info("Codec ID: {}".format(track.codec_id))
            text.print_info("Delay: {}".format(track.delay))
            text.print_info("Format Info: {}".format(track.format))
            text.print_info("Channel #: {}".format(track.channel))
            print("")

def print_codec_info(file):
    verify_file_existance(file)
    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            text.print_header('Codec Information')
            text.print_info("File Name: {}".format(track.complete_name))
            text.print_info("Date Encoded: {}".format(track.encoded_date))
            text.print_info("Format: {}".format(track.other_format[0]))
            text.print_info("Encoded Library: {}".format(track.encoded_library_name))
            text.print_info("Other Encoded Library: {}".format(track.internet_media_type))
            text.print_info("Codec ID: {}".format(track.codec_id))
            text.print_info("Encoded Settings: {}".format(track.encoding_settings))
            print("")

def print_hashes(file):
    verify_file_existance(file)
    text.print_header("Getting hashes")
    sha1 = return_sha1_hash(file)
    sha256 = return_sha256_hash(file)
    sha512 = return_sha512_hash(file)
    md5 = return_md5_hash(file)
    uid = MediaInfo.parse(file)
    text.print_info("SHA-1 Hash: " + sha1)
    text.print_info("SHA-256 Hash: " + sha256)
    text.print_info("SHA-512 Hash: " + sha512)
    text.print_info("MD5 Hash: " + md5)
    for track in uid.tracks:
        if track.track_type == 'General':
            text.print_info("Unique ID (.mkv only): {}".format(track.unique_id))

def usage2():
    print('## Description Arguments ##')
    print('-g : Find a movie_id from a keyword. Case sensitive(only use if u know the exact name)')
    print('-s : Search for a movie, and present general information')
    print('-ss : Do a soft search. Only shows titles and movie_id')
    print('-i [movie_id] : Show all information available about a movie')
    print('--episode-map [movie_id] : Show an episode map for a tv-series')
    print('--info-sets : Print info sets for movies, people, and companys') # for IMDBpy

def get_movie_id(keyword):
    ia = imdb.IMDb()
    for m in ia.search_movie(keyword):
        id = m.getID()
        break
    
    try:
        return id
    except UnboundLocalError:
        pass # no movie found

def print_movie_id():
    keyword = input("Get Movie ID: ")
    id = get_movie_id(keyword)
    if id is None:
        text.print_error('No movie found with that title')
    else:
        print('{k} [ID: {i}]'.format(k=keyword, i=id))

def soft_search():
    ia = imdb.IMDb()
    keyword = input('Search for media: ')
    i = 0
    for m in ia.search_movie(keyword):
        i = i + 1
        id = m.getID()
        print('{z} [ID: {i}]'.format(z=m, i=id))
    
    if i == 0:
        text.print_error('No media found with that title')

def check_for_key(var, media_obj):
    try:
        media_obj[var]
        return True
    except:
        return False

def print_general_info(id, verbose=False):
    ia = imdb.IMDb()

    media = ia.get_movie(id)
    title = media['title']
    plot = media['plot'][0]
    year = media['year']
    kind = media['kind']
    genres = media['genres']
    rating = media['rating']
    runtime = media['runtime'][0]
    countries = media['countries']
    languages = media['languages']

    text.print_header("Media Description")
    text.print_info("Title: {}".format(title))
    text.print_info("ID: {}".format(media.getID()))
    text.print_info("Year: {}".format(year))
    text.print_info("Media Type: {}".format(kind))
    text.print_info("Avg. Runtime: {} mins".format(runtime))
    
    text.print_info_no_end('Genres: ')
    for x in range(len(genres)):
        print(genres[x] + ', ', end=' ')
    print("")
    text.print_info("Countries: {}".format(countries))
    text.print_info('Languages: {}'.format(languages))
    
    text.print_info('Rating: {}/10'.format(rating))
    text.print_info("Plot: {}".format(plot))

def print_specific_information(id):
    ia = imdb.IMDb()
    media = ia.get_movie(id)

    kind = media['kind']
    if kind == 'movie':
        text.print_header('Movie Information')
        o = check_for_key('original air date', media)
        if o:
            text.print_movie('Original Air Date: ', media['original air date'])
        
        w = check_for_key('writer', media)
        if w:
            text.print_movie('Writer: ', media['writer'][0])
        
        d = check_for_key('director', media)
        if d:
            text.print_movie('Director: ', media['director'][0])

        # still need to implemennt box office information
    elif kind == 'tv series':
        text.print_header('TV Information')
        sy = check_for_key('series years', media)
        if sy:
            text.print_tv("Series Years: ", media['series years'])

        s = check_for_key('seasons', media)
        if s:
            text.print_tv('Seasons: ', media['seasons'])
        
        ia.update(media, 'episodes')
        e = check_for_key('episodes', media)
        if e:
            episode_count = 0
            episodes = media['episodes']
            for e in episodes:
                episode_count = episode_count + len(episodes[e])        
            text.print_tv('Epsiode Count: ', episode_count)

def episode_map(id):
    ia = imdb.IMDb()
    
    media = ia.get_movie(id)
    kind = media['kind']
    media_title = media['title']
    text.print_info('Title: {}'.format(media_title))

    if kind == 'tv series' or kind == 'tv mini series':
        episode_count = 0
        season_count = 0
        ia.update(media, 'episodes')

        all_episodes = media['episodes']
        for e in all_episodes:
            episode_count = episode_count + len(all_episodes[e])
        
        text.print_tv('Episode Count: ', episode_count)
        season_keys = sorted(all_episodes.keys())

        for x in season_keys:
            text.print_header('Season {}'.format(x))
            for z in all_episodes[x].items():
                obj = z[1]
                episode_number = obj['episode']
                episode_title = obj['title']

                try:
                    rating = obj['rating']
                except KeyError:
                    rating = None

                try:
                    year = obj['year']
                except KeyError:
                    year = None

                try:
                    print('- Episode {en}: {t} - ({y}) - [{r}/10]'.format(en=episode_number, t=episode_title, y=year, r=round(rating)))
                except TypeError:
                    print('- Episode {en}: {t} - ({y})'.format(en=episode_number, t=episode_title, y=year))
    else:
        text.print_error('Episode map is only supported on TV Shows')

def search():
    ia = imdb.IMDb()
    ret = []
    i = 0

    keyword = input('Search for media: ')
    for m in ia.search_movie(keyword):
        i = i + 1
        id = m.getID()
        ret.insert(i, m['title'])
    text.print_good('Results Found (with duplicates): {}'.format(i))

    picker = SelectOne(choices=ret)
    choice = picker.prompt()
    id = get_movie_id(choice)
    print("")
    print_general_info(id)

def info_sets():
    ia = imdb.IMDb()
    movie_info_set = ia.get_movie_infoset()
    people_info_set = ia.get_person_infoset()
    company_info_set = ia.get_company_infoset()

    text.print_info('Movie Infoset: {}'.format(movie_info_set))
    text.print_info('People Infoset: {}'.format(people_info_set))
    text.print_info('Company Infoset: {}'.format(company_info_set))

if __name__ == "__main__":
    try:
        if sys.argv[1] == '-h':
            usage()
            print('')
            usage2()
        elif sys.argv[1] == '-e':
            print_everything(sys.argv[2])
        elif sys.argv[1] == '-v':
            print_video_only(sys.argv[2])
        elif sys.argv[1] == '-a':
            print_audio_only(sys.argv[2])
        elif sys.argv[1] == '-c':
            print_codec_info(sys.argv[2])
        elif sys.argv[1] == '-V':
            open_in_vlc(sys.argv[2])
        elif sys.argv[1] == '-b':
            open_in_handbrake(sys.argv[2])
        elif sys.argv[1] == '-k':
            print_keys(sys.argv[2])
        elif sys.argv[1] == '--hash':
            print_hashes(sys.argv[2])
        elif sys.argv[1] == '-g':
            print_movie_id()
        elif sys.argv[1] == '-ss':
            soft_search()
        elif sys.argv[1] == '-s':
            search()
        elif sys.argv[1] == '-i':
            print_general_info(sys.argv[2])
            print_specific_information(sys.argv[2])
        elif sys.argv[1] == '--episode-map':
            episode_map(sys.argv[2])
        elif sys.argv[1] == '--info-sets':
            info_sets()
        else:
            print('[!] Unknown arugment')
    except IndexError:
        print('[!] Not enough arguments')
        usage()
        print('')
        usage2()
        sys.exit(1)
