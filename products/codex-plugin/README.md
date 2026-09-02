# Codex plugin adapter

[`rebuild-labs/`](rebuild-labs/) is an experimental plugin generated from the
canonical `rebuild-plan`, `rebuild-complete`, and `rebuild-incremental`
capabilities. The packaged skill directories are one atomic bundle and must not
be edited directly.

After the capability sources have a committed checkpoint, rebuild or verify the
adapter with:

```console
uv run python scripts/build_plugin.py
uv run python scripts/build_plugin.py --check
```

The repository exposes the adapter through its own local/Git marketplace for
native Codex discovery. This mechanical installation surface is experimental;
it is not a public or verified marketplace listing and does not transfer source
authority away from `capabilities/`.
