# QAstronaut

<span>&#x1f1e7;&#x1f1f7;</span> [Read in Portuguese](README_PT.md)

Welcome to **QAstronaut, Your Solution for Agile API Testing!**

![GitHub Logo](/images/logo_qastronaut.png)

QAstronaut is an ongoing project aimed at automating the execution and creation of test suites. This repository serves as a central space for development, documentation, and collaboration.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
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

Follow these instructions to download and set up QAstronaut in your environment.

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
    > **Note:** In some cases, you may need to use `python3` or `py` instead of `python` to invoke the Python 3 interpreter.

    This command will prompt for your Postman [API Key](https://learning.postman.com/docs/developer/postman-api/authentication/) and create QAstronaut configuration folders.

    After this process, QAstronaut is ready for use.

    For more information about QAstronaut, including its features, configurations and `first steps`, we recommend consulting our [Wiki](https://github.com/QAstronaut/qastronaut/wiki).

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
