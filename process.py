import os
from tqdm import tqdm

for filename in tqdm(os.listdir("source/_posts")):
    if filename[-3:] != ".md":
            continue
    try:
        with open(os.path.join("source/_posts", filename), "r", encoding="utf8") as f:
            blog = f.read()
    except:
        print(filename)
        break
    blog = blog.replace("/cdn.", "/gcore.")
    with open(os.path.join("source/_posts_2", filename), "w", encoding="utf8") as f:
        f.write(blog)