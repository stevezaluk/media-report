#!/usr/bin/env python3
import sys, os, subprocess, hashlib
from pymediainfo import MediaInfo
from colorama import Style, Fore, Back
import imdb
from teletype.components import SelectOne, ChoiceHelper

def print_info(text):
    print(Fore.BLUE + '[i]:' + Style.RESET_ALL + text)

def print_error(text):
    print(Fore.RED + '[!]:' + Style.RESET_ALL + text)

def print_good(text):
    print(Fore.GREEN + '[+]:' + Style.RESET_ALL + text)

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
        print("[!] file not found")
        sys.exit(1)

def open_in_handbrake(file):
    verify_file_existance(file)
    execute = subprocess.Popen("open {f} -a /Applications/HandBrake.app".format(f=file), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
    if execute:
        print("Opening file in handbrake")
    else:
        print("[!] Failed to open file")
        sys.exit(1)

def open_in_vlc(file):
    verify_file_existance(file)
    execute = subprocess.Popen("open {f} -a /Applications/VLC.app".format(f=file), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
    if execute:
        print("Opening file in vlc")
    else:
        print("[!] failed to open file")

# print information
def print_keys(file):
    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == "Video":
            print("Video Keys: ", track.to_data().keys())
            print("")
        elif track.track_type == "Audio":
            print("Audio Keys: ", track.to_data().keys())
            print("")
        elif track.track_type == "Text":
            print("Text Keys: ", track.to_data().keys())
            print("")
        elif track.track_type == "General":
            print("General Keys: ", track.to_data().keys())
        elif track.track_type == "Menu":
            print("Menu Keys: ", track.to_data().keys())

def print_everything(file, verbose=False):
    verify_file_existance(file)
    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == 'General':
            print("==> General Info: ")
            print("[i] File Name: ", track.complete_name)
            print("[i] Title: ", track.title)
            print("[i] File Size: ", track.other_file_size[0])
            print("[i] Date Encoded: ", track.encoded_date)
            print("[i] Unique ID: ", track.unique_id)
            print("[i] Writing Application: ", track.writing_application)
            print("[i] Writing Library:", track.writing_library)
            print("[i] Format: ", track.format)
            print("[i] Duration: ", track.other_duration[1])
            print("[i] Container: ", track.container)
            print("")
        elif track.track_type == 'Video':
            print("==> Video Track: ")
            print("[i] Resolution: ", track.width, 'x', track.height)
            print("[i] Pixel Aspect Ratio: ", track.pixel_aspect_ratio)
            print("[i] Frame Count: ", track.frame_count)
            print("[i] Frame Rate (FPS): ", track.frame_rate)
            print("[i] Bit Rate: ", track.bit_rate)
            print("[i] Bit Depth: ", track.bit_depth)
            print("[i] Format: ", track.other_format[0])
            print("[i] Encoded Library: ", track.encoded_library_name)
            print("[i] Other Encoded Library: ", track.internet_media_type)
            print("[i] Codec ID: ", track.codec_id)
            if verbose:
                print("[i] Encoded Settings: ", track.encoding_settings)
            print("")
        elif track.track_type == 'Audio':
            print("==> Audio Track:")
            print("[i] Language: ", track.other_language[1])
            print("[i] Codec ID: ", track.codec_id)
            print("[i] Format Info: ", track.format)
            print("[i] Channel #: ", track.channel)
            print("")
        elif track.track_type == 'Text':
            print("==> Subtitles Track:")
            print("[i] Hard Coded: " + track.forced)
            print("")


def print_video_only(file):
    verify_file_existance(file)
    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            print("==> Video Track: ")
            print("[i] File Name: " + file)
            print("[i] File Size: ", track.file_size)
            print("[i] Date Encoded: ", track.encoded_date)
            print("[i] Duration: ", track.other_duration[1])
            print("[i] Resolution: ", track.width, 'x', track.height)
            print("[i] Pixel Aspect Ratio: ", track.pixel_aspect_ratio)
            print("[i] Frame Count: ", track.frame_count)
            print("[i] Frame Rate (FPS): ", track.frame_rate)
            print("[i] Bit Rate: ", track.bit_rate)
            print("[i] Bit Depth: ", track.bit_depth)
            print("[i] Format: ", track.other_format[0])
            print("[i] Encoded Library: ", track.encoded_library_name)
            print("[i] Other Encoded Library: ", track.internet_media_type)
            print("[i] Codec ID: ", track.codec_id)
            print("[i] Encoded Settings: ", track.encoding_settings)
            print("\n")

def print_audio_only(file):
    verify_file_existance(file)
    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == 'Audio':
            print("==> Audio Track:")
            print("[i] Language: ", track.other_language[1])
            print("[i] Codec ID: ", track.codec_id)
            print("[i] Delay: ", track.delay)
            print("[i] Forced: ", track.forced)
            print("\n")

def print_codec_info(file):
    verify_file_existance(file)
    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            print('==> Codec Information')
            print("[i] File Name: " + file)
            print("[i] Date Encoded: ", track.encoded_date)
            print("[i] Format: ", track.other_format[0])
            print("[i] Encoded Library: ", track.encoded_library_name)
            print("[i] Other Encoded Library: ", track.internet_media_type)
            print("[i] Codec ID: ", track.codec_id)
            print("[i] Encoded Settings: ", track.encoding_settings)
            print("")

def print_hashes(file):
    verify_file_existance(file)
    print("Getting hashes...")
    sha1 = return_sha1_hash(file)
    sha256 = return_sha256_hash(file)
    sha512 = return_sha512_hash(file)
    md5 = return_md5_hash(file)
    uid = MediaInfo.parse(file)
    print("SHA-1 Hash: " + sha1)
    print("SHA-256 Hash: " + sha256)
    print("SHA-512 Hash: " + sha512)
    print("MD5 Hash: " + md5)
    for track in uid.tracks:
        if track.track_type == 'General':
            print("Unique ID (.mkv only): ", track.unique_id)

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
        print('[!] No movie found with that title')
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
        print('[!] No media found with that title')
        sys.exit(1)

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

    print("==> Media Description")
    print("[i] Title: {}".format(title))
    print("[i] ID: {}".format(media.getID()))
    print("[i] Year: {}".format(year))
    print("[i] Media Type: {}".format(kind))
    print("[i] Avg. Runtime: {} mins".format(runtime))
    print("[i] Genres: ", genres)
    print("[i] Countries: ", countries)
    print('[i] Languages: ', languages)
    print('[i] Rating: {}/10'.format(rating))
    print("[i] Plot: {}".format(plot))

def print_specific_information(id):
    ia = imdb.IMDb()
    media = ia.get_movie(id)

    kind = media['kind']
    if kind == 'movie':
        print('==> Movie Information')
        o = check_for_key('original air date', media)
        if o:
            print('[M] Original Air Date: ', media['original air date'])
        
        w = check_for_key('writer', media)
        if w:
            print('[M] Writer: ', media['writer'][0])
        
        d = check_for_key('director', media)
        if d:
            print('[M] Director: ', media['director'][0])

        # still need to implemennt box office information
    elif kind == 'tv series':
        print('==> TV Information')
        sy = check_for_key('series years', media)
        if sy:
            print("[TV] Series Years: ", media['series years'])

        s = check_for_key('seasons', media)
        if s:
            print('[TV] Seasons: ', media['seasons'])
        
        ia.update(media, 'episodes')
        e = check_for_key('episodes', media)
        if e:
            episode_count = 0
            episodes = media['episodes']
            for e in episodes:
                episode_count = episode_count + len(episodes[e])        
            print('[TV] Epsiode Count: ', episode_count)

def episode_map(id):
    ia = imdb.IMDb()
    
    media = ia.get_movie(id)
    
    kind = media['kind']

    if kind == 'tv series':
        print('==> Episode Map')
        title = media['title']
        print('[i] Title: ', title)
        s = check_for_key('seasons', media)
        if s:
            print('[i] Season Count: ', media['seasons'])
        
        ia.update(media, 'episodes')
        e = check_for_key('episodes', media)
        if e:
            episode_count = 0
            episodes = media['episodes']
            for e in episodes:
                episode_count = episode_count + len(episodes[e])
            print('[i] Epsiode Count: ', episode_count)
            for z in episodes:
                all_items = episodes[z].items()
                print('==> Season {}: '.format(z))
                for a in all_items:
                    print('-- Episode #{}: '.format(a[0]), a[1])
        else:
            print('[!] Tv Show does not have episodes listed')
            sys.exit(1)
    else:
        print('[!] Episode map only works for tv series')
        sys.exit(1)

def search():
    ia = imdb.IMDb()
    ret = []
    i = 0

    keyword = input('Search for media: ')
    for m in ia.search_movie(keyword):
        i = i + 1
        id = m.getID()
        ret.insert(i, m['title'])
    print('[+] Results Found (with duplicates): ', i)

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

    print('[i] Movie Infoset: ', movie_info_set)
    print('[i] People Infoset: ', people_info_set)
    print('[i] Company Infoset: ', company_info_set)

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
