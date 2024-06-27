songs = []

def add_song(name,artist):
    songs.append({"name" : name,"artist" : artist})

def search(keyword):
    is_success = False
    for song in songs:
        if keyword.lower() in song["name"].lower() or keyword.lower() in song["artist"].lower():
            is_success = True
            print(f"Found : (Name: {song['name']}, Artist: {song['artist']})")

    if not is_success:
        print("Not found")

def remove_song(name):
    global songs
    songs = [song for song in songs if song["name"].lower() != name.lower()]
    print("Success")

def display_songs():
    if len(songs) == 0:
        print("List is empty")
    else:
        for song in songs:
            print(f"Name : {song['name']}\tArtist : {song['artist']}")

add_song("Music 1","Artist A")
add_song("Music 2","Artist B")
add_song("Music 3","Artist C")
display_songs()
search("Music 2")
search("Artist C")
remove_song("Music 2")
display_songs()

#PART B
print("----------------------------------------------------------------------------------------------------------------------------------------------")
# Assuming 3 subjects in total

scores = [[50,60,70],
          [60,70,80],
          [50,70,20]]

for i in range(len(scores)):
    score = scores[i]

    average = sum(score)/len(score)
    maximum = max(score)
    minimum = min(score)

    print(f"Subject {i+1}")
    print(f"Average : {average}")
    print(f"Maximum : {maximum}")
    print(f"Minimum : {minimum}")

