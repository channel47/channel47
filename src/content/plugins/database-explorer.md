---
featured: false
draft: false
---

## What it does

Query and explore databases conversationally. Ask questions in plain English, get formatted results—no SQL syntax required (but full SQL access when you need it). Supports PostgreSQL, MySQL, SQLite, and MongoDB.

## Key Features

- **Natural language queries**: "Show me users who signed up last week" instead of writing SQL
- **Schema exploration**: Navigate tables, relationships, indexes without external tools
- **Query explanation**: Understands what queries are doing (performance implications, index usage)
- **Data visualization**: Renders query results as tables, charts, or JSON
- **Safe by default**: Read-only mode prevents accidental data modification
- **Multiple connections**: Switch between databases mid-conversation
- **Query history**: Reference and modify previous queries

## Real-world use cases

I use this for:

- Debugging production issues (quick queries without SSH or database clients)
- Exploring unfamiliar schemas (understanding table relationships and data patterns)
- Answering ad-hoc questions (stakeholder requests, analytics queries)
- Query optimization (explaining slow queries, suggesting indexes)
- Data validation (checking data integrity, finding anomalies)
- Generating test data (creating realistic fixtures from production patterns)

## What makes it different

Instead of:

- Opening database GUI client
- Writing SQL syntax from memory
- Exporting results to spreadsheet for analysis
- Looking up column names in schema documentation
- Switching between multiple tools for different operations

You just ask questions. The plugin translates to SQL, explains what's happening, and formats results however you need them.

## Setup

1. Install: `/plugin install database-explorer@channel47`
2. Configure connection: `/db-connect postgres://user:pass@localhost/dbname`
3. Start querying: "Show me the users table schema"

## Example workflows

**Explore database schema:**

```
"What tables are in this database?"
"Show me the users table structure"
"Which tables reference the users table?"
```

**Natural language queries:**

```
"Show me users who signed up in the last 7 days"
"Count orders by status for this month"
"Find the top 10 products by revenue"
```

**Query optimization:**

```
"Explain this query: SELECT * FROM orders WHERE user_id = 123"
"Why is this query slow?"
"What indexes would help this query?"
```

**Data investigation:**

```
"Are there any users without email addresses?"
"Show me duplicate email addresses"
"Find orders with negative amounts"
```

## Available skills

- `/db-connect` - Connect to database (PostgreSQL, MySQL, SQLite, MongoDB)
- `/db-query` - Run raw SQL query
- `/db-explain` - Explain query execution plan
- `/db-schema` - Show database schema

Most queries work via natural language without explicit skill invocation. The plugin automatically:

- Translates natural language to SQL
- Executes queries safely (read-only by default)
- Formats results appropriately (tables, JSON, charts)
- Suggests follow-up queries based on results

All database credentials are stored securely in plugin settings. Never committed to git.
