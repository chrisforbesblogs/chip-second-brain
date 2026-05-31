---
type: reference
status: active
updated: 2026-05-31
tags:
  - azure-openai
  - openclaw
  - models
  - configuration
---

# Azure OpenAI Models Used By OpenClaw

This note records the Azure/OpenAI-compatible model configuration currently used by ChipBoss/OpenClaw. It intentionally lists environment variable names and endpoints, but not API keys or tokens.

## Agent Model Routing

Primary model:
- Provider: `openai`
- Model: `gpt-5.5`
- Config id: `openai/gpt-5.5`
- Purpose: default primary model for OpenClaw agents.

Fallback model:
- Provider: `microsoft-foundry`
- Model/deployment: `gpt-5.4-mini`
- Config id: `microsoft-foundry/gpt-5.4-mini`
- Base URL: `https://cefdevai.openai.azure.com/openai/v1`
- API mode: `openai-responses`
- Purpose: fallback model for OpenClaw agents when the primary route is unavailable.

Related environment variables:
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_ENDPOINT=https://cefdevai.openai.azure.com/`
- `AZURE_OPENAI_BASE_URL=https://cefdevai.openai.azure.com/openai/v1`
- `AZURE_OPENAI_API_VERSION=preview`
- `AZURE_OPENAI_DEPLOYMENT_NAME_MAP=gpt-5.4-mini=gpt-5.4-mini`

## Memory Search Embeddings

Embedding provider:
- Provider: `openai-compatible`
- Model/deployment: `text-embedding-3-small`
- Base URL: `https://chris-mpr2tzn4-eastus2.cognitiveservices.azure.com/openai/v1/`
- Vector dimensions observed: `1536`
- Purpose: OpenClaw native memory search embeddings for the second brain and project hub.

Indexed paths:
- `~/.openclaw/workspace/second-brain`
- `~/.openclaw/workspace/chip-projecthub`

Related environment variables:
- `AZURE_OPENAI_EASTUS_EMBEDDINGS_API_KEY`
- `AZURE_OPENAI_EASTUS_EMBEDDINGS_BASE_URL=https://chris-mpr2tzn4-eastus2.cognitiveservices.azure.com/openai/v1/`
- `AZURE_OPENAI_EASTUS_EMBEDDINGS_MODEL=text-embedding-3-small`

OpenClaw config summary:
- `agents.defaults.memorySearch.enabled=true`
- `agents.defaults.memorySearch.provider=openai-compatible`
- `agents.defaults.memorySearch.model=text-embedding-3-small`
- `agents.defaults.memorySearch.remote.baseUrl=https://chris-mpr2tzn4-eastus2.cognitiveservices.azure.com/openai/v1/`

## Telegram Audio Transcription

Transcription deployment:
- Provider: Azure OpenAI East US/East US 2 resource
- Deployment: `gpt-4o-transcribe`
- Endpoint: `https://chris-mpr2tzn4-eastus2.cognitiveservices.azure.com/`
- API version: `2025-03-01-preview`
- Request path: `/openai/deployments/gpt-4o-transcribe/audio/transcriptions`
- Purpose: transcribe Telegram voice/audio notes into text for OpenClaw.

OpenClaw tool wrapper:
- Command: `/home/cef-admin/.openclaw/bin/azure-eastus-transcribe`
- OpenClaw config path: `tools.media.audio.models`
- Transcript echo format: `Transcribed: "{transcript}"`

Related environment variables:
- `AZURE_OPENAI_EASTUS_API_KEY`
- `AZURE_OPENAI_EASTUS_ENDPOINT=https://chris-mpr2tzn4-eastus2.cognitiveservices.azure.com/`
- `AZURE_OPENAI_EASTUS_BASE_URL=https://chris-mpr2tzn4-eastus2.cognitiveservices.azure.com/openai`
- `AZURE_OPENAI_EASTUS_API_VERSION=2025-03-01-preview`
- `AZURE_OPENAI_EASTUS_TRANSCRIBE_DEPLOYMENT=gpt-4o-transcribe`

## Naming Note

The local environment variable prefix is `AZURE_OPENAI_EASTUS_*`, while the Azure resource hostname includes `eastus2`. Keep the existing variable names unless intentionally migrating the configuration.

