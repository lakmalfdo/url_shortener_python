# URL Shortener

## Introduction
Welcome to the URL Shortener, a Python project developed to demonstrates the ability to efficiently shorten and expand URLs, providing a valuable service for simplifying long web addresses.

## Development
The URL Shortener project was developed using Python and Visual Studio Code, emphasizing clean code practices and modularity to create a user-friendly and robust command-line utility.

## Main Features
### URL Shortening and Expansion
The URL Shortener allows users to perform two primary functions:

1. **Shorten a URL**: Transform long and unwieldy URLs into concise, shareable links.
2. **Expand a Short URL**: Retrieve the original, full-length URL from a shortened link.

### Database Storage
The project utilizes an SQLite database to store mappings between original URLs and their corresponding short URLs. This approach ensures data integrity and efficient URL expansion.

### Command-Line Interface (CLI)
The URL Shortener features a user-friendly command-line interface that simplifies the process of shortening and expanding URLs.

## How to Use
1. Clone this repository to your local machine:
<pre>git clone https://github.com/lakmalfdo/url_shortener_python.git</pre>

2. Ensure that Python is installed on your computer.

3. Open your terminal and navigate to the project directory:
<pre>cd url_shortener</pre>

4. Run the URL Shortener by executing the script:

- To shorten a URL:
<pre>python url_shortener.py -s https://www.example.com/long-url</pre>

- To expand a short URL:
<pre>python url_shortener.py -e https://short.url/FGST</pre>

## Customization
To customize this project, follow these steps:

1. Clone the repository to your local machine:

<pre>git clone https://github.com/lakmalfdo/url_shortener_python.git</pre>

2. Open the project in your preferred code editor, such as Visual Studio Code.

3. Modify the URL Shortener to suit your specific requirements. You can add new features, enhance the URL shortening algorithm, or adapt the code to unique needs. This project showcases the flexibility and modularity of Python code.

Enjoy using the URL Shortener and feel free to customize it to meet your needs. Have fun!
