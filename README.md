# search_l3s_aimeta_srv

### To install the package
> pip install --upgrade pip setuptools wheels
> pip install -r requirements.txt
> pip install -e .[dev]

### To start the service
> flask run


### Folder Structue 

```plaintext

├── src/
|    ├── search_l3s_aimeta/
|        ├── swagger_client/     # swagger clients for L3S Gateway Service
|            ├── l3s_gateway_client/
|                ├── api/
|                ├── models/
|        ├── util/
|        ├── api/         # All api 
|            ├── trends/       # api for trends based on Agentur für Arbeit
|            ├── title/        # api for titles
|            ├── dataset_preprocess/   # api for pre-processing the dataset
|            ├── context_keywords/     # api for generating context keywords
|            ├── learning_goal/        # api for generating learing goals
|            ├── dataset_utils/        # api for accessing the MLS data
|            ├── summary/              # api for generating summary
|            ├── taught_skills/        # api for extracting taught skills
|            ├── quiz/                 # api for generating a quiz
|            ├── content_keywords/     # api for generating content keywords
            
