# Quick Start Guide

Get up and running with Upwork job monitoring in minutes!

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Get Upwork API Credentials

1. Visit [Upwork Developer Portal](https://www.upwork.com/services/api/apply)
2. Create a new application
3. Note your **Client ID** and **Client Secret**
4. Set OAuth2 redirect URI (e.g., `http://localhost:8080/callback`)

## 3. Set Up Configuration

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```env
UPWORK_CLIENT_ID=your_client_id_here
UPWORK_CLIENT_SECRET=your_client_secret_here
```

## 4. Get Access Token

Run the token generation script:

```bash
python get_access_token.py
```

Follow the prompts to:
1. Visit the authorization URL
2. Grant permissions to your app
3. Copy the authorization code
4. Get your access token

Add the access token to your `.env` file.

## 5. Test Connection

```bash
python test_connection.py
```

You should see:
```
✓ Successfully connected to Upwork API
Profile: Your Name - Your Title
```

## 6. Start Monitoring Jobs

### One-Time Search

```bash
python upwork_job_monitor.py
```

This will search for jobs and display a report showing:
- Total jobs found
- Job types (Hourly vs Fixed)
- Budget ranges
- Top 20 skills in demand
- Recent job listings

### Continuous Monitoring

```bash
python upwork_job_monitor.py --continuous --interval 60
```

This runs in the background, checking every 60 minutes for new jobs.

### Filter by Skills

```bash
python upwork_job_monitor.py --skill python
```

### Filter by Pay Rate

```bash
python upwork_job_monitor.py --min-rate 50 --max-rate 150
```

### Export Reports

**JSON format** (for data analysis):
```bash
python upwork_job_monitor.py --report json
```

**CSV format** (for spreadsheets):
```bash
python upwork_job_monitor.py --report csv
```

## 7. View Cached Jobs

All job data is saved to `upwork_jobs.json`. You can:

- View it directly with any text editor
- Import it into data analysis tools
- Process it with custom scripts

Example structure:
```json
{
  "~1234567890": {
    "title": "Python Developer Needed",
    "skills": ["Python", "Django", "REST API"],
    "budget": {
      "type": "Hourly",
      "hourly_rate_min": 50
    }
  }
}
```

## Common Use Cases

### Find High-Paying Python Jobs

```bash
python upwork_job_monitor.py --skill python --min-rate 100
```

### Monitor Multiple Technologies

Edit `.env` and set:
```env
SEARCH_QUERIES=python,javascript,react,node.js,docker,kubernetes
```

Then run:
```bash
python upwork_job_monitor.py --continuous
```

### Generate Daily Reports

Set up a cron job (Linux/Mac):
```bash
# Add to crontab (crontab -e)
0 9 * * * cd /path/to/upwork && python upwork_job_monitor.py --report csv
```

Or use Task Scheduler (Windows).

### Track Specific Skills Over Time

```bash
# Monday
python upwork_job_monitor.py --skill "machine learning" --report json

# Check again Friday
python upwork_job_monitor.py --skill "machine learning" --report json
```

Compare the JSON reports to see demand trends.

## Troubleshooting

### "No access token found"
- Make sure `UPWORK_ACCESS_TOKEN` is set in `.env`
- Run `python get_access_token.py` to generate a new token

### "Connection test failed"
- Verify your credentials are correct
- Check if your access token has expired
- Ensure your app has the required OAuth2 scopes: `r_myprofile`, `r_jobs`, `w_jobs`

### "Failed to search jobs"
- The Upwork API may have rate limits
- Try reducing search frequency
- Check Upwork API status

### No Jobs Found
- Try broader search queries in `.env`
- Adjust budget filters to be less restrictive
- Check if your Upwork account has proper permissions

## Advanced Usage

### Custom Search in Python

```python
from upwork_job_monitor import UpworkJobMonitor

monitor = UpworkJobMonitor()
monitor.search_and_monitor(query="AI developer")

# Get all AI jobs paying over $100/hr
ai_jobs = monitor.get_jobs_by_skill("artificial intelligence")
high_paying = [j for j in ai_jobs if j['budget'].get('hourly_rate_min', 0) > 100]

print(f"Found {len(high_paying)} high-paying AI jobs")
for job in high_paying:
    print(f"- {job['title']}: ${job['budget']['hourly_rate_min']}/hr")
```

### Combine with Other Tools

Export to CSV and analyze with pandas:
```python
import pandas as pd

df = pd.read_csv('upwork_report_20260304_120000.csv')
print(df.groupby('Experience Level')['Budget Amount'].mean())
```

## Next Steps

- Set up continuous monitoring to track market trends
- Analyze which skills command the highest pay
- Customize search queries to match your expertise
- Export data regularly for historical analysis
- Use the Job Application Agent (`upwork_agent.py`) for automated applications

## Support

For issues with:
- **Upwork API**: Visit [Upwork Developer Documentation](https://developers.upwork.com/)
- **This Tool**: Check the main README.md or create an issue

Happy job hunting! 🚀
