from cat import hook


@hook
def agent_prompt_prefix(prefix, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    prefix = settings["prompt_prefix"]

    return prefix


@hook
def before_cat_recalls_memories(config, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    config["k"] = settings["k"]
    config["threshold"] = settings["threshold"]
    config["latest_n_history"] = settings["latest_n_history"]

    return config


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
