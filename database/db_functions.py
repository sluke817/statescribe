import boto3
import json
import mysql.connector
from botocore.exceptions import ClientError


def get_db_secret():

    secret_name = "db-admin"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response["SecretString"]
    secret_dict = json.loads(secret)
    return secret_dict


def connect_to_db():
    secret_dict = get_db_secret()

    db = mysql.connector.connect(
        host=secret_dict["host"],
        user=secret_dict["username"],
        passwd=secret_dict["password"],
        database="statescribe",
        port=3306,
    )
    return db

# Returns json object of db query
def query_db(sql, post=False):

    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute(sql)

    if post:
        mysql.connection.commit()

    result = cursor.fetchall()
    cursor.close()
    return json.dumps(result)


def query_db(db, sql, post=False):

    cursor = db.cursor(dictionary=True)
    cursor.execute(sql)

    if post:
        db.commit()

    result = cursor.fetchall()
    cursor.close()
    return json.dumps(result)
