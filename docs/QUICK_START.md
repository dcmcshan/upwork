# Quick Start Guide

Get your Upwork Cover Letter Generator live in 5 minutes!

## ⚡ Super Quick Setup

### 1. Customize (2 minutes)

Edit `config.js`:

```javascript
const PROFESSIONAL_BACKGROUND = {
    name: "John Doe",  // ← Change this
    title: "Full-Stack Developer",  // ← Change this
    
    skills: [
        "Python",
        "JavaScript",
        // Add your skills here
    ],
    
    // Update experience, projects, etc.
};
```

### 2. Test Locally (1 minute)

```bash
cd docs
./test-local.sh
# Visit http://localhost:8000
```

Or just open `docs/index.html` in your browser!

### 3. Deploy to GitHub Pages (2 minutes)

1. Push to GitHub:
   ```bash
   git add docs/
   git commit -m "Add cover letter generator"
   git push
   ```

2. Enable GitHub Pages:
   - Go to repo Settings → Pages
   - Source: `main` branch, `/docs` folder
   - Save

3. Done! Visit: `https://[username].github.io/[repo]/`

## 🎯 How to Use

1. **Open your site** (the URL from step 3 above)
2. **Browse Upwork jobs** in the left panel
3. **Copy a job description** you like
4. **Paste it** in the right panel
5. **Click "Generate Cover Letter"**
6. **Copy and apply!**

## 🎨 Customize Further

### Change Upwork Search

Edit `index.html`:
```html
<iframe src="https://www.upwork.com/nx/search/jobs/?q=python"></iframe>
                                                        ↑
                                                   Change this
```

### Adjust Cover Letter Style

Edit `app.js` → `createCoverLetter()` function

### Change Colors

Edit `index.html` CSS:
```css
.header {
    background: #14a800;  /* ← Change this */
}
```

## 📱 Mobile Friendly

Works great on phones! The layout automatically stacks vertically.

## 🔒 Privacy

- Everything runs in your browser
- No data sent to servers
- No tracking or analytics (unless you add them)
- Your job descriptions stay private

## 🆘 Troubleshooting

### Site not loading?
- Wait 5 minutes after enabling GitHub Pages
- Check Settings → Pages for the URL
- Clear browser cache

### Upwork iframe blocked?
- Normal browser security
- Open Upwork in separate tab instead
- Generator still works perfectly!

### Cover letter not generating?
- Check browser console (F12)
- Make sure you pasted a job description
- Try a different job description

## 📚 More Help

- **Full setup guide**: `GITHUB_PAGES_SETUP.md`
- **Examples**: `EXAMPLE.md`
- **Features**: `FEATURES.md`
- **Checklist**: `DEPLOYMENT_CHECKLIST.md`

## 🎉 That's It!

You now have a professional cover letter generator that:
- ✅ Analyzes job descriptions
- ✅ Matches your skills
- ✅ Generates personalized letters
- ✅ Works on any device
- ✅ Is completely free

**Start applying to jobs with better cover letters today!** 🚀

---

**Your site URL:**
```
https://[your-github-username].github.io/[repo-name]/
```

**Questions?** Check the other documentation files or open an issue on GitHub.
