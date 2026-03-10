#!/usr/bin/env python3
"""
Upwork Job Monitor - Track job postings with skills and pay information
"""
import os
import json
import time
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv
from upwork_api_client import UpworkAPIClient

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class UpworkJobMonitor:
    """Monitor Upwork jobs and track skills and pay information."""
    
    def __init__(self, output_file: str = "upwork_jobs.json"):
        """
        Initialize the job monitor.
        
        Args:
            output_file: File to store job data
        """
        load_dotenv()
        
        self.output_file = output_file
        self.jobs_cache = self._load_jobs_cache()
        self.client = UpworkAPIClient()
        
        # Search configuration
        self.search_queries = os.getenv('SEARCH_QUERIES', 'python,javascript,web development').split(',')
        self.min_hourly_rate = float(os.getenv('MIN_HOURLY_RATE', '0'))
        self.max_hourly_rate = float(os.getenv('MAX_HOURLY_RATE', '200'))
        self.min_fixed_price = float(os.getenv('MIN_FIXED_PRICE', '0'))
        self.max_fixed_price = float(os.getenv('MAX_FIXED_PRICE', '10000'))
        
        logger.info(f"Monitor initialized. Caching jobs to: {self.output_file}")
    
    def _load_jobs_cache(self) -> Dict[str, Dict]:
        """Load previously cached jobs from file."""
        if os.path.exists(self.output_file):
            try:
                with open(self.output_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not load cache: {e}")
        return {}
    
    def _save_jobs_cache(self):
        """Save jobs cache to file."""
        try:
            with open(self.output_file, 'w') as f:
                json.dump(self.jobs_cache, f, indent=2, default=str)
            logger.info(f"Saved {len(self.jobs_cache)} jobs to {self.output_file}")
        except Exception as e:
            logger.error(f"Failed to save cache: {e}")
    
    def _extract_job_info(self, job: Dict) -> Dict[str, Any]:
        """
        Extract relevant job information from API response.
        
        Args:
            job: Job data from API
            
        Returns:
            Cleaned job information dictionary
        """
        job_info = {
            'id': job.get('id', job.get('ciphertext', 'unknown')),
            'title': job.get('title', job.get('snippet', 'No title')),
            'description': job.get('description', job.get('snippet', '')),
            'posted_on': job.get('date_created', job.get('created_time', datetime.now().isoformat())),
            'url': job.get('url', f"https://www.upwork.com/jobs/~{job.get('id', '')}"),
            'category': job.get('category2', job.get('category', 'Unknown')),
            'job_type': job.get('job_type', job.get('workload', 'Unknown')),
            'duration': job.get('duration', 'Unknown'),
            'experience_level': job.get('tier', job.get('contractor_tier', 'Unknown')),
            'skills': [],
            'budget': {},
            'client_info': {},
            'engagement': job.get('engagement', 'Unknown'),
            'first_seen': datetime.now().isoformat()
        }
        
        # Extract skills
        if 'skills' in job:
            if isinstance(job['skills'], list):
                job_info['skills'] = [
                    skill.get('name', skill) if isinstance(skill, dict) else skill 
                    for skill in job['skills']
                ]
            else:
                job_info['skills'] = job['skills'].split(',') if isinstance(job['skills'], str) else []
        
        # Extract budget information
        budget = job.get('budget', {})
        if isinstance(budget, dict):
            job_info['budget'] = {
                'type': job.get('job_type', 'Unknown'),
                'amount': budget.get('amount', 0) or budget.get('amount2', 0),
                'currency': budget.get('currency_code', 'USD')
            }
        elif budget:
            job_info['budget'] = {
                'type': job.get('job_type', 'Unknown'),
                'amount': float(budget),
                'currency': 'USD'
            }
        
        # For hourly jobs
        if 'hourly_rate' in job or job.get('job_type') == 'Hourly':
            hourly = job.get('hourly_rate', {})
            if isinstance(hourly, dict):
                job_info['budget']['hourly_rate_min'] = hourly.get('amount', 0)
                job_info['budget']['hourly_rate_max'] = hourly.get('amount_max', 0)
            elif 'amount' in job:
                job_info['budget']['hourly_rate_min'] = job.get('amount', 0)
        
        # Extract client information
        client = job.get('client', {})
        if isinstance(client, dict):
            job_info['client_info'] = {
                'location': client.get('location', {}).get('country', 'Unknown'),
                'total_spent': client.get('total_spent', 0),
                'total_jobs': client.get('total_jobs_posted', 0),
                'hire_rate': client.get('total_hire_rate', 0),
                'active_contracts': client.get('active_contract_count', 0),
                'reviews_count': client.get('total_reviews', 0),
                'rating': client.get('rating', 0),
                'payment_verified': client.get('payment_verification_status', False)
            }
        
        return job_info
    
    def _matches_filters(self, job_info: Dict) -> bool:
        """
        Check if job matches configured filters.
        
        Args:
            job_info: Extracted job information
            
        Returns:
            True if job matches filters
        """
        budget = job_info.get('budget', {})
        job_type = budget.get('type', '').lower()
        amount = budget.get('amount', 0)
        
        # Filter by budget
        if 'hourly' in job_type:
            hourly_min = budget.get('hourly_rate_min', 0)
            if hourly_min and (hourly_min < self.min_hourly_rate or hourly_min > self.max_hourly_rate):
                return False
        elif 'fixed' in job_type:
            if amount and (amount < self.min_fixed_price or amount > self.max_fixed_price):
                return False
        
        return True
    
    def search_and_monitor(self, query: str = None, page_size: int = 50):
        """
        Search for jobs and update the monitoring cache.
        
        Args:
            query: Search query (uses configured queries if None)
            page_size: Number of results to fetch per search
        """
        queries = [query] if query else self.search_queries
        
        new_jobs_count = 0
        updated_jobs_count = 0
        
        for search_query in queries:
            search_query = search_query.strip()
            logger.info(f"Searching for: {search_query}")
            
            try:
                response = self.client.search_jobs(
                    query=search_query,
                    page=0,
                    page_size=page_size
                )
                
                # Handle different response formats
                jobs = []
                if isinstance(response, dict):
                    jobs = (response.get('jobs') or 
                           response.get('results') or 
                           response.get('data') or [])
                
                logger.info(f"Found {len(jobs)} jobs for query: {search_query}")
                
                for job in jobs:
                    try:
                        job_info = self._extract_job_info(job)
                        job_id = job_info['id']
                        
                        # Check filters
                        if not self._matches_filters(job_info):
                            continue
                        
                        # Add to cache
                        if job_id not in self.jobs_cache:
                            self.jobs_cache[job_id] = job_info
                            new_jobs_count += 1
                            logger.info(f"New job: {job_info['title']}")
                        else:
                            # Update existing job
                            job_info['first_seen'] = self.jobs_cache[job_id].get('first_seen')
                            job_info['last_updated'] = datetime.now().isoformat()
                            self.jobs_cache[job_id] = job_info
                            updated_jobs_count += 1
                            
                    except Exception as e:
                        logger.error(f"Error processing job: {e}")
                        continue
                
            except Exception as e:
                logger.error(f"Error searching for '{search_query}': {e}")
                continue
        
        # Save updated cache
        self._save_jobs_cache()
        
        logger.info(f"Monitoring update complete: {new_jobs_count} new jobs, {updated_jobs_count} updated")
        return new_jobs_count, updated_jobs_count
    
    def get_jobs_by_skill(self, skill: str) -> List[Dict]:
        """
        Get all jobs that require a specific skill.
        
        Args:
            skill: Skill name to search for
            
        Returns:
            List of jobs requiring the skill
        """
        matching_jobs = []
        skill_lower = skill.lower()
        
        for job_id, job_info in self.jobs_cache.items():
            job_skills = [s.lower() for s in job_info.get('skills', [])]
            if skill_lower in job_skills or any(skill_lower in s for s in job_skills):
                matching_jobs.append(job_info)
        
        return matching_jobs
    
    def get_jobs_by_budget_range(self, min_amount: float = None, 
                                 max_amount: float = None,
                                 job_type: str = None) -> List[Dict]:
        """
        Get jobs within a specific budget range.
        
        Args:
            min_amount: Minimum budget/rate
            max_amount: Maximum budget/rate
            job_type: 'hourly' or 'fixed'
            
        Returns:
            List of matching jobs
        """
        matching_jobs = []
        
        for job_id, job_info in self.jobs_cache.items():
            budget = job_info.get('budget', {})
            b_type = budget.get('type', '').lower()
            
            if job_type and job_type.lower() not in b_type:
                continue
            
            if 'hourly' in b_type:
                rate = budget.get('hourly_rate_min', 0)
            else:
                rate = budget.get('amount', 0)
            
            if min_amount is not None and rate < min_amount:
                continue
            if max_amount is not None and rate > max_amount:
                continue
            
            matching_jobs.append(job_info)
        
        return matching_jobs
    
    def generate_report(self, output_format: str = 'console'):
        """
        Generate a report of monitored jobs.
        
        Args:
            output_format: 'console', 'json', or 'csv'
        """
        if not self.jobs_cache:
            logger.warning("No jobs in cache. Run search first.")
            return
        
        total_jobs = len(self.jobs_cache)
        
        # Aggregate statistics
        skills_count = {}
        budget_ranges = {'<50': 0, '50-100': 0, '100-200': 0, '>200': 0}
        job_types = {}
        
        for job_id, job_info in self.jobs_cache.items():
            # Count skills
            for skill in job_info.get('skills', []):
                skills_count[skill] = skills_count.get(skill, 0) + 1
            
            # Count budget ranges
            budget = job_info.get('budget', {})
            amount = budget.get('amount', 0) or budget.get('hourly_rate_min', 0)
            if amount < 50:
                budget_ranges['<50'] += 1
            elif amount < 100:
                budget_ranges['50-100'] += 1
            elif amount < 200:
                budget_ranges['100-200'] += 1
            else:
                budget_ranges['>200'] += 1
            
            # Count job types
            jtype = budget.get('type', 'Unknown')
            job_types[jtype] = job_types.get(jtype, 0) + 1
        
        # Sort skills by frequency
        top_skills = sorted(skills_count.items(), key=lambda x: x[1], reverse=True)[:20]
        
        if output_format == 'console':
            print("\n" + "="*80)
            print(f"UPWORK JOB MONITORING REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("="*80)
            print(f"\nTotal Jobs Tracked: {total_jobs}")
            
            print(f"\n{'Job Types:':<30}")
            for jtype, count in job_types.items():
                print(f"  {jtype:<25} {count:>5} ({count/total_jobs*100:.1f}%)")
            
            print(f"\n{'Budget Ranges ($/hr or $):':<30}")
            for range_name, count in budget_ranges.items():
                print(f"  {range_name:<25} {count:>5} ({count/total_jobs*100:.1f}%)")
            
            print(f"\n{'Top 20 Most Requested Skills:':<30}")
            for skill, count in top_skills:
                print(f"  {skill:<25} {count:>5} ({count/total_jobs*100:.1f}%)")
            
            print("\n" + "="*80)
            
            # Show recent jobs
            recent_jobs = sorted(
                self.jobs_cache.values(),
                key=lambda x: x.get('posted_on', ''),
                reverse=True
            )[:10]
            
            print(f"\nMost Recent Jobs:")
            for i, job in enumerate(recent_jobs, 1):
                budget = job.get('budget', {})
                amount = budget.get('amount', 0) or budget.get('hourly_rate_min', 0)
                job_type = budget.get('type', 'Unknown')
                skills = ', '.join(job.get('skills', [])[:5])
                
                print(f"\n{i}. {job['title']}")
                print(f"   Budget: ${amount} ({job_type})")
                print(f"   Skills: {skills}")
                print(f"   Posted: {job.get('posted_on', 'Unknown')}")
                print(f"   URL: {job.get('url', 'N/A')}")
        
        elif output_format == 'json':
            report = {
                'generated_at': datetime.now().isoformat(),
                'total_jobs': total_jobs,
                'job_types': job_types,
                'budget_ranges': budget_ranges,
                'top_skills': dict(top_skills),
                'jobs': list(self.jobs_cache.values())
            }
            
            report_file = f"upwork_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(report_file, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            logger.info(f"Report saved to: {report_file}")
        
        elif output_format == 'csv':
            import csv
            
            report_file = f"upwork_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            with open(report_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'Job ID', 'Title', 'Budget Type', 'Budget Amount', 
                    'Skills', 'Experience Level', 'Posted On', 'URL'
                ])
                
                for job_id, job_info in self.jobs_cache.items():
                    budget = job_info.get('budget', {})
                    writer.writerow([
                        job_id,
                        job_info.get('title', ''),
                        budget.get('type', ''),
                        budget.get('amount', 0) or budget.get('hourly_rate_min', 0),
                        ', '.join(job_info.get('skills', [])),
                        job_info.get('experience_level', ''),
                        job_info.get('posted_on', ''),
                        job_info.get('url', '')
                    ])
            
            logger.info(f"Report saved to: {report_file}")
    
    def run_continuous_monitor(self, interval_minutes: int = 60):
        """
        Run continuous monitoring loop.
        
        Args:
            interval_minutes: Minutes between each search
        """
        logger.info(f"Starting continuous monitoring (checking every {interval_minutes} minutes)")
        
        try:
            while True:
                logger.info("Running job search...")
                self.search_and_monitor()
                
                logger.info(f"Waiting {interval_minutes} minutes until next search...")
                time.sleep(interval_minutes * 60)
                
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
            self.generate_report()


