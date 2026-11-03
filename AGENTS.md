# Repository Guidelines

## Project Structure & Module Organization

This repository is a Hugo blog using the `PaperMod` theme, vendored as a git submodule at `themes/PaperMod/`. All site and theme parameters live in `hugo.toml`; there is no separate params file. Blog posts live in `content/posts/`; use `archetypes/default.md` for new Markdown content. Static files copied as-is belong in `static/`, such as `static/images/` and `static/avatar/`. Generated output is written to `public/`, which is git-ignored and rebuilt by CI on every push.

## Build, Test, and Development Commands

- `git submodule update --init --recursive`: fetch the `PaperMod` theme before the first local build.
- `hugo server -D`: run the local development server and include draft content.
- `hugo`: build the production site into `public/`.
- `hugo --minify`: build minified production output.

Run Hugo commands from the repository root unless noted.

## Coding Style & Naming Conventions

Write posts in Markdown with clear front matter and lowercase, hyphenated filenames, for example `content/posts/my-new-post.md`. Put local template overrides in `layouts/`; never edit files inside the `themes/PaperMod/` submodule, since those changes are not tracked by this repository.

## Testing Guidelines

There is no dedicated automated test suite. Validate changes by running `hugo` and fixing warnings or template errors before committing. For content changes, run `hugo server -D` and inspect affected posts, images, tags, and archive pages locally. For theme changes, check desktop and mobile layouts.

## Commit & Pull Request Guidelines

Recent commits use short Chinese summaries, often describing the completed change directly, such as `进行了主题的个性化配置`. Keep commits focused.

Pull requests should include a brief description, reason for the change, and screenshots for visual updates. Link related issues when available, and mention the validation command used, for example `hugo --minify`.

## Security & Configuration Tips

Do not commit secrets, analytics tokens, or private service credentials in `hugo.toml` or workflow files. Do not commit generated output: `public/`, `resources/_gen/`, and `.hugo_build.lock` are git-ignored because GitHub Actions builds the site on every push to `main`.
