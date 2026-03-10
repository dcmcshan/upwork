# Upwork Job Monitoring & Application Tools

A comprehensive toolkit for monitoring Upwork job postings, tracking skills and pay rates, and automating job applications using the official Upwork API.

## 🎯 What Can You Do?

- **Monitor Jobs**: Track Upwork postings with detailed skill and pay information
- **Analyze Trends**: See which skills are most in-demand and highest paying
- **Filter & Search**: Find jobs by skills, budget ranges, and keywords
- **Generate Reports**: Export data as console, JSON, or CSV reports
- **Track Insights**: Monitor client quality, budget distribution, and market trends
- **Automate**: Run continuous monitoring or schedule automated searches
- **Apply**: Optionally auto-apply to matching jobs
- **🆕 Cover Letter Generator**: Use the GitHub Pages site to generate personalized cover letters

## 🚀 Quick Start

```bash
# 1. Install
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API credentials

# 2. Test connection
python test_connection.py

# 3. Start monitoring
./upwork search --query "python developer"

# 4. Analyze results
./upwork analyze
```

**See [QUICKSTART.md](QUICKSTART.md) for detailed setup instructions.**

## 🌐 GitHub Pages - Cover Letter Generator

**NEW!** This repo includes a GitHub Pages site that helps you generate personalized cover letters!

### ✨ Features
- 🎨 Split-screen interface with Upwork iframe
- 🤖 AI-powered cover letter generation
- 🎯 Analyzes job descriptions and matches your skills
- 📋 One-click copy to clipboard
- 📱 Mobile-friendly responsive design
- 🔒 Privacy-focused (runs entirely in browser)
- ⚡ No API keys or backend required

### 🚀 Quick Setup (5 minutes)
1. **Customize**: Edit `docs/config.js` with your information
2. **Test**: Run `cd docs && ./test-local.sh` or open `docs/index.html`
3. **Deploy**: Enable GitHub Pages in Settings → Pages → Source: `main`, `/docs`
4. **Use**: Visit `https://[username].github.io/[repo-name]/`

### 📚 Documentation
- **Quick Start**: [START_HERE_GITHUB_PAGES.md](START_HERE_GITHUB_PAGES.md)
- **Full Setup Guide**: [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)
- **Deployment Checklist**: [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)
- **Visual Guide**: [VISUAL_GUIDE.md](VISUAL_GUIDE.md)
- **Examples**: [docs/EXAMPLE.md](docs/EXAMPLE.md)

---

## 📊 Key Features

### Job Monitoring
- Real-time job search and caching
- Track skills, pay rates, experience levels
- Client quality metrics (payment history, ratings)
- Continuous monitoring with configurable intervals
- Export to multiple formats (JSON, CSV, console)

