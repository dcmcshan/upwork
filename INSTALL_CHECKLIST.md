# Installation & Verification Checklist

## ✅ Pre-Installation Checklist

Before you start, make sure you have:

- [ ] Python 3.7 or higher installed
  ```bash
  python3 --version
  ```

- [ ] pip (Python package manager) installed
  ```bash
  pip3 --version
  ```

- [ ] Upwork API credentials ready
  - [ ] Client ID
  - [ ] Client Secret
  - Get them from: https://www.upwork.com/services/api/apply

## 📦 Installation Steps

### Option 1: Automatic Installation (Recommended)

```bash
# 1. Run installation script
./install.sh

# 2. Edit configuration
nano .env
# Add your UPWORK_CLIENT_ID and UPWORK_CLIENT_SECRET

# 3. Get access token
python get_access_token.py
# Follow the prompts to get UPWORK_ACCESS_TOKEN

# 4. Add token to .env
nano .env
# Add the UPWORK_ACCESS_TOKEN

# 5. Test connection
./upwork test
```

### Option 2: Manual Installation

```bash
# 1. Install dependencies
pip3 install -r requirements.txt

# 2. Create configuration file
cp .env.example .env

# 3. Edit .env with your credentials
nano .env

# 4. Get access token
python get_access_token.py

# 5. Make scripts executable
chmod +x upwork upwork_job_monitor.py job_analytics.py examples.py install.sh

# 6. Test connection
./upwork test
```

## ✅ Post-Installation Verification

### 1. Verify Files Exist

Check that all required files are present:

```bash
# Core scripts (7 files)
ls -1 upwork upwork_job_monitor.py job_analytics.py upwork_api_client.py \
     upwork_agent.py test_connection.py get_access_token.py examples.py

# Setup files (3 files)
ls -1 install.sh .env.example requirements.txt

# Documentation (7 files)
ls -1 *.md
```

Expected output: All files should be listed without "No such file" errors.

### 2. Verify Dependencies Installed

```bash
pip3 show python-dotenv requests selenium webdriver-manager schedule beautifulsoup4 gql aiohttp requests-oauthlib
```

All packages should show "Name:", "Version:", etc.

### 3. Verify Configuration

```bash
# Check .env file exists
ls -l .env

# Verify it contains your credentials (don't share this output!)
cat .env | grep -E "UPWORK_CLIENT_ID|UPWORK_CLIENT_SECRET|UPWORK_ACCESS_TOKEN"
```

You should see your actual values (not "your_client_id_here").

### 4. Test API Connection

```bash
./upwork test
```

Expected output:
```
✓ Successfully connected to Upwork API
Profile: Your Name - Your Title
✓ Connection successful!
```

### 5. Test Basic Search

```bash
./upwork search --query "test"
```

Expected output:
```
[INFO] Searching for: test
[INFO] Found X jobs
[INFO] Search complete: X new, 0 updated
```

### 6. Verify Cache File Created

```bash
ls -l upwork_jobs.json
```

File should exist and have size > 0 bytes.

### 7. Test Analytics

```bash
./upwork analyze
```

Should display a report with:
- Total jobs tracked
- Top skills
- Budget distribution
- etc.

### 8. Test CLI Commands

```bash
# Test stats command
./upwork stats

# Test filter command
./upwork filter --count
```

All commands should work without errors.

## ✅ Feature Verification

Test each major feature:

### Job Monitoring
```bash
# Basic search
./upwork search --query "python"
# Should: Find and cache jobs

# Filtered search
./upwork search --query "javascript"
# Should: Add more jobs to cache
```

### Filtering
```bash
# By skill
./upwork filter --skill python --list
# Should: Show Python jobs

# By rate
./upwork filter --min-rate 50 --max-rate 150 --list
# Should: Show jobs in rate range
```

