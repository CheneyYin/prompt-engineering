from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv
import os
import time

def current():
    return time.strftime("%H:%M:%S", time.localtime())

parser = StrOutputParser()
load_dotenv()

store = {}
def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# Initialize the LangChainOpenAI class
model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.deepseek.com"
    )

print("Model {} loaded successfully!".format(model.model_name))

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | model

chain_with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history=get_session_history,
    input_messages_key="messages"
)

session_id = "default"

while True:
    # Get user input
    user_input = input(current() + " |You:> ")
    if user_input.lower() == "exit":
        break
    # Call the API
    messages = [HumanMessage(content=user_input)]
    start_time = time.time()
    print(current(), "|Bot:> ", end="")

    ret = chain_with_message_history.invoke(
        {
            "messages": messages
        },
        config={"configurable": {"session_id": session_id}} 
    )

    print(ret.content)

    # for chunk in chain_with_message_history.stream(
    #     {
    #         "messages": messages
    #     },
    #     config={"configurable": {"session_id": session_id}}
    # ):
    #     print(chunk.content, end="", flush=True)

    end_time = time.time()
    print("")
    print("(Response time: {:.2f} seconds)".format(end_time - start_time))

print(current(), "|Bot:>", "Goodbye!")