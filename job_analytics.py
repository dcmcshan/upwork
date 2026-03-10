#!/usr/bin/env python3
"""
Upwork Job Analytics - Analyze cached job data and generate insights
"""
import json
import os
from collections import Counter, defaultdict
from datetime import datetime
from typing import Dict, List, Any
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class JobAnalytics:
    """Analyze Upwork job data for trends and insights."""
    
    def __init__(self, jobs_file: str = "upwork_jobs.json"):
        """
        Initialize analytics from cached jobs file.
        
        Args:
            jobs_file: Path to JSON file with cached jobs
        """
        self.jobs_file = jobs_file
        self.jobs = self._load_jobs()
        logger.info(f"Loaded {len(self.jobs)} jobs for analysis")
    
    def _load_jobs(self) -> Dict[str, Dict]:
        """Load jobs from cache file."""
        if not os.path.exists(self.jobs_file):
            logger.error(f"Jobs file not found: {self.jobs_file}")
            return {}
        
        try:
            with open(self.jobs_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load jobs: {e}")
            return {}
    
    def skill_frequency_analysis(self, top_n: int = 30) -> List[tuple]:
        """
        Analyze skill frequency across all jobs.
        
        Args:
            top_n: Number of top skills to return
            
        Returns:
            List of (skill, count) tuples
        """
        skill_counter = Counter()
        
        for job_id, job in self.jobs.items():
            skills = job.get('skills', [])
            skill_counter.update(skills)
        
        return skill_counter.most_common(top_n)
    
    def skill_pay_correlation(self) -> Dict[str, Dict[str, float]]:
        """
        Correlate skills with average pay rates.
        
        Returns:
            Dictionary mapping skills to pay statistics
        """
        skill_pay = defaultdict(list)
        
        for job_id, job in self.jobs.items():
            budget = job.get('budget', {})
            skills = job.get('skills', [])
            
            # Get pay rate
            rate = budget.get('hourly_rate_min', 0)
            if not rate:
                rate = budget.get('amount', 0)
            
            if rate > 0:
                for skill in skills:
                    skill_pay[skill].append(rate)
        
        # Calculate statistics
        skill_stats = {}
        for skill, rates in skill_pay.items():
            if len(rates) >= 3:  # Need at least 3 data points
                skill_stats[skill] = {
                    'avg_rate': sum(rates) / len(rates),
                    'min_rate': min(rates),
                    'max_rate': max(rates),
                    'median_rate': sorted(rates)[len(rates) // 2],
                    'job_count': len(rates)
                }
        
        return skill_stats
    
    def budget_distribution(self) -> Dict[str, int]:
        """
        Analyze budget distribution across jobs.
        
        Returns:
            Dictionary with budget ranges and counts
        """
        ranges = {
            '<$25/hr': 0,
            '$25-$50/hr': 0,
            '$50-$100/hr': 0,
            '$100-$150/hr': 0,
            '>$150/hr': 0,
            'Fixed <$500': 0,
            'Fixed $500-$1K': 0,
            'Fixed $1K-$5K': 0,
            'Fixed >$5K': 0
        }
        
        for job_id, job in self.jobs.items():
            budget = job.get('budget', {})
            job_type = budget.get('type', '').lower()
            
            if 'hourly' in job_type:
                rate = budget.get('hourly_rate_min', 0)
                if rate < 25:
                    ranges['<$25/hr'] += 1
                elif rate < 50:
                    ranges['$25-$50/hr'] += 1
                elif rate < 100:
                    ranges['$50-$100/hr'] += 1
                elif rate < 150:
                    ranges['$100-$150/hr'] += 1
                else:
                    ranges['>$150/hr'] += 1
            elif 'fixed' in job_type:
                amount = budget.get('amount', 0)
                if amount < 500:
                    ranges['Fixed <$500'] += 1
                elif amount < 1000:
                    ranges['Fixed $500-$1K'] += 1
                elif amount < 5000:
                    ranges['Fixed $1K-$5K'] += 1
                else:
                    ranges['Fixed >$5K'] += 1
        
        return ranges
    
    def experience_level_analysis(self) -> Dict[str, Dict]:
        """
        Analyze jobs by experience level.
        
        Returns:
            Dictionary with experience level statistics
        """
        level_stats = defaultdict(lambda: {'count': 0, 'rates': []})
        
        for job_id, job in self.jobs.items():
            level = job.get('experience_level', 'Unknown')
            budget = job.get('budget', {})
            rate = budget.get('hourly_rate_min', 0) or budget.get('amount', 0)
            
            level_stats[level]['count'] += 1
            if rate > 0:
                level_stats[level]['rates'].append(rate)
        
        # Calculate averages
        result = {}
        for level, stats in level_stats.items():
            result[level] = {
                'job_count': stats['count'],
                'avg_rate': sum(stats['rates']) / len(stats['rates']) if stats['rates'] else 0,
                'percentage': stats['count'] / len(self.jobs) * 100
            }
        
        return result
    
    def client_quality_analysis(self) -> Dict[str, Any]:
        """
        Analyze client quality metrics.
        
        Returns:
            Statistics about client quality
        """
        verified_count = 0
        total_spent_sum = 0
        hire_rates = []
        ratings = []
        
        for job_id, job in self.jobs.items():
            client = job.get('client_info', {})
            
            if client.get('payment_verified'):
                verified_count += 1
            
            total_spent = client.get('total_spent', 0)
            if total_spent > 0:
                total_spent_sum += total_spent
            
            hire_rate = client.get('hire_rate', 0)
            if hire_rate > 0:
                hire_rates.append(hire_rate)
            
            rating = client.get('rating', 0)
            if rating > 0:
                ratings.append(rating)
        
        return {
            'verified_percentage': verified_count / len(self.jobs) * 100 if self.jobs else 0,
            'avg_client_spent': total_spent_sum / len(self.jobs) if self.jobs else 0,
            'avg_hire_rate': sum(hire_rates) / len(hire_rates) if hire_rates else 0,
            'avg_client_rating': sum(ratings) / len(ratings) if ratings else 0,
            'total_clients': len(self.jobs)
        }
    
    def skill_combinations(self, min_occurrence: int = 3) -> List[tuple]:
        """
        Find common skill combinations.
        
        Args:
            min_occurrence: Minimum times a combination must appear
            
        Returns:
            List of (skill_pair, count) tuples
        """
        combo_counter = Counter()
        
        for job_id, job in self.jobs.items():
            skills = job.get('skills', [])
            # Generate pairs
            for i, skill1 in enumerate(skills):
                for skill2 in skills[i+1:]:
                    pair = tuple(sorted([skill1, skill2]))
                    combo_counter[pair] += 1
        
        # Filter by minimum occurrence
        return [(combo, count) for combo, count in combo_counter.most_common() 
                if count >= min_occurrence]
    
    def time_trend_analysis(self) -> Dict[str, int]:
        """
        Analyze job posting trends over time.
        
        Returns:
            Dictionary with date-based job counts
        """
        date_counts = defaultdict(int)
        
        for job_id, job in self.jobs.items():
            posted_on = job.get('posted_on', '')
            if posted_on:
                try:
                    # Extract date (YYYY-MM-DD)
                    date = posted_on.split('T')[0]
                    date_counts[date] += 1
                except:
                    continue
        
        return dict(sorted(date_counts.items()))
    
    def generate_insights_report(self) -> str:
        """
        Generate a comprehensive insights report.
        
        Returns:
            Formatted report string
        """
        report = []
        report.append("=" * 80)
        report.append("UPWORK JOB INSIGHTS REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Total Jobs Analyzed: {len(self.jobs)}")
        report.append("=" * 80)
        
        # Skill frequency
        report.append("\n📊 TOP 15 MOST DEMANDED SKILLS:")
        report.append("-" * 80)
        skills = self.skill_frequency_analysis(top_n=15)
        for i, (skill, count) in enumerate(skills, 1):
            percentage = count / len(self.jobs) * 100
            report.append(f"{i:2d}. {skill:<30} {count:>4} jobs ({percentage:5.1f}%)")
        
        # Skill pay correlation
        report.append("\n💰 TOP 10 HIGHEST PAYING SKILLS:")
        report.append("-" * 80)
        skill_pay = self.skill_pay_correlation()
        sorted_by_pay = sorted(skill_pay.items(), 
                               key=lambda x: x[1]['avg_rate'], 
                               reverse=True)[:10]
        
        for i, (skill, stats) in enumerate(sorted_by_pay, 1):
            report.append(
                f"{i:2d}. {skill:<30} "
                f"Avg: ${stats['avg_rate']:>6.2f}/hr  "
                f"Range: ${stats['min_rate']:.0f}-${stats['max_rate']:.0f}  "
                f"({stats['job_count']} jobs)"
            )
        
        # Budget distribution
        report.append("\n💵 BUDGET DISTRIBUTION:")
        report.append("-" * 80)
        budget_dist = self.budget_distribution()
        for range_name, count in budget_dist.items():
            if count > 0:
                percentage = count / len(self.jobs) * 100
                report.append(f"{range_name:<20} {count:>4} jobs ({percentage:5.1f}%)")
        
        # Experience level
        report.append("\n🎓 EXPERIENCE LEVEL BREAKDOWN:")
        report.append("-" * 80)
        exp_analysis = self.experience_level_analysis()
        for level, stats in sorted(exp_analysis.items(), 
                                   key=lambda x: x[1]['job_count'], 
                                   reverse=True):
            report.append(
                f"{level:<20} {stats['job_count']:>4} jobs ({stats['percentage']:5.1f}%)  "
                f"Avg Rate: ${stats['avg_rate']:.2f}"
            )
        
        # Client quality
        report.append("\n👤 CLIENT QUALITY METRICS:")
        report.append("-" * 80)
        client_stats = self.client_quality_analysis()
        report.append(f"Payment Verified:     {client_stats['verified_percentage']:.1f}%")
        report.append(f"Avg Client Spent:     ${client_stats['avg_client_spent']:,.2f}")
        report.append(f"Avg Hire Rate:        {client_stats['avg_hire_rate']*100:.1f}%")
        report.append(f"Avg Client Rating:    {client_stats['avg_client_rating']:.2f}/5.0")
        
        # Skill combinations
        report.append("\n🔗 TOP 10 SKILL COMBINATIONS:")
        report.append("-" * 80)
        combos = self.skill_combinations()[:10]
        for i, (combo, count) in enumerate(combos, 1):
            report.append(f"{i:2d}. {combo[0]} + {combo[1]:<30} ({count} jobs)")
        
        # Time trends
        report.append("\n📅 POSTING TRENDS (Last 7 Days):")
        report.append("-" * 80)
        time_trends = self.time_trend_analysis()
        recent_dates = sorted(time_trends.keys(), reverse=True)[:7]
        for date in reversed(recent_dates):
            count = time_trends[date]
            report.append(f"{date}  {'█' * (count // 2)} {count} jobs")
        
        report.append("\n" + "=" * 80)
        
        return "\n".join(report)
    
    def export_insights_json(self, output_file: str = None):
        """
        Export all insights as JSON.
        
        Args:
            output_file: Output file path
        """
        if not output_file:
            output_file = f"job_insights_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        insights = {
            'generated_at': datetime.now().isoformat(),
            'total_jobs': len(self.jobs),
            'top_skills': dict(self.skill_frequency_analysis(30)),
            'skill_pay_correlation': self.skill_pay_correlation(),
            'budget_distribution': self.budget_distribution(),
            'experience_levels': self.experience_level_analysis(),
            'client_quality': self.client_quality_analysis(),
            'skill_combinations': [
                {'skills': list(combo), 'count': count} 
                for combo, count in self.skill_combinations()
            ],
            'time_trends': self.time_trend_analysis()
        }
        
        with open(output_file, 'w') as f:
            json.dump(insights, f, indent=2)
        
        logger.info(f"Insights exported to: {output_file}")
        return output_file


def main():
    """Main entry point for job analytics."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze Upwork job data')
    parser.add_argument('--jobs-file', type=str, default='upwork_jobs.json',
                       help='Path to jobs JSON file')
    parser.add_argument('--export-json', action='store_true',
                       help='Export insights as JSON')
    parser.add_argument('--skill', type=str,
                       help='Analyze specific skill')
    
    args = parser.parse_args()
    
    try:
        analytics = JobAnalytics(jobs_file=args.jobs_file)
        
        if not analytics.jobs:
            logger.error("No jobs to analyze. Run upwork_job_monitor.py first.")
            return
        
        if args.skill:
            # Analyze specific skill
            skill_pay = analytics.skill_pay_correlation()
            if args.skill in skill_pay:
                stats = skill_pay[args.skill]
                print(f"\nAnalysis for skill: {args.skill}")
                print(f"  Jobs found: {stats['job_count']}")
                print(f"  Average rate: ${stats['avg_rate']:.2f}/hr")
                print(f"  Rate range: ${stats['min_rate']:.2f} - ${stats['max_rate']:.2f}")
                print(f"  Median rate: ${stats['median_rate']:.2f}")
            else:
                print(f"No data found for skill: {args.skill}")
        
        # Generate and display main report
        report = analytics.generate_insights_report()
        print(report)
        
        # Export JSON if requested
        if args.export_json:
            output_file = analytics.export_insights_json()
            print(f"\n✓ Insights exported to: {output_file}")
        
    except Exception as e:
        logger.error(f"Error during analysis: {e}")
        raise


if __name__ == "__main__":
    main()
