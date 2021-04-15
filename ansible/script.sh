#!/bin/sh

touch from_script1
a=$(aws ssm get-parameter --name "DB_NAME" --region us-east-1 --output text --query Parameter.Value)
echo "export RIS="$a"" >> ~/.bashrc

b=$(aws ssm get-parameter --name "NEW_RELIC_CONFIG_FILE" --region us-east-1 --output text --query Parameter.Value)
echo "export NEW_RELIC_CONFIG_FILE="$b"" >> ~/.bashrc

c=$(aws ssm get-parameter --name "POSTGRES_DB" --region us-east-1 --output text --query Parameter.Value)
echo "export POSTGRES_DB="$c"" >> ~/.bashrc

d=$(aws ssm get-parameter --name "POSTGRES_USER" --region us-east-1 --output text --query Parameter.Value)
echo "export POSTGRES_USER="$d"" >> ~/.bashrc

e=$(aws ssm get-parameter --name "POSTGRES_PASSWORD" --region us-east-1 --output text --query Parameter.Value)
echo "export POSTGRES_PASSWORD="$e"" >> ~/.bashrc

f=$(aws ssm get-parameter --name "SENDGRID_PASSWORD" --region us-east-1 --output text --query Parameter.Value)
echo "export SENDGRID_PASSWORD="$f"" >> ~/.bashrc

g=$(aws ssm get-parameter --name "SENTRY_DSN" --region us-east-1 --output text --query Parameter.Value)
echo "export SENTRY_DSN="$g"" >> ~/.bashrc

h=$(aws ssm get-parameter --name "db_path" --region us-east-1 --output text --query Parameter.Value)
echo "export db_path="$h"" >> ~/.bashrc

i=$(aws ssm get-parameter --name "redis_path" --region us-east-1 --output text --query Parameter.Value)
echo "export redis_path="$i"" >> ~/.bashrc

j=$(aws ssm get-parameter --name "CORS_ORIGIN_WHITELIST" --region us-east-1 --output text --query Parameter.Value)
echo "export CORS_ORIGIN_WHITELIST="$j"" >> ~/.bashrc

source ~/.bashrc
exec /bin/sh -c "$*"
