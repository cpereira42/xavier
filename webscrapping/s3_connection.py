# importando as bibliotecas
import boto3
import os
import configparser

# analisando o arquivo credentials que está na pasta .aws abaixo do home dir
config = configparser.ConfigParser()
path = os.path.join(os.path.expanduser('~'), '.aws/credentials')
config.read(path)

# pegando as chaves e a regiào para o projeto xavier
aws_access_key_id = config.get('ilia-ecole42-xavier', 'aws_access_key_id')
aws_secret_access_key = config.get(
        'ilia-ecole42-xavier', 'aws_secret_access_key')
aws_region = config.get('ilia-ecole42-xavier', 'aws_region')

# inicializando o cliente boto3
boto3.setup_default_session(
    region_name=aws_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
    )

# definindo o recurso da aws que será usado
s3 = boto3.client('s3')

# pegando todos os objetos do bucket da pasta users
response = s3.list_objects(
        Bucket='ilia-ecole42-xavier',
        Prefix='users',
        )

# loop para mostrar o nome dos objetos (pastas e arquivos)
# print(response['Contents'])
# for obj in response['Contents']:
#     if (obj['Key'] == 'users/lenzo-pe/'):
#         lenzo = obj
# pathing = 'ilia-ecole42-xavier/' + lenzo['Key']
# print(pathing)
# with open('startup.parquet', 'rb') as data:
#     s3.upload_fileobj(data, 'ilia-ecole42-xavier', 'startup.parquet')
s3.upload_file(
        'data_files/startup.parquet',
        'ilia-ecole42-xavier',
        'raw_data/startup.parquet')
s3.upload_file(
        'data_files/thor.parquet',
        'ilia-ecole42-xavier',
        'raw_data/thor.parquet')
