import requests
from models.post import Post

post = Post(
    "Como comer naranjas sin poner caras", 
    "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua", 
    "1"
)

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post.to_json(),
headers={
    "Content-Type": "application/json; charset=UTF-8"
})

if (response.ok):
    print(f"Post sin ID {post.get_id()}")
    print(response.json())
    post = Post.from_json(response.text)
    print(f"Post con ID: {post.get_id()} | Titulo: {post.title}")
else:
    print(response.text)