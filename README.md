# 🖥️ Server Health Monitor

A lightweight Python tool to monitor server performance (CPU, memory, disk, network) with optional alerting to Slack/Discord.  
Perfect for developers, sysadmins, or hobbyists who want an easy way to keep an eye on their machines.

---

## 🚀 Features
- Monitor **CPU, Memory, and Disk** usage
- Send alerts via **Slack or Discord webhooks**
- Configurable thresholds via `.env` file or CLI flags
- Lightweight, cross-platform, easy to extend
- Logs results locally for long-term tracking

---

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/realchrisevans/server-health-monitor.git
cd server-health-monitor
```

Set up your environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # (Windows: .\.venv\Scripts\Activate.ps1)
pip install -r requirements.txt
```

Create a `.env` file with your thresholds and webhook URLs:
```env
CPU_THRESHOLD=80
MEM_THRESHOLD=85
DISK_THRESHOLD=90
SLACK_WEBHOOK_URL=
DISCORD_WEBHOOK_URL=
```

---

## ▶️ Usage

Run the monitor:
```bash
python server_health_monitor.py
```

Schedule it (Linux/macOS via cron):
```bash
*/15 * * * * cd /path/to/server-health-monitor && /bin/bash -lc 'source .venv/bin/activate && export $(grep -v "^#" .env | xargs) && python server_health_monitor.py >> logs/cron.log 2>&1'
```

---

## 📥 Download

Want the **ready-to-use version** with extras?  
👉 [Download from Gumroad](https://northloomlabs.gumroad.com/l/ukxqv)  

This includes:
- Pre-configured `.env` templates
- Extra logging/alert integrations
- A step-by-step quickstart PDF

---

## 💼 Paid Products

Looking to go beyond this project? Check out my premium resources:

- **[DevOps Automation Pack v1.0](https://northloomlabs.gumroad.com/l/pxvtua)**  
  Automate common DevOps workflows with ready-to-use Python scripts and configs.

- Future packs coming soon: monitoring dashboards, CI/CD snippets, and more.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to add.

---

## 📄 License

[MIT](LICENSE)
