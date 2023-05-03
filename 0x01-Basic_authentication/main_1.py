#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.auth import Auth

b = Auth()

print(b.require_auth(None, None))
print(b.require_auth(None, []))
print(b.require_auth("/api/v1/status/", []))
print(b.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(b.require_auth("/api/v1/status", ["/api/v1/status/"]))
print(b.require_auth("/api/v1/users", ["/api/v1/status/"]))
print(b.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))
