# Upwork Job Monitoring Utility - Complete Guide

## Overview

This utility provides comprehensive tools for monitoring Upwork jobs, analyzing skills demand, and tracking pay rates. It consists of three main components:

1. **Job Monitor** (`upwork_job_monitor.py`) - Track and cache job postings
2. **Job Analytics** (`job_analytics.py`) - Analyze trends and generate insights
3. **Job Application Agent** (`upwork_agent.py`) - Automated job applications

## Key Features

### 📊 Job Monitoring
- Real-time job search and caching
- Track skills, pay rates, and client information
- Filter by keywords, skills, and budget ranges
- Continuous monitoring with configurable intervals
- Export to JSON, CSV, or console reports

### 📈 Analytics & Insights
- Skill frequency analysis
- Pay rate correlation by skill
- Budget distribution analysis
- Client quality metrics
- Skill combination patterns
- Time-based trends

### 🤖 Automation
- Automated job applications (optional)
- Scheduled searches
- Alert notifications for matching jobs

## Quick Start

### 1. Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your Upwork API credentials
nano .env
```

### 2. Get API Credentials

1. Visit https://www.upwork.com/services/api/apply
2. Create a new application
3. Get Client ID and Secret
4. Generate access token:

```bash
python get_access_token.py
```

### 3. Test Connection

```bash
python test_connection.py
```

### 4. Start Monitoring

```bash
# One-time search
python upwork_job_monitor.py

# Continuous monitoring
python upwork_job_monitor.py --continuous --interval 60
```

## Usage Examples

### Example 1: Basic Job Search

Search for Python jobs and display results:

```bash
python upwork_job_monitor.py --query "python developer"
```

Output shows:
- Total jobs found
- Job types (Hourly vs Fixed)
- Budget ranges
- Top skills
- Recent listings

### Example 2: Filter by Skills

Find all jobs requiring specific skills:

```bash
# Find Python jobs
python upwork_job_monitor.py --skill python

# Find React jobs
python upwork_job_monitor.py --skill react

# Find AI/ML jobs
python upwork_job_monitor.py --skill "machine learning"
```

### Example 3: Filter by Pay Rate

Find jobs within specific budget ranges:

```bash
# High-paying jobs ($100-200/hr)
python upwork_job_monitor.py --min-rate 100 --max-rate 200

# Entry-level jobs ($25-50/hr)
python upwork_job_monitor.py --min-rate 25 --max-rate 50

# Premium projects (>$150/hr)
python upwork_job_monitor.py --min-rate 150
```

### Example 4: Generate Reports

Export data in different formats:

```bash
# Console report (interactive)
python upwork_job_monitor.py --report console

# JSON export (for analysis)
python upwork_job_monitor.py --report json

# CSV export (for spreadsheets)
python upwork_job_monitor.py --report csv
```

### Example 5: Analyze Job Data

Run analytics on cached jobs:

```bash
# Generate insights report
python job_analytics.py

# Analyze specific skill
python job_analytics.py --skill python

# Export insights as JSON
python job_analytics.py --export-json
```

### Example 6: Continuous Monitoring

Run as a background service:

```bash
# Check every 60 minutes
python upwork_job_monitor.py --continuous --interval 60

# Check every 30 minutes
python upwork_job_monitor.py --continuous --interval 30

# Run in background (Linux/Mac)
nohup python upwork_job_monitor.py --continuous --interval 60 > monitor.log 2>&1 &
```

## Configuration

### Environment Variables (.env)

```env
# API Credentials (Required)
UPWORK_CLIENT_ID=your_client_id
UPWORK_CLIENT_SECRET=your_client_secret
UPWORK_ACCESS_TOKEN=your_access_token

