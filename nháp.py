import pygame
import webbrowser
class TextButton:
    def __init__(self,text,position):
        self.text = text
        self.position =position
    def is_mouse_on_text(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.position[0]< mouse_x<self.position[0]+self.text_box[2] and self.position[1]<mouse_y<self.position[1]+self.text_box[3]:
            return True
        else:
            return False
    def draw(self):
        font = pygame.font.SysFont('arial',20)
        text_render = font.render(self.text, True, (0, 0, 255))
        self.text_box = text_render.get_rect()
        if self.is_mouse_on_text():     # self là đại diện cho TextButton . function là để dùng chức năng của function cho cả hàm đấy
            text_render = font.render(self.text,True,(0,0,255))
            pygame.draw.line(screen, blue, (self.position[0], self.position[1] + self.text_box[3] + 3),(self.position[0] + self.text_box[2],self.position[1] + self.text_box[3] + 3))
        else:
            text_render = font.render(self.text, True, (0, 0, 0))
        pygame.draw.rect(screen,white,(self.position[0],self.position[1],self.text_box[2],self.text_box[3]))
        screen.blit(text_render, self.position) # hàm vẽ lên màn hình (chữ, vị trí X,Y)
pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chương trình Pygame đầu tiên")
white = (255, 255, 255)
blue =(0,0,255)
running = True
clock = pygame.time.Clock()
class Video:
    def __init__(self,title,link):
        self.title = title
        self.link = link
        self.seen = False
    def open(self):
        webbrowser.open(self.link)
        self.seen = True
class Playlist:
    def __init__(self,name,description,rating,videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos
def read_from_text(file):
    videos =[]
    total = file.readline()
    for i in range (int(total)):
        title = file.readline()
        link = file.readline()
        video = Video(title,link)
        videos.append(video)
    return videos
def read_playlist_txt(file):
    playlist_name = file.readline()
    playlist_description = file.readline()
    playlist_rating = file.readline()
    playlist_video = read_from_text(file)
    playlist = Playlist(playlist_name,playlist_description,playlist_rating,playlist_video)
    return playlist
def read_playlists_txt():
    playlists = []
    with open('video.txt', 'r') as file:
        total = file.readline()
        for i in range(int(total)):
            playlist = read_playlist_txt(file)
            playlists.append(playlist)
    return playlists
playlists = read_playlists_txt()
# playlist = playlists[1]# phải gọi hàm ra
list_videos = []
margin = 50
playlists_btn_name = []
for i in range(len(playlists)):
    playlists_btn = TextButton(playlists[i].name.rstrip(),(50,50+ margin*i))
    playlists_btn_name.append(playlists_btn)
playlist_choice = None
while running:
    clock.tick(60)
    screen.fill(white)
    for name in playlists_btn_name:
        name.draw()
    for i in range(len(list_videos)):
        list_videos[i].draw()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  # hàm hoạt động khi nhậ gtri True
            for i in range(len(playlists_btn_name)):
                if playlists_btn_name[i].is_mouse_on_text():
                    list_videos = []
                    playlist_choice = i
                    for j in range(len(playlists[i].videos)):
                        video_btn = TextButton(playlists[i].videos[j].title.rstrip(), (350, 50 + margin * j))
                        list_videos.append(video_btn)
            if playlist_choice != None:
                for i in range(len(list_videos)):
                    if list_videos[i].is_mouse_on_text():
                        playlists[playlist_choice].videos[i].open()
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()



