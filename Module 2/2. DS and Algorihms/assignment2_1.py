class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def skip_current_song(self):
        if not self.is_empty():
            self.enqueue(self.dequeue())

    def display_playlist(self):
        if not self.is_empty():
            print("Current Playlist:")
            for i in range(len(self.items)):
                print(f"{i+1}. {self.items[i]}")
        else:
            print("Playlist is empty.")

playlist = Queue()

playlist.enqueue("Happy")
playlist.enqueue("Uptown Funk")
playlist.enqueue("Can't Stop the Feeling!")

playlist.display_playlist()

playlist.skip_current_song()

playlist.display_playlist()

print("\nPlaying the next song...")
next_song = playlist.dequeue()
print(f"Next song: {next_song}")

playlist.display_playlist()
