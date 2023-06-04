# SQS queue
resource "aws_sqs_queue" "queue" {
  name = "${var.app_env}-s3-event-notification-queue"
  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:*:*:${var.app_env}-s3-event-notification-queue"
    }
  ]
}
POLICY
}
 
# Event source from SQS
resource "aws_lambda_event_source_mapping" "event_source_mapping" {
  event_source_arn = aws_sqs_queue.queue.arn
  enabled          = true
  function_name    = aws_lambda_function.sqs_processor.arn
  batch_size       = 1
}