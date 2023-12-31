# QAstronaut

<span>&#x1f1e7;&#x1f1f7;</span> [Read in Portuguese](README_PT.md)

Welcome to **QAstronaut, Your Solution for Agile API Testing!**

![GitHub Logo](/images/logo_qastronaut.png)

QAstronaut is an ongoing project aimed at automating the execution and creation of test suites. This repository serves as a central space for development, documentation, and collaboration.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Overview

**QAstronaut** is a revolutionary project that simplifies and accelerates the process of creating API test suites, in partnership with the well-known **Postman** tool. Our innovative approach is based on seamless integration with Postman via an **API Key**, allowing you to create test suites more agilely and efficiently, following reliable heuristics. But what makes QAstronaut so special?

### What Is QAstronaut?

**QAstronaut** is a platform designed to simplify the complexity of API testing. It is designed for development and testing teams who want to automate the testing process and ensure the quality of their APIs more quickly and reliably. With QAstronaut's help, you can easily create, organize, and execute API test suites, saving time and effort.

### What Is the Purpose of QAstronaut?

The purpose of **QAstronaut** is to provide a comprehensive solution to API testing needs. The project aims to:

1. **Accelerate Development:** Reduce the time required to create and maintain API test suites, allowing your team to focus on other critical tasks.

2. **Reliable Testing:** Use reliable heuristics to structure your tests, ensuring your APIs work as expected.

3. **Seamless Integration with Postman:** Integration with Postman via an API Key simplifies the test creation process, leveraging the popularity and advanced functionality of this tool.

4. **Efficient Collaboration:** Facilitate collaboration between developers and testers, ensuring everyone is on the same page, and tests are always up to date.

### Why Should You Be Interested in QAstronaut?

**QAstronaut** offers significant benefits to any team involved in API development. Here are some reasons to consider using our platform:

- **Time Savings:** Reduce the time spent on API testing, speeding up the development cycle.

- **Quality Improvement:** Use heuristics and best practices to ensure effective and reliable tests.

- **Simplicity and Ease of Use:** You don't need to be an API testing expert to take advantage of QAstronaut's features.

- **Integration with Postman:** Harness the power and versatility of Postman with a direct and simplified integration.

- **Increased Collaboration:** Promote collaboration between development and testing teams, ensuring a shared understanding of requirements and tests.

In summary, **QAstronaut** is the perfect solution for those looking to simplify and enhance the API testing process, allowing you to achieve your development goals more quickly and confidently. Join us and embark on this journey toward more agile and effective API testing with QAstronaut!

