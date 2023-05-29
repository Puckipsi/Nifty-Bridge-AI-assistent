# The Nifty Bridge AI Assistant

The Nifty Bridge AI Assistant is a FastAPI-based REST project that simulates a chatbot for interactive conversations. It leverages the power of Nifty Bridge AI to provide intelligent and contextual responses. 
## Description 
The Nifty Bridge AI Assistant project allows users to engage in simulated conversations with an AI chatbot. The chatbot utilizes large language model processing techniques to generate informative and engaging responses according to Nifty Bridge topics.

## Requirements

To run this application localy, you need the following requirements:

- Python 3.9 or later

## Installation

1. Clone the repository:

```shell
git clone https://github.com/Puckipsi/Nifty-Bridge-AI-assistent.git
```

2. Navigate to the project directory:
``` shell
cd NiftyBridge AI assistant
```

3. Create and activate a virtual environment:
``` shell
python -m venv venv
source venv/bin/activate  # For Unix/Linux
venv\Scripts\activate  # For Windows
``` 

4. Install the dependencies:
``` shell
pip install -r requirements.txt
``` 

## Configuration

The application requires the following environment variables to be set
You can set these environment variables in a .env file in the project's root directory.

REQUIRED:
 - OPENAI_KEY: Your OpenAI API key.

OPTIANAL:

 - OPENAI_MODEL: The OpenAI model to use for generating responses. Set this to 'gpt-3.5-turbo'.
 - OPENAI_TEMPERATURE: The temperature parameter for controlling the randomness of generated responses. Set this to 0.1 for more deterministic responses.

 - OPENAI_MAX_TOKENS: The maximum number of tokens allowed in the generated response. Set this to 4096.

 - SOURCE_DOCS_DIR: The directory to store the source documents. Set this to 'source_doc'.

 - SOURCE_DOC_URL: The direct download link from Dropbox API for the source document. 
 Replace 'www.dropbox.com' with 'dl.dropboxusercontent.com' in the URL to direct download. Example: 'https://dl.dropboxusercontent.com/s/9npstuvp2vhnq4z/Untitled%205.pdf'.

 - TARGET_SOURCE_FILE_PATH: The file path to store the downloaded source document within the SOURCE_DOCS_DIR. Example: 'source_doc/Untitled 5.pdf'.

 - API_KEY: The API key token used for authentication. Set this to 'some-api-key-token'



## Start the FastAPI application:

To run the application locally, follow these steps:

1. Make sure the required environment variables are set (see Configuration section).

2. Running the Application
``` shell
uvicorn main:app --host 0.0.0.0 --port 80
```
3. The application will be accessible at http://localhost:80

## API Documentation
The API documentation is automatically generated and available at:
 - http://localhost:80/docs
 - https://app.swaggerhub.com/apis/angelskijm/nifty-brifge_ai_assistant/0.1.0
 
You can use this interactive documentation to explore the available endpoints and test the API.


## Start application in a Docker container

1. To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:
``` shell
docker build -t nifty-bridge-ai-assintent-app .
```

2. To run the Docker container, use the following command:
``` shell
docker run -d -p 8000:8000 nifty-bridge-ai-assintent-app
```
After running the container, you should be able to access your FastAPI application at http://localhost:8000 in your browser.
