#!/usr/bin/env python3
import os, psutil, platform, socket, datetime, json, urllib.request

def send_webhook(msg: str):
    payload = {"text": msg}
    slack = os.getenv("SLACK_WEBHOOK_URL")
    disc = os.getenv("DISCORD_WEBHOOK_URL")
    if slack:
        req = urllib.request.Request(slack, data=json.dumps(payload).encode(), headers={"Content-Type":"application/json"})
        urllib.request.urlopen(req, timeout=5)
    if disc:
        payload = {"content": msg}
        req = urllib.request.Request(disc, data=json.dumps(payload).encode(), headers={"Content-Type":"application/json"})
        urllib.request.urlopen(req, timeout=5)

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    lines.append(f"--- Server Health Report ({now}) ---")
    lines.append(f"System: {platform.system()} {platform.release()}")
    lines.append(f"Hostname: {socket.gethostname()}")

    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    lines.append(f"CPU Usage: {cpu}%")
    lines.append(f"Memory Usage: {mem}%")
    lines.append(f"Disk Usage: {disk}%")

    alerts = []
    if cpu > int(os.getenv("CPU_THRESHOLD", 80)): alerts.append("High CPU")
    if mem > int(os.getenv("MEM_THRESHOLD", 85)): alerts.append("High Memory")
    if disk > int(os.getenv("DISK_THRESHOLD", 90)): alerts.append("Low Disk Space")

    if alerts:
        lines.append("WARNINGS: " + ", ".join(alerts))

    msg = "\n".join(lines)
    print(msg)

    if alerts:
        try: send_webhook(f"⚠️ {socket.gethostname()} Server Alerts: {', '.join(alerts)}\n{msg}")
        except Exception: pass

if __name__ == "__main__":
    main()
