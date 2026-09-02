import pygame
import socket
import platform
import os
import time
import subprocess
import urllib.request
import threading
from datetime import datetime

pygame.init()
pygame.font.init()

W, H = 1000, 680
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Net Info — By Amir-93")
clock = pygame.time.Clock()

FONT = pygame.font.Font(None, 28)
SMALL = pygame.font.Font(None, 22)
TITLE = pygame.font.Font(None, 48)
BIG = pygame.font.Font(None, 70)

BG = (10, 14, 24)
PANEL = (20, 27, 42)
PANEL2 = (27, 36, 55)
TEXT = (235, 242, 255)
MUTED = (145, 160, 185)
ACCENT = (70, 170, 255)
GREEN = (70, 220, 145)
RED = (245, 90, 100)
YELLOW = (245, 200, 80)

def text(s, x, y, font=FONT, color=TEXT):
    screen.blit(font.render(str(s), True, color), (x, y))

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "Unavailable"

def get_gateway():
    try:
        out = subprocess.check_output(["ip", "route"], text=True, stderr=subprocess.DEVNULL)
        for line in out.splitlines():
            if line.startswith("default"):
                parts = line.split()
                if "via" in parts:
                    return parts[parts.index("via") + 1]
    except Exception:
        pass
    return "Unavailable"

def get_dns():
    try:
        out = subprocess.check_output(["getprop", "net.dns1"], text=True,
                                      stderr=subprocess.DEVNULL).strip()
        if out:
            return out
    except Exception:
        pass
    return "Unavailable"

def internet_check():
    try:
        start = time.perf_counter()
        urllib.request.urlopen("https://www.google.com", timeout=3)
        return True, round((time.perf_counter() - start) * 1000)
    except Exception:
        return False, None

def get_info():
    hostname = socket.gethostname()
    try:
        fqdn = socket.getfqdn()
    except:
        fqdn = "Unavailable"

    return {
        "Hostname": hostname,
        "FQDN": fqdn,
        "Local IPv4": get_local_ip(),
        "Gateway": get_gateway(),
        "DNS": get_dns(),
        "Platform": platform.platform(),
        "System": platform.system(),
        "Release": platform.release(),
        "Architecture": platform.machine(),
        "Python": platform.python_version(),
        "CPU cores": os.cpu_count() or "Unknown",
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

info = {}
online = False
latency = None
last_update = 0
checking = False

def refresh():
    global info, online, latency, last_update, checking
    if checking:
        return
    checking = True
    info = get_info()
    online, latency = internet_check()
    last_update = time.time()
    checking = False

refresh()

# Boot screen
boot_start = time.time()
while time.time() - boot_start < 2.8:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill(BG)
    text("NET INFO", 355, 235, BIG, TEXT)
    text("By Amir-93", 445, 305, SMALL, ACCENT)

    progress = min(1.0, (time.time() - boot_start) / 2.8)
    pygame.draw.rect(screen, PANEL2, (300, 370, 400, 8), border_radius=4)
    pygame.draw.rect(screen, ACCENT, (300, 370, int(400 * progress), 8), border_radius=4)

    status = ["Initializing network engine", "Reading device information",
              "Checking internet connection"][min(2, int(progress * 3))]
    text(status + "...", 365, 405, SMALL, MUTED)
    pygame.display.flip()
    clock.tick(60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                refresh()
            elif event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 850 <= event.pos[0] <= 960 and 595 <= event.pos[1] <= 645:
                refresh()

    if time.time() - last_update > 8 and not checking:
        threading.Thread(target=refresh, daemon=True).start()

    screen.fill(BG)

    # Header
    pygame.draw.rect(screen, PANEL, (0, 0, W, 88))
    text("NET INFO", 35, 22, TITLE, TEXT)
    text("By Amir-93", 245, 36, SMALL, ACCENT)

    status_color = GREEN if online else RED
    status = "ONLINE" if online else "OFFLINE"
    pygame.draw.circle(screen, status_color, (900, 36), 8)
    text(status, 918, 26, SMALL, status_color)

    # Main cards
    cards = [
        ("NETWORK", [
            ("Local IPv4", info.get("Local IPv4", "...")),
            ("Gateway", info.get("Gateway", "...")),
            ("DNS", info.get("DNS", "...")),
            ("Internet", status),
            ("Latency", f"{latency} ms" if latency is not None else "N/A"),
        ]),
        ("DEVICE", [
            ("Hostname", info.get("Hostname", "...")),
            ("System", info.get("System", "...")),
            ("Release", info.get("Release", "...")),
            ("Architecture", info.get("Architecture", "...")),
            ("CPU cores", info.get("CPU cores", "...")),
        ]),
        ("RUNTIME", [
            ("Python", info.get("Python", "...")),
            ("Platform", info.get("Platform", "...")[:42]),
            ("FQDN", info.get("FQDN", "...")[:42]),
            ("Updated", info.get("Time", "...")),
        ]),
    ]

    x_positions = [30, 355, 680]
    for idx, (title, rows) in enumerate(cards):
        x = x_positions[idx]
        pygame.draw.rect(screen, PANEL, (x, 115, 290, 430), border_radius=14)
        pygame.draw.rect(screen, ACCENT, (x, 115, 290, 4), border_radius=4)
        text(title, x + 20, 138, FONT, ACCENT)

        y = 185
        for label, value in rows:
            text(label, x + 20, y, SMALL, MUTED)
            # wrap long values crudely
            if len(str(value)) > 28:
                value = str(value)[:28] + "…"
            text(value, x + 20, y + 25, SMALL, TEXT)
            y += 68

    # Bottom bar
    pygame.draw.rect(screen, PANEL, (30, 570, 930, 95), border_radius=14)
    text("Live network dashboard", 55, 592, SMALL, MUTED)
    text("Auto refresh: 8s   •   R: refresh   •   ESC: exit", 55, 620, SMALL, TEXT)

    pygame.draw.rect(screen, ACCENT, (850, 595, 110, 50), border_radius=10)
    text("REFRESH", 870, 610, SMALL, BG)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
