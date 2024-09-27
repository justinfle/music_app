import json
import os
import pandas as pd
import time
import math

class Song:
    def __init__(self, name, artist, album, genre, duration):
        self.name = name
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration

    def __str__(self):
        return f"{self.name} by {self.artist} - Album: {self.album}, Genre: {self.genre}, Duration: {self.duration}"

    def to_dict(self):
        return {
            "name": self.name,
            "artist": self.artist,
            "album": self.album,
            "genre": self.genre,
            "duration": self.duration
        }

    @staticmethod
    def from_dict(data):
        return Song(data['name'], data['artist'], data['album'], data['genre'], data['duration'])

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    def __le__(self, other):
        return self.name.lower() <= other.name.lower()

    def __gt__(self, other):
        return self.name.lower() > other.name.lower()

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        self.songs = [song for song in self.songs if song.name != song_name]

    def rename(self, new_name):
        self.name = new_name

    def to_dict(self):
        return {
            "name": self.name,
            "songs": [song.to_dict() for song in self.songs]
        }

    @staticmethod
    def from_dict(data):
        playlist = Playlist(data['name'])
        playlist.songs = [Song.from_dict(song_data) for song_data in data['songs']]
        return playlist

    def __str__(self):
        return f"Playlist: {self.name}, Songs: {len(self.songs)}"


class MusicApp:
    def __init__(self, data_file='music_data.json', csv_file='charts_renew.csv'):
        self.data_file = data_file
        self.csv_file = csv_file
        self.songs = []
        self.playlists = []
        self.load_data()
        self.load_songs_from_csv()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.songs = [Song.from_dict(song_data) for song_data in data.get('songs', [])]
                self.playlists = [Playlist.from_dict(pl_data) for pl_data in data.get('playlists', [])]
            print("Data loaded successfully.")
        else:
            print("No data file found. Starting with an empty database.")

    def save_data(self):
        data = {
            "songs": [song.to_dict() for song in self.songs],
            "playlists": [playlist.to_dict() for playlist in self.playlists]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")

    def load_songs_from_csv(self):
        if os.path.exists(self.csv_file):
            try:
                df = pd.read_csv(self.csv_file)
                for _, row in df.iterrows():
                    song = Song(row['name'], row['artist'], row['album'], row['genre'], row['duration'])
                    if song not in self.songs:
                        self.songs.append(song)
                print(f"Loaded {len(df)} songs from {self.csv_file}.")
            except Exception as e:
                print(f"Failed to load songs from CSV: {e}")
        else:
            print(f"CSV file {self.csv_file} not found.")

    # Sortieralgorithmen
    def bubblesort_songs(self):
        for i in range(len(self.songs)):
            for j in range(0, len(self.songs) - i - 1):
                if self.songs[j] > self.songs[j + 1]:
                    self.songs[j], self.songs[j + 1] = self.songs[j + 1], self.songs[j]
        print("Songs sorted using Bubblesort.")
        self.display_all_songs()

    def mergesort_songs(self):
        self.songs = self._mergesort(self.songs)
        print("Songs sorted using Mergesort.")
        self.display_all_songs()

    def _mergesort(self, songs):
        if len(songs) <= 1:
            return songs
        mid = len(songs) // 2
        left = self._mergesort(songs[:mid])
        right = self._mergesort(songs[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        sorted_list = []
        while left and right:
            if left[0] < right[0]:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        sorted_list.extend(left or right)
        return sorted_list

    def blocksort_songs(self):
        n = len(self.songs)
        block_size = int(math.sqrt(n))
        for i in range(0, n, block_size):
            self.songs[i:i + block_size] = sorted(self.songs[i:i + block_size])
        print("Songs sorted using Blocksort.")
        self.display_all_songs()

    def quicksort_songs(self):
        self.songs = self._quicksort(self.songs)
        print("Songs sorted using Quicksort.")
        self.display_all_songs()

    def _quicksort(self, songs):
        if len(songs) <= 1:
            return songs
        pivot = songs[len(songs) // 2]
        left = [x for x in songs if x < pivot]
        middle = [x for x in songs if x == pivot]
        right = [x for x in songs if x > pivot]
        return self._quicksort(left) + middle + self._quicksort(right)

    # Suchalgorithmen
    def linear_search(self, search_term):
        return [song for song in self.songs if search_term.lower() in song.name.lower() or search_term.lower() in song.artist.lower()]

    def binary_search(self, search_term):
        self.songs = self._quicksort(self.songs)
        low, high = 0, len(self.songs) - 1
        results = []
        while low <= high:
            mid = (low + high) // 2
            if search_term.lower() == self.songs[mid].name.lower() or search_term.lower() == self.songs[mid].artist.lower():
                results.append(self.songs[mid])
                break
            elif search_term.lower() < self.songs[mid].name.lower():
                high = mid - 1
            else:
                low = mid + 1
        return results

    def search_songs_advanced(self):
        search_term = input("Enter song name or artist to search: ")
        print("1. Linear Search")
        print("2. Binary Search")
        choice = input("Choose search algorithm: ")

        if choice == '1':
            results = self.linear_search(search_term)
        elif choice == '2':
            results = self.binary_search(search_term)
        else:
            print("Invalid choice. Returning to main menu.")
            return

        if results:
            print("Search Results:")
            for song in results:
                print(song)
        else:
            print("No songs found.")

    def display_all_songs(self):
        if not self.songs:
            print("No songs available.")
        else:
            print("\n--- All Songs ---")
            for song in self.songs:
                print(song)

    def main_menu(self):
        while True:
            print("\n--- Music App ---")
            print("1. Add New Song")
            print("2. Create Playlist")
            print("3. Add Song to Playlist")
            print("4. Search Songs")
            print("5. Advanced Search")
            print("6. Sort Songs")
            print("7. Display All Songs")
            print("8. Display Playlists")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_song()
            elif choice == '2':
                self.create_playlist()
            elif choice == '3':
                self.add_song_to_playlist()
            elif choice == '4':
                self.search_songs()
            elif choice == '5':
                self.search_songs_advanced()
            elif choice == '6':
                self.quicksort_songs()
            elif choice == '7':
                self.display_all_songs()
            elif choice == '8':
                self.display_playlists()
            elif choice == '9':
                self.save_data()
                print("Exiting the app.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = MusicApp()
    app.main_menu()
