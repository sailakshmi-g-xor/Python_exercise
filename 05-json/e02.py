import json


def get_nested(data, path, default=None):
    current = data

    for key in path.split("."):
        if not isinstance(current, dict):
            return default

        if key not in current:
            return default

        current = current[key]

    return current


with open("data/config.json", encoding="utf-8") as f:
    config = json.load(f)

print(f"app.name = {get_nested(config, 'app.name')!r}")
print(f"server.port = {get_nested(config, 'server.port')!r}")
print(f"server.timeouts.read = {get_nested(config, 'server.timeouts.read')!r}")
print(f"database.pool.max = {get_nested(config, 'database.pool.max')!r}")
print(f"features.beta_dashboard = {get_nested(config, 'features.beta_dashboard')!r}")

print(
    f"cache.ttl = "
    f"{get_nested(config, 'cache.ttl', 60)!r}"
)

print(
    f"server.host.name = "
    f"{get_nested(config, 'server.host.name', 'n/a')!r}"
)

admins = get_nested(config, "admins", [])

print(f"admins: {', '.join(admins)} ({len(admins)})")
