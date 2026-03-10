// CUSTOMIZE YOUR PROFESSIONAL BACKGROUND HERE
// Edit this file to personalize your cover letters

const PROFESSIONAL_BACKGROUND = {
    // Your basic information
    name: "Your Name",
    title: "Full-Stack Developer & AI/ML Specialist",
    
    // Your technical skills (add or remove as needed)
    skills: [
        // Programming Languages
        "Python",
        "JavaScript",
        "TypeScript",
        
        // Frontend
        "React",
        "Vue.js",
        "HTML/CSS",
        
        // Backend
        "Node.js",
        "Django",
        "FastAPI",
        "Express",
        
        // Databases
        "PostgreSQL",
        "MongoDB",
        "Redis",
        "MySQL",
        
        // Cloud & DevOps
        "AWS",
        "Docker",
        "Kubernetes",
        "CI/CD",
        "Git",
        
        // Specialized Skills
        "Machine Learning",
        "AI Integration",
        "API Development",
        "Web Scraping",
        "Automation",
        "Data Analysis",
        "RESTful APIs",
        "GraphQL"
    ],
    
    // Your work experience
    experience: [
        {
            role: "Technical Lead",
            company: "Syzygyx",
            description: "Led development of AI-powered platforms and automation tools"
        },
        {
            role: "Full-Stack Developer",
            company: "Various Projects",
            description: "Built scalable web applications, APIs, and automation systems"
        },
        {
            role: "Software Engineer",
            company: "Previous Company",
            description: "Developed and maintained production applications"
        }
    ],
    
    // Notable projects you've worked on
    projects: [
        "Upwork Job Monitoring & Analytics System with Python",
        "AI-powered automation tools and chatbots",
        "RESTful API development and integration",
        "Web scraping and data extraction systems",
        "Real-time monitoring dashboards",
        "E-commerce platforms with payment integration",
        "Mobile-responsive web applications"
    ],
    
    // Your professional strengths
    strengths: [
        "Quick learner and problem solver",
        "Strong communication skills",
        "Experience with agile development",
        "Proven track record of delivering quality code",
        "Self-motivated and detail-oriented",
        "Available for immediate start",
        "Comfortable with remote work",
        "Strong debugging and troubleshooting skills"
    ],
    
    // Optional: Your hourly rate or budget preferences
    rates: {
        hourly: "$50-100/hr",
        preferred: "Hourly or Fixed-price"
    },
    
    // Optional: Your availability
    availability: {
        hoursPerWeek: "40+",
        timezone: "Your Timezone",
        startDate: "Immediate"
    }
};

// Export for use in app.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = PROFESSIONAL_BACKGROUND;
}
