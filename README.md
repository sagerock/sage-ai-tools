# sage-ai-tools

I wanted to start contributing some items that I am using on my LLM journey.

I am interested in taking information from different file types, uploading it to a Pinecone Vector Database and then creating a front-end chatbot.

The front-end tool I'm using right now is based on [stephansturges/GPTflix](https://github.com/stephansturges/GPTflix). I'll just contribute any information over there if I have anything to say about that. 

But I'll add tools I've cobbled together through various tutorials and documentation here. 

## directoryloader.py

This code looks really simple. And it is. But because I'm super new to this all, this took several weeks for me to put together. And it is all thanks to other people that put up videos and blog posts helping all of us to learn this stuff. That's why I'm building this. It's just a way for me to give back in thanks to all the people who helped me.

If there is a better way to do these things, or if you think something I've done is wrong, just let me know in the "Discussions" section. 

### It's all behind the scenes.

While this code is simple enough, getting it to run was definitely NOT simple for me. 

This is using "Unstructured" to load the files. I wanted this because I would like to be able to load a variety of different files. Currently, Unstructured can load these file types: .txt, .docx, .pptx, .jpg, .png, .eml, .html, and .pdf

That's super cool, but getting it all to play nice on your computer is defintely NOT super cool. 

You can read the [Langchain documents here](https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/unstructured_file.html) on how to use Unstructured. 

The biggest issue I had was installing detectron2. I tried for hours to get it to run on Windows. They tell you that it is only supported on Linux or macOS [here](https://detectron2.readthedocs.io/en/latest/tutorials/install.html). But there are several really good tutorials that swear you can get it to run on your PC. I never was able to get it to run. 

So, I'm running all of this on a Mac. But even that wasn't particularly easy. I used [this guide](https://knowing.net/posts/2021/11/install-detectron2-draft/) on how to install Detectron2 on a Mac in CPU mode. The key for me was to be sure I was running Anaconda and I created a new environment that was running Python 3.8. 

I don't know if it's possible to run it in GPU mode. I suspect it is. But I had so much trouble getting to this point, I'm just happy I can get it to run at all. 

You also need to have something like Homebrew running. On top of being totally new to all this, I also am not a Mac guy. I usually do this kind of work on a PC. So, getting Homebrew was exciting. Not to mention that sometimes code will say to use "yarn" or "npm". But you just need to know that you are going to use "brew". 

[Here's a tutorial on installing Homebrew on a Mac](https://mac.install.guide/homebrew/3.html)

I will probably do a video of me attempting to recreate all of this so you can watch me do a walkthrough of it. 

I think there is value in me offering this content because I'm new to all this stuff and people that need the help are probably new too. So we kind of speak that "new" language. 

I'll help when and if I can. I'm not planning on setting up a discord. Maybe it's because I'm old, but I just don't find that text-vomit structure all that helpful. So, I'll probably just stick to this github discussion board. 

I've started (a Youtube Playlist of my LLM Journey here)[https://www.youtube.com/playlist?list=PLFLz8V0zGwuYsJWvS9XaaS4pdrtUGkgsi]


