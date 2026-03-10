# 🎯 Upwork Job Monitor - Start Here!

Welcome! This utility helps you monitor Upwork jobs, analyze market trends, and track skills and pay rates.

## ⚡ Quick Start (2 Minutes)

```bash
# 1. Install
./install.sh

# 2. Add your Upwork API credentials to .env
nano .env

# 3. Get access token
python get_access_token.py

# 4. Test connection
./upwork test

# 5. Start monitoring
./upwork search --query "your skill"
```

**That's it!** You're now monitoring Upwork jobs.

## 📖 Documentation

Choose your path:

- **🚀 Just Starting?** → Read [QUICKSTART.md](QUICKSTART.md) (5 min setup)
- **📘 Want Details?** → Read [USER_GUIDE.md](USER_GUIDE.md) (complete guide)
- **🎨 Visual Learner?** → Read [OVERVIEW.md](OVERVIEW.md) (diagrams & examples)
- **💻 Need Commands?** → Read [SUMMARY.md](SUMMARY.md) (quick reference)

## 🎯 What Can You Do?

### Monitor Jobs
```bash
./upwork search --query "python developer"
```
Track jobs with skills, pay rates, and client info

### Analyze Market
```bash
./upwork analyze
```
See what skills are in demand and what they pay

### Filter Results
```bash
./upwork filter --skill python --min-rate 100 --list
```
Find high-paying jobs matching your skills

### Continuous Monitoring
```bash
./upwork search --continuous --interval 60
```
Run in background, checking every hour

## 📊 Sample Output

```
UPWORK JOB MONITORING REPORT
Total Jobs Tracked: 150

TOP SKILLS:
  1. Python       85 jobs (56.7%)  Avg: $75/hr
  2. JavaScript   72 jobs (48.0%)  Avg: $68/hr
  3. React        45 jobs (30.0%)  Avg: $82/hr

HIGHEST PAYING:
  1. Machine Learning    $150/hr (avg)
  2. Blockchain          $140/hr (avg)
  3. DevOps              $130/hr (avg)
```

## 🛠️ All Commands

```bash
./upwork test                           # Test API connection
./upwork search                         # Search for jobs
./upwork search --continuous            # Monitor continuously
./upwork filter --skill python          # Filter by skill
./upwork analyze                        # Generate insights
./upwork stats                          # Show statistics
```

See [SUMMARY.md](SUMMARY.md) for complete command reference.

## 📁 What You Get

### Core Tools
- **upwork** - Main CLI tool (start here!)
- **upwork_job_monitor.py** - Job search & caching
- **job_analytics.py** - Market analysis
- **examples.py** - Code examples

### Documentation
- **README.md** - Main overview (this file)
- **QUICKSTART.md** - Fast setup guide
- **USER_GUIDE.md** - Complete manual
- **SUMMARY.md** - Command reference
- **OVERVIEW.md** - Visual guide

### Configuration
- **.env.example** - Settings template
- **requirements.txt** - Dependencies

## 🎓 Common Use Cases

### Find High-Paying Jobs
```bash
./upwork search --query "your skill"
./upwork filter --min-rate 100 --list
```

### Track Market Trends
```bash
./upwork search --continuous
# Wait a week, then:
./upwork analyze --export insights.json
```

### Benchmark Your Rates
```bash
./upwork search --query "your specialty"
./upwork analyze --skill "your specialty"
```

### Career Planning
```bash
./upwork search
./upwork analyze
# Check "HIGHEST PAYING SKILLS" section
```

## 🚨 Prerequisites

- Python 3.7 or higher
- Upwork API credentials ([get them here](https://www.upwork.com/services/api/apply))
- pip (Python package manager)

## 📦 Installation

### Option 1: Automatic (Recommended)
```bash
./install.sh
```

### Option 2: Manual
```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
python get_access_token.py
./upwork test
```

## 🔐 Getting API Credentials

1. Visit https://www.upwork.com/services/api/apply
2. Create a new application
3. Copy Client ID and Secret
4. Run `python get_access_token.py` to get access token
5. Add all credentials to `.env` file

Detailed instructions: [QUICKSTART.md](QUICKSTART.md)

## 💡 Examples

Run interactive examples:
```bash
python examples.py              # Show menu
python examples.py --example 1  # Run specific example
python examples.py --all        # Run all examples
```

## 📊 Output Files

- **upwork_jobs.json** - Cached job data
- **upwork_report_*.json** - JSON exports
- **upwork_report_*.csv** - CSV exports
- **job_insights_*.json** - Analytics data

## 🔧 Configuration

Edit `.env` to customize:

```env
# What to search for
SEARCH_QUERIES=python,javascript,react,docker

# Pay rate filters
MIN_HOURLY_RATE=25
MAX_HOURLY_RATE=200
MIN_FIXED_PRICE=100
MAX_FIXED_PRICE=10000
```

## 📚 Need Help?

1. **Just starting?** → [QUICKSTART.md](QUICKSTART.md)
2. **Want examples?** → `python examples.py`
3. **Need full docs?** → [USER_GUIDE.md](USER_GUIDE.md)
4. **Quick reference?** → [SUMMARY.md](SUMMARY.md)
5. **Visual guide?** → [OVERVIEW.md](OVERVIEW.md)

## 🤝 Contributing

This is a personal utility, but suggestions are welcome!

## ⚠️ Important Notes

- Respect Upwork's API rate limits
- Don't run continuous monitoring with intervals < 30 minutes
- Never commit `.env` to version control
- Comply with Upwork's Terms of Service

## 📝 License

Personal use. See Upwork's API terms for restrictions.

---

## 🎯 Ready to Start?

```bash
./install.sh                          # 1. Install
nano .env                             # 2. Add credentials
python get_access_token.py            # 3. Get token
./upwork test                         # 4. Test
./upwork search --query "your skill"  # 5. Go!
```

**Questions?** Check the documentation files or run `python examples.py`

**Happy job hunting!** 🚀
