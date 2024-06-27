class BrowserHistory:
    def __init__(self):
        self.history = []
        self.bookmarks = {}
    
    def visit(self, url):
        self.history.append(url)
        print(f"Visited: {url}")

    def back(self):
        if len(self.history) < 2:
            print("No previous pages to go back to.")
            return
        current_url = self.history.pop()
        previous_url = self.history[-1]
        print(f"Going back from {current_url} to {previous_url}")

    def add_bookmark(self, name):
        if not self.history:
            print("No pages to bookmark.")
            return
        current_url = self.history[-1]
        self.bookmarks[name] = current_url
        print(f"Bookmark Saved")

    def get_bookmark(self, name):
        url = self.bookmarks.get(name)
        if url:
            print(f"Bookmark '{name}' points to {url}")
        else:
            print(f"No bookmark found ")


browser = BrowserHistory()

browser.visit("www.example.com")
browser.visit("www.google.com")
browser.visit("www.yahoo.com")

browser.back()  
browser.back() 

browser.visit("www.python.org")
browser.add_bookmark("Python")
browser.get_bookmark("Python")
browser.get_bookmark("Example")