### Analytics & Insights
- Skill frequency analysis (what's in demand?)
- Pay rate correlation by skill (what pays best?)
- Budget distribution analysis
- Skill combination patterns
- Time-based posting trends
- Client quality metrics

### Automation
- Continuous background monitoring
- Automated job applications (optional)
- Scheduled searches
- Custom filtering and alerts

## Prerequisites

- Python 3.7 or higher
- Upwork API credentials (Client ID and Secret)
- Upwork OAuth2 access token

## Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd upwork-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your credentials:
```env
# Upwork OAuth2 Credentials
UPWORK_CLIENT_ID=your_client_id
UPWORK_CLIENT_SECRET=your_client_secret
UPWORK_ACCESS_TOKEN=your_access_token

# Job Search Criteria (for upwork_agent.py)
JOB_KEYWORDS=python,web development,automation
MIN_BUDGET=50
MAX_BUDGET=500

# Job Monitor Settings (for upwork_job_monitor.py)
SEARCH_QUERIES=python,javascript,web development,AI,machine learning
MIN_HOURLY_RATE=25
MAX_HOURLY_RATE=200
MIN_FIXED_PRICE=100
MAX_FIXED_PRICE=10000
```

### Getting Upwork API Credentials

1. Go to [Upwork Developer Portal](https://www.upwork.com/services/api/apply)
2. Create a new application
3. Get your Client ID and Client Secret
4. Set up OAuth2 redirect URI in your application settings
5. Generate an OAuth2 access token using one of these methods:

#### Method 1: Interactive Token Generation
```bash
python upwork_api_client.py
```
This will guide you through the OAuth2 flow to get an access token.

#### Method 2: Manual OAuth2 Flow
1. Get authorization URL (run `python upwork_api_client.py`)
2. Visit the authorization URL in your browser
3. Authorize the application
4. Copy the authorization code from the callback URL
5. Enter it in the script to get your access token

Required OAuth2 scopes:
- `r_myprofile` - Read your profile
- `r_jobs` - Read job listings
- `w_jobs` - Write/apply to jobs

## 💻 Usage

### CLI Tool (Recommended)

The unified CLI tool provides easy access to all features:

```bash
# Test connection
./upwork test

# Search for jobs
./upwork search --query "python developer"

# Continuous monitoring (every 60 minutes)
./upwork search --continuous --interval 60

# Filter cached jobs by skill
./upwork filter --skill python --list

# Filter by pay rate
./upwork filter --min-rate 100 --max-rate 200 --list

# Analyze job data
./upwork analyze

# Analyze specific skill
./upwork analyze --skill python

# Export insights
./upwork analyze --export insights.json

# Get cache statistics
./upwork stats
```

### Python Scripts (Direct Access)

You can also use the Python scripts directly:

#### Test Connection

```bash
python test_connection.py
```

#### Job Monitoring

```bash
# Basic search
python upwork_job_monitor.py

# Custom query
python upwork_job_monitor.py --query "python developer"

# Continuous monitoring
python upwork_job_monitor.py --continuous --interval 60

# Generate reports
python upwork_job_monitor.py --report console
python upwork_job_monitor.py --report json
python upwork_job_monitor.py --report csv

# Filter by skill/rate
python upwork_job_monitor.py --skill python
python upwork_job_monitor.py --min-rate 50 --max-rate 150
```

#### Analytics

```bash
# Full insights report
python job_analytics.py

# Analyze specific skill
python job_analytics.py --skill python

# Export as JSON
python job_analytics.py --export-json
```

#### Run Examples

```bash
# Show available examples
python examples.py

# Run specific example
python examples.py --example 1

# Run all examples
python examples.py --all
```

### Job Application Agent (Optional)

Automatically apply to matching jobs:

```bash
python upwork_agent.py
```

**Note:** Configure job criteria in `.env` before running.

### Using the API Client Directly

You can also use the `UpworkAPIClient` class directly in your own scripts:

```python
from upwork_api_client import UpworkAPIClient

# Initialize client (reads from .env file)
client = UpworkAPIClient()

# Test connection
client.test_connection()

# Get your profile
profile = client.get_profile()

# Search for jobs
jobs = client.search_jobs(query="python developer", page_size=20)

# Get job details
job = client.get_job_details(job_id="~1234567890abcdef")
```

### Using the Job Monitor Programmatically

```python
from upwork_job_monitor import UpworkJobMonitor

# Initialize monitor
monitor = UpworkJobMonitor(output_file="my_jobs.json")

# Search and cache jobs
monitor.search_and_monitor(query="python developer")

# Get jobs by skill
python_jobs = monitor.get_jobs_by_skill("python")
print(f"Found {len(python_jobs)} Python jobs")

# Get jobs by budget range
high_paying_jobs = monitor.get_jobs_by_budget_range(
    min_amount=100,
    max_amount=200,
    job_type="hourly"
)

# Generate report
monitor.generate_report(output_format='console')
```

## Configuration

### Environment Variables

Configure the tools via the `.env` file:

**API Credentials:**
- `UPWORK_CLIENT_ID`: Your Upwork OAuth2 client ID
- `UPWORK_CLIENT_SECRET`: Your Upwork OAuth2 client secret
- `UPWORK_ACCESS_TOKEN`: Your OAuth2 access token
- `UPWORK_REFRESH_TOKEN`: Your OAuth2 refresh token (optional)

**Job Application Agent Settings:**
- `JOB_KEYWORDS`: Comma-separated list of keywords to search for
- `MIN_BUDGET`: Minimum budget for jobs to apply to
- `MAX_BUDGET`: Maximum budget for jobs to apply to

**Job Monitor Settings:**
- `SEARCH_QUERIES`: Comma-separated list of search terms (default: python,javascript,web development)
- `MIN_HOURLY_RATE`: Minimum hourly rate to track (default: 0)
- `MAX_HOURLY_RATE`: Maximum hourly rate to track (default: 200)
- `MIN_FIXED_PRICE`: Minimum fixed price to track (default: 0)
- `MAX_FIXED_PRICE`: Maximum fixed price to track (default: 10000)

## Output Files

### Job Monitor Cache

The job monitor saves all tracked jobs to a JSON file (default: `upwork_jobs.json`):

```json
{
  "~job123": {
    "id": "~job123",
    "title": "Python Developer Needed",
    "skills": ["Python", "Django", "PostgreSQL"],
    "budget": {
      "type": "Hourly",
      "hourly_rate_min": 50,
      "hourly_rate_max": 75
    },
    "client_info": {
      "total_spent": 10000,
      "hire_rate": 0.95,
      "rating": 4.8
    },
    "posted_on": "2026-03-04T10:30:00",
    "first_seen": "2026-03-04T11:00:00"
  }
}
```

### Report Examples

**Console Report:**
- Total jobs tracked
- Job type distribution (Hourly vs Fixed)
- Budget ranges
- Top 20 most requested skills
- Most recent job postings

**JSON Report:**
- Complete data export with statistics
- Suitable for further analysis or dashboard integration

**CSV Report:**
- Spreadsheet-compatible format
- Easy to import into Excel/Google Sheets
- Columns: Job ID, Title, Budget Type, Amount, Skills, Experience Level, Posted On, URL

## Logging

All tools log activities to the console with timestamps:
- Successful job searches
- Job matches found
- New jobs discovered
- Successful applications
- API errors and warnings

## 📁 Project Structure

```
upwork/
├── upwork                      # Unified CLI tool
├── upwork_job_monitor.py      # Job monitoring script
├── job_analytics.py            # Analytics and insights
├── upwork_api_client.py        # Upwork API wrapper
├── upwork_agent.py             # Auto-application agent
├── test_connection.py          # Connection tester
├── get_access_token.py         # OAuth token generator
├── examples.py                 # Usage examples
├── requirements.txt            # Python dependencies
├── .env.example                # Environment template
├── README.md                   # This file
├── QUICKSTART.md              # Quick setup guide
└── USER_GUIDE.md              # Comprehensive documentation
```

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[USER_GUIDE.md](USER_GUIDE.md)** - Complete reference guide
- **[examples.py](examples.py)** - Code examples and use cases

## 🔧 Common Use Cases

1. **Market Research**: Track which skills are in demand
   ```bash
   ./upwork search --continuous --interval 120
   ./upwork analyze --export market_data.json
   ```

2. **Find High-Paying Jobs**: Filter by rate
   ```bash
   ./upwork filter --min-rate 100 --list
   ```

3. **Track Specific Skills**: Monitor skill demand
   ```bash
   ./upwork search --query "machine learning"
   ./upwork analyze --skill "machine learning"
   ```

4. **Career Planning**: See what pays best
   ```bash
   ./upwork analyze
   # Check "HIGHEST PAYING SKILLS" section
   ```

## 🤝 Contributing

This is a personal utility, but suggestions and improvements are welcome!

## 🔒 Security

- Never commit your `.env` file to version control
- Keep API credentials secure
- Rotate access tokens regularly
- Monitor API usage to stay within limits
- Use environment variables for sensitive data

## ⚠️ Disclaimer

This tool is for educational and personal use. Ensure compliance with Upwork's Terms of Service and API usage guidelines.

## 📝 License

Personal use. See Upwork's API terms for usage restrictions.

---

**Questions?** See [USER_GUIDE.md](USER_GUIDE.md) or [QUICKSTART.md](QUICKSTART.md) 