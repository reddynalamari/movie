import customtkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk
import key
from PIL import Image, ImageTk
import webbrowser
from tkinter import messagebox as mb

SEARCH_MOVIE_URL = "https://api.themoviedb.org/3/search/movie"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"


total = 0
def get_poster_path(movie_name, i=0):
    global total
    params = {
        "api_key": key.key,
        "query": movie_name,
        "language": "en-US"
    }
    try:
        d = dict()
        response = requests.get(SEARCH_MOVIE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        temp = (data)["results"]
        total = len(temp)
        # for i in temp:
        #     print(i)
        if data["results"]:
            movie = data["results"][i]
            title = movie["title"]
            release_date = movie.get("release_date", "Unknown")
            poster_path = movie.get("poster_path")
            if poster_path:
                full_poster_url = f"{IMAGE_BASE_URL}{poster_path}"
                print(full_poster_url)
                d["movie"] = movie['title']
                d["date"] = release_date
                d["url"] = full_poster_url
                d["overview"] = movie['overview']
                d["id"] = movie["id"]
                return d
            else:
                full_poster_url = f"https://github.com/noname25495/novafork/blob/main/placeholder.jpeg"
                d["movie"] = movie['title']
                d["date"] = release_date
                d["url"] = full_poster_url
                d["overview"] = movie['overview']
                d["id"] = movie["id"]
                mb.showinfo("Ping Pong","No poster available for this movie.")
                return d
        else:
            mb.showinfo("Ping Pong","No results found for the movie.")
            return None
    except Exception as e:
        mb.showerror("Ping Pong",f"Error: {e}")
        return None

root = tk.CTk()
root.config(height=900, width=750)
root.resizable(False,False)
tk.CTkLabel(master=root, text="PING PONG Movies Hub", font=("Monospace",40,"bold")).place(x=50,y=10)
class ping_pong():
    def __init__(self):
        self.num = 0
        self.poster_label = tk.CTkLabel(master=root,text=" ")
        self.poster_label.place(x=100,y=180)

    def movie_name(self):
        self.movie_name_enter = tk.CTkEntry(master=root)
        self.movie_name_enter.place(x=100,y=100)
        submit = tk.CTkButton(master=root, text = "SEARCH", command=self.search)
        submit.place(x=300,y=100)
    
    def search(self):
        self.num = 0
        self.name = self.movie_name_enter.get()
        self.data = get_poster_path(self.name,self.num)
        if self.data:
            self.data_screen()
    
    global total

    def data_screen(self):
        data = self.data
        # print(data)
        try:
            self.a.configure(text=" ")
            self.results.configure(text=" ")
            self.relese.configure(text=" ")
            self.poster_label.configure(text=" ")
        except:
            "Lost in your eyes"
        self.a = tk.CTkLabel(master=root, font=("Monospace",20,"bold"), anchor="center", width=450)
        self.a.place(x=50,y=150)
        self.a.configure(text=data["movie"])
        self.display_poster()
        o = tk.CTkTextbox(master=root, wrap="word",width=550, height=150)
        o.place(x=50,y=550)
        o.insert(index=tk.END,text=data["overview"])
        self.relese = tk.CTkLabel(master=root, text=f'Released on {data["date"]}', font=("Monospace",20))
        self.relese.place(x=350,y=450)
        tk.CTkButton(master=root, text="Server 1", font=("Monospace",20), command=self.s1).place(x=400, y=200)
        tk.CTkButton(master=root, text="Server 2", font=("Monospace",20), command=self.s2).place(x=400, y=250)
        self.p = tk.CTkButton(master=root, text="Prev", font=("Monospace",20), command=self.prev, width=100)
        self.p.place(x=350, y=350)
        self.p.configure(state=tk.DISABLED)
        self.n = tk.CTkButton(master=root, text="Next", font=("Monospace",20), command=self.next, width=100)
        self.n.place(x=480, y=350)
        self.results = tk.CTkLabel(master=root, text=f"Showing: {self.num+1}/{total}")
        if self.num+1 == total:
            self.n.configure(state=tk.DISABLED)
        self.results.place(x=420, y=400)
    

    def next(self):
        if self.num < total:
            self.num += 1
            self.data = get_poster_path(self.name,self.num)
            if self.data:
                self.data_screen()
            self.results.configure(text=f"Showing: {self.num+1}/{total}")
        if self.num == total-1:
            self.n.configure(state=tk.DISABLED)
        if self.num > 0:
            self.p.configure(state=tk.NORMAL)
        if self.num < total-1:
            self.n.configure(state=tk.NORMAL)
            
    
    def prev(self):
        print(self.num)
        if self.num > 0:
            self.p.configure(state=tk.NORMAL)
            self.num -= 1
            self.data = get_poster_path(self.name,self.num)
            if self.data:
                self.data_screen()
            self.results.configure(text=f"Showing: {self.num+1}/{total}")
        if self.num == 0:
            self.p.configure(state=tk.DISABLED)
        if self.num > 0:
            self.p.configure(state=tk.NORMAL)
        if self.num < total-1:
            self.n.configure(state=tk.NORMAL)
    

    def display_poster(self):
        try:
            img_data = requests.get(self.data["url"]).content
            img = Image.open(BytesIO(img_data))
            img = img.resize((300, 450), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.poster_label.configure(image=img)
            self.poster_label.image = img
        except Exception as e:
            print(f"Error displaying image: {e}")
    
    def s1(self):
        webbrowser.open(f"https://vidbinge.dev/embed/movie/{self.data["id"]}")
    
    def s2(self):
        webbrowser.open(f"https://flicky.host/embed/movie/?id=${self.data["id"]}")


p = ping_pong()
p.movie_name()
root.mainloop()