# Search Configuration
SEARCH_QUERIES=python,javascript,react,node.js,docker
MIN_HOURLY_RATE=25
MAX_HOURLY_RATE=200
MIN_FIXED_PRICE=100
MAX_FIXED_PRICE=10000
```

### Command-Line Options

#### upwork_job_monitor.py

```
--query TEXT           Custom search query
--interval INT         Minutes between searches (default: 60)
--output FILE          Output file for cache (default: upwork_jobs.json)
--report FORMAT        Report format: console, json, csv
--continuous           Run continuous monitoring
--skill TEXT           Filter by skill
--min-rate FLOAT       Minimum hourly rate or budget
--max-rate FLOAT       Maximum hourly rate or budget
```

#### job_analytics.py

```
--jobs-file FILE       Path to jobs JSON file
--export-json          Export insights as JSON
--skill TEXT           Analyze specific skill
```

## Output Files

### upwork_jobs.json (Job Cache)

Stores all tracked jobs with complete information:

```json
{
  "~1234567890": {
    "id": "~1234567890",
    "title": "Python Developer Needed",
    "description": "Looking for experienced Python dev...",
    "skills": ["Python", "Django", "PostgreSQL", "REST API"],
    "budget": {
      "type": "Hourly",
      "hourly_rate_min": 75,
      "hourly_rate_max": 100,
      "currency": "USD"
    },
    "client_info": {
      "location": "United States",
      "total_spent": 50000,
      "hire_rate": 0.95,
      "rating": 4.8,
      "payment_verified": true
    },
    "experience_level": "Expert",
    "posted_on": "2026-03-04T10:30:00",
    "url": "https://www.upwork.com/jobs/~1234567890"
  }
}
```

### job_insights_*.json (Analytics Export)

Contains aggregated statistics and insights:

```json
{
  "generated_at": "2026-03-04T12:00:00",
  "total_jobs": 150,
  "top_skills": {
    "Python": 85,
    "JavaScript": 72,
    "React": 45
  },
  "skill_pay_correlation": {
    "Python": {
      "avg_rate": 75.50,
      "min_rate": 25,
      "max_rate": 200,
      "job_count": 85
    }
  }
}
```

## Programmatic Usage

### Python API Examples

#### Basic Monitoring

```python
from upwork_job_monitor import UpworkJobMonitor

# Initialize
monitor = UpworkJobMonitor()

# Search for jobs
monitor.search_and_monitor(query="python developer")

# Get specific jobs
python_jobs = monitor.get_jobs_by_skill("python")
high_paying = monitor.get_jobs_by_budget_range(min_amount=100)

# Generate report
monitor.generate_report(output_format='console')
```

#### Analytics

```python
from job_analytics import JobAnalytics

# Load cached data
analytics = JobAnalytics(jobs_file="upwork_jobs.json")

# Get insights
top_skills = analytics.skill_frequency_analysis(top_n=20)
skill_pay = analytics.skill_pay_correlation()
budget_dist = analytics.budget_distribution()

# Generate report
report = analytics.generate_insights_report()
print(report)
```

#### Custom Filtering

```python
# Find best opportunities
def find_best_opportunities(monitor):
    # Get Python jobs
    jobs = monitor.get_jobs_by_skill("python")
    
    # Filter: $75-150/hr, verified clients, >$5K spent
    quality_jobs = [
        job for job in jobs
        if (75 <= job['budget'].get('hourly_rate_min', 0) <= 150 and
            job['client_info'].get('payment_verified', False) and
            job['client_info'].get('total_spent', 0) > 5000)
    ]
    
    # Sort by client rating
    quality_jobs.sort(
        key=lambda x: x['client_info'].get('rating', 0),
        reverse=True
    )
    
    return quality_jobs[:10]  # Top 10

