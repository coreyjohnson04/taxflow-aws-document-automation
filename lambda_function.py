import json
import os
import urllib.parse

import boto3

s3 = boto3.client("s3")
sns = boto3.client("sns")


def lambda_handler(event, context):
    processed = []

    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])
        size = record["s3"]["object"].get("size", 0)

        object_info = s3.head_object(Bucket=bucket, Key=key)
        content_type = object_info.get("ContentType", "unknown")
        etag = object_info.get("ETag", "unknown").replace('"', "")

        message = (
            "TaxFlow received a new fictional client document.\n\n"
            f"Bucket: {bucket}\n"
            f"Object key: {key}\n"
            f"Size: {size} bytes\n"
            f"Content type: {content_type}\n"
            f"ETag: {etag}\n"
            f"AWS request ID: {context.aws_request_id}\n\n"
            "Next action: Verify the fictional client's checklist and move the "
            "document to the review stage."
        )

        sns.publish(
            TopicArn=os.environ["SNS_TOPIC_ARN"],
            Subject="TaxFlow: new document received",
            Message=message,
        )

        processed.append({"bucket": bucket, "key": key, "size": size})
        print(json.dumps({"status": "processed", "document": processed[-1]}))

    return {
        "statusCode": 200,
        "body": json.dumps({"processed": processed}),
    }
