# post contents generated from chatgpt
posts = [
    {"username": "user1", "content": "This is post 1. #python #socialmedia", "likes": 15},
    {"username": "user2", "content": "Check out my new photo!", "likes": 25},
    {"username": "user3", "content": "Excited about the weekend! #weekendvibes", "likes": 30},
    {"username": "user4", "content": "Python programming is awesome #python", "likes": 20},
    {"username": "user5", "content": "Hello world!", "likes": 10}
]

total_posts = len(posts)
total_likes = sum(post["likes"] for post in posts)
total_characters = sum(len(post["content"]) for post in posts)

# Finding no of hashtags
hashtags_used = {}
for post in posts:
    hashtags = []
    for word in post["content"].split():
        if word.startswith('#'):
            hashtags.append(word)
    for hashtag in hashtags:
        hashtags_used[hashtag] = hashtags_used.get(hashtag, 0) + 1

average_length = total_characters / total_posts if total_posts > 0 else 0

print(f"Total posts: {total_posts}")
print(f"Total likes: {total_likes}")
print(f"Average post length: {average_length:.2f}")

print("\nHashtags used:")
for hashtag, count in hashtags_used.items():
    print(f"{hashtag}: {count}")
