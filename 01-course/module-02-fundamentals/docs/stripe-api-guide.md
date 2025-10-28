# Stripe Payment API

## Create Payment Intent

**Endpoint:** `POST /v1/payment_intents`

Creates a PaymentIntent object.

### Required Fields

- `amount` (integer): Amount in cents (e.g., $10.00 = 1000)
- `currency` (string): 3-letter ISO code (USD, EUR, GBP, etc.)
- `payment_method` (string): ID of payment method to use

### Optional Fields

- `description` (string): Description of payment
- `metadata` (object): Custom key-value pairs

### Response Codes

- **200**: Success - Returns payment_intent object
- **400**: Validation error - Invalid request parameters
- **401**: Authentication error - Invalid or missing API key

### Example Response

```json
{
  "id": "pi_3AbCdEfGhIjKlMnO",
  "object": "payment_intent",
  "amount": 1000,
  "currency": "usd",
  "status": "requires_payment_method"
}
```
