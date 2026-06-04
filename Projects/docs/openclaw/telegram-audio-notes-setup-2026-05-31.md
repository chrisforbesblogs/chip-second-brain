# Telegram Audio Notes Setup - 2026-05-31

## Purpose

Allow project audio notes sent to ChipBoss over Telegram to be captured and transcribed for follow-up work.

## Current Flow

- Telegram voice/audio attachments are saved locally by OpenClaw under `/home/cef-admin/.openclaw/media/inbound/`.
- OpenClaw's built-in audio understanding path should transcribe inbound Telegram audio.
- Transcript echo is enabled so users can verify what was heard.
- Audio transcription is pinned to a local `whisper` CLI wrapper backed by `faster-whisper`.

## Implementation Note

OpenClaw is configured to call a local `whisper` command for Telegram audio transcription, using the CPU `tiny` model for speed on this host.
This avoids spending OpenAI API credits for voice notes.

## First Test

The first Telegram audio test transcribed successfully as:

```text
Can you hear me?
```
