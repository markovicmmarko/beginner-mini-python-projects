import http.server as server
import urllib.parse as parse

model = {
    "1": {
        "naziv": "Fender stratocaster YJM WH",
        "slika": "https://images.musicstore.de/images/1280/fender-yngwie-malmsteen-stratocaster-mn-vintage-white-_1_GIT0010252-000.jpg",
        "cena": 2300
    },
    "2": {
        "naziv": "Ibanez Jem",
        "slika": "https://mixmusiccompany.com/wp-content/uploads/2021/05/Ibanez-JEMJR-WH-1.jpg",
        "cena": 500
    },
    "3": {
        "naziv": "Gibson LesPaul Slash",
        "slika": "https://images.musicstore.de/images/1280/gibson-slash-les-paul-standard-appetite-burst_1_GIT0051804-000.jpg",
        "cena": 2800
    },
}

class Handler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Host","localhost")
        self.send_header("Content-Type","text/html")
        self.end_headers()

        izlaz = "Nase gitare :<br><br>"
        parametri = self.path.split("?")
        if len(parametri) > 1:
            parametri = dict(parse.parse_qsl(parametri[1]))
            pid = parametri["id"]
            gitara = model[pid]
            izlaz = f"<h3>{gitara['naziv']}</h3><img width=200 src='{gitara['slika']}' /><br><strong>Cena: </strong>{gitara['cena']}<br><br><a href='/'>Nazad</a>"
        else:
            for k,v in model.items():
                izlaz += f"<a href='?id={k}'>{v['naziv']}</a><br>"
            izlaz += "<br><br><a href='/admin.html'>Unesi novu gitaru</a>"
        self.wfile.write(izlaz.encode())

    def do_POST(self):
        duzina = int(self.headers["Content-Length"])
        telo = self.rfile.read(duzina).decode()
        parametri = dict(parse.parse_qsl(telo))
        novi_id = 1
        for i in model:
            novi_id = int(i)+1
            novi_id = str(novi_id)
        model[novi_id] = parametri
        self.send_response(301)
        self.send_header("Location","/")
        self.end_headers()

    




s = server.HTTPServer(("0.0.0.0",8000), Handler)
s.serve_forever()