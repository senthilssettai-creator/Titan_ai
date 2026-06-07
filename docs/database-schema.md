# TITAN AI Database Schema

## Memory tables

- `memory_entries`
  - `id` INTEGER PRIMARY KEY
  - `category` TEXT
  - `content` TEXT
  - `metadata` TEXT
  - `created_at` DATETIME

## Agent logs

- `agent_events`
  - `id` INTEGER PRIMARY KEY
  - `agent_name` TEXT
  - `event_type` TEXT
  - `payload` TEXT
  - `created_at` DATETIME

## Task plans

- `task_plans`
  - `id` INTEGER PRIMARY KEY
  - `objective` TEXT
  - `plan` TEXT
  - `status` TEXT
  - `created_at` DATETIME
  - `updated_at` DATETIME

## Security and audit

- `audit_log`
  - `id` INTEGER PRIMARY KEY
  - `action` TEXT
  - `user_id` TEXT
  - `resource` TEXT
  - `context` TEXT
  - `approved` BOOLEAN
  - `created_at` DATETIME
