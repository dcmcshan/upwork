# Upwork Cover Letter Generator

A GitHub Pages site that combines Upwork job browsing with an AI-powered cover letter generator.

## Features

- **Split-screen interface**: Browse Upwork jobs on the left, generate cover letters on the right
- **Smart cover letter generation**: Analyzes job descriptions and creates personalized cover letters
- **Skill matching**: Automatically highlights your relevant skills based on job requirements
- **One-click copy**: Copy generated cover letters to clipboard instantly
- **Responsive design**: Works on desktop and mobile devices

## How to Use

1. Browse Upwork jobs in the left panel
2. Copy a job description you're interested in
3. Paste it into the "Job Description" field on the right
4. Click "Generate Cover Letter"
5. Review and copy the generated cover letter
6. Apply to the job with your personalized cover letter!

## Customization

Edit `docs/app.js` to customize your professional background:

```javascript
const PROFESSIONAL_BACKGROUND = {
    name: "Your Name",
    title: "Your Professional Title",
    skills: [...],
    experience: [...],
    projects: [...],
    strengths: [...]
};
```

## GitHub Pages Setup

1. Go to your repository Settings
2. Navigate to Pages section
3. Under "Source", select "Deploy from a branch"
4. Choose the `main` branch and `/docs` folder
5. Click Save
6. Your site will be available at: `https://[username].github.io/[repo-name]/`

## Technology Stack

- Pure HTML/CSS/JavaScript (no build process required)
- Responsive design with CSS Grid and Flexbox
- Modern ES6+ JavaScript
- GitHub Pages for hosting

## Local Development

Simply open `docs/index.html` in your browser. No build process or server required!

## License

Personal use. See Upwork's Terms of Service for job application guidelines.
