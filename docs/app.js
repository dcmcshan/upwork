// Professional background and skills - loaded from config.js
// If config.js is not loaded, use default values
// Note: config.js defines PROFESSIONAL_BACKGROUND, app.js just uses it

// Generate cover letter using AI-like logic
async function generateCoverLetter() {
    const jobDescription = document.getElementById('jobDescription').value.trim();
    const generateBtn = document.getElementById('generateBtn');
    const outputSection = document.getElementById('outputSection');
    const outputDiv = document.getElementById('coverLetterOutput');
    
    if (!jobDescription) {
        alert('Please paste a job description first!');
        return;
    }
    
    // Show loading state
    generateBtn.disabled = true;
    generateBtn.textContent = 'Generating...';
    outputSection.style.display = 'block';
    outputDiv.innerHTML = '<div class="loading">✨ Crafting your cover letter...</div>';
    
    try {
        // Simulate processing time
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        // Extract key information from job description
        const jobInfo = extractJobInfo(jobDescription);
        
        // Generate personalized cover letter
        const coverLetter = createCoverLetter(jobInfo);
        
        // Display result
        outputDiv.textContent = coverLetter;
        
    } catch (error) {
        outputDiv.innerHTML = `<div class="error">Error generating cover letter. Please try again.</div>`;
    } finally {
        generateBtn.disabled = false;
        generateBtn.textContent = 'Generate Cover Letter';
    }
}

// Extract relevant information from job description
function extractJobInfo(description) {
    const lowerDesc = description.toLowerCase();
    
    // Extract required skills
    const requiredSkills = PROFESSIONAL_BACKGROUND.skills.filter(skill => 
        lowerDesc.includes(skill.toLowerCase())
    );
    
    // Detect job type
    const isAI = lowerDesc.includes('ai') || lowerDesc.includes('machine learning') || 
                 lowerDesc.includes('ml') || lowerDesc.includes('artificial intelligence');
    const isFullStack = lowerDesc.includes('full stack') || lowerDesc.includes('full-stack');
    const isBackend = lowerDesc.includes('backend') || lowerDesc.includes('back-end');
    const isFrontend = lowerDesc.includes('frontend') || lowerDesc.includes('front-end');
    const isAPI = lowerDesc.includes('api') || lowerDesc.includes('rest') || lowerDesc.includes('graphql');
    const isAutomation = lowerDesc.includes('automation') || lowerDesc.includes('scraping');
    
    // Detect technologies
    const hasPython = lowerDesc.includes('python');
    const hasJavaScript = lowerDesc.includes('javascript') || lowerDesc.includes('js');
    const hasReact = lowerDesc.includes('react');
    const hasNode = lowerDesc.includes('node') || lowerDesc.includes('nodejs');
    const hasAWS = lowerDesc.includes('aws') || lowerDesc.includes('amazon web services');
    const hasDocker = lowerDesc.includes('docker') || lowerDesc.includes('container');
    
    return {
        requiredSkills,
        isAI,
        isFullStack,
        isBackend,
        isFrontend,
        isAPI,
        isAutomation,
        hasPython,
        hasJavaScript,
        hasReact,
        hasNode,
        hasAWS,
        hasDocker,
        description
    };
}

// Create personalized cover letter
function createCoverLetter(jobInfo) {
    const greeting = "Dear Hiring Manager,";
    
    // Opening paragraph - show enthusiasm and relevance
    let opening = "I'm excited to apply for this position. ";
    
    if (jobInfo.isFullStack) {
        opening += "As a full-stack developer with extensive experience in both frontend and backend technologies, I'm confident I can deliver exactly what you need. ";
    } else if (jobInfo.isBackend) {
        opening += "With my strong background in backend development and API design, I'm well-equipped to tackle this project. ";
    } else if (jobInfo.isFrontend) {
        opening += "As a frontend developer with a keen eye for user experience, I can create the polished interface you're looking for. ";
    } else {
        opening += "With my diverse technical background and problem-solving skills, I'm confident I can deliver excellent results for your project. ";
    }
    
    // Skills paragraph - highlight relevant skills
    let skillsPara = "My technical expertise includes ";
    
    if (jobInfo.requiredSkills.length > 0) {
        skillsPara += jobInfo.requiredSkills.slice(0, 5).join(", ");
        if (jobInfo.requiredSkills.length > 5) {
            skillsPara += ", and more";
        }
    } else {
        skillsPara += PROFESSIONAL_BACKGROUND.skills.slice(0, 6).join(", ");
    }
    
    skillsPara += ". ";
    
    // Add specific technology mentions
    if (jobInfo.isAI) {
        skillsPara += "I have hands-on experience with machine learning, AI integration, and building intelligent automation systems. ";
    }
    
    if (jobInfo.isAPI) {
        skillsPara += "I've designed and built numerous RESTful APIs with proper authentication, rate limiting, and comprehensive documentation. ";
    }
    
    if (jobInfo.isAutomation) {
        skillsPara += "I've developed sophisticated web scraping and automation tools, including my recent Upwork job monitoring system. ";
    }
    
    // Experience paragraph
    let experiencePara = "I've successfully delivered projects ranging from ";
    
    const relevantProjects = [];
    if (jobInfo.hasPython) relevantProjects.push("Python-based automation tools");
    if (jobInfo.hasReact) relevantProjects.push("React applications");
    if (jobInfo.hasNode) relevantProjects.push("Node.js backends");
    if (jobInfo.isAPI) relevantProjects.push("RESTful API development");
    
    if (relevantProjects.length > 0) {
        experiencePara += relevantProjects.join(", ");
    } else {
        experiencePara += "web applications to data processing systems";
    }
    
    experiencePara += ". I'm comfortable working independently, communicating clearly, and delivering clean, maintainable code on schedule. ";
    
    // Closing paragraph
    const closing = "I'd love to discuss how I can contribute to your project. I'm available to start immediately and can adapt to your preferred communication style and workflow. Looking forward to hearing from you!";
    
    const signature = "\nBest regards,\n" + PROFESSIONAL_BACKGROUND.name;
    
    // Combine all parts
    return `${greeting}\n\n${opening}\n\n${skillsPara}\n\n${experiencePara}\n\n${closing}\n${signature}`;
}

// Copy cover letter to clipboard
async function copyCoverLetter() {
    const coverLetter = document.getElementById('coverLetterOutput').textContent;
    
    try {
        await navigator.clipboard.writeText(coverLetter);
        
        // Show feedback
        const btn = event.target;
        const originalText = btn.textContent;
        btn.textContent = '✓ Copied!';
        btn.style.background = '#14a800';
        
        setTimeout(() => {
            btn.textContent = originalText;
            btn.style.background = '#0073b1';
        }, 2000);
        
    } catch (err) {
        // Fallback for older browsers
        const textarea = document.createElement('textarea');
        textarea.value = coverLetter;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        
        alert('Cover letter copied to clipboard!');
    }
}

// Allow Enter key to generate (with Ctrl/Cmd)
document.getElementById('jobDescription').addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        generateCoverLetter();
    }
});
