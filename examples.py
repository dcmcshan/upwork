#!/usr/bin/env python3
"""
Example script showing how to use the Upwork job monitoring tools
"""
from upwork_job_monitor import UpworkJobMonitor
from job_analytics import JobAnalytics
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def example_basic_monitoring():
    """Example: Basic job monitoring."""
    print("\n" + "="*80)
    print("EXAMPLE 1: Basic Job Monitoring")
    print("="*80)
    
    # Initialize monitor
    monitor = UpworkJobMonitor(output_file="example_jobs.json")
    
    # Test connection
    if not monitor.client.test_connection():
        logger.error("Cannot connect to Upwork API. Check your credentials.")
        return
    
    # Search for jobs
    logger.info("Searching for Python jobs...")
    new_count, updated_count = monitor.search_and_monitor(query="python developer")
    
    logger.info(f"Found {new_count} new jobs, updated {updated_count} jobs")
    
    # Generate console report
    monitor.generate_report(output_format='console')


def example_skill_filtering():
    """Example: Filter jobs by skill."""
    print("\n" + "="*80)
    print("EXAMPLE 2: Filter Jobs by Skill")
    print("="*80)
    
    monitor = UpworkJobMonitor(output_file="example_jobs.json")
    
    # Get all Python jobs
    python_jobs = monitor.get_jobs_by_skill("python")
    logger.info(f"Found {len(python_jobs)} Python jobs")
    
    # Get all JavaScript jobs
    js_jobs = monitor.get_jobs_by_skill("javascript")
    logger.info(f"Found {len(js_jobs)} JavaScript jobs")
    
    # Print some details
    if python_jobs:
        print("\nSample Python Jobs:")
        for job in python_jobs[:3]:
            budget = job.get('budget', {})
            rate = budget.get('hourly_rate_min', 0) or budget.get('amount', 0)
            print(f"  - {job['title']}")
            print(f"    Rate: ${rate} ({budget.get('type', 'Unknown')})")
            print(f"    Skills: {', '.join(job.get('skills', [])[:5])}")


def example_budget_filtering():
    """Example: Filter jobs by budget range."""
    print("\n" + "="*80)
    print("EXAMPLE 3: Filter Jobs by Budget")
    print("="*80)
    
    monitor = UpworkJobMonitor(output_file="example_jobs.json")
    
    # Get high-paying hourly jobs ($100-200/hr)
    high_paying = monitor.get_jobs_by_budget_range(
        min_amount=100,
        max_amount=200,
        job_type="hourly"
    )
    
    logger.info(f"Found {len(high_paying)} high-paying hourly jobs ($100-200/hr)")
    
    # Get mid-range fixed price jobs ($1000-5000)
    mid_fixed = monitor.get_jobs_by_budget_range(
        min_amount=1000,
        max_amount=5000,
        job_type="fixed"
    )
    
    logger.info(f"Found {len(mid_fixed)} mid-range fixed price jobs ($1K-5K)")
    
    # Print details
    if high_paying:
        print("\nHigh-Paying Hourly Jobs:")
        for job in high_paying[:5]:
            budget = job.get('budget', {})
            rate = budget.get('hourly_rate_min', 0)
            print(f"  - {job['title']}: ${rate}/hr")


def example_analytics():
    """Example: Analyze job data for insights."""
    print("\n" + "="*80)
    print("EXAMPLE 4: Job Analytics and Insights")
    print("="*80)
    
    analytics = JobAnalytics(jobs_file="example_jobs.json")
    
    if not analytics.jobs:
        logger.warning("No jobs to analyze. Run examples 1-3 first.")
        return
    
    # Get top skills
    top_skills = analytics.skill_frequency_analysis(top_n=10)
    print("\nTop 10 Most Demanded Skills:")
    for i, (skill, count) in enumerate(top_skills, 1):
        print(f"  {i:2d}. {skill:<25} {count:>3} jobs")
    
    # Get highest paying skills
    skill_pay = analytics.skill_pay_correlation()
    sorted_skills = sorted(skill_pay.items(), 
                          key=lambda x: x[1]['avg_rate'], 
                          reverse=True)[:10]
    
    print("\nTop 10 Highest Paying Skills:")
    for i, (skill, stats) in enumerate(sorted_skills, 1):
        print(f"  {i:2d}. {skill:<25} ${stats['avg_rate']:>6.2f}/hr (avg)")
    
    # Get budget distribution
    budget_dist = analytics.budget_distribution()
    print("\nBudget Distribution:")
    for range_name, count in budget_dist.items():
        if count > 0:
            print(f"  {range_name:<20} {count:>3} jobs")


