#!/usr/bin/env bash
echo "formating files"
uv run ruff format --config ruff.toml .
git add -u
