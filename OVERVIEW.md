# Upwork Job Monitoring Utility

## 🎯 What is This?

A complete system for monitoring Upwork job postings, analyzing market trends, and tracking skills and pay rates using the official Upwork API.

```
                    ┌─────────────────────────────┐
                    │   Upwork API (Official)     │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   upwork_api_client.py      │
                    │   (OAuth2 Authentication)    │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
    ┌─────────▼─────────┐ ┌───────▼────────┐ ┌────────▼────────┐
    │  Job Monitor      │ │  Job Analytics  │ │  Job Agent      │
    │  (Search & Cache) │ │  (Insights)     │ │  (Auto-Apply)   │
    └─────────┬─────────┘ └───────┬────────┘ └────────┬────────┘
              │                    │                    │
              └────────────────────┼────────────────────┘
                                   │
                         ┌─────────▼─────────┐
                         │  Unified CLI Tool  │
                         │     ./upwork       │
                         └───────────────────┘
```

## 📦 Components

### 1. Core Engine
- **`upwork_api_client.py`** - Handles all Upwork API communication
- OAuth2 authentication, token management, job searching

### 2. Job Monitor
- **`upwork_job_monitor.py`** - Search and cache job postings
- Tracks: skills, pay rates, client info, experience levels
- Outputs: `upwork_jobs.json`

### 3. Analytics Engine
- **`job_analytics.py`** - Analyze cached data
- Generates insights on skills, pay, trends
- Outputs: Console reports, JSON exports

### 4. Application Agent
- **`upwork_agent.py`** - Automated job applications
- Filter by criteria, auto-apply to matches

### 5. Unified CLI
- **`upwork`** - Single command-line interface
- Access all features through one tool

## 🚀 Quick Commands

```bash
# Setup
./install.sh                              # One-time setup
./upwork test                             # Test API connection

# Search
./upwork search                           # Search with default queries
./upwork search --query "python"          # Custom search
./upwork search --continuous              # Monitor continuously

# Filter
./upwork filter --skill python --list     # Jobs requiring Python
./upwork filter --min-rate 100 --list     # High-paying jobs

# Analyze
./upwork analyze                          # Full insights report
./upwork analyze --skill python           # Skill-specific analysis
./upwork analyze --export data.json       # Export insights

# Stats
./upwork stats                            # Show cache statistics
```

## 📊 What You Get

### Real-Time Job Data
```json
{
  "title": "Senior Python Developer",
  "skills": ["Python", "Django", "PostgreSQL", "AWS"],
  "budget": {
    "type": "Hourly",
    "hourly_rate_min": 75,
    "hourly_rate_max": 100
  },
  "client_info": {
    "total_spent": 50000,
    "rating": 4.8,
    "payment_verified": true
  }
}
```

### Market Insights
- **Most Demanded Skills**: What employers need
- **Highest Paying Skills**: What pays best
- **Budget Distribution**: Typical pay ranges
- **Client Quality**: Payment history, ratings
- **Skill Combinations**: Common pairings
- **Time Trends**: Posting patterns

### Reports & Exports
- Console reports (interactive viewing)
- JSON exports (data analysis)
- CSV files (spreadsheet import)

## 🎓 Use Cases

### 1. Market Research
**Goal**: Understand job market trends

```bash
# Monitor for a week
./upwork search --continuous --interval 120

# Analyze results
./upwork analyze --export weekly_insights.json
```

**Output**: Skill demand, pay trends, client patterns

### 2. Job Hunting
**Goal**: Find best opportunities

```bash
# Search your skills
./upwork search --query "python django"

# Filter high-paying jobs
./upwork filter --skill python --min-rate 75 --list

# Check client quality in upwork_jobs.json
```

**Output**: Vetted job opportunities with good clients

### 3. Rate Benchmarking
**Goal**: Set competitive rates

```bash
# Search your market
./upwork search --query "your specialty"

# Analyze pay rates
./upwork analyze --skill "your specialty"
```

**Output**: Average, min, max rates for your skills

### 4. Career Planning
**Goal**: Identify valuable skills to learn

```bash
# Broad market scan
./upwork search

# Check highest-paying skills
./upwork analyze
# Look at "HIGHEST PAYING SKILLS" section
```

**Output**: Skills with best ROI

### 5. Competition Analysis
**Goal**: Monitor specific markets

```bash
# Edit .env: SEARCH_QUERIES=AI,blockchain,web3
./upwork search --continuous

# Weekly reports
./upwork analyze --export report_$(date +%Y%m%d).json
```

**Output**: Market evolution over time

## 📈 Sample Output

