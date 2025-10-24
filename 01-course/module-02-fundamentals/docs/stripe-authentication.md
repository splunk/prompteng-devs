# Stripe Authentication

## API Key Authentication

All API requests require authentication using Bearer tokens in the Authorization header.

### Header Format

```
Authorization: Bearer sk_test_abc123
```

### API Key Types

- **Test mode:** `sk_test_...` (for development and testing)
- **Live mode:** `sk_live_...` (for production)

### Security Best Practices

1. **Never expose API keys** in client-side code (JavaScript, mobile apps)
2. **Store keys securely** in environment variables
3. **Rotate keys regularly** as part of security maintenance
4. **Use separate keys** for development, staging, and production environments

### Error Codes

- **401 Unauthorized:** Invalid or missing API key
- **403 Forbidden:** Valid key but insufficient permissions
