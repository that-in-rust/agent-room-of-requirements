# Discussions GraphQL Patterns

## Table Of Contents

1. Why Discussions need GraphQL
2. Repo-wide discussion index
3. Focused discussion thread
4. Limits and caveats

## Why Discussions Need GraphQL

GitHub Discussions are not covered by a first-class top-level `gh discussion` command in standard GHCLI usage. Use `gh api graphql` for both discovery and focused thread capture.

## Repo-Wide Discussion Index

Use this shape when you need a lightweight repo-wide index:

```graphql
query($owner: String!, $name: String!, $endCursor: String) {
  repository(owner: $owner, name: $name) {
    discussions(first: 100, after: $endCursor, orderBy: {field: UPDATED_AT, direction: DESC}) {
      nodes {
        number
        title
        url
        createdAt
        updatedAt
        answerChosenAt
        category { name }
        author { login }
        comments { totalCount }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
```

## Focused Discussion Thread

Use this shape when you need the full story for one discussion:

```graphql
query($owner: String!, $name: String!, $number: Int!, $endCursor: String) {
  repository(owner: $owner, name: $name) {
    discussion(number: $number) {
      number
      title
      body
      url
      createdAt
      updatedAt
      answerChosenAt
      category { name }
      author { login }
      comments(first: 100, after: $endCursor) {
        nodes {
          id
          body
          createdAt
          updatedAt
          url
          isAnswer
          author { login }
          replyTo { id }
          replies(first: 100) {
            totalCount
            nodes {
              id
              body
              createdAt
              updatedAt
              url
              isAnswer
              author { login }
              replyTo { id }
            }
          }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
  }
}
```

## Limits And Caveats

- `--paginate` only paginates the top-level connection tied to `$endCursor`.
- Nested `replies(first: 100)` may still truncate very large reply sets.
- A repo-wide discussion index is good for discovery; a focused follow-up query is better for explanation.
- Always note when Discussions are disabled or inaccessible.
