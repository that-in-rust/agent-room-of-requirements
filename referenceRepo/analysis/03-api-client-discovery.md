# API Client Discovery - Phase 4 (Started)

**Analysis Date:** 2026-02-01
**Phase:** 4 of 8 - API Communication Protocol
**Status:** STARTED (30% complete)

## API Client Instantiation

**Line 138,259:**
```javascript
new Anthropic({ apiKey, dangerouslyAllowBrowser: true });
```

**Key Parameters:**
- `apiKey` - Authentication credential
- `dangerouslyAllowBrowser: true` - Allows browser-like execution

**Fetch Requirement (Line 135,743):**
```
"`fetch` is not defined as a global; Either pass `fetch` to the client,
`new Anthropic({ fetch })` or polyfill the global, `globalThis.fetch = fetch`"
```

## API Configuration

### Production Environment (Lines 23,822-23,835)

**Variable:** `BA8`

```javascript
{
  BASE_API_URL: "https://api.anthropic.com",
  CONSOLE_AUTHORIZE_URL: "https://platform.claude.com/oauth/authorize",
  CLAUDE_AI_AUTHORIZE_URL: "https://claude.ai/oauth/authorize",
  TOKEN_URL: "https://platform.claude.com/v1/oauth/token",
  API_KEY_URL: "https://api.anthropic.com/api/oauth/claude_cli/create_api_key",
  ROLES_URL: "https://api.anthropic.com/api/oauth/claude_cli/roles",
  CONSOLE_SUCCESS_URL: "https://platform.claude.com/buy_credits?returnUrl=/oauth/code/success%3Fapp%3Dclaude-code",
  CLAUDEAI_SUCCESS_URL: "https://platform.claude.com/oauth/code/success?app=claude-code",
  MANUAL_REDIRECT_URL: "https://platform.claude.com/oauth/code/callback",
  CLIENT_ID: "9d1c250a-e61b-44d9-88ed-5944d1962f5e",
  OAUTH_FILE_SUFFIX: "",
  MCP_PROXY_URL: "https://mcp-proxy.anthropic.com",
  MCP_PROXY_PATH: "/v1/mcp/{server_id}",
}
```

### Local Development Environment (Lines 23,836-23,849)

**Variable:** `H1K`

```javascript
{
  BASE_API_URL: "http://localhost:3000",
  CONSOLE_AUTHORIZE_URL: "http://localhost:3000/oauth/authorize",
  CLAUDE_AI_AUTHORIZE_URL: "http://localhost:4000/oauth/authorize",
  TOKEN_URL: "http://localhost:3000/v1/oauth/token",
  API_KEY_URL: "http://localhost:3000/api/oauth/claude_cli/create_api_key",
  ROLES_URL: "http://localhost:3000/api/oauth/claude_cli/roles",
  CONSOLE_SUCCESS_URL: "http://localhost:3000/buy_credits?returnUrl=/oauth/code/success%3Fapp%3Dclaude-code",
  CLAUDEAI_SUCCESS_URL: "http://localhost:3000/oauth/code/success?app=claude-code",
  MANUAL_REDIRECT_URL: "https://console.staging.ant.dev/oauth/code/callback",
  CLIENT_ID: "22422756-60c9-4084-8eb7-27705fd5cf9a",
  OAUTH_FILE_SUFFIX: "-local-oauth",
  MCP_PROXY_URL: "http://localhost:8205",
  MCP_PROXY_PATH: "/v1/toolbox/shttp/mcp/{server_id}",
}
```

## API Endpoints Discovered

### OAuth Endpoints
1. **Authorize (Console):** `https://platform.claude.com/oauth/authorize`
2. **Authorize (Claude.ai):** `https://claude.ai/oauth/authorize`
3. **Token Exchange:** `https://platform.claude.com/v1/oauth/token`
4. **API Key Creation:** `https://api.anthropic.com/api/oauth/claude_cli/create_api_key`
5. **Roles:** `https://api.anthropic.com/api/oauth/claude_cli/roles`

### Success Redirects
- Console: `https://platform.claude.com/buy_credits?returnUrl=/oauth/code/success%3Fapp%3Dclaude-code`
- Claude.ai: `https://platform.claude.com/oauth/code/success?app=claude-code`
- Manual: `https://platform.claude.com/oauth/code/callback`

### MCP Proxy
- **URL:** `https://mcp-proxy.anthropic.com`
- **Path:** `/v1/mcp/{server_id}`
- Allows communication with MCP servers

## Client IDs

**Production:** `9d1c250a-e61b-44d9-88ed-5944d1962f5e`
**Local:** `22422756-60c9-4084-8eb7-27705fd5cf9a`

## User Agent

**Lines 125,797-125,803:**

```javascript
// External
return `claude-cli/${VERSION} (external, ${process.env.CLAUDE_CODE_ENTRYPOINT}${A})`;

// Default
return `claude-code/${VERSION}`;
```

**Pattern:** Includes version 2.1.29, environment context

## Beta Headers

**Line 136,525:**
```javascript
headers: Z3([{ "anthropic-beta": [...(K ?? []), "files-api-2025-04-14"].toString() }, q?.headers])
```

**Beta Features Enabled:**
- `files-api-2025-04-14` - File uploads support

## Organization Access Check

**Line 126,743:**
```javascript
let Y = `https://api.anthropic.com/api/organization/${A}/claude_code_sonnet_1m_access`;
```

Checks if organization has access to Sonnet 1M context feature.

## Security Metadata

**Build Information:**
```javascript
{
  ISSUES_EXPLAINER: "report the issue at https://github.com/anthropics/claude-code/issues",
  PACKAGE_URL: "@anthropic-ai/claude-code",
  README_URL: "https://code.claude.com/docs/en/overview",
  VERSION: "2.1.29",
  FEEDBACK_CHANNEL: "https://github.com/anthropics/claude-code/issues",
  BUILD_TIME: "2026-01-31T20:12:07Z"
}
```

## Logger Creation

**Lines 213,850-213,868:**
```javascript
return { setLogLevel: w, getLogLevel: $, createClientLogger: _, logger: z };
return QU7.createClientLogger(A);
return A2A.createClientLogger(A);
```

Multiple logger instances for client operations.

## AWS Bedrock Support

**Line 190,014:**
```javascript
`Failed to import '@aws-sdk/credential-providers'.
You can provide a custom \`providerChainResolver\` in the client options if your runtime
does not have access to '@aws-sdk/credential-providers':
\`new AnthropicBedrock({ providerChainResolver })\`
Original error: ${A.message}`
```

Supports AWS Bedrock as alternative to Anthropic API.

## TLS/Handshake Implementation

**Lines 247,585-248,475:**
- `createClientHello` (line 247,974)
- `createClientKeyExchange` (line 248,073)
- Custom TLS handshake implementation
- Record queue management

## Next Steps

### To Investigate
1. Message creation and sending logic
2. Streaming response handling
3. Tool use protocol implementation
4. Error handling and retries
5. Request/response middleware
6. Cost calculation integration

### Expected Locations
- Search for "messages.create" or similar
- Look for streaming event handlers
- Find tool use formatting logic
- Trace request/response interceptors

## Summary

✅ **Found:**
- API client instantiation
- Production and local configurations
- OAuth flow endpoints
- MCP proxy integration
- Beta feature flags
- User agent construction
- AWS Bedrock support

❓ **Still Need:**
- Message sending implementation
- Streaming handler
- Tool use protocol
- Response parsing
- Cost tracking integration

**Phase 4 Status:** 30% complete
**Next:** Locate message creation and tool use protocol