# Use it
monitor = UpworkJobMonitor()
best_jobs = find_best_opportunities(monitor)
```

## Use Cases

### 1. Market Research
Track which skills are in demand and their associated pay rates:

```bash
python upwork_job_monitor.py --continuous --interval 120
python job_analytics.py --export-json
```

Analyze the exported JSON to identify trends over time.

### 2. Career Planning
Identify high-paying skill combinations:

```python
analytics = JobAnalytics()
report = analytics.generate_insights_report()
# Check "HIGHEST PAYING SKILLS" and "SKILL COMBINATIONS" sections
```

### 3. Competitive Analysis
Monitor specific technologies or markets:

```bash
# Track AI/ML market
SEARCH_QUERIES="machine learning,artificial intelligence,deep learning" \
python upwork_job_monitor.py --continuous
```

### 4. Job Hunting
Find the best opportunities matching your skills:

```bash
# Your skills: Python, Django, PostgreSQL
python upwork_job_monitor.py --skill python --min-rate 75
python upwork_job_monitor.py --skill django --min-rate 75
```

### 5. Rate Benchmarking
Determine appropriate rates for your skills:

```bash
python job_analytics.py --skill "your-skill"
# Shows avg, min, max rates for that skill
```

## Running Examples

Interactive examples are provided in `examples.py`:

```bash
# Show available examples
python examples.py

# Run specific example
python examples.py --example 1

# Run all examples
python examples.py --all
```

Available examples:
1. Basic Monitoring
2. Skill Filtering
3. Budget Filtering
4. Analytics
5. Combined Analysis
6. Find Best Opportunities

## Troubleshooting

### Common Issues

#### "No access token found"
**Solution:** Run `python get_access_token.py` to generate a token.

#### "Connection test failed"
**Solutions:**
- Verify credentials in `.env`
- Check if token expired (regenerate)
- Ensure app has required OAuth2 scopes: `r_myprofile`, `r_jobs`, `w_jobs`

#### "No jobs found"
**Solutions:**
- Try broader search queries
- Adjust budget filters to be less restrictive
- Verify Upwork API status

#### "Rate limit exceeded"
**Solution:** Increase monitoring interval or reduce search frequency.

### Debug Mode

Enable detailed logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Best Practices

### 1. Monitoring Frequency
- **Market research**: Check every 2-4 hours
- **Active job hunting**: Check every 30-60 minutes
- **Passive monitoring**: Check every 4-12 hours

### 2. Search Queries
- Use specific, relevant terms
- Include variations (e.g., "python", "python developer", "python engineer")
- Avoid overly broad terms that return noise

### 3. Data Management
- Archive old job cache files periodically
- Export insights regularly for historical analysis
- Keep separate cache files for different queries/purposes

### 4. API Usage
- Respect Upwork's rate limits
- Don't run continuous monitoring with intervals < 30 minutes
- Test with small searches before large deployments

## Advanced Features

### Scheduling with Cron

Linux/Mac crontab example:

```bash
# Run every 2 hours
0 */2 * * * cd /path/to/upwork && python upwork_job_monitor.py --report json

# Daily analytics report at 9 AM
0 9 * * * cd /path/to/upwork && python job_analytics.py --export-json
```

### Integration with Other Tools

Export to CSV and analyze with pandas:

```python
import pandas as pd

# Load job data
df = pd.read_csv('upwork_report_20260304.csv')

# Analyze
print(df.groupby('Budget Type')['Budget Amount'].describe())
print(df['Skills'].value_counts())
```

### Custom Alerts

Add notifications when high-value jobs appear:

```python
def check_and_notify(monitor):
    jobs = monitor.get_jobs_by_budget_range(min_amount=150)
    if jobs:
        # Send email, Slack message, etc.
        send_alert(f"Found {len(jobs)} high-paying jobs!")
```

## Support & Resources

- **Upwork API Documentation**: https://developers.upwork.com/
- **Quick Start Guide**: See `QUICKSTART.md`
- **Examples**: See `examples.py`
- **API Client**: See `upwork_api_client.py`

## Security Notes

- Never commit `.env` file to version control
- Keep API credentials secure
- Rotate access tokens regularly
- Monitor API usage to stay within limits
- Use environment variables for sensitive data

## License

This utility is for educational and personal use. Ensure compliance with Upwork's Terms of Service and API usage guidelines.

---

**Happy job hunting!** 🚀
