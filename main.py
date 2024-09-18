from backend.core import run_llm

import streamlit as st

from streamlit_chat import message

st.header("Langchain Course - Documentation Helper Bot")


if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []


def create_sources_string(source_urls: set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string

def on_message_change():
    st.session_state["user_prompt_history"].append(st.session_state.prompt)
    #st.session_state["chat_answers_history"].append(formatted_response)

try:
    if st.session_state["user_prompt_history"][-1]:
        with st.spinner("Generating response.."):
            generated_response = run_llm(query=st.session_state["user_prompt_history"][-1])
            sources = set(
                [doc.metadata["source"] for doc in generated_response["source_documents"]]
            )

            formatted_response = (
                f"{generated_response['result']} \n\n {create_sources_string(sources)}"
            )

        #st.session_state["user_prompt_history"].append(st.session_state.prompt)
        st.session_state["chat_answers_history"].append(formatted_response)
except: pass

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(user_query, is_user=True)
        message(generated_response)

st.text_input("Prompt", placeholder="Enter your prompt here..", key="prompt", on_change=on_message_change)
