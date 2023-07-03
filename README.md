# News to S3 Lambda

News to S3 Lambda is an ETL (Extract, Transform, Load) pipeline that fetches news articles about a particular topic using the NewsAPI service and transfers the extracted text to an S3 bucket. It is designed to run as a scheduled job on AWS Lambda.

## Functionality

The pipeline follows the ETL process with the following steps:

1. **Extract**: The pipeline calls the NewsAPI service to fetch URLs of news articles based on a search query and date range.
2. **Transform**: The visible text is extracted from each article by parsing the HTML content of the article's URL.
3. **Load**: The extracted text is uploaded to an S3 bucket for further processing and analysis.

## Setup and Configuration

To deploy and run the News to S3 Lambda pipeline, follow these steps:

1. Clone the project repository.
2. Create and configure your AWS IAM user, credentials, S3 bucket, Lambda function and associated policies.
3. Customize the pipeline configuration by modifying the relevant variables. For example, search query, S3 bucket name, and namespace prefix in `news_article_pipeline.py`. [(See Planned Work)](#planned-work)
4. Set up the necessary secrets for AWS Secrets Manager with the required values. For example, your secrets should contain the necessary API keys.
5. With [invoke](https://www.pyinvoke.org/) installed, build the Lambda package by running the invoke task:
      ```sh
      invoke package-lambda
      ```
6. Deploy the Lambda function by uploading the built package via your preferred method (e.g., AWS CLI, AWS Console).
7. Schedule the Lambda function to run as a scheduled job at your desired frequency via AWS CloudWatch, EventBridge, etc...

## Planned Work

The News to S3 Lambda pipeline is an initial implementation that can be further improved and extended. Some planned work includes:

- **Testing**: Adding comprehensive test cases to ensure the correctness and robustness of the pipeline.
- **Abstraction**: Abstracting the pipeline to allow for more general use by making the query term and other parameters configurable.
- **Continuous Deployment**: Setting up a continuous deployment task to automatically update the Lambda function package when changes are made.

## Contributing

Contributions to the News to S3 Lambda project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue in the project repository.

## License

This project is licensed under the [MIT License](LICENSE).