def example_combined_analysis():
    """Example: Combined search and analysis workflow."""
    print("\n" + "="*80)
    print("EXAMPLE 5: Combined Workflow - Multiple Searches + Analysis")
    print("="*80)
    
    monitor = UpworkJobMonitor(output_file="example_jobs.json")
    
    if not monitor.client.test_connection():
        logger.error("Cannot connect to Upwork API")
        return
    
    # Search for multiple technologies
    technologies = ["python", "javascript", "react", "node.js", "docker"]
    
    for tech in technologies:
        logger.info(f"Searching for {tech} jobs...")
        try:
            monitor.search_and_monitor(query=tech)
        except Exception as e:
            logger.error(f"Error searching for {tech}: {e}")
    
    # Now analyze all collected data
    analytics = JobAnalytics(jobs_file="example_jobs.json")
    
    # Generate full report
    report = analytics.generate_insights_report()
    print(report)
    
    # Export to JSON
    analytics.export_insights_json(output_file="example_insights.json")
    logger.info("Insights exported to example_insights.json")


def example_find_best_opportunities():
    """Example: Find the best job opportunities based on criteria."""
    print("\n" + "="*80)
    print("EXAMPLE 6: Find Best Opportunities")
    print("="*80)
    
    monitor = UpworkJobMonitor(output_file="example_jobs.json")
    
    # Criteria: Python jobs paying $75-150/hr with good clients
    python_jobs = monitor.get_jobs_by_skill("python")
    
    # Filter by budget
    good_paying = [
        job for job in python_jobs
        if 75 <= job.get('budget', {}).get('hourly_rate_min', 0) <= 150
    ]
    
    # Filter by client quality
    quality_clients = [
        job for job in good_paying
        if job.get('client_info', {}).get('payment_verified', False) and
           job.get('client_info', {}).get('total_spent', 0) > 1000
    ]
    
    logger.info(f"Found {len(quality_clients)} high-quality Python opportunities")
    
    # Sort by client rating
    quality_clients.sort(
        key=lambda x: x.get('client_info', {}).get('rating', 0),
        reverse=True
    )
    
    # Display top 5
    print("\nTop 5 Best Python Job Opportunities:")
    for i, job in enumerate(quality_clients[:5], 1):
        client = job.get('client_info', {})
        budget = job.get('budget', {})
        
        print(f"\n{i}. {job['title']}")
        print(f"   Rate: ${budget.get('hourly_rate_min', 0)}/hr")
        print(f"   Client spent: ${client.get('total_spent', 0):,}")
        print(f"   Client rating: {client.get('rating', 0):.1f}/5.0")
        print(f"   Skills: {', '.join(job.get('skills', [])[:5])}")
        print(f"   URL: {job.get('url', 'N/A')}")


def main():
    """Run all examples."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Run Upwork monitoring examples')
    parser.add_argument('--example', type=int, choices=range(1, 7),
                       help='Run specific example (1-6)')
    parser.add_argument('--all', action='store_true',
                       help='Run all examples')
    
    args = parser.parse_args()
    
    examples = {
        1: ("Basic Monitoring", example_basic_monitoring),
        2: ("Skill Filtering", example_skill_filtering),
        3: ("Budget Filtering", example_budget_filtering),
        4: ("Analytics", example_analytics),
        5: ("Combined Analysis", example_combined_analysis),
        6: ("Find Best Opportunities", example_find_best_opportunities)
    }
    
    try:
        if args.example:
            name, func = examples[args.example]
            logger.info(f"Running Example {args.example}: {name}")
            func()
        elif args.all:
            for num, (name, func) in examples.items():
                logger.info(f"Running Example {num}: {name}")
                func()
                print("\n")
        else:
            # Interactive menu
            print("\n" + "="*80)
            print("UPWORK JOB MONITORING - EXAMPLES")
            print("="*80)
            print("\nAvailable Examples:")
            for num, (name, _) in examples.items():
                print(f"  {num}. {name}")
            print("\nUsage:")
            print("  python examples.py --example 1    # Run specific example")
            print("  python examples.py --all          # Run all examples")
            print("\n")
            
    except Exception as e:
        logger.error(f"Error running example: {e}")
        raise


if __name__ == "__main__":
    main()
