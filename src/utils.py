def colorfull_print(text, color):
    print(f"{color}{text}{'\033[0m'}")

def line(symbol='=', n=80, color='\033[0m'):
    colorfull_print(symbol * n, color)

def print_header(text, color='\033[0m', symbol='=', n=80):
    line(symbol, n, color)
    colorfull_print(text, color)
    line(symbol, n, color)

class Colors:
    def __init__(self):
        self.red = '#e74c3c'
        self.green = '#2ecc71'
        self.blue = '#3498db'
        self.yellow = '#f1c40f'
        self.purple = '#9b59b6'
        self.orange = '#e67e22'
        self.gray = '#95a5a6'
        self.black = '#34495e'
        self.white = '#ecf0f1'
        self.cyan = '#1abc9c'
        self.magenta = '#e84393'
        
        self.text_red = '\033[91m'
        self.text_green = '\033[92m'
        self.text_yellow = '\033[93m'
        self.text_blue = '\033[94m'
        self.text_magenta = '\033[95m'
        self.text_cyan = '\033[96m'
        self.text_white = '\033[97m'
        self.text_reset = '\033[0m'