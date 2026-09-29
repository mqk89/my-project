# Security Policy

## Reporting a vulnerability

Please do not disclose security vulnerabilities in a public GitHub issue.

Open a private GitHub security advisory when available, or contact the
maintainer privately with a clear description and reproduction steps.

## Security considerations

This project can call external APIs and webhooks. Before production use:

- Keep API keys in environment variables or a secrets manager.
- Never commit credentials.
- Authenticate public API endpoints.
- Validate and restrict webhook destinations.
- Add rate limiting.
- Review AI-generated actions before allowing them to affect external systems.
- Pin and regularly update dependencies.
