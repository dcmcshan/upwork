# Project Structure

## 📁 Directory Layout

```
upwork-agent/
├── docs/                          # GitHub Pages site
│   ├── index.html                 # Main page (UI)
│   ├── app.js                     # Cover letter generation logic
│   ├── config.js                  # Your professional background (CUSTOMIZE THIS!)
│   ├── test-local.sh              # Local testing script
│   ├── README.md                  # Docs folder readme
│   ├── QUICK_START.md             # Quick start guide
│   ├── EXAMPLE.md                 # Example cover letters
│   └── FEATURES.md                # Feature documentation
│
├── Python Scripts (Job Monitoring)
│   ├── upwork_api_client.py       # Upwork API wrapper
│   ├── upwork_job_monitor.py      # Job tracking & caching
│   ├── job_analytics.py           # Analytics & insights
│   ├── upwork_agent.py            # Auto-application agent
│   ├── test_connection.py         # API connection tester
│   ├── get_access_token.py        # OAuth token generator
│   ├── examples.py                # Usage examples
│   └── upwork                     # Unified CLI tool
│
├── Configuration
│   ├── .env                       # Your API credentials (DO NOT COMMIT!)
│   ├── .env.example               # Template for .env
│   └── requirements.txt           # Python dependencies
│
├── Documentation
│   ├── README.md                  # Main project readme
│   ├── QUICKSTART.md              # Python tools quick start
│   ├── USER_GUIDE.md              # Comprehensive guide
│   ├── OVERVIEW.md                # Visual overview
│   ├── SUMMARY.md                 # Command reference
│   ├── GITHUB_PAGES_SETUP.md      # GitHub Pages setup guide
│   ├── DEPLOYMENT_CHECKLIST.md    # Deployment checklist
│   └── PROJECT_STRUCTURE.md       # This file
│
└── Other Files
    ├── .gitignore                 # Git ignore rules
    ├── install.sh                 # Installation script
    └── McShanCV.pdf               # Your CV (for reference)
```

## 🎯 Two Main Components

### 1. GitHub Pages Site (docs/)
**Purpose**: Generate personalized cover letters in your browser

**Key Files**:
- `index.html` - The web interface
- `app.js` - Cover letter generation logic
- `config.js` - **YOUR PROFILE** (customize this!)

**How it works**:
```
User visits site
    ↓
Pastes job description
    ↓
Clicks "Generate"
    ↓
app.js analyzes job + matches skills from config.js
    ↓
Generates personalized cover letter
    ↓
User copies and applies
```

### 2. Python Job Monitor (root/)
**Purpose**: Track Upwork jobs, analyze trends, monitor market

**Key Files**:
- `upwork_api_client.py` - API communication
- `upwork_job_monitor.py` - Job tracking
- `job_analytics.py` - Market insights

**How it works**:
```
Script runs
    ↓
Searches Upwork via API
    ↓
Caches jobs to upwork_jobs.json
    ↓
Analyzes skills, pay rates, trends
    ↓
Generates reports
```

## 🔄 How They Work Together

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  1. Python Scripts Monitor Upwork                      │
│     - Track jobs                                        │
│     - Analyze market trends                            │
│     - Identify in-demand skills                        │
│                                                         │
│  2. Update Your Skills in config.js                    │
│     - Based on market insights                         │
│     - Add trending technologies                        │
│     - Highlight valuable skills                        │
│                                                         │
│  3. GitHub Pages Site Generates Letters                │
│     - Uses your updated profile                        │
│     - Matches job requirements                         │
│     - Creates personalized cover letters               │
│                                                         │
│  4. Apply to Jobs                                      │
│     - With data-driven cover letters                   │
│     - Highlighting relevant skills                     │
│     - Based on market insights                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 📝 File Purposes

### GitHub Pages Files

| File | Purpose | Customize? |
|------|---------|------------|
| `index.html` | UI layout and styling | Optional |
| `app.js` | Cover letter generation logic | Optional |
| `config.js` | **Your professional background** | **YES!** |
| `test-local.sh` | Local testing script | No |
| `*.md` | Documentation | No |

