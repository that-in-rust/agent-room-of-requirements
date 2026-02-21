# Z.AI Droid Streaming Fix

## Problem
When using Z.AI Coding Plan with Droid (Factory CLI), got error:
```
Error: Streaming is required for operations that may take longer than 10 minutes.
```

## Root Cause
Using Anthropic protocol (`provider: "anthropic"`) triggers the Anthropic TypeScript SDK's 10-minute timeout on non-streaming requests.

## Solution
Switch to OpenAI protocol with Z.AI's Coding API endpoint.

### Before (Broken)
```json
{
  "model": "glm-5",
  "baseUrl": "https://api.z.ai/api/anthropic",
  "provider": "anthropic"
}
```

### After (Fixed)
```json
{
  "model": "glm-5",
  "baseUrl": "https://api.z.ai/api/coding/paas/v4",
  "provider": "generic-chat-completion-api"
}
```

## Full Working Config
```json
{
  "customModels": [
    {
      "model": "glm-5",
      "displayName": "GLM-5 [Z.AI Coding Plan] - OpenAI",
      "baseUrl": "https://api.z.ai/api/coding/paas/v4",
      "apiKey": "YOUR_ZAI_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 131072
    },
    {
      "model": "glm-4.7",
      "displayName": "GLM-4.7 [Z.AI Coding Plan] - OpenAI",
      "baseUrl": "https://api.z.ai/api/coding/paas/v4",
      "apiKey": "YOUR_ZAI_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 131072
    }
  ]
}
```

## Key Points
- Use `/api/coding/paas/v4` endpoint (Z.AI's recommended Coding API for GLM Coding Plan)
- Use `generic-chat-completion-api` provider (OpenAI Chat Completions format)
- Avoid `extraHeaders` with timeout values - they don't help
- Config file: `~/.factory/settings.json`

## References
- Z.AI Docs: https://docs.z.ai/devpack/quick-start
- Factory BYOK Docs: https://docs.factory.ai/cli/configuration/byok
