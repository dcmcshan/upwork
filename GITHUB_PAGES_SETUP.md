# GitHub Pages Setup Guide

This guide will help you deploy your Upwork Cover Letter Generator to GitHub Pages.

## Quick Setup (5 minutes)

### Step 1: Customize Your Profile

1. Open `docs/config.js`
2. Update your information:
   - Name and title
   - Skills (add/remove as needed)
   - Work experience
   - Projects
   - Professional strengths

### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Scroll down to **Pages** (left sidebar)
4. Under **Source**:
   - Select branch: `main`
   - Select folder: `/docs`
5. Click **Save**

### Step 3: Access Your Site

After a few minutes, your site will be live at:
```
https://[your-username].github.io/[repo-name]/
```

For example:
```
https://johndoe.github.io/upwork-agent/
```

## How to Use the Site

1. **Browse Jobs**: The left panel shows Upwork's job search
2. **Copy Job Description**: Find a job you like and copy its description
3. **Generate Cover Letter**: Paste the description in the right panel
4. **Click Generate**: The AI will create a personalized cover letter
5. **Copy & Apply**: Copy the letter and use it in your Upwork application

## Customization Tips

### Update Your Skills

Edit `docs/config.js`:

```javascript
skills: [
    "Python",
    "JavaScript",
    "Your Skill Here",
    // Add more skills
]
```

### Change the Upwork URL

Edit `docs/index.html` to change the default Upwork search:

```html
<iframe src="https://www.upwork.com/nx/search/jobs/?q=python"></iframe>
```

You can customize the search query:
- `?q=python` - Search for Python jobs
- `?q=javascript` - Search for JavaScript jobs
- `?q=web+development` - Search for web development jobs

### Modify Cover Letter Style

Edit the `createCoverLetter()` function in `docs/app.js` to change:
- Greeting style
- Paragraph structure
- Tone and language
- Closing signature

## Advanced Customization

### Add Your Photo

1. Add your photo to `docs/` folder (e.g., `profile.jpg`)
2. Update `docs/index.html` to include it in the header

### Change Colors

Edit the CSS in `docs/index.html`:

```css
.header {
    background: #14a800; /* Upwork green - change this */
}

.btn {
    background: #14a800; /* Button color - change this */
}
```

### Add Analytics

Add Google Analytics or other tracking to `docs/index.html`:

```html
<head>
    <!-- Your analytics code here -->
</head>
```

## Troubleshooting

### Site Not Loading?

1. Check that GitHub Pages is enabled in Settings
2. Verify the branch is `main` and folder is `/docs`
3. Wait 5-10 minutes for initial deployment
4. Check the Actions tab for build errors

### Upwork iframe Not Showing?

Some browsers block iframes. Users can:
1. Open Upwork in a separate tab
2. Copy job descriptions from there
3. Use the generator panel on your site

### Cover Letters Not Generating?

1. Check browser console for errors (F12)
2. Verify `config.js` is loaded before `app.js`
3. Make sure JavaScript is enabled

## Local Testing

Test locally before deploying:

```bash
# Option 1: Open directly
open docs/index.html

# Option 2: Use a local server
cd docs
python -m http.server 8000
# Visit http://localhost:8000
```

## Updating Your Site

1. Edit files in the `docs/` folder
2. Commit and push to GitHub:
   ```bash
   git add docs/
   git commit -m "Update cover letter generator"
   git push
   ```
3. Changes will be live in 1-2 minutes

## Security Notes

- Never commit API keys or tokens to the repository
- The site runs entirely in the browser (no backend)
- No data is stored or transmitted to external servers
- Cover letters are generated locally using JavaScript

## Next Steps

1. Customize `docs/config.js` with your real information
2. Test the generator with real job descriptions
3. Adjust the cover letter template to match your style
4. Share your site URL on your resume or LinkedIn

## Need Help?

- Check the browser console for errors (F12)
- Review the code comments in `docs/app.js`
- Test with different job descriptions
- Adjust the skill matching logic as needed

---

**Your site URL will be:**
`https://[your-github-username].github.io/[this-repo-name]/`

Happy job hunting! 🚀
