import boto3
import json
from datetime import datetime, timedelta

def lambda_handler(event, context):
    """
    Simple Lambda to find unused AWS resources monthly
    Triggered by EventBridge on last day of month
    """
    
    # Initialize AWS clients
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')
    
    # Configuration
    SNS_TOPIC = 'arn:aws:sns:us-east-1:123456789012:unused-resources'
    
    unused_resources = []
    
    try:
        # 1. Find stopped EC2 instances
        stopped_instances = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]
        )
        
        for reservation in stopped_instances['Reservations']:
            for instance in reservation['Instances']:
                unused_resources.append({
                    'type': 'EC2',
                    'id': instance['InstanceId'],
                    'state': 'stopped'
                })
        
        # 2. Find unattached EBS volumes
        unattached_volumes = ec2.describe_volumes(
            Filters=[{'Name': 'status', 'Values': ['available']}]
        )
        
        for volume in unattached_volumes['Volumes']:
            unused_resources.append({
                'type': 'EBS',
                'id': volume['VolumeId'],
                'size': f"{volume['Size']}GB"
            })
        
        # 3. Find unassociated Elastic IPs
        elastic_ips = ec2.describe_addresses()
        
        for eip in elastic_ips['Addresses']:
            if 'InstanceId' not in eip:  # Not associated
                unused_resources.append({
                    'type': 'EIP',
                    'id': eip['PublicIp'],
                    'state': 'unassociated'
                })
        
        # Send email report
        if unused_resources:
            message = create_report(unused_resources)
            
            sns.publish(
                TopicArn=SNS_TOPIC,
                Subject='Monthly Unused AWS Resources Report',
                Message=message
            )
            
            print(f"Found {len(unused_resources)} unused resources. Email sent.")
        else:
            print("No unused resources found.")
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Found {len(unused_resources)} unused resources')
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def create_report(resources):
    """Create simple email report"""
    report = f"Monthly Unused Resources Report - {datetime.now().strftime('%B %Y')}\n"
    report += "=" * 50 + "\n\n"
    
    for resource in resources:
        report += f"Type: {resource['type']}\n"
        report += f"ID: {resource['id']}\n"
        if 'size' in resource:
            report += f"Size: {resource['size']}\n"
        if 'state' in resource:
            report += f"State: {resource['state']}\n"
        report += "\n"
    
    report += f"Total unused resources: {len(resources)}\n"
    report += "Please review and cleanup as needed."
    
    return report

# EventBridge Schedule: cron(0 9 28-31 * ? *) - Last few days of month