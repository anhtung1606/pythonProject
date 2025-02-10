import webbrowser
class Video:
    def __init__(self,title,link):
        self.title = title
        self.link = link
    def open(self):
        webbrowser.open(self.link)
class Playlist:
    def __init__(self,name,description,rating,videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos
def read_video():
   read_link = input('enter your link: ') + '\n'
   read_title = input('enter your title: ') +'\n'
   video = Video(read_title,read_link)
   return video
def print_video(video):
    print('your link: ' , video.link, end='')
    print('your title: ', video.title, end='')
def read_videos():
    numbers = int(input('how many videos: '))
    videos =[]
    for i in range (numbers):
        print('video ', i+1)
        vid = read_video()
        videos.append (vid)
    return videos
def print_videos(videos):
    vid = len(videos)
    for i in range(vid):
        print('video ' , i+1)
        print_video(videos[i])
def write_to_text(videos,file):
        file.write(str(len(videos)) + '\n')
        for i in range(len(videos)):
            file.write(videos[i].title )
            file.write(videos[i].link )
def read_from_text(file):
    videos =[]
    total = file.readline()
    for i in range (int(total)):
        title = file.readline()
        link = file.readline()
        video = Video(title,link)
        videos.append(video)
    return videos
def read_playlist():  # option 1
    playlist_name = input('enter playlist name: ') + '\n'
    playlist_description = input('enter description: ') +'\n'
    playlist_rating =input('enter rating(1-5): ') +'\n'
    playlist_videos = read_videos()
    playlist = Playlist(playlist_name,playlist_description,playlist_rating,playlist_videos)
    return playlist
def write_playlist_txt(playlist):   #option 7
    with open ('video.txt','w') as file:
        file.write(playlist.name )
        file.write(playlist.description  )
        file.write(playlist.rating  )
        write_to_text(playlist.videos, file)

def read_playlist_txt():
    with open ('video.txt','r') as file:
        playlist_name = file.readline()
        playlist_description = file.readline()
        playlist_rating = file.readline()
        playlist_video = read_from_text(file)
    playlists = Playlist(playlist_name,playlist_description,playlist_rating,playlist_video)
    return playlists
def print_playlist(playlists):  #option 2
    print(playlists.name,playlists.description,playlists.rating, end="")
    print_videos(playlists.videos)
def select_in_range(prompt,min,max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    choice= int(choice)
    return choice
def play_video(playlist):   # option 3
    print_videos(playlist.videos)
    total = len(playlist.videos)
    choice = select_in_range('play a music song(1,'+ str(total) + '): ',1,total)
    print('Open video: '+ playlist.videos[choice-1].title + playlist.videos[choice-1].link)
    playlist.videos[choice -1].open()
def add_video(playlist):    # option 4
    new_title = input('enter your title: ') + '\n'
    new_link = input('enter your link: ') + '\n'
    new_video = Video(new_title,new_link)
    playlist.videos.append(new_video)
def update_playlist(playlist):  # option 5
    print('update name (1):')
    print('update description(2):')
    print('update rating(3):')
    choice = select_in_range('choice update(1,3): ',1,3)
    if choice == 1:
        playlist.name = input('enter your new name: ') +'\n'
        return playlist.name
    elif choice == 2:
        playlist.description = input('enter your new description: ') +'\n'
        return playlist.description
    else:
        playlist.rating = str(select_in_range('enter your new rating(1-5): ',1,5)) + '\n'
        return playlist.rating
def remove_video(playlist):    # option 6
    print_videos(playlist.videos)
    delete = select_in_range('enter your video which you want to remove: ',1,len(playlist.videos))
    del playlist.videos[delete-1]
    print('delete successfully!!!')
def show_menu():
    print('|--------------------------|')
    print('|option 1: make a playlist.|')
    print('|option 2: show playlist.  |')
    print('|option 3: play video.     |')
    print('|option 4: add new video.  |')
    print('|option 5: update playlist.|')
    print('|option 6: remove video.   |')
    print('|option 7: save and exit.  |')
    print('|--------------------------|')
def main():
    # playlist = read_playlist()
    # write_playlist_txt(playlist)
    # playlist = read_playlist_txt()
    # print_playlist(playlist)
    playlist = read_playlist_txt()
    try:
        playlist = read_playlist_txt()
        print('successfully')
    except:
        print('welcome first user')
    while True:
        show_menu()
        choice = select_in_range('choice a numbers(1,2,3,4,5,6,7): ',1,7)
        if choice == 1:
            playlist = read_playlist()
            input('press enter to continue')
        elif choice == 2:
            print_playlist(playlist)
            input('press enter to continue')
        elif choice == 3:
            play_video(playlist)
            input('press enter to continue')
        elif choice ==4:
            add_video(playlist)
            input('press enter to continue')
        elif choice == 5:
            update_playlist(playlist)
            input('press enter to continue')
        elif choice ==6:
            remove_video(playlist)
        elif choice == 7:
            write_playlist_txt(playlist)
            break
main()