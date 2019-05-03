# AWS Lambda Python SQLServer

Simple Aws Lambda to execute a query to SQLServer

## Getting Started

I guess you were looking a way to connect to RDS SQL Server endpoint for your micro serverless app and you like Python

### Prerequisites

AWS Account (obviously)

Python 3.7

Lambda and SQLServer instance need to be in the same Cloud

### Installing

First create a Lambda Layer with pyodbc-layer.zip file and set it for "Python 3.7"

Then you need to create a Lambda with the code of lambda_function.py

The Lambda need to use the same VPC, Subnets and Security Groups as the SQLServer instance 

## Running the tests

TODO

## Deployment

TODO

## Authors

* **Jesus.Martinez** - *Copy from somewhere* - [jmartinezl](https://github.com/jmartinezl)

## License

This project is licensed under the MIT License

## References

* https://gist.github.com/diriver63/b72a954fa0da4851d89e5086aa13c6e8