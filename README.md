# TaxFlow: AWS Document Upload Automation

A hands-on AWS portfolio project that detects document uploads, processes file metadata, and sends email notifications.

**Built by Corey Johnson**

## The Problem

A document-based business should not have to repeatedly check an upload folder to know when something new arrives.

TaxFlow demonstrates an event-driven approach: an upload starts the workflow automatically.

## Workflow

**S3 Upload → Lambda → SNS → Email Notification**

CloudWatch records execution results, while IAM controls the function’s access to AWS resources.

## Tools Used

- **Amazon S3:** Stores fictional documents and generates object-created events.
- **AWS Lambda:** Runs the Python processing function.
- **Python and boto3:** Read event details, retrieve object metadata, and publish notifications.
- **Amazon SNS:** Delivers notifications to a confirmed email subscriber.
- **AWS IAM:** Provides scoped permissions for S3 access, SNS publishing, and logging.
- **Amazon CloudWatch Logs:** Records processing results and supports troubleshooting.

## What I Built

1. Created a document-storage bucket with public access blocked.
2. Created an SNS topic and confirmed an email subscription.
3. Built a Python Lambda function to handle S3 upload events.
4. Configured the SNS topic through an environment variable.
5. Added IAM permissions for the required AWS operations.
6. Configured S3 object-created notifications for the `incoming/` prefix.
7. Tested the workflow and inspected its execution logs.

## What the Function Does

- Reads the bucket name and object key from the S3 event.
- Decodes the object key.
- Retrieves object metadata using `head_object`.
- Publishes a notification through SNS.
- Logs the processing result in CloudWatch.

The function handles file metadata—not the contents of tax documents.

## Troubleshooting and Lessons Learned

### Folder-prefix mismatch

The original upload folder was named `text incoming/`, but the event filter expected `incoming/`.

Uploads to the original folder did not match the configured trigger. Using the correct folder resolved the mismatch.

**Lesson:** S3 event filters must match the beginning of the object key exactly.

### Copied text in the Python file

A stray `python` label was pasted above the import statements.

I removed it and deployed the corrected function.

**Lesson:** Check copied code for formatting labels and verify the deployed version.

## Verification

- Confirmed the SNS email subscription and demonstrated email delivery.
- Verified the actual test document under `incoming/`.
- Inspected the CloudWatch processing record showing the document’s filename, a size of **310 bytes**, and a status of **processed**.

## Video Walkthrough

YouTube walkthrough link will be added here.

## Project Scope

This is a personal portfolio lab using fictional documents. It is not a production client portal, tax-preparation system, or employer project.

Before real client use, the workflow would need additional security review, input validation, duplicate-event handling, failure recovery, and operational monitoring.

## Skills Demonstrated

AWS service integration, event-driven automation, Python scripting, IAM permissions, environment-variable configuration, logging, testing, and troubleshooting.