### Console Report
```
UPWORK JOB MONITORING REPORT
Total Jobs Tracked: 150

TOP 15 MOST DEMANDED SKILLS:
  1. Python                    85 jobs (56.7%)
  2. JavaScript                72 jobs (48.0%)
  3. React                     45 jobs (30.0%)
  4. Node.js                   38 jobs (25.3%)
  5. Docker                    32 jobs (21.3%)

TOP 10 HIGHEST PAYING SKILLS:
  1. Machine Learning          $150.00/hr (avg)
  2. Blockchain                $140.50/hr (avg)
  3. DevOps                    $130.25/hr (avg)
  4. AWS                       $125.00/hr (avg)
  5. Kubernetes                $120.75/hr (avg)

BUDGET DISTRIBUTION:
  $50-$100/hr              65 jobs (43.3%)
  $100-$150/hr             40 jobs (26.7%)
  >$150/hr                 20 jobs (13.3%)
```

## 🔧 Installation

### Quick Install
```bash
./install.sh
```

### Manual Install
```bash
# 1. Dependencies
pip install -r requirements.txt

# 2. Configuration
cp .env.example .env
nano .env  # Add API credentials

# 3. Get access token
python get_access_token.py

# 4. Test
./upwork test

# 5. Start monitoring
./upwork search
```

## 📚 Documentation

| File | Purpose |
|------|---------|
| **README.md** | Main overview and features |
| **QUICKSTART.md** | 5-minute setup guide |
| **USER_GUIDE.md** | Complete reference manual |
| **SUMMARY.md** | Command reference |
| **OVERVIEW.md** | This file - visual guide |

## 🛠️ Files Overview

### Scripts You Run
- `upwork` - Main CLI tool (use this!)
- `upwork_job_monitor.py` - Direct monitoring
- `job_analytics.py` - Direct analytics
- `examples.py` - Code examples
- `test_connection.py` - Connection tester
- `install.sh` - Setup script

### Configuration
- `.env` - Your settings (create from .env.example)
- `.env.example` - Template
- `requirements.txt` - Dependencies

### Data Files (Auto-Created)
- `upwork_jobs.json` - Cached jobs
- `upwork_report_*.json/csv` - Exports
- `job_insights_*.json` - Analytics

## 💡 Tips

### Best Practices
1. **Start broad**: Let the tool build a database first
2. **Filter later**: Use analytics to find what you need
3. **Export regularly**: Keep historical data
4. **Respect limits**: Don't query too frequently (<30min)
5. **Monitor continuously**: Better insights over time

### Typical Workflow
```bash
# Week 1: Build database
./upwork search --continuous --interval 120

# Week 2: Analyze patterns
./upwork analyze --export week1.json

# Ongoing: Track specific skills
./upwork filter --skill python --list
./upwork analyze --skill python
```

### Pro Tips
- Set `SEARCH_QUERIES` in `.env` for automatic broad searches
- Export insights weekly to track trends
- Use `--continuous` to run in background
- Filter by client quality (check `payment_verified`, `total_spent`)
- Combine skills: Search "python django aws" for specific stacks

## 🎯 Getting Started

```bash
# 1. Setup (5 minutes)
./install.sh
# Edit .env with your API credentials
python get_access_token.py

# 2. Test
./upwork test

# 3. First search
./upwork search --query "python"

# 4. See results
./upwork analyze

# 5. Filter what you want
./upwork filter --skill python --min-rate 75 --list
```

## 📊 Real Example Session

```bash
$ ./upwork test
✓ Connection successful!

$ ./upwork search --query "python developer"
[INFO] Searching for: python developer
[INFO] Found 50 jobs
[INFO] Search complete: 50 new, 0 updated

$ ./upwork analyze --skill python
Skill Analysis: python
============================================================
Jobs found:    50
Average rate:  $78.50/hr
Rate range:    $25.00 - $200.00
Median rate:   $75.00

$ ./upwork filter --skill python --min-rate 100 --list
Found 12 jobs in budget range

1. Senior Python Developer for AI Platform
   Rate: $150/hr (Hourly)
   Skills: Python, Machine Learning, TensorFlow, AWS
   URL: https://www.upwork.com/jobs/~123...

2. Python Backend Engineer - FinTech
   Rate: $125/hr (Hourly)
   Skills: Python, Django, PostgreSQL, Redis
   URL: https://www.upwork.com/jobs/~456...
```

## 🔗 Resources

- Upwork API Docs: https://developers.upwork.com/
- Run examples: `python examples.py`
- Need help? Check USER_GUIDE.md

---

**Ready to monitor Upwork jobs? Start with: `./upwork test`** 🚀