### Analytics
```bash
# Full report
./upwork analyze
# Should: Display comprehensive report

# Skill analysis
./upwork analyze --skill python
# Should: Show Python-specific stats

# Export
./upwork analyze --export test_insights.json
# Should: Create JSON file
ls -l test_insights.json
```

### Statistics
```bash
./upwork stats
# Should: Show cache statistics
```

## ✅ Documentation Verification

Check that all documentation exists and is readable:

```bash
# Essential docs
ls -l START_HERE.md README.md QUICKSTART.md USER_GUIDE.md SUMMARY.md OVERVIEW.md PROJECT_MAP.txt

# Try reading one
cat START_HERE.md | head -20
```

## 🔍 Troubleshooting Common Issues

### Issue: "ModuleNotFoundError: No module named 'dotenv'"
**Solution:**
```bash
pip3 install python-dotenv
# or
pip3 install -r requirements.txt
```

### Issue: "Permission denied" when running scripts
**Solution:**
```bash
chmod +x upwork upwork_job_monitor.py job_analytics.py examples.py install.sh
```

### Issue: "No access token found"
**Solution:**
```bash
python get_access_token.py
# Follow prompts to get token
# Add token to .env file
```

### Issue: "Connection test failed"
**Solutions:**
1. Check credentials in `.env`
2. Verify token hasn't expired
3. Regenerate token: `python get_access_token.py`
4. Ensure OAuth2 scopes: r_myprofile, r_jobs, w_jobs

### Issue: "./upwork: command not found"
**Solution:**
```bash
# Use full path
./upwork test

# Or add to PATH
export PATH=$PATH:$(pwd)
upwork test
```

### Issue: "No jobs found"
**Solutions:**
1. Try broader search queries
2. Check Upwork API status
3. Verify your account has proper permissions
4. Try different search terms

## ✅ Final Checklist

Before considering the installation complete, verify:

- [x] All files present (21 total)
- [x] Dependencies installed
- [x] .env file configured with actual credentials
- [x] Access token obtained and added to .env
- [x] Connection test passes (./upwork test)
- [x] Basic search works (./upwork search --query "test")
- [x] Cache file created (upwork_jobs.json)
- [x] Analytics works (./upwork analyze)
- [x] All CLI commands work
- [x] Documentation readable

## 🎉 Success!

If all checks pass, you're ready to start monitoring Upwork jobs!

### First Steps:

1. **Build your job database:**
   ```bash
   ./upwork search --query "your primary skill"
   ```

2. **Analyze the market:**
   ```bash
   ./upwork analyze
   ```

3. **Find high-value opportunities:**
   ```bash
   ./upwork filter --min-rate 75 --list
   ```

4. **Set up continuous monitoring:**
   ```bash
   ./upwork search --continuous --interval 60
   ```

### Next Steps:

- Read [USER_GUIDE.md](USER_GUIDE.md) for advanced features
- Run `python examples.py` to see code examples
- Customize `.env` with your preferred search queries
- Schedule regular exports for historical analysis

### Getting Help:

- **Quick questions**: Check [SUMMARY.md](SUMMARY.md)
- **Setup issues**: See [QUICKSTART.md](QUICKSTART.md)
- **Feature details**: Read [USER_GUIDE.md](USER_GUIDE.md)
- **Visual guide**: See [OVERVIEW.md](OVERVIEW.md)

## 📝 Maintenance

### Regular Tasks:

1. **Update dependencies** (monthly):
   ```bash
   pip3 install --upgrade -r requirements.txt
   ```

2. **Rotate access token** (every 3-6 months):
   ```bash
   python get_access_token.py
   # Update .env with new token
   ```

3. **Archive old data** (as needed):
   ```bash
   mv upwork_jobs.json archive/upwork_jobs_$(date +%Y%m%d).json
   ```

4. **Export insights** (weekly/monthly):
   ```bash
   ./upwork analyze --export insights_$(date +%Y%m%d).json
   ```

---

**Happy job monitoring!** 🚀

For any issues, refer to the documentation or run `python examples.py` for interactive examples.
