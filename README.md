# clarity-notes

A small tool that turns messy, free-text patient complaints (the kind of thing someone types into a WhatsApp message to a clinic) into a structured summary: symptoms, duration, severity, and red flags, alongside a clean human-readable version a practitioner could skim in seconds.

## Why

Built in the same spirit as [CDSS for Unani Medicine Practitioners](https://arxiv.org/abs/2310.18361) — the idea that practitioners in under-resourced settings often work from unstructured patient descriptions with no tooling to help triage them. This is a separate, smaller utility exploring the same problem from a different angle: not diagnosis, just structuring.

## Features

- **Symptom structuring** — paste a free-text complaint, get back structured JSON (symptoms, duration, severity, red flags) plus a clean human-readable summary.
- **Multi-language input** — detects Urdu, Punjabi, or English input and structures it correctly regardless of source language.

## Stack

- Backend: FastAPI (Python)
- Frontend: React
- LLM: Claude API, for the free-text -> structured-output step and language detection

## Status

Early scaffold. Core features in progress.

## Setup

See `backend/README.md` and `frontend/README.md`.
