import boto3


class DynamoDataAccess(object):
    def __init__(self, table_name):
        self.dynamo = boto3.client("dynamodb")
        self.table_name = table_name
        self.null_obj = {
            "NULL": True
        }
        self.nullable_vals = ["branch", "end_time", "header_text", "cause_name"]
        super(DynamoDataAccess, self).__init__()

    def add_delay_record(self, record_dict):
        expressionAttributeValues = {
                ":severity": {
                    "S": record_dict["severity"]
                },
                ":branch": {
                    "S": record_dict["branch"]
                },
                ":start_time": {
                    "N": record_dict["start_time"]
                },
                ":end_time": {
                    "N": record_dict["end_time"]
                },
                ":header_text": {
                    "S": record_dict["header_text"]
                },
                ":cause_name": {
                    "S": record_dict["cause_name"]
                }
            }

        for key in self.nullable_vals:
            if record_dict[key] is None:
                expressionAttributeValues[":" + key] = self.null_obj

        return self.dynamo.update_item(
            TableName=self.table_name,
            Key={'alert_id': {
                    "S": str(record_dict["alert_id"])
                },
                'line': {
                    "S": record_dict["line"]
                }
            },
            UpdateExpression="SET severity = :severity, branch = :branch, start_time = :start_time, "
                             "end_time = :end_time, header_text = :header_text, cause = :cause_name",
            ExpressionAttributeValues=expressionAttributeValues
        )