> If you are not familiar with the Postman tool, we recommend reading its [documentation](https://learning.postman.com/docs/getting-started/overview/). This can be helpful to become familiar with the tool we integrate with.

## Installation

Follow these instructions to download, set up, and run QAstronaut in your environment.

### Prerequisites

Ensure that you have the following requirements met before getting started:

- [Postman](https://www.postman.com/downloads/)
- [Python3+](https://www.python.org/)
- [Python Libraries](requirements.txt)

### Installation Steps

1. Clone the QAstronaut repository from GitHub to your system:

   ```bash
   git clone https://github.com/QAstronaut/qastronaut.git
   ```

2. With **Python installed**, run the following command in the *qastronaut/* directory:

    ```bash
    pip install -r requirements.txt
    ```

3. Next, run the command:

    ```bash
    python qastronaut.py --init
    ```
    > **Note:** In some cases, you may need to use `python3` instead of `python` to invoke the Python 3 interpreter on Linux.

    This command will prompt for your [API Key](https://learning.postman.com/docs/developer/postman-api/authentication/) and create QAstronaut configuration folders.

    After this process, QAstronaut is ready for use.

## Usage

After installation you will have a folder structure similar to this:

```bash
qastronaut/
│
├── config/
│   ├── requests/
│   │   └── curl.txt
│   ├── requests_names/
│   │   └── user_requests.txt
│   ├── tests/
│   │   └── body/
│   │       ├── empty.txt
│   │       ├── invalid.txt
│   │       ├── nonexistent.txt
│   │       ├── null.txt
│   │       └── size.txt
│   └── api_key.json
│
├── functions/
│   ├── create_postman.py
│   ├── fetch_data_postman.py
│   └── welcome.py
│
├── images/
│   └── logo_qastronaut.png
│
├── unit_tests/
│   ├── test_create_postman.py
│   ├── test_fetch_data_postman.py
│   └── test_welcome.py
│
├── qastronaut.py
├── README.md
├── requirements.txt
└── LICENSE 
```

**Remember**: The API Key is an essential component for QAstronaut to function properly. If you've changed it or didn't provide it during installation, it's important to update the `api_key.json` file with a valid key.

## Test and Scenario Configuration

All interaction with QAstronaut is done via command line for execution. At the configuration point, we will focus on the `config/` directory.

### Adding an HTTP Request

To include an HTTP request, follow the procedure below:

1. Save the cURL of the desired request and paste it into a file named `curl.txt`.
2. `curl.txt` is located in the `config/requests/` directory.

This ensures proper configuration for HTTP requests in your testing environment.

> Currently, QAstronaut is only capable of testing one endpoint at a time. If you need to test multiple endpoints, you will need to replace the curl.txt file each time.

### Test Configuration

In the `config/tests/` directory, you'll find all the JavaScript test scripts available for QAstronaut, for each test scenario that QAstronaut is capable of creating. It is essential to note that this list of tests is constantly evolving and requires changes to fit the requirements of the planned endpoint. Be sure to keep these scripts up-to-date to ensure adequate testing coverage.

Alternatively, you have the option to create your test script for the scenarios listed in the tests folder, overwriting the existing ones. This approach allows for complete customization according to your specific needs.

> QAstronaut's test configuration refers to the [Tests](https://learning.postman.com/docs/getting-started/first-steps/write-your-first-test/) element in Postman.

>**Obs:** In terms of the number of test scenarios available, QAstronaut is committed to continuous improvement by expanding its repertoire of test heuristics and broadening the scope of API testing. We are constantly working to offer a greater variety of test scenarios and enhance the overall test coverage, ensuring that QAstronaut remains a valuable tool for comprehensive API testing.

> **Remember:** Other project directories, such as `functions/`, are folders linked to the operation of QAstronaut. Any changes or deletions will directly affect its operation.

### Parameterizing Test Scenario Titles

In QAstronaut, the names of [Requests](https://learning.postman.com/docs/sending-requests/requests/) are defined as follows:

```text
CT000 - user_requests - JSON Field - Scenario
```

1. "CT000" represents a unique counter for each test scenario.
2. "user_requests" is the name of the file that should be customized to identify the test suite. 
> **Attention:** Ensure that you fill in the `user_requests` file because QAstronaut relies on it to function correctly, and it can be found in the `config/requests_names/` directory.
3. The "JSON Field" refers to the field being tested in the test scenario.
4. The "Scenario" describes the actual test scenario, such as "Non-existent," "Empty," "Null," and so forth.

For a practical example, a real request name can be defined as follows:

```text
CT023 - RegisterUser - Name - Empty
```

This naming structure allows for easy identification and tracking of test scenarios, helping to keep your test project organized and efficient.

## Creating Test Suites

Once the `curl.txt` file has been created and placed in the `config/requests/` directory, you are ready to run QAstronaut. Follow these steps:

1. Navigate to the `qastronaut/` directory, which contains the `qastronaut.py`

 file.
2. Execute the following command:

```bash
python qastronaut.py
```

> **Note:** In some cases, especially on Linux, you may need to use `python3` instead of `python` to invoke the Python 3 interpreter.

3. You will receive the following instructions:

```bash
Please place the cURL command in a text file named 'curl.txt' and press 'Enter'.

Did you place the cURL command in 'curl.txt'? (Y/n): 
```

4. If you have already added the `curl.txt` file, press Enter to proceed. Otherwise, add the `curl.txt` file and continue.

5. After this step, you will be prompted to provide the name of the collection that will be created for the test suite and the folder name:

```bash
What will be the name of the collection? Test
What will be the name of the folder? Test

Collection 'Test' created successfully with the collection ID: 23485401-2e399297-2c19-41b1-b1ee-a3f209bfee97

Folder 'Test' created successfully with the folder ID: 156a5f3f-a018-1943-1373-ba635b2fad44
```

6. After QAstronaut confirms the successful creation of the collection and folder, the next step is to inform the desired HTTP method:

```bash
Which HTTP method do you want to use (GET/POST/PUT/DELETE, etc.)? post
```

7. Once that is done, QAstronaut will show the corresponding HTTP request and start creating tests in the Postman workspace, providing feedback for each created HTTP request.

```bash
Request Method: POST
Request URL: https://serverest.dev/produtos
Request Body: {'nome': 'Cheese IV', 'preco': 524, 'descricao': 'Produto', 'detalhes': {'peso': '100g', 'fabricante': 'Empresa XYZ'}, 'imagens': ['imagem1.jpg', 'imagem2.jpg']}
Request Headers: Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IkFteTg0QGhvdG1haWwuY29tIiwicGFzc3dvcmQiOiJJTUlVQmpOU1hKSnSv8AAxsOn1LBfU1dBQn38x8nDSHnJvCs9bUeV2y3Ynu1pa9wRa3B06XDvDYxQjwzx4T6Y1sAt30raXnu3wsDDjx36tvZBjc1S2gjEDGvDD Al7eSvA1xG3k7Nk6A
Content-Type: application/json

----------------------------------------------------------------------

<Response [200]>
name has been tested empty
<Response [200]>
price has been tested empty
...
```

## Contributing

We appreciate your interest in contributing to the **QAstronaut** project. Your contribution can help improve the software and benefit the user community. Below, we explain how you can contribute:

### Sending Pull Requests (PRs)

If you want to add a new feature, fix a bug, or enhance the existing code, follow these steps:

1. Fork the **QAstronaut** repository to your GitHub account.

2. Clone your fork to your local development environment.

```bash
git clone https://github.com/your-username/QAstronaut.git
```

3. Create a branch for your contribution. Be sure to name the branch descriptively.

```bash
git checkout -b my-contribution
```

4. Make the desired code changes.

5. Ensure that the changes are accompanied by appropriate tests.

6. Commit your changes.

```bash
git commit -m "Add feature X"
```

7. Push the branch with the changes to your GitHub fork.

```bash
git push origin my-contribution
```

8. Access your GitHub fork and click "New Pull Request" to submit your contribution. Make sure to provide a clear description of the changes.

### Reporting Issues

If you encounter issues or bugs in the software, we appreciate you reporting these problems. To report an issue, follow these steps:

1. Go to the "Issues" section of this repository.

2. Click "New Issue" and describe the issue in detail. Include relevant information such as the environment where you encountered the problem and steps to reproduce it.

3. Wait for the project team to review and respond to your report.

Claro, aqui está a tradução da parte que você solicitou:

### Suggesting Enhancements

If you have suggestions for improving the software, we'd love to hear your ideas. Follow these steps to suggest improvements:

1. Access the "Issues" section of this repository.

2. Click on "New Issue" and select the "Feature Request" or "Enhancement" option. Describe the improvement you would like to see in the software.

3. Wait for the project team to consider your suggestion.

We appreciate all contributors for their time and effort dedicated to making the **QAstronaut** project better. Together, we can create more robust and effective software.

## Acknowledgments

We would like to express our deep gratitude to the following individuals who played crucial roles in the success of this project:

- Professor Dr. Fabio Vieira: We extend our thanks to Professor Dr. Fabio for guiding and supervising our project. His academic guidance and support were essential to its success.

- [Paula Santiago](https://www.linkedin.com/in/paulasanty): We thank Paula Santiago for sharing her practical knowledge in Quality Assurance (QA) and her experience with the Postman tool. Her contributions were vital to the quality of our project.

- [Samara Suelen Garofalo](https://github.com/samaragarofalo): We express our gratitude to Samara for her valuable guidance and mentoring throughout the development process. Her expertise and insights were invaluable.

- Enzo Marinho: We appreciate Enzo for his creativity and for assisting in the development of the project's logo. His contribution added a special touch to our work.

We are deeply thankful to these individuals for their valuable contributions. Your support and dedication were essential to our project's success. Thank you for being part of this journey with us.

## License

This project is licensed under the [MIT License](https://github.com/QAstronaut/qastronaut/blob/main/LICENSE)