### Python Files

| File | Purpose | Use When |
|------|---------|----------|
| `upwork_api_client.py` | API wrapper | Building custom tools |
| `upwork_job_monitor.py` | Job tracking | Monitoring market |
| `job_analytics.py` | Market analysis | Understanding trends |
| `upwork_agent.py` | Auto-apply | Automating applications |
| `test_connection.py` | API testing | Setting up |
| `upwork` | CLI tool | Daily use |

### Configuration Files

| File | Purpose | Required? |
|------|---------|-----------|
| `.env` | API credentials | For Python scripts |
| `.env.example` | Template | No (reference) |
| `requirements.txt` | Python packages | For Python scripts |
| `config.js` | Your profile | For GitHub Pages |

## 🚀 Quick Start Paths

### Path 1: Just Want Cover Letters
```bash
1. Edit docs/config.js
2. Open docs/index.html in browser
3. Start generating letters!
```

### Path 2: Want Job Monitoring Too
```bash
1. Install Python dependencies
2. Set up .env with API credentials
3. Run: ./upwork search
4. Analyze: ./upwork analyze
5. Update docs/config.js with insights
6. Deploy GitHub Pages
```

### Path 3: Full Setup
```bash
1. Follow QUICKSTART.md for Python setup
2. Follow GITHUB_PAGES_SETUP.md for site
3. Use both tools together
4. Iterate and improve
```

## 🎨 Customization Points

### Essential (Do These First)
1. ✅ `docs/config.js` - Your profile
2. ✅ `.env` - API credentials (if using Python)

### Optional (Nice to Have)
3. `docs/index.html` - Colors, layout
4. `docs/app.js` - Letter generation logic
5. `upwork_job_monitor.py` - Search queries

### Advanced (For Power Users)
6. Custom analytics in `job_analytics.py`
7. Auto-apply logic in `upwork_agent.py`
8. API client extensions in `upwork_api_client.py`

## 📊 Data Flow

### GitHub Pages Site
```
Job Description (input)
    ↓
extractJobInfo() - Analyze requirements
    ↓
Match with config.js skills
    ↓
createCoverLetter() - Generate text
    ↓
Cover Letter (output)
```

### Python Job Monitor
```
Upwork API
    ↓
upwork_api_client.py - Fetch jobs
    ↓
upwork_job_monitor.py - Cache & filter
    ↓
upwork_jobs.json - Store data
    ↓
job_analytics.py - Analyze trends
    ↓
Reports & Insights
```

## 🔧 Development Workflow

### For GitHub Pages Site
```bash
1. Edit docs/config.js or docs/app.js
2. Test: cd docs && ./test-local.sh
3. Commit: git add docs/ && git commit -m "Update"
4. Push: git push
5. Wait 1-2 minutes for GitHub Pages to update
```

### For Python Scripts
```bash
1. Edit Python files
2. Test: python script_name.py
3. Verify output
4. Commit and push
```

## 📚 Documentation Map

**Getting Started**:
- `README.md` - Project overview
- `QUICKSTART.md` - Python setup
- `docs/QUICK_START.md` - GitHub Pages setup

**Detailed Guides**:
- `USER_GUIDE.md` - Python tools reference
- `GITHUB_PAGES_SETUP.md` - Deployment guide
- `OVERVIEW.md` - Visual guide

**Reference**:
- `SUMMARY.md` - Command reference
- `docs/EXAMPLE.md` - Cover letter examples
- `docs/FEATURES.md` - Feature documentation

**Checklists**:
- `DEPLOYMENT_CHECKLIST.md` - Deployment steps
- `INSTALL_CHECKLIST.md` - Installation steps

## 🎯 Next Steps

1. **For Cover Letters**: Start with `docs/QUICK_START.md`
2. **For Job Monitoring**: Start with `QUICKSTART.md`
3. **For Both**: Do both guides in order

---

**Questions about the structure?** Check the relevant documentation file or open an issue!
