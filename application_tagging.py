import boto3
import os

# Exported Environment variables
REGION = os.getenv('AWS_REGION')
AWS_APPLICATION_ARN = os.getenv('AWS_APPLICATION_ARN')
TAG_KEY = os.getenv('TAG_KEY')
TAG_VALUE = os.getenv('TAG_VALUE')


def list_and_tag_resources():
    print(f"Checking resources in region: {REGION}")
    
    session = boto3.Session(region_name=REGION)
    resource_client = session.client('resourcegroupstaggingapi')

    tag_filters = {
        'TagFilters': [
            {
                'Key': TAG_KEY,
                'Values': [TAG_VALUE]
            }
        ]
    }

    # Get resources with the specified tag
    response = resource_client.get_resources(**tag_filters)

    resources = response.get('ResourceTagMappingList', [])
    tagged_resources = 0

    for resource in resources:
        resource_arn = resource['ResourceARN']
        tags = {tag['Key']: tag['Value'] for tag in resource['Tags']}
        resource_type = resource_arn.split(':')[5] 
        region = resource_arn.split(':')[3]  

        # Check if 'awsApplication' tag is present
        if 'awsApplication' not in tags:
            try:
                resource_client.tag_resources(
                    ResourceARNList=[resource_arn],
                    Tags={'awsApplication': AWS_APPLICATION_ARN}
                )
                tagged_resources += 1
                print(f"Successfully tagged resource: {resource_arn}")
            except Exception as e:
                print(f"Failed to tag resource: {resource_arn}. Error: {str(e)}")
        else:
            print(f"Resource already tagged: {resource_arn}")

   
    if tagged_resources > 0:
        print(f"Tagging completed successfully in {REGION}. Tagged {tagged_resources} resources.")
    else:
        print(f"No resources were tagged in {REGION}.")

if __name__ == "__main__":
    list_and_tag_resources()