from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

if __name__ == '__main__':

    base_dir = Path(__file__).resolve().parent
    os.chdir(base_dir)
    httpd = HTTPServer(('0.0.0.0', 8000), CORSRequestHandler)
    print("Serving with CORS at http://0.0.0.0:8000")
    httpd.serve_forever()
