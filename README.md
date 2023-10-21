Toys-logic
============
AWS Lambda functions for the Angular front-end

## Pre-requisites
- Install Python 3.8 or higher
* Install Python 3rd Party packages:
  * `pip3 install boto3`
  * `pip3 install requests`
* Create an AWS account
* Install the AWS CLI: https://docs.aws.amazon.com/cli/index.html?nc2=h_ql_doc_cli

All downloaded 3rd party libraries can be found in `<python install dir>\Lib\site-packages`

## Testing and packaging
* To execute all unit tests, run: `python3 -m unittest discover -v -s test`
* To manually generate the build archive, run: `zip build/toys.zip toys-*.py dg/Toy*.py`
* To upload the archive to AWS, run: `aws lambda update-function-code --function-name $awsFunctionName --zip-file fileb://$buildDir/$zipFile`
* Or manually upload via the AWS web console

## References
* https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

In order to install 3rd party dependencies in an AWS Lambda Layer, the important part is to
put all the contents in a `python` directory and then create your ZIP file

* https://medium.com/@adhorn/getting-started-with-aws-lambda-layers-for-python-6e10b1f9a5d
* https://gist.github.com/gene1wood/4a052f39490fae00e0c3#file-all_aws_lambda_modules_python3-7-txt
* https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html