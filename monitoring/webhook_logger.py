import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class AlertHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        payload = json.loads(self.rfile.read(length))
        for alert in payload["alerts"]:
            print(
                f'[{alert["status"].upper()}] {alert["labels"]["alertname"]} '
                f'({alert["labels"].get("severity", "none")}): '
                f'{alert["annotations"].get("summary", "")}',
                flush=True,
            )
        self.send_response(200)
        self.end_headers()

    def log_message(self, *args):
        pass

HTTPServer(("0.0.0.0", 5001), AlertHandler).serve_forever()