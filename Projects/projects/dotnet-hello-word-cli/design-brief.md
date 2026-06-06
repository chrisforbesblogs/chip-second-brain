# .NET HelloWord CLI - Design Brief

## Owner

Prepared for ChipArchitect.

## Goal

Create a very small .NET command-line application that can run a routine called `-HelloWord`.

When invoked, the routine prints:

- `hello`
- the current local date and time

## Scope

This is a minimal proof-of-write and proof-of-execution project. Keep it intentionally simple.

## Proposed User Command

```bash
dotnet run -- -HelloWord
```

If compiled/published as a binary, the equivalent should be:

```bash
hello-word-cli -HelloWord
```

## Behaviour

When the CLI receives the `-HelloWord` argument, it should print a single friendly line containing `hello` and the current date/time.

Example:

```text
hello - 2026-06-06 15:52:00
```

If no argument or an unknown argument is supplied, print a short usage message:

```text
Usage: dotnet run -- -HelloWord
```

## Implementation Shape

- Use a standard .NET console app.
- Keep all logic in `Program.cs` unless the implementation naturally needs a small helper.
- Use local system time via `DateTime.Now`.
- Format date/time clearly, for example `yyyy-MM-dd HH:mm:ss`.
- No external packages are required.

## Suggested File Layout

Source code should be created under:

```text
/home/cef-admin/projects-source-code/dotnet-hello-word-cli/
```

```text
dotnet-hello-word-cli/
  HelloWordCli.csproj
  Program.cs
  README.md
```

## Acceptance Criteria

- Running `dotnet run -- -HelloWord` prints `hello` and the current date/time.
- Running with no argument prints usage help.
- Running with an unknown argument prints usage help.
- The app builds with `dotnet build`.
- No network access, database, or external service is required.

## Notes

The requested routine name is spelled `-HelloWord`, not `-HelloWorld`. Preserve the requested spelling unless Chris confirms it should be corrected.
