from cat.mad_hatter.decorators import tool, hook
from cat.log import log


@hook
def agent_prompt_prefix(prefix, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    prefix = settings["prompt_prefix"]

    return prefix


@hook
def before_cat_recalls_memories(default_declarative_recall_config, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    default_declarative_recall_config["k"] = settings["declarative_memory_k"]
    default_declarative_recall_config["threshold"] = settings[
        "declarative_memory_threshold"
    ]

    return default_declarative_recall_config


@hook
def agent_prompt_suffix(suffix, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    username = settings["user_name"] if settings["user_name"] != "" else "Human"
    suffix = f"""
# Context
{{context}}
"""

    if settings["language"] == "Human":
        suffix += f"""
ALWAYS answer in the {username}'s language
"""
    elif settings["language"] not in ["None", "Human"]:
        suffix += f"""
ALWAYS answer in {settings["language"]}
"""

    return suffix

@hook
def rabbithole_instantiates_splitter(text_splitter, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    text_splitter._chunk_size = settings["chunk_size"]
    text_splitter._chunk_overlap = settings["chunk_overlap"]
    return text_splitter
