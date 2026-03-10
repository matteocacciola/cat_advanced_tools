from cat import hook, RecallSettings


@hook
def agent_prompt_prefix(prefix: str, cat) -> str:
    settings = cat.mad_hatter.get_plugin().load_settings()
    prefix = settings["prompt_prefix"]

    return prefix


@hook
def before_cat_recalls_memories(config: RecallSettings, cat) -> RecallSettings:
    settings = cat.mad_hatter.get_plugin().load_settings()
    config.k = settings["k"]
    config.threshold = settings["threshold"]
    config.latest_n_history = settings["latest_n_history"]

    return config


@hook
def agent_prompt_suffix(suffix: str, cat) -> str:
    settings = cat.mad_hatter.get_plugin().load_settings()
    suffix = f"""
# Context
{{context}}
"""

    try:
        if not settings["language"] or str(settings["language"]).lower() == "human":
            return f"""
{suffix}
ALWAYS answer in the user's language
"""
    
        return f"""
{suffix}
ALWAYS answer in {settings["language"]}
"""
    except Exception:
        return f"""
{suffix}
ALWAYS answer in the user's language
"""
