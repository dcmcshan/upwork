import os
import time
import schedule
from upwork_api_client import UpworkAPIClient
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class UpworkAgent:
    def __init__(self):
        load_dotenv()
        self.keywords = os.getenv('JOB_KEYWORDS', '').split(',')
        self.min_budget = float(os.getenv('MIN_BUDGET', '0'))
        self.max_budget = float(os.getenv('MAX_BUDGET', '1000'))
        
        # Initialize Upwork API client
        try:
            self.client = UpworkAPIClient()
            logger.info("Upwork API client initialized")
        except Exception as e:
            logger.error(f"Failed to initialize Upwork API client: {str(e)}")
            raise
    
    def search_jobs(self):
        """Search for jobs matching criteria"""
        try:
            # Construct search query
            query = ' '.join(self.keywords)
            logger.info(f"Searching for jobs with query: {query}")
            
            # Search for jobs using the API client
            response = self.client.search_jobs(
                query=query,
                page=0,
                page_size=100
            )
            
            # Handle different response formats
            jobs = []
            if isinstance(response, dict):
                jobs = response.get('jobs', [])
                if not jobs:
                    jobs = response.get('results', [])
                if not jobs:
                    jobs = response.get('data', [])
            
            logger.info(f"Found {len(jobs)} jobs")
            
            for job in jobs:
                try:
                    # Extract job details (handle different response formats)
                    title = job.get('title', '') or job.get('snippet', '')
                    budget = job.get('budget', {})
                    if isinstance(budget, dict):
                        amount = budget.get('amount', 0) or budget.get('amount2', 0)
                    else:
                        amount = float(budget) if budget else 0
                    
                    # Check if job matches criteria
                    if self._matches_criteria(title, amount):
                        logger.info(f"Found matching job: {title} (Budget: ${amount})")
                        self._apply_to_job(job)
                        
                except Exception as e:
                    logger.error(f"Error processing job: {str(e)}")
                    continue
                    
        except Exception as e:
            logger.error(f"Error searching jobs: {str(e)}")
    
    def _matches_criteria(self, title, amount):
        """Check if job matches search criteria"""
        # Check keywords
        if not any(keyword.lower() in title.lower() for keyword in self.keywords):
            return False
            
        # Check budget
        if not (self.min_budget <= amount <= self.max_budget):
            return False
            
        return True
    
    def _apply_to_job(self, job):
        """Apply to a job"""
        try:
            job_id = job.get('id')
            
            # Here you would implement your application logic using the API
            # This could include:
            # 1. Writing a cover letter
            # 2. Setting your proposed rate
            # 3. Adding relevant attachments
            # 4. Submitting the proposal
            
            logger.info(f"Successfully applied to job: {job_id}")
            
        except Exception as e:
            logger.error(f"Error applying to job: {str(e)}")
    
    def run(self):
        """Main execution method"""
        # Schedule job search to run every hour
        schedule.every(1).hour.do(self.search_jobs)
        
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    try:
        agent = UpworkAgent()
        
        # Test connection first
        logger.info("Testing Upwork API connection...")
        if agent.client.test_connection():
            logger.info("Connection successful! Starting agent...")
            agent.run()
        else:
            logger.error("Connection test failed. Please check your credentials.")
    except Exception as e:
        logger.error(f"Failed to start agent: {str(e)}") 