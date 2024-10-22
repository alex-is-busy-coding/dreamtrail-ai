from langchain_community.llms import Bedrock

llm = Bedrock(
    model_id="amazon.titan-text-lite-v1",
    credentials_profile_name="bedrock",
)
