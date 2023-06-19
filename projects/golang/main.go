package main

import (
    "embed"
)

//go:embed schemas/*.json
var schemas embed.FS
