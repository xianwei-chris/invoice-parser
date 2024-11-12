# Setup and Run
### 1. Get an OpenAI API Key
If you don’t already have an OpenAI API key, follow this [guide](https://medium.com/@lorenzozar/how-to-get-your-own-openai-api-key-f4d44e60c327) to obtain one.

### 2. Create an Environment Variable File
Add the API key into an environment variable file by creating a `.env` file in the root path of your project with the following content:
```
OPENAI_API_KEY=[Insert your API Key Here]
```
Note: no single quote / double quote is needed

### 3. Build the Docker Image
Run the following command to build the Docker image:
```
docker build -t invoice-parser:latest .
```

### 4. Run the Docker Image with Environment Variables
Use this command to start the container and pass the .env file to the container:
```
docker run -p 8501:8501 --env-file .env invoice-parser
```

### 5. Access the App
Open your browser and go to http://localhost:8501/ to access the app.


# Pending Improvement
### 1. Multi-Page PDF Handling
Currently, the application only extracts information from the first page of a PDF. To fully support multi-page documents, we can consider two approaches:  

__Approach 1__: Convert each page of the PDF into separate images and pass them all in a single request to OpenAI. The prompt can guide OpenAI to extract and combine information across pages, displaying a unified set of extracted fields.

__Approach 2__: Process each page individually, submitting each as a separate request to OpenAI. Once all pages are processed, the responses can be combined in post-processing to present a consolidated view of the extracted information.

### 2. OpenAI Cost and Usage Tracking
Tracking both cost and usage rate is essential for efficient API management:

__Cost Tracking__: Given that OpenAI API calls can be costly, tracking usage costs per request helps optimize prompt usage and identify high-cost operations.

__Rate Usage Tracking__: Monitoring API rate limits can prevent overuse and avoid reaching rate limits, which would impact application performance. By managing usage, we can better control costs and optimize request patterns.

### 3. Data Validation with Pydantic Models
- Implementing Pydantic models for data validation can ensure consistency in the structure and types of data returned by OpenAI.  
- By enforcing schema validation on the response data, we can improve reliability and reduce errors, especially when handling structured fields.