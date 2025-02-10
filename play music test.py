import webbrowser
class Video:
    def __init__(self,title,link):
        self.title = title
        self.link = link
class Playlist:
    def __init__(self,name,description,rating,videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos
def write_playlist_to_txt(playlist):    # để chuyền ko ghi đề lên thì mở 1 file,file còn lại truyền vào
    with open('data2.txt', 'w') as file:
        file.write(playlist.name )
        file.write(playlist.description)
        file.write(playlist.rating)
        write_to_txt(playlist.videos,file)
def read_playlist_txt():
    with open('data2.txt','r') as file:
        name = file.readline()
        description = file.readline()
        rating = file.readline()
        videos =read_to_txt(file)
        playlist = Playlist(name,description,rating,videos)
        return playlist
def print_playlist(playlists):
    print(playlists.name,playlists.description,playlists.rating,end='')
    print_videos(playlists.videos)
def read_video():
    title = input('Enter your title: ')+ '\n'
    link = input('Enter your link: ')+'\n'
    video = Video(title,link)
    return video
def print_video(video):
    print('your title: ',video.title,end='')
    print('your link: ',video.link,end='')
def read_videos():
    videos =[]
    numbers = int(input('how many video: '))
    for i in range(numbers):
        print('video ',i+1,)
        a = read_video()
        videos.append(a)
 # vì hàm read_video đc mở lên nên đã lưu link và title vào class -- sau đó lại tiếp tục vòng lặp for và lưu tiếp vid 2
 #    => nên list có 2 phần tử là vid 1, vid 2 trong vid 1 chứa class title và class link
 #bản chất list videos là 2 địa chỉ 1 và 2 trong 1 thì sẽ có class title,link trong 2... và đều được gọi ra bởi videos[i].link,title
    return videos
# def print_videos(videos):
#     numbers = len(videos)
#     for i in range(numbers):
#         print_video(videos[i]) # videos là danh sách gồm địa chỉ vid 1 và địa chỉ vid 2 trong vid 1 chứa class link,title
                            # vì thế nên khi print videos[i] nó sẽ chỉ hiện địa chỉ
#         vì thế trong hàm print_video nó sẽ tự gắn class link,title vào
def print_videos(videos):
    for i in range(len(videos)):
        print('Videos:',i+1)
        print_video(videos[i])
def write_to_txt(videos,file):
        file.write(str(len(videos))+ '\n')
        for i in range(len(videos)):
            file.write(str(videos[i].title))
            file.write(str(videos[i].link))
def read_to_txt(file):
    videos = []
    total = file.readline()
    for i in range (int(total)):
        title = file.readline()
        link = file.readline()
        video= Video(title,link)
        videos.append(video)
    return videos
# video[i] : là địa chỉ vid1 và vid2 và .title là: gtri class title trong vid1,2
# dùng vòng lặp for vì có 2 giá trị nếu không dùng nó sẽ chỉ chạy title vid 1 đầu tiên

def read_playlist():#1 lỗi dấu xuống dòng có thể: do cả input (và chỉ sửa đc = cách thêm dấu xuống dòng)
    name = input('enter your name playlist: ') + '\n'
    description = input('enter your description playlist: ')+ '\n'
    rating = input('enter your rating playlist: ')+ '\n'
    videos = read_videos()
    playlist = Playlist(name,description,rating,videos)
    return playlist
def show_menu():
    print('option 1: create album ')
    print('option 2: show album ')
    print('option 3: play music ')
    print('option 4: add new video ')
    print('option 5: update')
    print('option 6: deleted')
    print('option 7: save and exit')
def range_number(prompt,min,max):
    choice =input(prompt)
    while not choice.isdigit() or int(choice) <min or int(choice)>max:
        choice = input(prompt)
    choice = int(choice)
    return choice
def open_link_youtube(playlist):
    print_videos(playlist.videos)
    choice = range_number('enter your music ',0, len(playlist.videos))
    webbrowser.open(playlist.videos[choice-1].link)
def add_new_video(playlist):
    title = input('enter your title: ')+ '\n'
    link = input('enter your link: ')
    video = Video(title,link)
    playlist.videos.append(video)
def update_playlist(playlist):
    print_playlist(playlist)
    choice = range_number('what option you want to update: ',0,4)
    if choice == 1:
        playlist.name = input('Update new name to your playlist: ') + '\n'
        return playlist.name
    if choice ==2:
        playlist.description = input('Update new description: ') + '\n'
        return playlist.description
    else:
        playlist.rating = input('update new rating: ')+'\n'
        return playlist.rating
def remove_video(playlist):
    print_videos(playlist)
    choice = range_number('enter your video were deleted: ',0,len(playlist.videos))
    del playlist.videos[choice-1]
    print('Remove successfully!!!')
def main():
    # playlist = read_playlist()
    # write_playlist_to_txt(playlist)
    play = read_playlist_txt() #1để đọc lại playlist cũ đã lưu
    # print_playlist(playlist)

    while True: #1 vòng while true sẽ luôn quay về chạy lại từ đầu nếu ko break
        show_menu()
        choice = range_number('enter your option(1-7): ',1,7)
        if choice == 1:
           play = read_playlist() #1để tạo cái mới phải truyền vào biến mới của nó ( cái này để thay đổi biến cũ)
        elif choice == 2:
            print_playlist(play)
        elif choice ==3:
            open_link_youtube(play)# vì vòng while dùng thuộc tính playlist nên tất cả các hàm trong phải cùng dùng
                                # Ex: cách gọi phần tử trong thuộc tính playlist.videos[0,1].title,mn,
        elif choice ==4:
            add_new_video(play)
        elif choice ==5:
            update_playlist(play)
        # elif choice == 6:
           # remove_video(play)
        else:
            write_playlist_to_txt(play)
            break

main()






