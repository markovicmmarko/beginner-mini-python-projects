import http.server as server
from urllib import parse
import uuid,time


def authenticate(uname,pwd):
    fajl = open("users.txt","r").read()
    for linija in fajl.split("\n"):
        uf,pf = linija.split(",")
        if uf == uname:
            if pf == pwd:
                return 0
            else:
                return -1
    else:
        return -2
    
model = [
    {"naziv":"Rod Stewart", "vreme":"03.12"},
    {"naziv":"Hatebreed", "vreme":"10.10"},
    {"naziv":"Arctic Monkeys", "vreme":"23.06"},
    {"naziv":"Tigar bend", "vreme":"29.09"}
]

session_storage = {}


class Handler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        strana = self.path.lstrip("/")
        if not strana or strana == "index.html":
            index_strana = open("index.html","r").read()
            cookie = self.headers["Cookie"]
            if cookie:
                name = cookie.replace("user_id=","")
                if name in session_storage:
                    vreme_pristupa = session_storage[name]['vreme']
                    current_time = int(time.time())
                    if current_time - vreme_pristupa > 60:
                        del session_storage[name]
                        index_strana += "<p>istekla ti je sesija bato <a href='login.html'>ulogujte se</a>.....</p>"
                    else:
                        session_storage[name]['vreme'] = current_time
                        name = session_storage[name]['ime']
                        index_strana += f"<h4>Welcome {name.capitalize()}</h4>"
                        for x in model:
                            index_strana += f"<div style='border:2px solid blue; padding:4px; margin:4px'>{x['naziv']} / {x['vreme']}</div>"
                else:
                    index_strana += "<p>Mene si nasao, <a href='login.html'>ulogujte se</a>.....</p>"
            else:
                index_strana += "<p>Niste ulogovani, <a href='login.html'>ulogujte se</a>.....</p>"
            self.send_response(200)
            self.send_header("Content-Type","text/html")
            self.end_headers()
            self.wfile.write(index_strana.encode())
        else:
            super().do_GET()


    def do_POST(self):
        telo = int(self.headers["Content-Length"])
        podaci = self.rfile.read(telo).decode()
        podaci = dict(parse.parse_qsl(podaci))
        res = authenticate(podaci["username"], podaci["password"])
        if res == 0:
            self.send_response(301)
            self.send_header("Content-Type","text/html")
            self.send_header("Location","/index.html")
            code = uuid.uuid4().hex
            session_storage[code] = {"ime": podaci['username'],"vreme": int(time.time())}
            self.send_header("Set-Cookie",f"user_id={code}")
            self.end_headers()
        elif res == -1:
            self.send_response(200)
            self.send_header("Content-Type","text/html")
            self.end_headers()
            self.wfile.write(b"Incorrect password.....<br><br><a href='login.html'>Povratak na login stranu</a>")
        else:
            self.send_response(200)
            self.send_header("Content-Type","text/html")
            self.end_headers()
            self.wfile.write(b"User not found.<br><br><a href='login.html'>Povratak na login stranu</a>")




s = server.HTTPServer(("0.0.0.0",8000),Handler)
s.serve_forever()