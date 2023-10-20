class Song:
    
    count = 0
    
    def __init__(self,name,artist,genres):
        self.name = name 
        self.artist = artist
        self.genres = genres
        
    def add_song_to_count(self):
        self.count += 1
    
    def add_to_genres(self):
        self.genres = []
        
    def add_to_artists(self):
        self.artist = []
    pass