def main():
    """Main entry point for the job monitor."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Monitor Upwork jobs with skills and pay tracking')
    parser.add_argument('--query', type=str, help='Custom search query')
    parser.add_argument('--interval', type=int, default=60, 
                       help='Minutes between searches (default: 60)')
    parser.add_argument('--output', type=str, default='upwork_jobs.json',
                       help='Output file for job cache (default: upwork_jobs.json)')
    parser.add_argument('--report', choices=['console', 'json', 'csv'],
                       default='console', help='Report format')
    parser.add_argument('--continuous', action='store_true',
                       help='Run continuous monitoring')
    parser.add_argument('--skill', type=str, help='Filter jobs by skill')
    parser.add_argument('--min-rate', type=float, help='Minimum hourly rate or budget')
    parser.add_argument('--max-rate', type=float, help='Maximum hourly rate or budget')
    
    args = parser.parse_args()
    
    try:
        monitor = UpworkJobMonitor(output_file=args.output)
        
        # Test connection first
        logger.info("Testing Upwork API connection...")
        if not monitor.client.test_connection():
            logger.error("Connection test failed. Please check your credentials.")
            return
        
        logger.info("Connection successful!")
        
        # Run search
        if args.continuous:
            monitor.run_continuous_monitor(interval_minutes=args.interval)
        else:
            monitor.search_and_monitor(query=args.query)
            
            # Filter and report
            if args.skill:
                jobs = monitor.get_jobs_by_skill(args.skill)
                logger.info(f"Found {len(jobs)} jobs requiring '{args.skill}'")
            elif args.min_rate or args.max_rate:
                jobs = monitor.get_jobs_by_budget_range(
                    min_amount=args.min_rate,
                    max_amount=args.max_rate
                )
                logger.info(f"Found {len(jobs)} jobs in budget range")
            
            # Generate report
            monitor.generate_report(output_format=args.report)
            
    except Exception as e:
        logger.error(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()
